import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
host = 'smtp.gmail.com'
port = 587
user = 'mayconmottadasilva18@gmail.com'
password = 'faoozqinjcovahme'
server = smtplib.SMTP(host, port)


server.ehlo()
server.starttls()
server.login(user, password)


message = 'Fatura NuBank'
email_msg = MIMEMultipart()
email_msg['From'] = user
email_msg['To'] = 'mayconmottadasilva@outlook.com'
email_msg['Subject'] = 'Sua Fatura do mês está próxima de vencer!'

email_msg.attach(MIMEText(message, 'plain'))

server.sendmail(email_msg['From'] ,email_msg['To'], email_msg.as_string())
server.quit()