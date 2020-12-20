# Importing Required Module
from reportlab.pdfgen import canvas

def create_invoice():
    # Creating Canvas
    c = canvas.Canvas("invoice.pdf",pagesize=(200,250),bottomup=0)
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

    patient = ["Ali Veli","4950@gmail.com"]

    c.drawRightString(90,90,patient[0])
    c.drawRightString(110,100,patient[1])

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

    cartlist = [["1","Parol","10","20"],["1","Minoset","20","12"]]
    y = 128
    margin = 0
    total = 0
    for i in cartlist:
        amount = int(i[2]) * int(i[3])
        c.drawCentredString(25,y + margin,i[0])
        c.drawCentredString(75,y + margin,i[1])
        c.drawCentredString(125,y + margin,i[2] + " TL")
        c.drawCentredString(148,y + margin,i[3])
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

create_invoice()
