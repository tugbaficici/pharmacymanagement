import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import sys

def send_mail(even,self,to,bodytext,pdfname):
    try:
        mail = smtplib.SMTP("smtp.gmail.com",587)
        mail.ehlo()
        mail.starttls()
        mail.login("opensourcepms@gmail.com", "sifre")

        mesaj = MIMEMultipart()
        mesaj["From"] = "opensourcepms@gmail.com" 
        mesaj["To"] = str(to)      
        mesaj["Subject"] = "Open Source PMS | İlaç Bilgileriniz" 

        body ="""Open Source PMS | İlaç Bilgileriniz

Eczanemizden temin ettiğiniz ilaçların prospektüs bilgileri ve satın alımınıza ait faturanız ektedir.

""" +bodytext+"""

Sağlıklı günler dileriz.
Open Source PMS
"""
         
        body_text = MIMEText(body, "plain") 
        mesaj.attach(body_text)
        attach_file_name = '/tmp/invoices/'+pdfname+'.pdf'
        attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
        payload = MIMEBase('application', 'octate-stream')
        payload.set_payload((attach_file).read())
        encoders.encode_base64(payload) #encode the attachment
        payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
        mesaj.attach(payload)

        mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
        print("Success !")
        mail.close()

    except:
        print("Hata:", sys.exc_info()[0])