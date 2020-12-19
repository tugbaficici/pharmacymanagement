#!/usr/bin/python3
# -*- coding: utf-8 -*-
import gi,sqlite3
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
gi.require_version('Gdk', '3.0')
from gi.repository import Gdk, GLib,Pango

hasta_columns = ["ID", "TC NO", "First Name", "Last Name", "EMAIL"]
ilac_columns = ["ID", "NAME", "DOSE", "ACTIVE", "PIECE", "PRICE","FACTORY"]
cart_columns = ["ID", "NAME", "DOSE", "ACTIVE", "PIECE", "PRICE","FACTORY","COUNT"]
fabrika_columns = ["ID","NAME"]

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

    def ana_ekran(self):
        self.notebook = Gtk.Notebook()
        self.add(self.notebook)
        
        self.satis_ekrani()
        self.alis_ekrani()
        self.ilac_ekrani()

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
        self.page4.add(Gtk.Label(label="Default Page!"))
        self.notebook.append_page(self.page4, Gtk.Label(label="Settings"))       
    
        self.notebook.show_all()

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

    def satis_ekrani(self):
        
        self.hasta_tablo()
        self.satis_Table = Gtk.Table(n_rows=10, n_columns=10, homogeneous=False)

        satis_patienceLabel = Gtk.Label(label = "Patients")
        satis_patientSearch = Gtk.SearchEntry()
        satis_patientSearch.connect("activate",self.patients_searchBar)

        satis_patienceAddButton = Gtk.Button(label = "Add")
        satis_patienceAddButton.connect('clicked',self.hasta_ekle)
        
        self.cart_tablo()
        satis_cartLabel = Gtk.Label(label = "Cart")
        satis_cartCleanButton = Gtk.Button(label = "Clean")
        satis_cartCleanButton.connect('clicked',self.on_click_clean)

        self.ilac_tablo()
        satis_medicineSearch = Gtk.SearchEntry()
        satis_medicineSearch.connect("activate",self.medicines_searchBar)

        satis_medicineLabel = Gtk.Label(label = "Medicines")

        self.satis_checkoutButton = Gtk.Button(label = "Checkout to Proceed")

        self.satis_Table.attach(satis_patienceLabel,0,3,0,1)
        self.satis_Table.attach(satis_patientSearch,0,2.5,1,2)
        self.satis_Table.attach(satis_patienceAddButton,2,3,1,2)
        self.satis_Table.attach(self.scroll_patientTable,0,3,2,5)

        self.satis_Table.attach(satis_cartLabel,0,2,5,6)
        self.satis_Table.attach(satis_cartCleanButton,2,3,5,6)
        self.satis_Table.attach(self.scroll_cartTable,0,3,6,9)
    
        self.satis_Table.attach(satis_medicineLabel,3,10,0,1)
        self.satis_Table.attach(satis_medicineSearch,3,10,1,2)

        self.satis_Table.attach(self.scroll_medicineTable,3,10,2,10)
        self.satis_Table.attach(self.satis_checkoutButton,0,3,9,10)

        self.view.show_all()
        self.satis_Table.show_all()
    
    def alis_ekrani(self):
        self.alis_Table = Gtk.Table(n_rows=10, n_columns=10, homogeneous=False)

        alis_factoriesLabel = Gtk.Label(label = "Factories")
        alis_searchEntry = Gtk.SearchEntry()
        alis_searchEntry.connect("activate",self.factory_SearchBar)

        alis_factoriesAddButton = Gtk.Button(label = 'Add')
        alis_factoriesAddButton.connect('clicked',self.fabrika_ekle)
        
        alis_cartLabel = Gtk.Label(label = "Cart")
        alis_cartCleanButton = Gtk.Button(label = "Clean")

        alis_medicineSearch = Gtk.SearchEntry()
        alis_medicineLabel = Gtk.Label(label = "Medicines")
        alis_medicineSearch.connect("activate",self.medicines_searchBar2)

        self.alis_checkoutButton = Gtk.Button(label = "Checkout to Proceed")

        self.fabrika_tablo()
        self.alis_Table.attach(alis_factoriesLabel,0,3,0,1)
        self.alis_Table.attach(alis_searchEntry,0,2.5,1,2)
        self.alis_Table.attach(alis_factoriesAddButton,2,3,1,2)
        self.alis_Table.attach(self.scroll_factoriesTable,0,3,2,5)

        self.cart_tablo()
        self.alis_Table.attach(alis_cartLabel,0,2,5,6)
        self.alis_Table.attach(alis_cartCleanButton,2,3,5,6)
        self.alis_Table.attach(self.scroll_cartTable,0,3,6,9)
    
        self.facilac_tablo()
        self.alis_Table.attach(alis_medicineLabel,3,10,0,1)
        self.alis_Table.attach(alis_medicineSearch,3,10,1,2)
        self.alis_Table.attach(self.scroll_fmedicineTable,3,10,2,10)
        self.alis_Table.attach(self.alis_checkoutButton,0,3,9,10)

        self.fabrika_view.show_all()
        self.alis_Table.show_all()
    
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

        self.ilac_addTable.show_all()
    
    def ilac_listWindow(self):
        self.ilac_tablo()
        self.ilac_listTable = Gtk.Table(n_rows=10, n_columns=10, homogeneous=False)
        self.ilac_listTable.attach(self.scroll_medicineTable,0,10,0,10)
        self.ilac_listTable.show_all()
    
    def ilac_addWindow(self):
        self.ilac_addTable = Gtk.Table(n_rows=10, n_columns=10, homogeneous=False)

        self.ilac_nameEntry = Gtk.Entry()
        self.ilac_doseEntry = Gtk.Entry()
        self.ilac_activeEntry = Gtk.Entry()
        self.ilac_pieceEntry = Gtk.Entry()
        self.ilac_priceEntry = Gtk.Entry()
        

        ilac_nameLabel = Gtk.Label(label = "Name :")
        ilac_doseLabel = Gtk.Label(label = "Dose :")
        ilac_activeLabel = Gtk.Label(label = "Active :")
        ilac_pieceLabel = Gtk.Label(label = "Piece :")
        ilac_priceLabel = Gtk.Label(label = "Price :")
        

        self.ilac_addButton = Gtk.Button(label = "Add") 
        self.ilac_addButton.connect('clicked',self.ilac_addButtonEvent)    
        
        self.ilac_addTable.attach(ilac_nameLabel,1,2,2,3)
        self.ilac_addTable.attach(self.ilac_nameEntry,3,5,2,3)

        self.ilac_addTable.attach(ilac_doseLabel,6,7,2,3)
        self.ilac_addTable.attach(self.ilac_doseEntry,8,10,2,3)

        self.ilac_addTable.attach(ilac_activeLabel,1,2,4,5)
        self.ilac_addTable.attach(self.ilac_activeEntry,3,5,4,5)

        self.ilac_addTable.attach(ilac_pieceLabel,6,7,4,5)
        self.ilac_addTable.attach(self.ilac_pieceEntry,8,10,4,5)

        self.ilac_addTable.attach(ilac_priceLabel,1,2,6,7)
        self.ilac_addTable.attach(self.ilac_priceEntry,3,5,6,7)

        self.ilac_addTable.attach(self.ilac_addButton,8,10,6,7)

        self.ilac_addTable.show_all()
    
    def hasta_listWindow(self):
        self.hasta_tablo()
        self.hasta_listTable = Gtk.Table(n_rows=10, n_columns=10, homogeneous=False)
        self.hasta_listTable.attach(self.scroll_patientTable,0,10,0,10)
        self.hasta_listTable.show_all()

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
    
    def factory_guncelle(self,event):
        self.cursor.execute("SELECT * FROM factories WHERE ID = ?",(self.secilen_Satir,))
        liste = list()
        liste = self.cursor.fetchall()

        self.update_FactoryWindow = Gtk.Window()
        self.update_FactoryWindow.set_title("Update Factory")
        self.update_FactoryWindow.set_border_width(10)

        update_FactoryWindowTable = Gtk.Table(n_rows=2, n_columns=0, homogeneous=True)
        self.update_FactoryWindow.add(update_FactoryWindowTable)

        self.update_factoryname = Gtk.Entry()
        

        self.update_factoryname.set_text(str(liste[0][1]))
        

        self.update_FactoryButton = Gtk.Button(label ="Send")
        self.update_FactoryButton.connect('clicked',self.onclick_Update)
  
        self.update_factoryname.set_placeholder_text("Factory Name")
       

        update_FactoryWindowTable.attach(self.update_factoryname,0,1,0,1)
        update_FactoryWindowTable.attach(self.update_FactoryButton,0,1,1,2)
      

        self.update_FactoryWindow.present()
        self.update_FactoryWindow.show_all()

    def cart_guncelle(self,event):
        self.cartGuncelleWindow = Gtk.Window()
        self.cartGuncelleWindow.set_title("Box")
        self.cartGuncelleWindow.set_border_width(10)

        self.cartGuncelleWindowTable = Gtk.Table(n_rows=2, n_columns=0, homogeneous=True)
        self.cartGuncelleWindow.add(self.cartGuncelleWindowTable)

        self.cartGuncelleSayi = Gtk.Entry()
            

        self.cartGuncelleButton = Gtk.Button(label ="Send")
        self.cartGuncelleButton.connect('clicked',self.onclick_Update)
    
        self.cartGuncelleSayi.set_placeholder_text("Piece")
        

        self.cartGuncelleWindowTable.attach(self.cartGuncelleSayi,0,1,0,1)
        self.cartGuncelleWindowTable.attach(self.cartGuncelleButton,0,1,1,2)
        

        self.cartGuncelleWindow.present()
        self.cartGuncelleWindow.show_all()

    def hasta_guncelle(self,event):
        self.cursor.execute("SELECT * FROM patients WHERE ID = ?",(self.secilen_Satir,))
        liste = list()
        liste = self.cursor.fetchall()

        self.update_PatientWindow = Gtk.Window()
        self.update_PatientWindow.set_title("Update Patient")
        self.update_PatientWindow.set_border_width(10)

        update_PatientWindowTable = Gtk.Table(n_rows=9, n_columns=0, homogeneous=True)
        self.update_PatientWindow.add(update_PatientWindowTable)

        self.update_tcnumber = Gtk.Entry()
        self.update_name = Gtk.Entry()
        self.update_surname = Gtk.Entry()
        self.update_email = Gtk.Entry()

        self.update_tcnumber.set_text(str(liste[0][1]))
        self.update_name.set_text(str(liste[0][2]))
        self.update_surname.set_text(str(liste[0][3]))
        self.update_email.set_text(str(liste[0][4]))

        self.update_PatientButton = Gtk.Button(label ="Send")
        self.update_PatientButton.connect('clicked',self.onclick_Update)
  
        self.update_tcnumber.set_placeholder_text("TC Number (11)")
        self.update_name.set_placeholder_text("Patient Name")
        self.update_surname.set_placeholder_text("Patient Surname")
        self.update_email.set_placeholder_text("Email (Optional)")

        update_PatientWindowTable.attach(self.update_tcnumber,0,1,0,1)
        update_PatientWindowTable.attach(self.update_name,0,1,2,3)
        update_PatientWindowTable.attach(self.update_surname,0,1,4,5)
        update_PatientWindowTable.attach(self.update_email,0,1,6,7)
        update_PatientWindowTable.attach(self.update_PatientButton,0,1,8,9)

        self.update_PatientWindow.present()
        self.update_PatientWindow.show_all()
    
    def ilac_guncelle(self,event):
        self.cursor.execute("SELECT * FROM medicines WHERE ID = ?",(self.secilen_Satir,))
        liste = list()
        liste = self.cursor.fetchall()

        self.update_MedicineWindow= Gtk.Window()
        self.update_MedicineWindow.set_title("Update Patient")
        self.update_MedicineWindow.set_border_width(10)

        update_MedicineWindowTable = Gtk.Table(n_rows=11, n_columns=0, homogeneous=True)
        self.update_MedicineWindow.add(update_MedicineWindowTable)

        self.update_Medicinename = Gtk.Entry()
        self.update_Medicinedose = Gtk.Entry()
        self.update_Medicineactive = Gtk.Entry()
        self.update_Medicinepiece = Gtk.Entry()
        self.update_Medicineprice = Gtk.Entry()

        self.update_Medicinename.set_text(str(liste[0][1]))
        self.update_Medicinedose.set_text(str(liste[0][2]))
        self.update_Medicineactive.set_text(str(liste[0][3]))
        self.update_Medicinepiece.set_text(str(liste[0][4]))
        self.update_Medicineprice.set_text(str(liste[0][5]))

        self.update_Medicinebutton = Gtk.Button(label ="Send")
        self.update_Medicinebutton.connect('clicked',self.onclick_Update)
  
        self.update_Medicinename.set_placeholder_text("Medicine Name")
        self.update_Medicinedose.set_placeholder_text("Medicine Dose")
        self.update_Medicineactive.set_placeholder_text("Medicine Active")
        self.update_Medicinepiece.set_placeholder_text("Medicine Piece")
        self.update_Medicineprice.set_placeholder_text("Medicine Price")

        update_MedicineWindowTable.attach(self.update_Medicinename,0,1,0,1)
        update_MedicineWindowTable.attach(self.update_Medicinedose,0,1,2,3)
        update_MedicineWindowTable.attach(self.update_Medicineactive,0,1,4,5)
        update_MedicineWindowTable.attach(self.update_Medicinepiece,0,1,6,7)
        update_MedicineWindowTable.attach(self.update_Medicineprice,0,1,8,9)
        update_MedicineWindowTable.attach(self.update_Medicinebutton,0,1,10,11)

        self.update_MedicineWindow.present()
        self.update_MedicineWindow.show_all()

    def fabrika_ekle(self,event):
        self.add_factoriesWindow = Gtk.Window()
        self.add_factoriesWindow.set_title("Add New Factory")
        self.add_factoriesWindow.set_border_width(10)

        add_factoriesWindowTable = Gtk.Table(n_rows=3, n_columns=0, homogeneous=True)
        self.add_factoriesWindow.add(add_factoriesWindowTable)

        self.factory_Name = Gtk.Entry()
        self.add_factorybutton = Gtk.Button(label ="Send")
        self.add_factorybutton.connect('clicked',self.add_NewFactory)
  
        self.factory_Name.set_placeholder_text("Factory Name")
        add_factoriesWindowTable.attach(self.factory_Name,0,1,0,1)
        add_factoriesWindowTable.attach(self.add_factorybutton,0,1,2,3)

        self.add_factoriesWindow.present()
        self.add_factoriesWindow.show_all()
    
    ### Tablolar ###
    listmodel = Gtk.ListStore(str, str, str,str,str)
    def hasta_tablo(self):
   
        self.hasta_vericekme_query()
        self.listmodel.clear()
        for i in range(len(self.hasta_listesi)):
            self.listmodel.append(self.hasta_listesi[i])
        
        self.view = Gtk.TreeView(model=self.listmodel)
        for i, column in enumerate(hasta_columns):
            cell = Gtk.CellRendererText()
            col = Gtk.TreeViewColumn(column, cell, text=i)
            self.view.append_column(col)
        
        self.view.connect('button-press-event' , self.tablo_rightClick,'patients')
        self.view.show_all()
        self.scroll_patientTable = Gtk.ScrolledWindow()
        self.scroll_patientTable.add(self.view)
        self.scroll_patientTable.show_all()

    ilac_listmodel=Gtk.ListStore(str, str, str ,str ,str, str,str,str)

    def ilac_tablo(self):

        self.ilac_vericekme_query()
        self.ilac_listmodel.clear()
        for i in range(len(self.ilac_listesi)):
            self.ilac_listmodel.append(self.ilac_listesi[i])

        self.ilac_view = Gtk.TreeView(model=self.ilac_listmodel)
        for i, column in enumerate(ilac_columns):
            cell = Gtk.CellRendererText()
            col = Gtk.TreeViewColumn(column, cell, text=i)
            self.ilac_view.append_column(col)

        self.ilac_view.connect('button-press-event' , self.tablo_rightClick,'medicines') 
        self.ilac_view.show_all()        

        self.ilac_view.enable_model_drag_source(Gdk.ModifierType.BUTTON1_MASK, TARGETS, DRAG_ACTION)
        self.ilac_view.connect("drag-data-get", self.on_drag_data_get)

        
        self.scroll_medicineTable = Gtk.ScrolledWindow()
        self.scroll_medicineTable.add(self.ilac_view)
        self.scroll_medicineTable.show_all()

    facilac_listmodel=Gtk.ListStore(str, str, str ,str ,str, str,str,str)

    def facilac_tablo(self):

        self.facilac_vericekme_query(None)
        self.facilac_listmodel.clear()
        for i in range(len(self.ilac_listesi)):
            self.facilac_listmodel.append(self.facilac_listesi[i])

        self.facilac_view = Gtk.TreeView(model=self.facilac_listmodel)
        for i, column in enumerate(ilac_columns):
            cell = Gtk.CellRendererText()
            col = Gtk.TreeViewColumn(column, cell, text=i)
            self.facilac_view.append_column(col)

        self.facilac_view.connect('button-press-event' , self.tablo_rightClick,'medicines') 
        self.facilac_view.show_all()        

        self.facilac_view.enable_model_drag_source(Gdk.ModifierType.BUTTON1_MASK, TARGETS, DRAG_ACTION)
        self.facilac_view.connect("drag-data-get", self.on_drag_data_get)

        
        self.scroll_fmedicineTable = Gtk.ScrolledWindow()
        self.scroll_fmedicineTable.add(self.facilac_view)
        self.scroll_fmedicineTable.show_all()    

    factories_listmodel = Gtk.ListStore(str, str)
    
    def fabrika_tablo(self):
        self.fabrika_vericekme_query()
        self.factories_listmodel.clear()
        for i in range(len(self.fabrika_listesi)):
            self.factories_listmodel.append(self.fabrika_listesi[i])
        
        self.fabrika_view = Gtk.TreeView(model=self.factories_listmodel)
        for i, column in enumerate(fabrika_columns):
            cell = Gtk.CellRendererText()
            col = Gtk.TreeViewColumn(column, cell, text=i)
            self.fabrika_view.append_column(col)
        
        self.fabrika_view.connect('button-press-event' , self.tablo_rightClickFac,'factories')
        self.fabrika_view.show_all()

        self.scroll_factoriesTable = Gtk.ScrolledWindow()
        self.scroll_factoriesTable.add(self.fabrika_view)
        self.scroll_factoriesTable.show_all()

    cartlistmodel = Gtk.ListStore(str, str, str ,str ,str, str,str,str,str)
    def cart_tablo(self):
        
        #for i in range(len(self.ilac_listesi)):
        #    listmodel.append(self.ilac_listesi[i])

        self.cart_view = Gtk.TreeView(model=self.cartlistmodel)
        for i, column in enumerate(cart_columns):
            cell = Gtk.CellRendererText()
            col = Gtk.TreeViewColumn(column, cell, text=i)
            self.cart_view.append_column(col)

        self.cart_view.enable_model_drag_dest(TARGETS, DRAG_ACTION)
        self.cart_view.connect("drag-data-received", self.on_drag_data_received)

        self.cart_view.connect('button-press-event' , self.tablo_rightClick,'cart')
        self.cart_view.show_all()

        self.scroll_cartTable = Gtk.ScrolledWindow()
        self.scroll_cartTable.add(self.cart_view)
        self.cart_view.show_all()

    ###DRAG AND DROP
    def on_drag_data_get(self, widget, drag_context, data, info, time):
        select = widget.get_selection()
        model, treeiter = select.get_selected()
        
        self.Dragliste=list()
        for i in model[treeiter]:
            self.Dragliste.append(i)
  
    geciciliste=list()
    def on_drag_data_received(self, widget, drag_context, x, y, data, info, time):
        print(self.geciciliste)
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

    def cartUpdate(self,event):
        self.geciciliste.append(self.Dragliste[0])
        a=self.Dragliste[7]
        self.Dragliste.pop()
        self.ddKutuSayisi.hide()
        self.Dragliste.append(self.ddKutuSayisi_sayi.get_text())
        self.Dragliste.append(a)
        self.cartlistmodel.append(self.Dragliste)
        
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

        self.listmodel.clear()
        self.hasta_vericekme_query()

        for i in range(len(self.hasta_listesi)):
            self.listmodel.append(self.hasta_listesi[i])
    
    def add_NewFactory(self,event):

        factory_Name = self.factory_Name.get_text()

        self.cursor.execute("INSERT INTO factories(NAME) Values(?)",(factory_Name,))
        self.con.commit()

        self.add_factoriesWindow.hide()

        self.factories_listmodel.clear()
        self.fabrika_vericekme_query()

        for i in range(len(self.fabrika_listesi)):
            self.factories_listmodel.append(self.fabrika_listesi[i])
        
    def hasta_vericekme_query(self):
        self.cursor.execute("SELECT * FROM patients")
        hasta_list = self.cursor.fetchall()
        self.hasta_listesi = list()
        for i in list(hasta_list):
            gecici_liste = list()
            for j in i:
                gecici_liste.append(str(j))
            
            self.hasta_listesi.append(gecici_liste)

    def ilac_vericekme_query(self):
        self.cursor.execute("SELECT * FROM medicines")
        ilac_list = self.cursor.fetchall()
        self.ilac_listesi = list()
        for i in list(ilac_list):
            gecici_liste = list()
            for j in i:
                gecici_liste.append(str(j))
            
            self.ilac_listesi.append(gecici_liste)

    def facilac_vericekme_query(self,facname):
        if(facname==None):
            self.cursor.execute("SELECT * FROM medicines")
        else:
            self.cursor.execute("SELECT * FROM medicines WHERE FACTORY=?",(facname,))
        facilac_list = self.cursor.fetchall()
        self.facilac_listesi = list()
        for i in list(facilac_list):
            gecici_liste = list()
            for j in i:
                gecici_liste.append(str(j))
            
            self.facilac_listesi.append(gecici_liste)

    def fabrika_vericekme_query(self):
        self.cursor.execute("SELECT * FROM factories")
        fabrika_list = self.cursor.fetchall()
        self.fabrika_listesi = list()
        for i in list(fabrika_list):
            gecici_liste = list()
            for j in i:
                gecici_liste.append(str(j))
            
            self.fabrika_listesi.append(gecici_liste)

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

    #### İşlevsel Fonksiyonlar ####

    def tablo_rightClick(self,treeview, event,tablename):
        self.table_type = tablename
        if event.button == 3: # right click
            pthinfo = treeview.get_path_at_pos(event.x, event.y)
            if pthinfo != None:
                path,col,cellx,celly = pthinfo
                treeview.grab_focus()
                treeview.set_cursor(path,col,0)
            selection = treeview.get_selection()
            (model, iter) = selection.get_selected()
            self.secilen_Satir=model[iter][0] # seçilen satırı id si
            print(self.secilen_Satir)
            print(treeview.get_model())

            menu = self.context_menu()
            menu.popup( None, None, None,None, event.button, event.get_time())
            return True
    
    def tablo_rightClickFac(self,treeview, event,tablename):
        self.table_type = tablename
        
        pthinfo = treeview.get_path_at_pos(event.x, event.y)
        if pthinfo != None:
            path,col,cellx,celly = pthinfo
            treeview.grab_focus()
            treeview.set_cursor(path,col,0)
        selection = treeview.get_selection()
        (model, iter) = selection.get_selected()
        self.secilen_Satir=model[iter][0] # seçilen satırı id si
        print(self.secilen_Satir)
        print(model[iter][1])

        self.facilac_listmodel.clear()
        self.facilac_vericekme_query(model[iter][1])

        for i in range(len(self.facilac_listesi)):
            self.facilac_listmodel.append(self.facilac_listesi[i])

     
    def context_menu(self): # Buton sağ tıkında açılan menü 
        menu = Gtk.Menu()

        menu_item_del = Gtk.MenuItem(label = "Sil")
        menu.append(menu_item_del)
        menu_item_del.connect("activate",self.onclick_Delete)

        menu_item_update = Gtk.MenuItem(label = "Güncelle")
        menu.append(menu_item_update)
        if self.table_type == 'patients':
            menu_item_update.connect("activate",self.hasta_guncelle)
        
        if self.table_type == 'medicines':
            menu_item_update.connect("activate",self.ilac_guncelle)

        if self.table_type == 'factories':
            menu_item_update.connect("activate",self.factory_guncelle)
        
        if self.table_type == 'cart':
            menu_item_update.connect("activate",self.cart_guncelle)

        menu.show_all()

        return menu
    
    def onclick_Delete(self,action):
        if self.table_type == 'patients':
            self.cursor.execute("DELETE FROM patients WHERE ID = ?",(self.secilen_Satir,))
            self.con.commit()
     
            self.listmodel.clear()
            self.hasta_vericekme_query()

            for i in range(len(self.hasta_listesi)):
                self.listmodel.append(self.hasta_listesi[i])
        
        if self.table_type == 'medicines':
            self.cursor.execute("DELETE FROM medicines WHERE ID = ?",(self.secilen_Satir,))
            self.con.commit()
     
            self.ilac_listmodel.clear()
            self.ilac_vericekme_query()

            for i in range(len(self.ilac_listesi)):
                self.ilac_listmodel.append(self.ilac_listesi[i])

        if self.table_type == 'factories':
            self.cursor.execute("DELETE FROM factories WHERE ID = ?",(self.secilen_Satir,))
            self.con.commit()
     
            self.factories_listmodel.clear()
            self.fabrika_vericekme_query()

            for i in range(len(self.fabrika_listesi)):
                self.factories_listmodel.append(self.fabrika_listesi[i])

        if self.table_type == 'cart':
            for row in self.cartlistmodel:
                if row[0] == self.secilen_Satir:
                    self.cartlistmodel.remove(row.iter)
                    break
            for row2 in self.geciciliste:
                if row2[0] == self.secilen_Satir:
                    self.geciciliste.remove(row2)
                    break
            
            

    def onclick_Update(self,action):
        if self.table_type == 'patients':
        
            self.cursor.execute("UPDATE patients SET TC = ?, NAME = ?, SURNAME = ?, EMAIL = ? WHERE ID = ?",(int(self.update_tcnumber.get_text()),
                self.update_name.get_text(),self.update_surname.get_text(),self.update_email.get_text(),self.secilen_Satir))
            self.con.commit()

            self.update_PatientWindow.hide()
            self.listmodel.clear()
            self.hasta_vericekme_query()

            for i in range(len(self.hasta_listesi)):
                self.listmodel.append(self.hasta_listesi[i])

        if self.table_type == 'factories':
        
            self.cursor.execute("UPDATE factories SET NAME = ? WHERE ID = ?",(self.update_factoryname.get_text(),self.secilen_Satir))
            self.con.commit()

            self.update_FactoryWindow.hide()
            self.factories_listmodel.clear()
            self.fabrika_vericekme_query()

            for i in range(len(self.fabrika_listesi)):
                self.factories_listmodel.append(self.fabrika_listesi[i])

        if self.table_type == 'medicines':
            self.cursor.execute("UPDATE medicines SET NAME = ?, DOSE = ?, ACTIVE = ?, PIECE = ?, PRICE = ? WHERE ID = ?",(self.update_Medicinename.get_text(),
                int(self.update_Medicinedose.get_text()),
                self.update_Medicineactive.get_text(),
                int(self.update_Medicinepiece.get_text()),
                self.update_Medicineprice.get_text(),
                self.secilen_Satir))
            self.con.commit()

            self.update_MedicineWindow.hide()
            self.ilac_listmodel.clear()
            self.ilac_vericekme_query()

            for i in range(len(self.ilac_listesi)):
                self.ilac_listmodel.append(self.ilac_listesi[i])

        if self.table_type == 'cart':
            self.cartGuncelleWindow.hide()
            for row in self.cartlistmodel:
                if row[0] == self.secilen_Satir:
                    row[7]=self.cartGuncelleSayi.get_text()
                    break

    
    def ilac_addButtonEvent(self,event):
        self.cursor.execute("INSERT INTO medicines (NAME,DOSE,ACTIVE,PIECE,PRICE) Values(?,?,?,?,?)",
            (self.ilac_nameEntry.get_text(),self.ilac_doseEntry.get_text(),self.ilac_activeEntry.get_text(),self.ilac_pieceEntry.get_text(),
                                                                                                            self.ilac_priceEntry.get_text()))
        self.con.commit()

        self.ilac_nameEntry.set_text('')
        self.ilac_doseEntry.set_text('')
        self.ilac_activeEntry.set_text('')
        self.ilac_pieceEntry.set_text('')
        self.ilac_priceEntry.set_text('')

        self.ilac_listmodel.clear()
        self.ilac_vericekme_query()

        for i in range(len(self.ilac_listesi)):
            self.ilac_listmodel.append(self.ilac_listesi[i])
    
    def patients_searchBar(self,searchentry):
        search_text = searchentry.get_text()

        self.cursor.execute("SELECT * FROM patients")
        list_Patients = self.cursor.fetchall()
        tc_Number = list()
        for i in range(len(list_Patients)):
            tc_Number.append(list_Patients[i][1])

        self.listmodel.clear()
        self.hasta_vericekme_query()

        for j in range(len(tc_Number)):
            if search_text in str(tc_Number[j]):
                self.listmodel.append(self.hasta_listesi[j])
    
    def medicines_searchBar(self,searchentry):
        search_text = searchentry.get_text()
        self.cursor.execute("SELECT NAME FROM medicines")
        list_MedicineNames = self.cursor.fetchall()

        self.ilac_listmodel.clear()
        self.ilac_vericekme_query()

        for j in range(len(list_MedicineNames)):
            if search_text in str(list_MedicineNames[j]):
                self.ilac_listmodel.append(self.ilac_listesi[j])
    
    def medicines_searchBar2(self,searchentry):
        search_text = searchentry.get_text()
        self.cursor.execute("SELECT NAME FROM medicines")
        list_MedicineNames = self.cursor.fetchall()

        self.facilac_listmodel.clear()
        self.facilac_vericekme_query(None)

        for j in range(len(list_MedicineNames)):
            if search_text in str(list_MedicineNames[j]):
                self.facilac_listmodel.append(self.facilac_listesi[j])
    
    def factory_SearchBar(self,searchentry):
        search_text = searchentry.get_text()
        self.cursor.execute("SELECT NAME FROM factories")
        list_factoryNames = self.cursor.fetchall()

        self.factories_listmodel.clear()
        self.fabrika_vericekme_query()

        for j in range(len(list_factoryNames)):
            if search_text in str(list_factoryNames[j]):
                self.factories_listmodel.append(self.fabrika_listesi[j])
    



    def on_click_clean(self,event):
        self.cartlistmodel.clear()
        self.geciciliste.clear()

window = MyWindow()
window.show_all()
Gtk.main()