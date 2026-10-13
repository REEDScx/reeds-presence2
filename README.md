# REEDS Presence

Canal **público oficial de distribuição** do aplicativo Android REEDS Presence. O código-fonte do aplicativo permanece no repositório **privado** `REEDScx/reeds-precense`.

## Instalação e atualizações

**[Baixar a versão estável oficial](https://github.com/REEDScx/reeds-presence2/releases/latest)** · [Prévias para testes](https://github.com/REEDScx/reeds-presence2/releases)

Android **10 ou superior**, dispositivos ARM/ARM64. Baixe o arquivo terminado em `.apk` nos Assets da release; os arquivos “Source code” não são o aplicativo.

Distribuição direta pelo GitHub, independente da Play Store. O aplicativo usa integração com Discord, mas não é um produto oficial do Discord. A instalação depende de confirmação do Android; não há instalação silenciosa. Mantenha o Play Protect ativo.

As releases incluem APK assinado e `SHA256SUMS.txt`. O atualizador padrão consulta apenas o canal estável (`latest.json`); `beta.json` é opcional para testes. As prévias podem conter regressões e não substituem automaticamente a versão estável.

Consulte [instalação e atualização](docs/INSTALLATION.md), [notas e limitações](releases/NOTES.md) e [política de privacidade](PRIVACY.md).

## Contribua

Aceitamos issues de bugs, propostas de recursos, correções de documentação, templates e melhorias na distribuição pública. Consulte [CONTRIBUTING.md](CONTRIBUTING.md), [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) e [SUPPORT.md](SUPPORT.md). O código Android privado não é aceito neste repositório.

## Documentação

[Instalação](docs/INSTALLATION.md) · [Configuração](docs/CONFIGURATION.md) · [Arquitetura](docs/ARCHITECTURE.md) · [Desenvolvimento](docs/DEVELOPMENT.md) · [API de atualização](docs/API.md) · [Publicação](docs/DEPLOYMENT.md) · [Testes](docs/TESTING.md) · [FAQ](docs/FAQ.md) · [Roadmap](docs/ROADMAP.md)

## Segurança, licenças e direitos

Consulte [SECURITY.md](SECURITY.md), [LICENSE](LICENSE) e [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). A licença deste repositório cobre somente o conteúdo sobre o qual o titular possui direitos e que é disponibilizado sob seus termos; **não concede licença para o código Android privado, SDKs proprietários, marcas ou APKs distribuídos**. O pacote Android é `com.reeds.presence`.

Não publique tokens, credenciais, keystores, arquivos de assinatura, dados pessoais, SDKs proprietários ou código-fonte privado. Reporte falhas de segurança por canal privado.

