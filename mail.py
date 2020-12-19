import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

try:
    mail = smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login("opensourcepms@gmail.com", "passw")

    mesaj = MIMEMultipart()
    mesaj["From"] = "opensourcepms@gmail.com" 
    mesaj["To"] = "zekiahmetbayar1@gmail.com"         
    mesaj["Subject"] = "Open Source PMS | İlaç Bilgileriniz" 

    body = """

    Open source pms mail gönderme scripti.

    """

    body_text = MIMEText(body, "plain") 
    mesaj.attach(body_text)

    mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
    print("Success !")
    mail.close()

except:
    print("Hata:", sys.exc_info()[0])