#!/usr/bin/env python3
"""Promote an existing signed APK; never build, re-sign or replace its assets."""
import base64
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

REPO = "REEDScx/reeds-presence2"
CERT = "e5d429e9aa321135cdbbe1ba689a7598e6915dbb7d0285a6493ce5c3e922c13b"
BASE = f"https://github.com/{REPO}/releases"

def validate_request(data):
    version = data["versionName"]
    if not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+", version):
        raise ValueError("Invalid version")
    if type(data["versionCode"]) is not int or not 0 < data["versionCode"] <= 2100000000:
        raise ValueError("Invalid versionCode")
    if not re.fullmatch(r"[a-f0-9]{64}", data["sha256"]):
        raise ValueError("Invalid SHA-256")
    if data["format"] != "reeds-presence-release-v1":
        raise ValueError("Unsupported format")
    tag = "v" + version
    asset = f"REEDSPresence-{tag}-assinado.apk"
    if data["releaseUrl"] != f"{BASE}/tag/{tag}" or data["apkUrl"] != f"{BASE}/download/{tag}/{asset}":
        raise ValueError("Only official release assets are allowed")
    return tag, asset

def validate_upgrade(current, requested):
    if current["versionCode"] > requested["versionCode"]:
        raise ValueError("Refusing to downgrade the default update feed")
    if current["versionCode"] == requested["versionCode"] and current["sha256"] != requested["sha256"]:
        raise ValueError("Same versionCode with a different APK")

def command(*args):
    return subprocess.check_output(args, text=True)

def api(path):
    return json.loads(command("gh", "api", f"repos/{REPO}/{path}"))

def main():
    if os.environ.get("GITHUB_REF") != "refs/heads/main":
        raise RuntimeError("Stable promotion is restricted to main")
    data = json.loads(Path("releases/stable.json").read_text())
    tag, asset = validate_request(data)
    current = api("contents/latest.json")
    validate_upgrade(json.loads(base64.b64decode(current["content"])), data)
    release = api(f"releases/tags/{tag}")
    if release["draft"]:
        raise ValueError("Draft releases cannot be promoted")
    assets = {item["name"]: item for item in release["assets"]}
    if assets[asset]["browser_download_url"] != data["apkUrl"]:
        raise ValueError("Unexpected asset location")
    if assets[asset].get("digest") != "sha256:" + data["sha256"]:
        raise ValueError("GitHub asset digest does not match request")
    with tempfile.TemporaryDirectory() as directory:
        command("gh", "release", "download", tag, "--repo", REPO,
                "--pattern", asset, "--pattern", "SHA256SUMS.txt", "--dir", directory)
        apk = Path(directory) / asset
        if hashlib.sha256(apk.read_bytes()).hexdigest() != data["sha256"]:
            raise ValueError("Downloaded APK hash mismatch")
        checksum = (Path(directory) / "SHA256SUMS.txt").read_text().split()
        if checksum != [data["sha256"], asset]:
            raise ValueError("Checksum file mismatch")
        sdk = Path(os.environ["ANDROID_HOME"]) / "build-tools/35.0.0"
        signature = command(str(sdk / "apksigner"), "verify", "--verbose", "--print-certs", str(apk))
        fingerprints = re.findall(r"Signer #\d+ certificate SHA-256 digest: ([a-fA-F0-9]{64})", signature)
        if [value.lower() for value in fingerprints] != [CERT]:
            raise ValueError("APK is not signed with the permanent REEDS certificate")
        badging = command(str(sdk / "aapt"), "dump", "badging", str(apk))
        package = re.search(r"^package: name='([^']+)' versionCode='([^']+)' versionName='([^']+)'", badging, re.M)
        if not package or package.groups() != ("com.reeds.presence", str(data["versionCode"]), data["versionName"]):
            raise ValueError("APK package or version mismatch")
        if "sdkVersion:'29'" not in badging:
            raise ValueError("Unexpected minimum Android version")
    # Re-read immediately before writing: never overwrite a concurrently updated feed.
    newest = api("contents/latest.json")
    if newest["sha"] != current["sha"]:
        raise RuntimeError("Update feed changed; inspect and retry")
    command("gh", "release", "edit", tag, "--repo", REPO, "--prerelease=false", "--latest",
            "--title", f"REEDS Presence {data['versionName']} — lançamento oficial",
            "--notes-file", "releases/NOTES.md")
    encoded = base64.b64encode((json.dumps(data, ensure_ascii=False, indent=2) + "\n").encode()).decode()
    command("gh", "api", "--method", "PUT", f"repos/{REPO}/contents/latest.json",
            "-f", f"message=release: publish stable feed {tag}", "-f", f"content={encoded}",
            "-f", f"sha={current['sha']}", "-f", "branch=main")
    print(f"Stable release verified and published: {data['releaseUrl']}")

if __name__ == "__main__":
    main()
