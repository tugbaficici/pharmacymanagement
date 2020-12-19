import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

def send_mail(self,event,to,bodytext):
    try:
        mail = smtplib.SMTP("smtp.gmail.com",587)
        mail.ehlo()
        mail.starttls()
        mail.login("opensourcepms@gmail.com", "kjdkdkd")

        mesaj = MIMEMultipart()
        mesaj["From"] = "opensourcepms@gmail.com" 
        mesaj["To"] = str(to)      
        mesaj["Subject"] = "Open Source PMS | İlaç Bilgileriniz" 

        body = bodytext

        body_text = MIMEText(body, "plain") 
        mesaj.attach(body_text)

        mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
        print("Success !")
        mail.close()

    except:
        print("Hata:", sys.exc_info()[0])