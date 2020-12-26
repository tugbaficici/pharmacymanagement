#!/usr/bin/python3
# -*- coding: utf-8 -*-
import gi,sqlite3
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
gi.require_version('Gdk', '3.0')
from gi.repository import Gdk, GLib,Pango
from mail import send_mail
from qr import QRdanEkle
import datetime
from reportlab.pdfgen import canvas
from gi.repository.GdkPixbuf import Pixbuf

from islevselFonksiyonlar import *
from kullaniciFonksiyonlar import *
from searchBars import *
from guncelleFonksiyonlar import *
from addFonksiyonlar import *
from deleteFonksiyonlar import *
from veriCekmeFonksiyonlar import *
from clickFonksiyonlar import *

hasta_columns = ["ID", "TC NO", "First Name", "Last Name", "EMAIL"]
ilac_columns = ["ID", "NAME", "DOSE", "ACTIVE", "PIECE", "PRICE","FACTORY"]
cart_columns = ["ID", "NAME", "DOSE", "ACTIVE", "PIECE", "PRICE","FACTORY","COUNT"]
fabrika_columns = ["ID","NAME"]
ts_columns = ["NAME","ACTIVE","COUNT"]

TARGETS = [('MY_TREE_MODEL_ROW', Gtk.TargetFlags(2) , 0),
('text/plain', 0, 1),
('TEXT', 0, 2),('STRING', 0, 3),]
DRAG_ACTION = Gdk.DragAction.COPY

