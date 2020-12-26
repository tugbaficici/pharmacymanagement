
from qr import QRdanEkle
from reportlab.pdfgen import canvas
from datetime import date
import gi,sqlite3
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# QR kod çekme fonksiyonu
def QRkodcekme(event,self):
        ###
        ### Kameradan çıkmak için ESCYE basılması gerekir.
        ###
        #yakalanan="5 Parol 500 Parasetamol"
        yakalanan=QRdanEkle(self)
        ilaclar = yakalanan.split(',')
        for ilac in ilaclar:
            x=ilac.split()
            self.Dragliste=list()
            for i in self.ilac_listmodel:
                if(x[0]==i[0]):
                    for a in i:
                        self.Dragliste.append(a)

            if self.Dragliste[0] in self.geciciliste:
                pass
            else:
                if(int(self.Dragliste[4])>=int(x[2])):
                    self.geciciliste.append(self.Dragliste[0])
                    a=self.Dragliste[7]
                    b=self.Dragliste[8]
                    self.Dragliste.pop()
                    self.Dragliste.pop()
                    self.Dragliste.append(x[2])
                    self.Dragliste.append(a)
                    self.Dragliste.append(b)
                    self.cartlistmodel.append(self.Dragliste)
                else:
                    errorWin(self,"Out of stock " + x[1].upper() + "!")

# Fatura oluşturma fonksiyonu
def create_invoice(self,pdfname):
        # Creating Canvas
        today = date.today()
    
        c = canvas.Canvas("/tmp/invoices/"+pdfname+".pdf",pagesize=(200,250),bottomup=0)
        c.translate(10,40)
        c.scale(1,-1)
        c.drawImage("logo.jpg",0,0,width=50,height=30)

        c.scale(1,-1)
        c.translate(-10,-40)
        c.setFont("Helvetica-Bold",10)
        c.drawCentredString(125,20,"Open Source PMS")

        c.line(70,22,180,22)
        c.setFont("Helvetica-Bold",5)
        c.drawCentredString(125,30,"Halkali Cad. No: 281")
        c.drawCentredString(125,35," Halkali Mahallesi,Küçükçekmece / ISTANBUL ")
        # Changing the font size for Specifying GST Number of firm
        c.setFont("Helvetica-Bold",6)
        c.drawCentredString(125,42,"P.K.:34303")

        # Line Seprating the page header from the body
        c.line(5,45,195,45)

        # Document Information
        # Changing the font for Document title
        c.setFont("Courier-Bold",8)
        c.drawCentredString(100,55,"PHARMACY INVOICE")

        # This Block Consist of Costumer Details
        c.roundRect(15,63,170,40,10,stroke=1,fill=0)
        c.setFont("Times-Bold",5)
        c.drawRightString(70,70,"INVOICE No. :")
        c.drawRightString(70,80,"DATE :")
        c.drawRightString(70,90,"CUSTOMER NAME :")
        c.drawRightString(70,100,"E-MAIL :")
        

        c.drawCentredString(90,80,str(today))
        c.drawCentredString(97,90,self.proceedPatName + " " + self.proceedPatSurname )
        c.drawCentredString(105,100,self.proceedPatMail)

        # This Block Consist of Item Description
        c.roundRect(15,108,170,130,10,stroke=1,fill=0)
        c.line(15,120,185,120)
        c.drawCentredString(25,118,"ID")
        c.drawCentredString(75,118,"NAME")
        c.drawCentredString(125,118,"PRIECE")
        c.drawCentredString(148,118,"PIECE")
        c.drawCentredString(173,118,"TOTAL")

        # Drawing table for Item Description
        c.line(15,210,185,210)
        c.line(35,108,35,220)
        c.line(115,108,115,220)
        c.line(135,108,135,220)
        c.line(160,108,160,220)

        y = 128
        margin = 0
        total = 0
        for i in self.cartlistmodel:
            amount = float(i[5]) * float(i[7])
            c.drawCentredString(25,y + margin,i[0])
            c.drawCentredString(75,y + margin,i[1])
            c.drawCentredString(125,y + margin,i[5] + " TL")
            c.drawCentredString(148,y + margin,i[7])
            c.drawCentredString(173,y + margin,str(amount) + " TL")
            total += amount
            margin += 5
        
        c.drawCentredString(173,y + margin + 5 ,str(total) + " TL")

        # Declaration and Signature
        c.line(15,220,185,220)
        c.line(100,220,100,238)
        c.drawString(20,225,"The prospectus and your invoice ")
        c.drawString(20,230,"will be sent to your e-mail.")
        c.drawString(20,235,"Healthy Days !")
        c.drawRightString(180,235,"OpenSourcePMS\nDigital Signature")

        # End the Page and Start with new
        c.showPage()
        # Saving the PDF
        c.save()

# Error ekranı
def errorWin(self,error_text):
        global errorWindow
        errorWindow = Gtk.Window()
        errorWindow.set_title("Error !")
        errorWindow.set_border_width(10)

        errorTable = Gtk.Table(n_rows=2, n_columns=1, homogeneous=True)
        errorWindow.add(errorTable)

        errorLabel = Gtk.Label(label = error_text)
        errorButton = Gtk.Button(label ="Close")
        errorButton.connect('clicked',error_close,self)
  
        errorTable.attach(errorLabel,0,1,0,1)
        errorTable.attach(errorButton,0,1,1,2)

        errorWindow.present()
        errorWindow.show_all()

# Error ekranı kapatma butonu görevi
def error_close(self,event):
        errorWindow.hide()