#!/usr/bin/python3
# -*- coding: utf-8 -*-
import gi,sqlite3
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
gi.require_version('Gdk', '3.0')
from gi.repository import Gdk, GLib,Pango

hasta_columns = ["ID", "TC NO", "First Name", "Last Name", "EMAIL"]
ilac_columns = ["ID", "NAME", "DOSE", "ACTIVE", "PIECE", "PRICE"]

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

    def giris_ekrani(self):

        self.main_Table = Gtk.Table(n_rows=10, n_columns=10, homogeneous=True)
        main_Label = Gtk.Label(label = "Open Source Pharmacy Management Sysem")

        main_IdLabel = Gtk.Label(label = "ID : ")
        self.main_IdEntry = Gtk.Entry()

        main_PassLabel = Gtk.Label(label = "Password : ")
        self.main_PassEntry = Gtk.Entry()
        self.main_PassEntry.set_visibility(False)

        self.main_LoginButton = Gtk.Button(label = "Login")
        self.main_LoginButton.connect('clicked',self.kullanici_giris)
        self.main_RegisterButton = Gtk.Button(label = "Register")
        self.main_RegisterButton.connect('clicked',self.kullanici_kayit)

        self.main_Table.attach(main_Label,0,10,0,2)
        self.main_Table.attach(main_IdLabel,0,4,3,4)
        self.main_Table.attach(main_PassLabel,0,4,4,5)
        self.main_Table.attach(self.main_IdEntry,5,8,3,4)
        self.main_Table.attach(self.main_PassEntry,5,8,4,5)
        self.main_Table.attach(self.main_LoginButton,4,6,6,7)
        self.main_Table.attach(self.main_RegisterButton,4,6,7,8)

        self.add(self.main_Table)
        self.show_all()
    
    def kayit_ekrani(self):

        self.kayit_Table = Gtk.Table(n_rows=10, n_columns=10, homogeneous=True)
        kayit_Label = Gtk.Label(label = "Open Source Pharmacy Management Sysem\nRegister")

        kayit_IdLabel = Gtk.Label(label = "ID : ")
        self.kayit_IdEntry = Gtk.Entry()

        kayit_PassLabel = Gtk.Label(label = "Password : ")
        self.kayit_PassEntry = Gtk.Entry()
        self.kayit_PassEntry.set_visibility(False)

        self.kayit_RegisterButton = Gtk.Button(label = "Register")
        self.kayit_RegisterButton.connect('clicked',self.kullanici_ekle)

        self.kayit_Table.attach(kayit_Label,0,10,0,2)
        self.kayit_Table.attach(kayit_IdLabel,0,4,3,4)
        self.kayit_Table.attach(kayit_PassLabel,0,4,4,5)
        self.kayit_Table.attach(self.kayit_IdEntry,5,8,3,4)
        self.kayit_Table.attach(self.kayit_PassEntry,5,8,4,5)
        self.kayit_Table.attach(self.kayit_RegisterButton,4,6,6,7)

        self.add(self.kayit_Table)
        self.show_all()
    
    def ana_ekran(self):
        self.notebook = Gtk.Notebook()
        self.add(self.notebook)
        
        self.satis_ekrani()
        self.alis_ekrani()
        
        self.page1 = Gtk.Box()
        self.page1.set_border_width(10)
        self.page1.set_homogeneous(True)
        self.page1.add(self.satis_Table)
        self.notebook.append_page(self.page1, Gtk.Label(label="Sell"))

        self.page2 = Gtk.Box()
        self.page2.set_border_width(10)
        self.page2.set_homogeneous(True)
        self.page2.add(self.alis_Table)
        self.page2.add(self.satis_Table)
        self.notebook.append_page(self.page2, Gtk.Label(label="Buy"))

        self.page3 = Gtk.Box()
        self.page3.set_border_width(10)
        self.page3.add(Gtk.Label(label="Default Page!"))
        self.notebook.append_page(self.page3, Gtk.Label(label="Medicines"))

        self.page4 = Gtk.Box()
        self.page4.set_border_width(10)
        self.page4.add(Gtk.Label(label="Default Page!"))
        self.notebook.append_page(self.page4, Gtk.Label(label="Patients"))

        self.page4 = Gtk.Box()
        self.page4.set_border_width(10)
        self.page4.add(Gtk.Label(label="Default Page!"))
        self.notebook.append_page(self.page4, Gtk.Label(label="Settings"))       
    
        self.notebook.show_all()

    def satis_ekrani(self):
        
        self.hasta_tablo()
        
        self.satis_Table = Gtk.Table(n_rows=10, n_columns=10, homogeneous=False)

        satis_patienceLabel = Gtk.Label(label = "Patients")
        satis_patientSearch = Gtk.SearchEntry()
        #satis_searchEntry.connect("activate")
        satis_patienceAddButton = Gtk.Button(label = "Add")
        satis_patienceAddButton.connect('clicked',self.hasta_ekle)
        
        self.cart_tablo()
        satis_cartLabel = Gtk.Label(label = "Cart")
        satis_cartCleanButton = Gtk.Button(label = "Clean")

        self.ilac_tablo()

        satis_medicineSearch = Gtk.SearchEntry()
        satis_medicineLabel = Gtk.Label(label = "Medicines")

        self.satis_Table.attach(satis_patienceLabel,0,3,0,1)
        self.satis_Table.attach(satis_patientSearch,0,2.5,1,2)
        self.satis_Table.attach(satis_patienceAddButton,2,3,1,2)
        self.satis_Table.attach(self.view,0,3,2,5)

        self.satis_Table.attach(satis_cartLabel,0,2,6,7)
        self.satis_Table.attach(satis_cartCleanButton,2,3,6,7)
        self.satis_Table.attach(self.cart_view,0,3,7,10)
    
        self.satis_Table.attach(satis_medicineLabel,3,10,0,1)
        self.satis_Table.attach(satis_medicineSearch,3,10,1,2)

        self.satis_Table.attach(self.ilac_view,3,10,2,10)

        self.view.show_all()
        self.satis_Table.show_all()
    
    def alis_ekrani(self):

        self.alis_Table = Gtk.Table(n_rows=10, n_columns=10, homogeneous=False)

        alis_factoriesLabel = Gtk.Label(label = "Factories")
        alis_searchEntry = Gtk.SearchEntry()
        #satis_searchEntry.connect("activate")
        
        alis_cartLabel = Gtk.Label(label = "Cart")
        alis_cartCleanButton = Gtk.Button(label = "Clean")

        alis_medicineSearch = Gtk.SearchEntry()
        alis_medicineLabel = Gtk.Label(label = "Medicines")

        self.alis_Table.attach(alis_factoriesLabel,0,3,0,1)
        self.alis_Table.attach(alis_searchEntry,0,3,1,2)
        self.alis_Table.attach(self.view,0,3,2,5)

        self.alis_Table.attach(alis_cartLabel,0,2,6,7)
        self.alis_Table.attach(alis_cartCleanButton,2,3,6,7)
        self.alis_Table.attach(self.view,0,3,7,10)
    
        self.alis_Table.attach(alis_medicineLabel,3,10,0,1)
        self.alis_Table.attach(alis_medicineSearch,3,10,1,2)

        self.alis_Table.attach(self.view,3,10,2,10)

        self.alis_Table.show_all()

    ### Yan Ekranlar ###
    def hasta_ekle(self,event):
        self.add_PatientWindow = Gtk.Window()
        self.add_PatientWindow.set_title("Add New Patient")
        self.add_PatientWindow.set_border_width(10)

        add_PatientWindowTable = Gtk.Table(n_rows=9, n_columns=0, homogeneous=True)
        self.add_PatientWindow.add(add_PatientWindowTable)

        self.tcnumber = Gtk.Entry()
        self.name = Gtk.Entry()
        self.surname = Gtk.Entry()
        self.email = Gtk.Entry()

        self.add_PatientButton = Gtk.Button(label ="Send")
        self.add_PatientButton.connect('clicked',self.add_NewPatient)
  
        self.tcnumber.set_placeholder_text("TC Number (11)")
        self.name.set_placeholder_text("Patient Name")
        self.surname.set_placeholder_text("Patient Surname")
        self.email.set_placeholder_text("Email (Optional)")

        add_PatientWindowTable.attach(self.tcnumber,0,1,0,1)
        add_PatientWindowTable.attach(self.name,0,1,2,3)
        add_PatientWindowTable.attach(self.surname,0,1,4,5)
        add_PatientWindowTable.attach(self.email,0,1,6,7)
        add_PatientWindowTable.attach(self.add_PatientButton,0,1,8,9)

        self.add_PatientWindow.present()
        self.add_PatientWindow.show_all()

    ### Tablolar ###

    def hasta_tablo(self):
        self.hasta_vericekme_query()
        listmodel = Gtk.ListStore(str, str, str,str,str)
        for i in range(len(self.hasta_listesi)):
            listmodel.append(self.hasta_listesi[i])
        
        self.view = Gtk.TreeView(model=listmodel)
        for i, column in enumerate(hasta_columns):
            cell = Gtk.CellRendererText()
            col = Gtk.TreeViewColumn(column, cell, text=i)
            self.view.append_column(col)
        self.view.show_all()

    def ilac_tablo(self):
        self.ilac_vericekme_query()
        listmodel = Gtk.ListStore(str, str, str ,str ,str, str)
        for i in range(len(self.ilac_listesi)):
            listmodel.append(self.ilac_listesi[i])

        self.ilac_view = Gtk.TreeView(model=listmodel)
        for i, column in enumerate(ilac_columns):
            cell = Gtk.CellRendererText()
            col = Gtk.TreeViewColumn(column, cell, text=i)
            self.ilac_view.append_column(col)

    def cart_tablo(self):
        listmodel = Gtk.ListStore(str, str, str ,str ,str, str)
        #for i in range(len(self.ilac_listesi)):
        #    listmodel.append(self.ilac_listesi[i])

        self.cart_view = Gtk.TreeView(model=listmodel)
        for i, column in enumerate(ilac_columns):
            cell = Gtk.CellRendererText()
            col = Gtk.TreeViewColumn(column, cell, text=i)
            self.cart_view.append_column(col)


    #### Veri Tabanı Fonksiyonları ####

    def baglanti_baslat(self):
        self.con = sqlite3.connect('pharmacy.db')
        self.cursor = self.con.cursor()
    
    def kullanici_ekle_query(self,ids,passw):
        self.cursor.execute("INSERT INTO users(USERNAME,PASSWORD) Values(?,?)",(ids,passw))
        self.con.commit()
    
    def kullanici_giris_query(self,ids,passw):
        self.cursor.execute("SELECT * FROM users WHERE USERNAME == ? AND PASSWORD == ?",(ids,passw))
        liste = self.cursor.fetchall()

        if len(liste) == 1:
            self.remove(self.main_Table)
            self.ana_ekran()
        else:
            self.main_hataLabel = Gtk.Label(label = "Wrong credentials!")
            self.main_Table.attach(self.main_hataLabel,2,8,8,9)
            self.main_Table.show_all()

    def add_NewPatient(self,event):

        tc = self.tcnumber.get_text()
        name = self.name.get_text()
        surname = self.surname.get_text()
        email = self.email.get_text()

        self.cursor.execute("INSERT INTO patients(TC,NAME,SURNAME,EMAIL) Values(?,?,?,?)",(tc,name,surname,email))
        self.con.commit()

        self.add_PatientWindow.hide()
        self.notebook.remove(self.page1)
        self.satis_ekrani()

        self.page1 = Gtk.Box()
        self.page1.set_border_width(10)
        self.page1.set_homogeneous(True)
        self.page1.add(self.satis_Table)

        self.notebook.prepend_page(self.page1, Gtk.Label(label = "Sell"))
        self.notebook.show_all()
        page_number = self.notebook.page_num(self.page1)
        self.notebook.set_current_page(page_number)
        
    def hasta_vericekme_query(self):
        self.cursor.execute("SELECT * FROM patients")
        hasta_list = self.cursor.fetchall()
        self.hasta_listesi = list()
        for i in list(hasta_list):
            gecici_liste = list()
            for j in i:
                gecici_liste.append(str(j))
            
            self.hasta_listesi.append(gecici_liste)
        
        print(self.hasta_listesi)

    
    def ilac_vericekme_query(self):
        self.cursor.execute("SELECT * FROM medicines")
        ilac_list = self.cursor.fetchall()
        self.ilac_listesi = list()
        for i in list(ilac_list):
            gecici_liste = list()
            for j in i:
                gecici_liste.append(str(j))
            
            self.ilac_listesi.append(gecici_liste)






    #### Prio 2 Veri Tabanı Fonksiyonları ####
    
    def kullanici_ekle(self,event):
        ids = self.kayit_IdEntry.get_text()
        passw = self.kayit_PassEntry.get_text()
        self.kullanici_ekle_query(ids,passw)

        self.remove(self.kayit_Table)
        self.giris_ekrani()
    
    def kullanici_kayit(self,event):
        self.remove(self.main_Table)
        self.kayit_ekrani()

    def kullanici_giris(self,event):
        ids = self.main_IdEntry.get_text()
        passw = self.main_PassEntry.get_text()
        self.kullanici_giris_query(ids,passw)
    
    

window = MyWindow()
window.show_all()
Gtk.main()