class MyWindow(Gtk.Window):

    def __init__(self):

        Gtk.Window.__init__(self)
        self.set_default_size(1300, 700)
        self.connect("destroy", Gtk.main_quit)
        self.set_title("Pharmacy Management System")
        self.main()

    def main(self):
        self.baglanti_baslat()
        self.giris_ekrani()

    #### Ekranlar #####

    # Giriş ekranı 
    def giris_ekrani(self):

        self.main_Table = Gtk.Table(n_rows=10, n_columns=10, homogeneous=True)
        main_Label = Gtk.Label(label = "Open Source Pharmacy Management Sysem")

        main_IdLabel = Gtk.Label(label = "ID : ")
        self.main_IdEntry = Gtk.Entry()

        main_PassLabel = Gtk.Label(label = "Password : ")
        self.main_PassEntry = Gtk.Entry()
        self.main_PassEntry.set_visibility(False)

        self.main_LoginButton = Gtk.Button(label = "Login")
        self.main_LoginButton.connect('clicked',kullanici_giris,self)
        self.main_RegisterButton = Gtk.Button(label = "Register")
        self.main_RegisterButton.connect('clicked',kullanici_kayit,self)

        self.main_Table.attach(main_Label,0,10,0,2)
        self.main_Table.attach(main_IdLabel,0,4,3,4)
        self.main_Table.attach(main_PassLabel,0,4,4,5)
        self.main_Table.attach(self.main_IdEntry,5,8,3,4)
        self.main_Table.attach(self.main_PassEntry,5,8,4,5)
        self.main_Table.attach(self.main_LoginButton,4,6,6,7)
        self.main_Table.attach(self.main_RegisterButton,4,6,7,8)

        self.add(self.main_Table)
        self.show_all()
    
    # Ana ekran 
    def ana_ekran(self):
        self.notebook = Gtk.Notebook()
        self.add(self.notebook)
        
        self.satis_ekrani()
        self.alis_ekrani()
        self.ilac_ekrani()
        self.settings_ekrani()

        self.page1 = Gtk.Box()
        self.page1.set_border_width(10)
        self.page1.set_homogeneous(True)
        self.page1.add(self.satis_Table)
        self.notebook.append_page(self.page1, Gtk.Label(label="Sell"))

        self.page2 = Gtk.Box()
        self.page2.set_border_width(10)
        self.page2.set_homogeneous(True)
        self.page2.add(self.alis_Table)
        self.notebook.append_page(self.page2, Gtk.Label(label="Buy"))

        self.page3 = Gtk.Box()
        self.page3.set_border_width(10)
        self.page3.set_homogeneous(True)
        self.page3.add(self.ilac_notebook)
        self.notebook.append_page(self.page3, Gtk.Label(label="Medicines"))

        self.hasta_listWindow()
        self.page4 = Gtk.Box()
        self.page4.set_border_width(20)
        self.page4.set_homogeneous(True)
        self.page4.add(self.hasta_listTable)
        self.notebook.append_page(self.page4, Gtk.Label(label="Patients"))

        self.page4 = Gtk.Box()
        self.page4.set_border_width(10)
        self.page4.set_homogeneous(True)
        self.page4.add(self.setting_table)
        self.notebook.append_page(self.page4, Gtk.Label(label="Settings"))       
    
        self.notebook.show_all()

    # Ayarlar ekranı 
    def settings_ekrani(self):

        self.setting_table = Gtk.Table(n_rows=10, n_columns=10, homogeneous=True)
        main_Label = Gtk.Label(label = "Open Source Pharmacy Management System")
        self.setting_LogoutButton = Gtk.Button(label = "Çıkış Yap")
        self.setting_LogoutButton.connect('clicked',log_out,self)
        self.setting_table.attach(main_Label,0,10,0,2)
        self.setting_table.attach(self.setting_LogoutButton,0,10,2,3)

    # Kayıt ekranı 
    def kayit_ekrani(self):

        self.kayit_Table = Gtk.Table(n_rows=10, n_columns=10, homogeneous=True)
        kayit_Label = Gtk.Label(label = "Open Source Pharmacy Management Sysem\nRegister")

        kayit_IdLabel = Gtk.Label(label = "ID : ")
        self.kayit_IdEntry = Gtk.Entry()

        kayit_PassLabel = Gtk.Label(label = "Password : ")
        self.kayit_PassEntry = Gtk.Entry()
        self.kayit_PassEntry.set_visibility(False)

        self.kayit_RegisterButton = Gtk.Button(label = "Register")
        self.kayit_RegisterButton.connect('clicked',kullanici_ekle,self)

        self.kayit_Table.attach(kayit_Label,0,10,0,2)
        self.kayit_Table.attach(kayit_IdLabel,0,4,3,4)
        self.kayit_Table.attach(kayit_PassLabel,0,4,4,5)
        self.kayit_Table.attach(self.kayit_IdEntry,5,8,3,4)
        self.kayit_Table.attach(self.kayit_PassEntry,5,8,4,5)
        self.kayit_Table.attach(self.kayit_RegisterButton,4,6,6,7)

        self.add(self.kayit_Table)
        self.show_all()

    # Satış ekranı 
    def satis_ekrani(self):
        
        self.hasta_tablo()
        self.satis_Table = Gtk.Table(n_rows=10, n_columns=10, homogeneous=False)

        satis_patienceLabel = Gtk.Label(label = "Patients")
        satis_patientSearch = Gtk.SearchEntry()
        satis_patientSearch.connect("activate",patients_searchBar,self)

        satis_patienceAddButton = Gtk.Button(label = "Add")
        satis_patienceAddButton.connect('clicked',hasta_ekle,self)
        
        self.cart_tablo()
        satis_cartLabel = Gtk.Label(label = "Cart")
        satis_cartCleanButton = Gtk.Button(label = "Clean")
        satis_cartCleanButton.connect('clicked',self.on_click_clean,1)

        pb = Pixbuf.new_from_file_at_size('qr-code.png', 30, 30)
        image = Gtk.Image()
        image.set_from_pixbuf(pb)
        satis_cartQRButton = Gtk.Button(label = "QR")
        satis_cartQRButton.set_image(image)
        satis_cartQRButton.set_image_position(Gtk.PositionType.TOP)
        satis_cartQRButton.set_always_show_image (True)
        satis_cartQRButton.connect('clicked',QRkodcekme,self)

        self.ilac_tablo()
        satis_medicineSearch = Gtk.SearchEntry()
        satis_medicineSearch.connect("activate",medicines_searchBar,self)

        satis_medicineLabel = Gtk.Label(label = "Medicines")

        self.satis_checkoutButton = Gtk.Button(label = "Checkout to Proceed")
        self.satis_checkoutButton.connect('clicked',self.proceedScreen)

        self.satis_Table.attach(satis_patienceLabel,0,3,0,1)
        self.satis_Table.attach(satis_patientSearch,0,2.5,1,2)
        self.satis_Table.attach(satis_patienceAddButton,2,3,1,2)
        self.satis_Table.attach(self.scroll_patientTable,0,3,2,5)

        self.satis_Table.attach(satis_cartLabel,0,1,5,6)
        self.satis_Table.attach(satis_cartCleanButton,1,2,5,6)
        self.satis_Table.attach(satis_cartQRButton,2,3,5,6)
        self.satis_Table.attach(self.scroll_cartTable,0,3,6,9)
    
        self.satis_Table.attach(satis_medicineLabel,3,10,0,1)
        self.satis_Table.attach(satis_medicineSearch,3,10,1,2)

        self.satis_Table.attach(self.scroll_medicineTable,3,10,2,10)
        self.satis_Table.attach(self.satis_checkoutButton,0,3,9,10)

        self.view.show_all()
        self.satis_Table.show_all()
    
    # Alış ekranı 
    def alis_ekrani(self):
        self.alis_Table = Gtk.Table(n_rows=10, n_columns=10, homogeneous=False)

        alis_factoriesLabel = Gtk.Label(label = "Factories")
        alis_searchEntry = Gtk.SearchEntry()
        alis_searchEntry.connect("activate",factory_SearchBar,self)

        alis_factoriesAddButton = Gtk.Button(label = 'Add')
        alis_factoriesAddButton.connect('clicked',fabrika_ekle,self)
        
        alis_cartLabel = Gtk.Label(label = "Cart")
        alis_cartCleanButton = Gtk.Button(label = "Clean")
        alis_cartCleanButton.connect('clicked',self.on_click_clean,2)

        alis_medicineSearch = Gtk.SearchEntry()
        alis_medicineLabel = Gtk.Label(label = "Medicines")
        alis_medicineSearch.connect("activate",medicines_searchBar2,self)

        self.alis_checkoutButton = Gtk.Button(label = "Checkout to Proceed")
        self.alis_checkoutButton.connect('clicked',self.proceedScreen2)

        self.fabrika_tablo()
        self.alis_Table.attach(alis_factoriesLabel,0,3,0,1)
        self.alis_Table.attach(alis_searchEntry,0,2.5,1,2)
        self.alis_Table.attach(alis_factoriesAddButton,2,3,1,2)
        self.alis_Table.attach(self.scroll_factoriesTable,0,3,2,5)

        self.cart_tablo2()
        self.alis_Table.attach(alis_cartLabel,0,2,5,6)
        self.alis_Table.attach(alis_cartCleanButton,2,3,5,6)
        self.alis_Table.attach(self.scroll_cartTable2,0,3,6,9)
    
        self.facilac_tablo()
        self.alis_Table.attach(alis_medicineLabel,3,10,0,1)
        self.alis_Table.attach(alis_medicineSearch,3,10,1,2)
        self.alis_Table.attach(self.scroll_fmedicineTable,3,10,2,10)
        self.alis_Table.attach(self.alis_checkoutButton,0,3,9,10)

        self.fabrika_view.show_all()
        self.alis_Table.show_all()
    
    # İlaç ekranı 
    def ilac_ekrani(self):
        self.ilac_notebook = Gtk.Notebook()

        self.ilac_addWindow()
        self.ilac_addPage = Gtk.Box()
        self.ilac_addPage.set_border_width(10)
        self.ilac_addPage.set_homogeneous(True)
        self.ilac_addPage.add(self.ilac_addTable)
        self.ilac_notebook.append_page(self.ilac_addPage, Gtk.Label(label="Add"))

        self.ilac_listWindow()
        self.ilac_listPage = Gtk.Box()
        self.ilac_listPage.set_border_width(10)
        self.ilac_listPage.set_homogeneous(True)
        self.ilac_listPage.add(self.ilac_listTable)
        self.ilac_notebook.append_page(self.ilac_listPage, Gtk.Label(label="List"))

        self.ts_listWindow()
        self.ts_listPage = Gtk.Box()
        self.ts_listPage.set_border_width(10)
        self.ts_listPage.set_homogeneous(True)
        self.ts_listPage.add(self.ts_listTable)
        self.ilac_notebook.append_page(self.ts_listPage, Gtk.Label(label="Disease Follow"))
        
        self.ilac_addTable.show_all()
    
    # İlaç listeleme ekranı
    def ilac_listWindow(self):
        self.ilac_tablo()
        self.ilac_listTable = Gtk.Table(n_rows=10, n_columns=10, homogeneous=False)
        self.ilac_listTable.attach(self.scroll_medicineTable,0,10,0,10)
        self.ilac_listTable.show_all()

    # Hastalık takibi ekranı
    def ts_listWindow(self):
        self.ts_tablo()
        self.ts_listTable = Gtk.Table(n_rows=10, n_columns=10, homogeneous=False)
        self.ts_listTable.attach(self.scroll_tsTable,0,10,0,10)
        self.ts_listTable.show_all()

    # İlaç ekleme ekranı
    def ilac_addWindow(self):
        self.ilac_addTable = Gtk.Table(n_rows=10, n_columns=10, homogeneous=False)

        self.ilac_nameEntry = Gtk.Entry()
        self.ilac_doseEntry = Gtk.Entry()
        self.ilac_activeEntry = Gtk.Entry()
        self.ilac_pieceEntry = Gtk.Entry()
        self.ilac_priceEntry = Gtk.Entry()
        self.ilac_factoryEntry = Gtk.Entry()
        self.ilac_prosEntry = Gtk.Entry()

        self.ilac_factoryEntry.set_text("Eczane Stok")
        
        ilac_nameLabel = Gtk.Label(label = "Name :")
        ilac_doseLabel = Gtk.Label(label = "Dose :")
        ilac_activeLabel = Gtk.Label(label = "Active :")
        ilac_pieceLabel = Gtk.Label(label = "Piece :")
        ilac_priceLabel = Gtk.Label(label = "Price :")
        ilac_factoryLabel = Gtk.Label(label = "Factory :")
        ilac_prosLabel = Gtk.Label(label = "Prospectus :")
        
        self.ilac_addButton = Gtk.Button(label = "Add") 
        self.ilac_addButton.connect('clicked',ilac_addButtonEvent,self)    
        
        self.ilac_addTable.attach(ilac_nameLabel,1,2,1,2)
        self.ilac_addTable.attach(self.ilac_nameEntry,3,5,1,2)

        self.ilac_addTable.attach(ilac_doseLabel,6,7,1,2)
        self.ilac_addTable.attach(self.ilac_doseEntry,8,10,1,2)

        self.ilac_addTable.attach(ilac_activeLabel,1,2,3,4)
        self.ilac_addTable.attach(self.ilac_activeEntry,3,5,3,4)

        self.ilac_addTable.attach(ilac_pieceLabel,6,7,3,4)
        self.ilac_addTable.attach(self.ilac_pieceEntry,8,10,3,4)

        self.ilac_addTable.attach(ilac_prosLabel,1,2,5,6)
        self.ilac_addTable.attach(self.ilac_prosEntry,3,5,5,6)

        self.ilac_addTable.attach(ilac_factoryLabel,6,7,5,6)
        self.ilac_addTable.attach(self.ilac_factoryEntry,8,10,5,6)

        self.ilac_addTable.attach(ilac_priceLabel,1,2,7,8)
        self.ilac_addTable.attach(self.ilac_priceEntry,3,5,7,8)
        
        self.ilac_addTable.attach(self.ilac_addButton,8,10,7,8)

        self.ilac_addTable.show_all()
    
    # Hasta listeleme ekranı
    def hasta_listWindow(self):
        self.hasta_tablo()
        self.hasta_listTable = Gtk.Table(n_rows=10, n_columns=10, homogeneous=False)
        self.hasta_listTable.attach(self.scroll_patientTable,0,10,0,10)
        self.hasta_listTable.show_all()

    ### Yan Ekranlar ###
    
    # Fatura ekranı
    def proceedScreen(self,event):
        try:
            self.proceedWindow = Gtk.Window()
            self.proceedWindow.set_title("Proceed to "+self.proceedPatName + " " + self.proceedPatSurname)
            self.proceedWindow.set_border_width(10)
            proceedTable = Gtk.Table(n_rows=10, n_columns=10, homogeneous=True)
            self.proceedWindow.add(proceedTable)
            proceedLabel = Gtk.Label(label= "Proceed to "+self.proceedPatName + " " + self.proceedPatSurname)
            proceedMedicineLabel = Gtk.Label(label = "Medicines")
            proceedTotal = Gtk.Label(label = "Total Amount of Proceed : ")
            amount=0
            medicines=""
            prospektuslinks=""
            for i in self.cartlistmodel:
                    amount+=float(i[5])*int(i[7])
                    medicines+=i[1]+"("+i[7]+"),"
                    prospektuslinks+=i[1]+" : "+i[8]+"""
"""
            proceedAmount = Gtk.Label(label = str(amount)+" ₺" )
            self.cursor.execute("INSERT INTO bills(PATIENTTC,MEDICINES,AMOUNT) Values(?,?,?)",(self.proceedPatTC,medicines,amount))
            self.con.commit() 
            proceedName = Gtk.Label(label = "Name : ")
            proceedSurname = Gtk.Label(label = "Surname : ")
            proceedTC = Gtk.Label(label = "TC No:")
            proceedMail = Gtk.Label(label = "Email : ")
            proceedAttention = Gtk.Label(label = "The prospectus will be sent to your e-mail. Healthy Days !")
            
            #prospektüs string oluşturulcak
            pdfname=self.proceedPatTC+"-"+str(datetime.datetime.now())
            create_invoice(self,pdfname)

            self.proceedButton = Gtk.Button(label = "Send")
            self.proceedButton.connect('clicked',send_mail,self,self.proceedPatMail,prospektuslinks,pdfname)
            self.proceedButton.connect('clicked',self.decrease_amount)
            self.proceedButton.connect('clicked',self.proceedex)
            self.proceedExit = Gtk.Button(label = "Exit")
            self.proceedExit.connect('clicked',self.proceedex)
            
            proceedTCLabel = Gtk.Label(label = self.proceedPatTC)
            proceedNameLabel = Gtk.Label(label = self.proceedPatName)
            proceedSurnameLabel = Gtk.Label(label = self.proceedPatSurname)
            proceedMailLabel = Gtk.Label(label = self.proceedPatMail)

            self.cart_tablo()
            proceedTable.attach(proceedLabel,4,6,0,1)
            proceedTable.attach(proceedMedicineLabel,0,5,1,2)
            proceedTable.attach(self.scroll_cartTable,0,5,2,8)
            proceedTable.attach(proceedTotal,0,2,8,10)
            proceedTable.attach(proceedAmount,2,4,8,10)
            
            proceedTable.attach(proceedTC,5,8,2,3)
            proceedTable.attach(proceedName,5,8,3,4)
            proceedTable.attach(proceedSurname,5,8,4,5)
            proceedTable.attach(proceedMail,5,8,5,6)
            
            proceedTable.attach(proceedTCLabel,8,10,2,3)
            proceedTable.attach(proceedNameLabel,8,10,3,4)
            proceedTable.attach(proceedSurnameLabel,8,10,4,5)
            proceedTable.attach(proceedMailLabel,8,10,5,6)

            proceedTable.attach(proceedAttention,5,10,7,8)
            proceedTable.attach(self.proceedButton,5,8,8,10)
            proceedTable.attach(self.proceedExit,8,10,8,10)

            self.proceedWindow.present()
            self.proceedWindow.show_all()
        
        except AttributeError:
            errorWin(self,"Please select a patient !")
            
    # Fabrika fatura ekranı
    def proceedScreen2(self,event):
        self.proceedWindow2 = Gtk.Window()
        self.proceedWindow2.set_title("Proceed to "+self.proceedPatFactory)
        self.proceedWindow2.set_border_width(10)

        proceedTable = Gtk.Table(n_rows=10, n_columns=10, homogeneous=True)
        self.proceedWindow2.add(proceedTable)

        proceedLabel = Gtk.Label(label= "Proceed to "+self.proceedPatFactory)
        proceedMedicineLabel = Gtk.Label(label = "Medicines")
        proceedTotal = Gtk.Label(label = "Total Amount of Proceed : ")
        amount=0
        medicines=""
        for i in self.cartlistmodel2:
                amount+=float(i[5])*int(i[7])
                medicines+=i[1]+"("+i[7]+"),"
        proceedAmount = Gtk.Label(label = str(amount)+" ₺" )
        self.cursor.execute("INSERT INTO factorybills(FACTORYNAME,MEDICINES,AMOUNT) Values(?,?,?)",(self.proceedPatFactory,medicines,amount))
        self.con.commit() 
        
        proceedName = Gtk.Label(label = "Factory Name : ")
        proceedAttention = Gtk.Label(label = "Healthy Days !")

        self.proceedButton2 = Gtk.Button(label = "Send")
        self.proceedButton2.connect('clicked',self.decrease_amount2)
        self.proceedButton2.connect('clicked',self.proceedex2)
        self.proceedExit2 = Gtk.Button(label = "Exit")
        self.proceedExit2.connect('clicked',self.proceedex2)
        
        proceedNameLabel = Gtk.Label(label = self.proceedPatFactory)
        self.cart_tablo2()
        proceedTable.attach(proceedLabel,4,6,0,1)
        proceedTable.attach(proceedMedicineLabel,0,5,1,2)
        proceedTable.attach(self.scroll_cartTable2,0,5,2,8)
        proceedTable.attach(proceedTotal,0,2,8,10)
        proceedTable.attach(proceedAmount,2,4,8,10)
        proceedTable.attach(proceedName,5,8,3,4)
        proceedTable.attach(proceedNameLabel,8,10,3,4)
        proceedTable.attach(proceedAttention,5,10,7,8)
        proceedTable.attach(self.proceedButton2,5,8,8,10)
        proceedTable.attach(self.proceedExit2,8,10,8,10)

        self.proceedWindow2.present()
        self.proceedWindow2.show_all()
    
    # Fatura ekranı kapatma butonu görevi
    def proceedex(self,event):
        self.proceedWindow.hide()

    # Stoktan ilaç düşme işlemini gerçekleştiren fonksiyon
    def decrease_amount(self,event):
        for i in self.cartlistmodel:
                count=int(i[4])-int(i[7])
                sellcount=int(i[7])+int(i[9])
                id=int(i[0])
                self.cursor.execute("UPDATE medicines SET PIECE=? , SELLCOUNT=? WHERE ID=?",(count,sellcount,id))
                self.con.commit()
        
        self.ilac_listmodel.clear()
        self.cartlistmodel.clear()
        self.geciciliste.clear()
        ilac_vericekme_query(self)

        for i in range(len(self.ilac_listesi)):
            self.ilac_listmodel.append(self.ilac_listesi[i]) 
        
    # Fabrika fatura ekranı kapatma butonu fonksiyonu
    def proceedex2(self,event):
        self.proceedWindow2.hide()

    # Fabrika stoğundan ilaç düşme işlemini gerçekleştiren fonksiyon
    def decrease_amount2(self,event):
        
        for i in self.cartlistmodel2:
                factorycount=int(i[4])-int(i[7])
                count=int(i[7])
                id=int(i[0])
                self.cursor.execute("UPDATE factorystock SET PIECE=? WHERE ID=?",(factorycount,id))
                self.con.commit()
                for j in self.ilac_listmodel:
                    if (id==int(j[0])):
                        pharmacycount=int(j[4])+count
                        self.cursor.execute("UPDATE medicines SET PIECE=? WHERE ID=?",(pharmacycount,id))
                        self.con.commit()

        self.ilac_listmodel.clear()
        self.facilac_listmodel.clear()
        self.cartlistmodel2.clear()
        self.controlfactory=""
        self.geciciliste2.clear()
        ilac_vericekme_query(self)
        facilac_vericekme_query(self,None)

        for i in range(len(self.ilac_listesi)):
            self.ilac_listmodel.append(self.ilac_listesi[i])

        for i in range(len(self.facilac_listesi)):
            self.facilac_listmodel.append(self.facilac_listesi[i])  
                
    ### Tablolar ###

    # Hastalık takibi tablosu
    ts_listmodel = Gtk.ListStore(str, str, str)
    def ts_tablo(self):
        ts_vericekme_query(self)
        self.ts_listmodel.clear()
        for i in range(len(self.ts_listesi)):
            self.ts_listmodel.append(self.ts_listesi[i])
        
        self.ts_view = Gtk.TreeView(model=self.ts_listmodel)
        for i, column in enumerate(ts_columns):
            cell = Gtk.CellRendererText()
            col = Gtk.TreeViewColumn(column, cell, text=i)
            self.ts_view.append_column(col)

        self.scroll_tsTable = Gtk.ScrolledWindow()
        self.scroll_tsTable.add(self.ts_view)
        self.scroll_tsTable.show_all()

    # Hasta tablosu
    listmodel = Gtk.ListStore(str, str, str,str,str)
    def hasta_tablo(self):
   
        hasta_vericekme_query(self)
        self.listmodel.clear()
        for i in range(len(self.hasta_listesi)):
            self.listmodel.append(self.hasta_listesi[i])
        
        self.view = Gtk.TreeView(model=self.listmodel)
        for i, column in enumerate(hasta_columns):
            cell = Gtk.CellRendererText()
            col = Gtk.TreeViewColumn(column, cell, text=i)
            self.view.append_column(col)
        
        self.view.connect('button-press-event' , tablo_rightClick,'patients',self)
        self.view.connect('button-press-event',tablo_leftClick,'patients',self)
        self.view.show_all()
        self.scroll_patientTable = Gtk.ScrolledWindow()
        self.scroll_patientTable.add(self.view)
        self.scroll_patientTable.show_all()

    # İlaç tablosu
    ilac_listmodel=Gtk.ListStore(str, str, str ,str ,str, str,str,str,str)
    def ilac_tablo(self):

        ilac_vericekme_query(self)
        self.ilac_listmodel.clear()
        for i in range(len(self.ilac_listesi)):
            self.ilac_listmodel.append(self.ilac_listesi[i])

        self.ilac_view = Gtk.TreeView(model=self.ilac_listmodel)
        for i, column in enumerate(ilac_columns):
            cell = Gtk.CellRendererText()
            col = Gtk.TreeViewColumn(column, cell, text=i)
            self.ilac_view.append_column(col)

        self.ilac_view.connect('button-press-event' ,tablo_rightClick,'medicines',self) 
        self.ilac_view.show_all()        

        self.ilac_view.enable_model_drag_source(Gdk.ModifierType.BUTTON1_MASK, TARGETS, DRAG_ACTION)
        self.ilac_view.connect("drag-data-get", self.on_drag_data_get)

        self.scroll_medicineTable = Gtk.ScrolledWindow()
        self.scroll_medicineTable.add(self.ilac_view)
        self.scroll_medicineTable.show_all()

    # Fabrika ilaç tablosu
    facilac_listmodel=Gtk.ListStore(str, str, str ,str ,str, str,str,str,str)
    def facilac_tablo(self):

        facilac_vericekme_query(self,None)
        self.facilac_listmodel.clear()
        for i in range(len(self.ilac_listesi)):
            self.facilac_listmodel.append(self.facilac_listesi[i])

        self.facilac_view = Gtk.TreeView(model=self.facilac_listmodel)
        for i, column in enumerate(ilac_columns):
            cell = Gtk.CellRendererText()
            col = Gtk.TreeViewColumn(column, cell, text=i)
            self.facilac_view.append_column(col)

        self.facilac_view.connect('button-press-event' ,tablo_rightClick,'medicines',self) 
        self.facilac_view.show_all()        

        self.facilac_view.enable_model_drag_source(Gdk.ModifierType.BUTTON1_MASK, TARGETS, DRAG_ACTION)
        self.facilac_view.connect("drag-data-get", self.on_drag_data_get)
        self.scroll_fmedicineTable = Gtk.ScrolledWindow()
        self.scroll_fmedicineTable.add(self.facilac_view)
        self.scroll_fmedicineTable.show_all()    

    # Fabrika tablosu
    factories_listmodel = Gtk.ListStore(str, str)
    def fabrika_tablo(self):
        fabrika_vericekme_query(self)
        self.factories_listmodel.clear()
        for i in range(len(self.fabrika_listesi)):
            self.factories_listmodel.append(self.fabrika_listesi[i])
        
        self.fabrika_view = Gtk.TreeView(model=self.factories_listmodel)
        for i, column in enumerate(fabrika_columns):
            cell = Gtk.CellRendererText()
            col = Gtk.TreeViewColumn(column, cell, text=i)
            self.fabrika_view.append_column(col)
        
        self.fabrika_view.connect('button-press-event' , tablo_rightClickFac,'factories',self)
        self.fabrika_view.connect('button-press-event' , tablo_leftClickFac,'factories',self)
        
        self.fabrika_view.show_all()

        self.scroll_factoriesTable = Gtk.ScrolledWindow()
        self.scroll_factoriesTable.add(self.fabrika_view)
        self.scroll_factoriesTable.show_all()

    # Sepet tablosu
    cartlistmodel = Gtk.ListStore(str, str, str ,str ,str, str,str,str,str,str)
    def cart_tablo(self):

        self.cart_view = Gtk.TreeView(model=self.cartlistmodel)
        for i, column in enumerate(cart_columns):
            cell = Gtk.CellRendererText()
            col = Gtk.TreeViewColumn(column, cell, text=i)
            self.cart_view.append_column(col)

        self.cart_view.enable_model_drag_dest(TARGETS, DRAG_ACTION)
        self.cart_view.connect("drag-data-received", self.on_drag_data_received)

        self.cart_view.connect('button-press-event' , tablo_rightClick,'cart',self)
        self.cart_view.connect('button-press-event', tablo_leftClick,'cart',self)
        self.cart_view.show_all()

        self.scroll_cartTable = Gtk.ScrolledWindow()
        self.scroll_cartTable.add(self.cart_view)
        self.cart_view.show_all()

    # Fabrika sepet tablosu
    cartlistmodel2 = Gtk.ListStore(str, str, str ,str ,str, str,str,str,str,str)
    def cart_tablo2(self):

        self.cart_view2 = Gtk.TreeView(model=self.cartlistmodel2)
        for i, column in enumerate(cart_columns):
            cell = Gtk.CellRendererText()
            col = Gtk.TreeViewColumn(column, cell, text=i)
            self.cart_view2.append_column(col)

        self.cart_view2.enable_model_drag_dest(TARGETS, DRAG_ACTION)
        self.cart_view2.connect("drag-data-received", self.on_drag_data_received2)

        self.cart_view2.connect('button-press-event' , tablo_rightClick,'cart2',self)
        self.cart_view2.show_all()

        self.scroll_cartTable2 = Gtk.ScrolledWindow()
        self.scroll_cartTable2.add(self.cart_view2)
        self.cart_view2.show_all()

    ###Drag and Drop

    # Seçilen ilacın alınması
    def on_drag_data_get(self, widget, drag_context, data, info, time):
        select = widget.get_selection()
        model, treeiter = select.get_selected()
        
        self.Dragliste=list()
        for i in model[treeiter]:
            self.Dragliste.append(i)
  
    geciciliste=list()
    geciciliste2=list()

    # Satışta alınan verinin tutulması
    def on_drag_data_received(self, widget, drag_context, x, y, data, info, time):
        if self.Dragliste[0] in self.geciciliste:
            pass
        else:
            self.ddKutuSayisi = Gtk.Window()
            self.ddKutuSayisi.set_title("Box")
            self.ddKutuSayisi.set_border_width(10)
            self.ddKutuSayisiTable = Gtk.Table(n_rows=2, n_columns=0, homogeneous=True)
            self.ddKutuSayisi.add(self.ddKutuSayisiTable)
            self.ddKutuSayisi_sayi = Gtk.Entry()
            self.ddKutuSayisi_button = Gtk.Button(label ="Send")
            self.ddKutuSayisi_button.connect('clicked',self.cartUpdate)
            self.ddKutuSayisi_sayi.set_placeholder_text("Piece")
            self.ddKutuSayisiTable.attach(self.ddKutuSayisi_sayi,0,1,0,1)
            self.ddKutuSayisiTable.attach(self.ddKutuSayisi_button,0,1,1,2)
            self.ddKutuSayisi.present()
            self.ddKutuSayisi.show_all()
    
    # Fabrikadan alınan ürünün tutulması
    def on_drag_data_received2(self, widget, drag_context, x, y, data, info, time):
        if self.Dragliste[0] in self.geciciliste2:
            pass
        else:
            self.ddKutuSayisi2 = Gtk.Window()
            self.ddKutuSayisi2.set_title("Box")
            self.ddKutuSayisi2.set_border_width(10)
            self.ddKutuSayisiTable2 = Gtk.Table(n_rows=2, n_columns=0, homogeneous=True)
            self.ddKutuSayisi2.add(self.ddKutuSayisiTable2)
            self.ddKutuSayisi_sayi2 = Gtk.Entry()
            self.ddKutuSayisi_button2 = Gtk.Button(label ="Send")
            self.ddKutuSayisi_button2.connect('clicked',self.cartUpdate2)
            self.ddKutuSayisi_sayi2.set_placeholder_text("Piece")
            self.ddKutuSayisiTable2.attach(self.ddKutuSayisi_sayi2,0,1,0,1)
            self.ddKutuSayisiTable2.attach(self.ddKutuSayisi_button2,0,1,1,2)
            self.ddKutuSayisi2.present()
            self.ddKutuSayisi2.show_all()
    
    # Satılan ilacın sepete eklenmesi
    def cartUpdate(self,event):
        if(int(self.Dragliste[4])>=int(self.ddKutuSayisi_sayi.get_text())):
            self.geciciliste.append(self.Dragliste[0])
            a=self.Dragliste[7]
            b=self.Dragliste[8]
            self.Dragliste.pop()
            self.Dragliste.pop()
            self.ddKutuSayisi.hide()
            self.Dragliste.append(self.ddKutuSayisi_sayi.get_text())
            self.Dragliste.append(a)
            self.Dragliste.append(b)
            self.cartlistmodel.append(self.Dragliste)
        else:
            errorWin(self,"Out of stock !")
    
    controlfactory=""
    
    # Fabrikadan alınan ilacın sepete eklenmesi
    def cartUpdate2(self,event):
        if((self.controlfactory== self.Dragliste[6]) or (self.controlfactory=="")):
            if(int(self.Dragliste[4])>=int(self.ddKutuSayisi_sayi2.get_text())):
                self.controlfactory=self.Dragliste[6]
                self.geciciliste2.append(self.Dragliste[0])
                a=self.Dragliste[7]
                b=self.Dragliste[8]
                self.Dragliste.pop()
                self.Dragliste.pop()
                self.ddKutuSayisi2.hide()
                self.Dragliste.append(self.ddKutuSayisi_sayi2.get_text())
                self.Dragliste.append(a)
                self.Dragliste.append(b)
                self.cartlistmodel2.append(self.Dragliste)
            else:
                errorWin(self,"Out of stock !")
        else:
            errorWin(self,"Please select same factory !")
        
    # Veri tabanı bağlantısı başlatan fonksiyon
    def baglanti_baslat(self):
        self.con = sqlite3.connect('pharmacy.db')
        self.cursor = self.con.cursor()
    
    # Sepet temizleme butonu görevi
    def on_click_clean(self,event,carttip):
        if(carttip==1):
            self.cartlistmodel.clear()
            self.geciciliste.clear()
        if(carttip==2):
            self.cartlistmodel2.clear()
            self.controlfactory=""
            self.geciciliste2.clear()


window = MyWindow()
window.show_all()
Gtk.main()