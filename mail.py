import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

try:
    mail = smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login("opensourcepms@gmail.com", "123123123Aa*")

    mesaj = MIMEMultipart()
    mesaj["From"] = "opensourcepms@gmail.com" 
    mesaj["To"] = "bayar.zeki@std.izu.edu.tr"         
    mesaj["Subject"] = "Open Source PMS | İlaç Bilgileriniz" 

    body = """
    
    İlaç Adı | Günde kaç kere kullanılacak | Hebekl hübele prospektüs

    """

    body_text = MIMEText(body, "plain") 
    mesaj.attach(body_text)

    mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
    print("Success !")
    mail.close()

except:
    print("Hata:", sys.exc_info()[0])