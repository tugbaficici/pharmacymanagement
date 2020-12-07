#!/usr/bin/python3
# -*- coding: utf-8 -*-
import gi,sqlite3
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
gi.require_version('Gdk', '3.0')
from gi.repository import Gdk, GLib,Pango


columns = ["First Name",
           "Last Name",
           "Phone Number"]

phonebook = [["Jurg", "Billeter", "555-0123"],
             ["Johannes", "Schmid", "555-1234"],
             ["Julita", "Inca", "555-2345"],
             ["Javier", "Jardon", "555-3456"],
             ["Jason", "Clinton", "555-4567"],
             ["Random J.", "Hacker", "555-5678"]]

class MyWindow(Gtk.Window):

    def __init__(self):

        Gtk.Window.__init__(self)
        self.set_default_size(1300, 700)
        self.connect("destroy", Gtk.main_quit)
        self.set_title("Pharmacy Management System")
        self.main()

    def main(self):

        self.baglanti_baslat()
        self.kullanici_tablo_olustur()
        self.ana_ekran()

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

    satis_Table = Gtk.Table(n_rows=10, n_columns=10, homogeneous=True)
    
    def satis_ekrani(self):
        
        self.tablo_gosterimi()

        satis_patienceLabel = Gtk.Label(label = "Patients")
        satis_patientSearch = Gtk.SearchEntry()
        #satis_searchEntry.connect("activate")
        satis_patienceAddButton = Gtk.Button(label = "Add")
        
        satis_cartLabel = Gtk.Label(label = "Cart")
        satis_cartCleanButton = Gtk.Button(label = "Clean")

        satis_medicineSearch = Gtk.SearchEntry()
        satis_medicineLabel = Gtk.Label(label = "Medicines")

        #self.add(self.satis_Table)
        self.satis_Table.attach(satis_patienceLabel,0,3,0,1)
        self.satis_Table.attach(satis_patientSearch,0,2,1,2)
        self.satis_Table.attach(satis_patienceAddButton,2,3,1,2)
        self.satis_Table.attach(self.view,0,3,2,5)

        self.tablo_gosterimi()

        self.satis_Table.attach(satis_cartLabel,0,2,6,7)
        self.satis_Table.attach(satis_cartCleanButton,2,3,6,7)
        self.satis_Table.attach(self.view,0,3,7,10)
    
        

        self.satis_Table.attach(satis_medicineLabel,3,10,0,1)
        self.satis_Table.attach(satis_medicineSearch,3,10,1,2)
        self.tablo_gosterimi()
        self.satis_Table.attach(self.view,3,10,2,10)

        self.satis_Table.show_all()

    
    def ana_ekran(self):
        self.notebook = Gtk.Notebook()
        self.add(self.notebook)
        self.satis_ekrani()
        
        
        self.page1 = Gtk.Box()
        self.page1.set_border_width(10)
        self.page1.set_homogeneous(True)
        self.page1.add(self.satis_Table)
        self.notebook.append_page(self.page1, Gtk.Label(label="Sell"))


        self.page2 = Gtk.Box()
        self.page2.set_border_width(10)
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
        self.notebook.append_page(self.page4, Gtk.Label(label="Patients"))       
        

        self.notebook.show_all()

    def tablo_gosterimi(self):
        listmodel = Gtk.ListStore(str, str, str)
        for i in range(len(phonebook)):
            listmodel.append(phonebook[i])

        self.view = Gtk.TreeView(model=listmodel)
        for i, column in enumerate(columns):
            cell = Gtk.CellRendererText()

            if i == 0:
                cell.props.weight_set = True
                cell.props.weight = Pango.Weight.BOLD

            col = Gtk.TreeViewColumn(column, cell, text=i)
            self.view.append_column(col)


    #### Veri Tabanı Fonksiyonları ####

    def baglanti_baslat(self):
        self.con = sqlite3.connect('pharmacy.db')
        self.cursor = self.con.cursor()
        
    def kullanici_tablo_olustur(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (ID TEXT, Password TEXT)")
        self.con.commit()
    
    def kullanici_ekle_query(self,ids,passw):
        self.cursor.execute("INSERT INTO users Values(?,?)",(ids,passw))
        self.con.commit()
    
    def kullanici_giris_query(self,ids,passw):
        self.cursor.execute("SELECT * FROM users WHERE ID == ? AND PASSWORD == ?",(ids,passw))
        liste = self.cursor.fetchall()

        if len(liste) == 1:
            self.remove(self.main_Table)
            self.ana_ekran()
        else:
            self.main_hataLabel = Gtk.Label(label = "Wrong credentials!")
            self.main_Table.attach(self.main_hataLabel,2,8,8,9)
            self.main_Table.show_all()
    
    def hasta_tablo_olustur(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS patients (Name TEXT, Surname TEXT, Mail TEXT)")
        self.con.commit()

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