#!/usr/bin/python3
# -*- coding: utf-8 -*-
import gi,sqlite3
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
gi.require_version('Gdk', '3.0')
from gi.repository import Gdk, GLib



class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(500, 500)
        self.connect("destroy", Gtk.main_quit)
        self.set_title("Pharmacy Management System")
        self.main()

    def main(self):
        self.baglanti_baslat()
        self.kullanici_tablo_olustur()
        self.kayit_ekrani()

    def giris_ekrani(self):

        main_Table = Gtk.Table(n_rows=10, n_columns=10, homogeneous=True)
        main_Label = Gtk.Label(label = "Open Source Pharmacy Management Sysem")

        main_IdLabel = Gtk.Label(label = "ID : ")
        self.main_IdEntry = Gtk.Entry()

        main_PassLabel = Gtk.Label(label = "Password : ")
        self.main_PassEntry = Gtk.Entry()
        self.main_PassEntry.set_visibility(False)

        self.main_LoginButton = Gtk.Button(label = "Login")
        self.main_RegisterButton = Gtk.Button(label = "Register")
        self.main_RegisterButton.connect('clicked',self.kayit_ekrani)
        self.add(main_Table)

        main_Table.attach(main_Label,0,10,0,2)
        main_Table.attach(main_IdLabel,0,4,3,4)
        main_Table.attach(main_PassLabel,0,4,4,5)
        main_Table.attach(self.main_IdEntry,5,8,3,4)
        main_Table.attach(self.main_PassEntry,5,8,4,5)
        main_Table.attach(self.main_LoginButton,4,6,6,7)
        main_Table.attach(self.main_RegisterButton,4,6,7,8)
    
    def kayit_ekrani(self):

        kayit_Table = Gtk.Table(n_rows=10, n_columns=10, homogeneous=True)
        kayit_Label = Gtk.Label(label = "Open Source Pharmacy Management Sysem\nRegister")

        kayit_IdLabel = Gtk.Label(label = "ID : ")
        self.kayit_IdEntry = Gtk.Entry()

        kayit_PassLabel = Gtk.Label(label = "Password : ")
        self.kayit_PassEntry = Gtk.Entry()
        self.kayit_PassEntry.set_visibility(False)

        self.kayit_RegisterButton = Gtk.Button(label = "Register")
        self.kayit_RegisterButton.connect('clicked',self.kullanici_ekle)
        self.kayit_GeriButton = Gtk.Button(label = "Back")

        kayit_Table.attach(kayit_Label,0,10,0,2)
        kayit_Table.attach(kayit_IdLabel,0,4,3,4)
        kayit_Table.attach(kayit_PassLabel,0,4,4,5)
        kayit_Table.attach(self.kayit_IdEntry,5,8,3,4)
        kayit_Table.attach(self.kayit_PassEntry,5,8,4,5)
        kayit_Table.attach(self.kayit_RegisterButton,4,6,6,7)
        kayit_Table.attach(self.kayit_GeriButton,4,6,7,8)

        self.add(kayit_Table)

    def baglanti_baslat(self):
        self.con = sqlite3.connect('pharmacy.db')
        self.cursor = self.con.cursor()
        
    def kullanici_tablo_olustur(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (ID TEXT, Password TEXT)")
        self.con.commit()
    
    def kullanici_ekle(self,event):
        ids = self.kayit_IdEntry.get_text()
        passw = self.kayit_PassEntry.get_text()
        self.kullanici_ekle_query(ids,passw)


    def kullanici_ekle_query(self,ids,passw):
        self.cursor.execute("INSERT INTO users Values(?,?)",(ids,passw))
        self.con.commit()
    
    


window = MyWindow()
window.show_all()
Gtk.main()