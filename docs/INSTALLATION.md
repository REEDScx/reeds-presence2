# Instalação e atualização

## Requisitos
- Android 10 ou superior, processador ARM/ARM64.
- Discord instalado e configurado para usar a integração de presença. O comportamento depende do Discord, do SDK e do Android.
- Internet para publicação da presença, imagens remotas e consulta de atualizações.

## Primeira instalação
1. Abra [a release estável oficial](https://github.com/REEDScx/reeds-presence2/releases/latest).
2. Leia as notas e baixe somente o arquivo `.apk` dos Assets. `Source code` não instala o aplicativo.
3. Abra o APK. Se o Android solicitar, permita a instalação por esse navegador ou gerenciador de arquivos. A opção e o nome variam por fabricante.
4. Confirme a instalação. Depois, revogue a autorização de instalar apps desconhecidos se não precisar dela. Mantenha o Play Protect ativo; se houver alerta de bloqueio, não o ignore: confira a origem e procure suporte.
5. Abra o REEDS Presence, configure uma atividade e confira o resultado no Discord.
6. A detecção automática é opcional. Leia o consentimento e conceda Acesso ao uso somente se desejar ativá-la. Você pode revogar o consentimento nos Ajustes.

## Atualizar sem perder dados
Use a verificação de atualização nos Ajustes ou baixe o novo APK oficial e instale sobre o existente. O atualizador confere hash, pacote e certificado antes de solicitar a instalação ao Android. Não existe instalação silenciosa.

Não desinstale nem limpe os dados antes de exportar um backup. Builds debug antigas assinadas com outra chave não aceitam atualização direta; procure suporte em caso de conflito. Uma migração para a Play Store dependerá da configuração de assinatura escolhida no futuro.

## Conferir integridade
Cada release inclui `SHA256SUMS.txt`. Compare o hash SHA-256 do APK baixado com esse arquivo. O certificado de assinatura permanente do projeto tem SHA-256:

`e5d429e9aa321135cdbbe1ba689a7598e6915dbb7d0285a6493ce5c3e922c13b`

O hash do APK muda a cada versão; o certificado identifica a chave de assinatura. Um hash correto confirma integridade, não certificação de segurança do aplicativo.

## Estável e prévias
O feed padrão `latest.json` acompanha somente releases promovidas para estável. Para testar prévias, a fonte avançada pode usar `https://raw.githubusercontent.com/REEDScx/reeds-presence2/main/beta.json`. Essa é uma escolha voluntária. Voltar ao feed estável não permite instalar uma versão de código inferior à que está no aparelho; aguarde uma estável mais nova.

## Ajuda
Leia as [limitações conhecidas](../releases/NOTES.md), a [privacidade](../PRIVACY.md) e o [suporte](../SUPPORT.md). Nunca compartilhe tokens do Discord, chaves ou backups pessoais em issues públicas.
