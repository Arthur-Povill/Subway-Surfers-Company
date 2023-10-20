import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from panel import models as admin_models

class email:
    def __init__(self):
        smtp_host = admin_models.configsApplication.objects.get(name='smtp_host_recovery').value
        smtp_port = int(admin_models.configsApplication.objects.get(name='smtp_port_recovery').value)
        self.smtp_email  = admin_models.configsApplication.objects.get(name='smtp_email_recovery').value
        smtp_password = admin_models.configsApplication.objects.get(name='smtp_password_recovery').value
        try:
            self.server = smtplib.SMTP(smtp_host, smtp_port)
            self.server.ehlo()
            self.server.starttls()
            self.server.login(self.smtp_email, smtp_password)
        except Exception as e:
            print("Erro ao enviar o e-mail:", e)

    def send(self, email, subject, body):
        msg = MIMEMultipart()
        msg['From'] = self.smtp_email
        msg['To'] = email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        self.server.sendmail(self.smtp_email, email, msg.as_string())
        self.server.quit()