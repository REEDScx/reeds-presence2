# REEDS Presence — Atualizações oficiais

Este repositório **público** é o canal de distribuição de atualizações do aplicativo Android REEDS Presence. O **código-fonte original continua privado**.

## Baixar atualizações

As versões serão publicadas em [Releases](https://github.com/REEDScx/reeds-presence2/releases) com:
- `REEDSPresence-v*-assinado.apk` — APK Android assinado;
- `SHA256SUMS.txt` — soma SHA-256 do arquivo;
- `latest.json` — metadados da versão, hash e URLs oficiais.

O aplicativo pode consultar periodicamente o arquivo [latest.json](https://raw.githubusercontent.com/REEDScx/reeds-presence2/main/latest.json) **após o primeiro Release sincronizado**. O download precisa de consentimento e a instalação deve ser confirmada no Android. Não existe instalação silenciosa.

## Segurança e privacidade

- Pacote Android: `com.reeds.presence`.
- O APK é verificado por identificador do pacote, `versionCode`, assinatura digital e SHA-256 antes da instalação.
- Este repositório **não deve receber** código-fonte privado, AAR proprietário do SDK Discord, keystore, senhas, tokens de usuário ou segredos do GitHub.
- As versões podem permanecer identificadas como **Beta** enquanto não houver testes em aparelhos reais.
- A publicação é automatizada a partir do pipeline de compilação do aplicativo privado, quando a credencial de escrita de escopo mínimo estiver configurada.

## Limites

A Rich Presence usa o SDK oficial do Discord. Uma resposta de sucesso do SDK não garante visibilidade remota para outros usuários.
