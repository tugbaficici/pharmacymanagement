import gi,sqlite3
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from veriCekmeFonksiyonlar import *

# Fabrika sağ tık menüsündeki güncelle seçeneği görev fonksiyonu
def factory_guncelle(event,self):
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
        self.update_FactoryButton.connect('clicked',onclick_Update,self)
        self.update_factoryname.set_placeholder_text("Factory Name")
       
        update_FactoryWindowTable.attach(self.update_factoryname,0,1,0,1)
        update_FactoryWindowTable.attach(self.update_FactoryButton,0,1,1,2)
      
        self.update_FactoryWindow.present()
        self.update_FactoryWindow.show_all()

# İlaç cart tablosu sağ tık menüsündeki güncelle seçeneği görev fonksiyonu
def cart_guncelle(event,self):
        self.cartGuncelleWindow = Gtk.Window()
        self.cartGuncelleWindow.set_title("Box")
        self.cartGuncelleWindow.set_border_width(10)
        self.cartGuncelleWindowTable = Gtk.Table(n_rows=2, n_columns=0, homogeneous=True)
        self.cartGuncelleWindow.add(self.cartGuncelleWindowTable)
        self.cartGuncelleSayi = Gtk.Entry()
            
        self.cartGuncelleButton = Gtk.Button(label ="Send")
        self.cartGuncelleButton.connect('clicked',onclick_Update,self)
        self.cartGuncelleSayi.set_placeholder_text("Piece")
        
        self.cartGuncelleWindowTable.attach(self.cartGuncelleSayi,0,1,0,1)
        self.cartGuncelleWindowTable.attach(self.cartGuncelleButton,0,1,1,2)
        
        self.cartGuncelleWindow.present()
        self.cartGuncelleWindow.show_all()

# Fabrika cart tablosu sağ tık menüsündeki güncelle seçeneği görev fonksiyonu
def cart_guncelle2(event,self):
        self.cartGuncelleWindow2 = Gtk.Window()
        self.cartGuncelleWindow2.set_title("Box")
        self.cartGuncelleWindow2.set_border_width(10)

        self.cartGuncelleWindowTable2 = Gtk.Table(n_rows=2, n_columns=0, homogeneous=True)
        self.cartGuncelleWindow2.add(self.cartGuncelleWindowTable2)

        self.cartGuncelleSayi2 = Gtk.Entry()
        self.cartGuncelleButton2 = Gtk.Button(label ="Send")
        self.cartGuncelleButton2.connect('clicked',onclick_Update,self)
    
        self.cartGuncelleSayi2.set_placeholder_text("Piece")
        self.cartGuncelleWindowTable2.attach(self.cartGuncelleSayi2,0,1,0,1)
        self.cartGuncelleWindowTable2.attach(self.cartGuncelleButton2,0,1,1,2)
        
        self.cartGuncelleWindow2.present()
        self.cartGuncelleWindow2.show_all()

# Hasta güncelleme ekranı
def hasta_guncelle(event,self):
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
        self.update_PatientButton.connect('clicked',onclick_Update,self)
  
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
    
# İlaç güncelleme ekranı
def ilac_guncelle(event,self):
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
        self.update_Medicinebutton.connect('clicked',onclick_Update,self)
  
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

# Hasta - fabrika - ilaç güncelleme fonksiyonu görevi
def onclick_Update(action,self):
        if self.table_type == 'patients':
        
            self.cursor.execute("UPDATE patients SET TC = ?, NAME = ?, SURNAME = ?, EMAIL = ? WHERE ID = ?",(int(self.update_tcnumber.get_text()),
                self.update_name.get_text(),self.update_surname.get_text(),self.update_email.get_text(),self.secilen_Satir))
            self.con.commit()

            self.update_PatientWindow.hide()
            self.listmodel.clear()
            hasta_vericekme_query(self)

            for i in range(len(self.hasta_listesi)):
                self.listmodel.append(self.hasta_listesi[i])

        if self.table_type == 'factories':
        
            self.cursor.execute("UPDATE factories SET NAME = ? WHERE ID = ?",(self.update_factoryname.get_text(),self.secilen_Satir))
            self.con.commit()

            self.update_FactoryWindow.hide()
            self.factories_listmodel.clear()
            fabrika_vericekme_query(self)

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
            ilac_vericekme_query(self)

            for i in range(len(self.ilac_listesi)):
                self.ilac_listmodel.append(self.ilac_listesi[i])

        if self.table_type == 'cart':
            self.cartGuncelleWindow.hide()
            for row in self.cartlistmodel:
                if row[0] == self.secilen_Satir:
                    row[7]=self.cartGuncelleSayi.get_text()
                    break
        if self.table_type == 'cart2':
            self.cartGuncelleWindow2.hide()
            for row in self.cartlistmodel2:
                if row[0] == self.secilen_Satir:
                    row[7]=self.cartGuncelleSayi2.get_text()
                    break
