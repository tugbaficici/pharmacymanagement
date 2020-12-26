import gi,sqlite3
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from veriCekmeFonksiyonlar import *

def hasta_ekle(event,self):
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
        self.add_PatientButton.connect('clicked',add_NewPatient,self)
  
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
    
def fabrika_ekle(event,self):
        self.add_factoriesWindow = Gtk.Window()
        self.add_factoriesWindow.set_title("Add New Factory")
        self.add_factoriesWindow.set_border_width(10)

        add_factoriesWindowTable = Gtk.Table(n_rows=3, n_columns=0, homogeneous=True)
        self.add_factoriesWindow.add(add_factoriesWindowTable)

        self.factory_Name = Gtk.Entry()
        self.add_factorybutton = Gtk.Button(label ="Send")
        self.add_factorybutton.connect('clicked',add_NewFactory,self)
  
        self.factory_Name.set_placeholder_text("Factory Name")
        add_factoriesWindowTable.attach(self.factory_Name,0,1,0,1)
        add_factoriesWindowTable.attach(self.add_factorybutton,0,1,2,3)

        self.add_factoriesWindow.present()
        self.add_factoriesWindow.show_all()

def ilac_addButtonEvent(event,self):
        self.cursor.execute("INSERT INTO medicines (NAME,DOSE,ACTIVE,PIECE,PRICE,FACTORY,PROSPECTUS) Values(?,?,?,?,?,?,?)",
            (self.ilac_nameEntry.get_text(),self.ilac_doseEntry.get_text(),self.ilac_activeEntry.get_text(),self.ilac_pieceEntry.get_text(),
            self.ilac_priceEntry.get_text(),self.ilac_factoryEntry.get_text(),self.ilac_prosEntry.get_text()))
        self.con.commit()

        self.ilac_nameEntry.set_text('')
        self.ilac_doseEntry.set_text('')
        self.ilac_activeEntry.set_text('')
        self.ilac_pieceEntry.set_text('')
        self.ilac_priceEntry.set_text('')
        self.ilac_prosEntry.set_text('')
        self.ilac_factoryEntry.set_text('Eczane Stok')

        self.ilac_listmodel.clear()
        ilac_vericekme_query(self)

        for i in range(len(self.ilac_listesi)):
            self.ilac_listmodel.append(self.ilac_listesi[i])

def add_NewPatient(event,self):

        tc = self.tcnumber.get_text()
        name = self.name.get_text()
        surname = self.surname.get_text()
        email = self.email.get_text()

        self.cursor.execute("INSERT INTO patients(TC,NAME,SURNAME,EMAIL) Values(?,?,?,?)",(tc,name,surname,email))
        self.con.commit()

        self.add_PatientWindow.hide()

        self.listmodel.clear()
        hasta_vericekme_query(self)

        for i in range(len(self.hasta_listesi)):
            self.listmodel.append(self.hasta_listesi[i])
    
def add_NewFactory(event,self):

        factory_Name = self.factory_Name.get_text()

        self.cursor.execute("INSERT INTO factories(NAME) Values(?)",(factory_Name,))
        self.con.commit()

        self.add_factoriesWindow.hide()

        self.factories_listmodel.clear()
        fabrika_vericekme_query(self)

        for i in range(len(self.fabrika_listesi)):
            self.factories_listmodel.append(self.fabrika_listesi[i])

