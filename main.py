#!/usr/bin/python3
# -*- coding: utf-8 -*-
import gi
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
        self.giris_ekrani()

    

    def giris_ekrani(self):
        main_Table = Gtk.Table(n_rows=10, n_columns=10, homogeneous=True)
        main_Label = Gtk.Label(label = "Open Source Pharmacy Management Sysem")

        main_IdLabel = Gtk.Label(label = "ID : ")
        self.main_IdEntry = Gtk.Entry()

        main_PassLabel = Gtk.Label(label = "Password : ")
        self.main_PassEntry = Gtk.Entry()
        self.main_PassEntry.set_visibility(False)

        self.main_LoginButton = Gtk.Button(label = "Login")
        self.add(main_Table)

        main_Table.attach(main_Label,0,10,0,2)
        main_Table.attach(main_IdLabel,0,4,3,4)
        main_Table.attach(main_PassLabel,0,4,4,5)
        main_Table.attach(self.main_IdEntry,5,8,3,4)
        main_Table.attach(self.main_PassEntry,5,8,4,5)
        main_Table.attach(self.main_LoginButton,4,6,7,8)



window = MyWindow()
window.show_all()
Gtk.main()