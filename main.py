import csv
import smtplib
import os
import time
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv(dotenv_path="senha.env") # Arquivo .env que conterá a senha EMAIL_APP_PASSWORD, que deve ser alterada.
EMAIL = "colocar_seu_email@gmail.com" # Colocar o email que enviará a mensagem.
SENHA = os.environ.get("EMAIL_APP_PASSWORD")

# Leitura do arquivo de mensagem
with open("mensagem.txt", "r", encoding="utf-8") as arquivo:
        modelo = arquivo.read()

# Conexão com o servidor
try:
        with smtplib.SMTP("smtp.gmail.com", 587) as servidor:
                servidor.starttls()
                servidor.login(EMAIL, SENHA)

                # Leitura dos contatos no CSV.
                with open("contatos.csv", newline='', encoding="utf-8") as arquivo:
                        leitor = csv.DictReader(arquivo)

                        for contato in leitor:
                                nome = contato["nome"]
                                destino = contato["email"]
                                mensagem = modelo.format(nome=nome)
                                time.sleep(3)  # pausa de 3 segundo entre envio de emails. É para evitar o possível spam e consequente bloqueio do gmail.
                                if not destino:
                                        continue

                                # Criação do email com UTF-8.
                                email_msg = EmailMessage()
                                email_msg['From'] = EMAIL
                                email_msg['To'] = destino
                                email_msg['Subject'] = f"Olá {nome}!" # Altere como achar melhor para o tópico da mensagem.
                                email_msg.set_content(mensagem)

                                try:
                                        servidor.send_message(email_msg)
                                        print(f"Enviado para {nome}")
                                        with open("log_envio.txt", "a", encoding="utf-8") as log:
                                                log.write(f"Enviado para {nome} - {destino}\n")

                                except Exception as e:
                                        print(f"Erro ao enviar para {destino}: {e}")
                                        with open("log_envio.txt", "a", encoding="utf-8") as log:
                                                log.write(f"Falha ao enviar para {nome} - {destino}: {e}\n")
except smtplib.SMTPAuthenticationError:
        raise ValueError("Falha no login: senha incorreta ou App Password inválido")