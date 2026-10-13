# REEDS Presence — lançamento oficial fora da Play Store

Distribuição direta do APK Android assinado pelo projeto REEDS. Esta publicação não representa aprovação do Google Play ou endosso do Discord.

## Novidades
- Editor de imagens por URL HTTPS, sem envio de fotos para hospedagem pública.
- Consentimento para detecção automática de jogos e opção de revogação nos Ajustes.
- Detecção adaptativa e proteção contra reativação de um jogo que já saiu do primeiro plano.
- Interface responsiva, perfis de atividades, favoritos e backup local.
- Atualizações com verificação de SHA-256, pacote e certificado antes de abrir o instalador Android.

## Instalação
Android 10 ou superior, processador ARM/ARM64. Baixe o arquivo `REEDSPresence-v0.16.185.1-assinado.apk` nos Assets desta release. Não é necessário baixar os arquivos Source code.

O Android solicitará autorização para instalar a partir do navegador ou gerenciador de arquivos utilizado. A autorização é por aplicativo; você pode revogá-la após a instalação. Mantenha o Play Protect ativo.

Para atualizar uma instalação compatível, instale por cima. Não desinstale nem limpe os dados para resolver conflito de assinatura sem antes exportar um backup.

## Limitações conhecidas
- A exibição no Discord depende do aplicativo Discord, do Social SDK, da conexão e das restrições do Android. Não há garantia de detecção ou publicação em 200 ms.
- Fabricantes podem restringir atividades em segundo plano. Consulte os diagnósticos do aplicativo.
- URLs de imagens precisam continuar acessíveis. O projeto não hospeda as fotos do usuário.
- Testes unitários e compilação passaram. A matriz completa de aparelhos, acessibilidade e execução em ambiente de 16 KB ainda não foi validada nesta publicação.

## Integridade e suporte
Confira `SHA256SUMS.txt`. O certificado permanente SHA-256 é:
`e5d429e9aa321135cdbbe1ba689a7598e6915dbb7d0285a6493ce5c3e922c13b`.

[Instalação e atualização](https://github.com/REEDScx/reeds-presence2/blob/main/docs/INSTALLATION.md) · [Privacidade](https://github.com/REEDScx/reeds-presence2/blob/main/PRIVACY.md) · [Suporte](https://github.com/REEDScx/reeds-presence2/blob/main/SUPPORT.md)
