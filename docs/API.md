# Metadados públicos de atualização

- `latest.json`: canal estável padrão, atualizado após promoção verificada.
- `beta.json`: prévias assinadas geradas pelo pipeline privado. Uso opcional.
- `releases/stable.json`: pedido versionado de promoção, não é o feed que o aplicativo consulta.

Formato `reeds-presence-release-v1`, com `versionName`, `versionCode`, `sha256`, `releaseUrl`, `apkUrl` e `notes`. O versionName mantém quatro componentes numéricos para compatibilidade com as instalações atuais.

Os consumidores devem usar HTTPS, validar a origem e verificar o APK, a assinatura e a versão antes de instalar. Não use a ordem da lista de releases para identificar estabilidade: confira `prerelease` ou use `/releases/latest`. Não faça download sem ação explícita do visitante.

O pipeline de promoção não recompila nem substitui APKs publicados. Ele verifica hash, checksum, certificado permanente, pacote e versão; rejeita downgrade e alteração de binário com o mesmo versionCode.
