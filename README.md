# Automação de Emails

O projeto utiliza Python, CSV e .env para enviar mensagens diretamente para os emails dos contatos salvos.

## O programa é capaz de:
1. Leitura de contatos a partir de um arquivo CSV.
2. Envio em massa ou individual de mensagens por email.
3. Registrar toda ação executada pelo programa, salvando erros e sucessos.

**⚠️ Aviso: Vale-se dizer que o projeto foi feito puramente para fins de estudo e desenvolvimento, não sendo recomendado para uso real.**

## Como usar:
1. Coloque os nomes e emails dos contatos no arquivo `contatos.csv`.
2. Crie uma senha de aplicativo no seu email para o programa utilizá-lo nas mensagens, depois configure o `senha.env` com a senha de programa. **Não compartilhe o `arquivo .env`, já que terá sua senha.**
3. Configure o arquivo `mensagem.txt` para a mensagem que você desejar, usando `{nome}` para personalizar o destinatário.
