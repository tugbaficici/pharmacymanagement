#### Prio 2 Veri Tabanı Fonksiyonları ####
import gi,sqlite3
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk 

def kullanici_ekle(event,self):
    ids = self.kayit_IdEntry.get_text()
    passw = self.kayit_PassEntry.get_text()
    kullanici_ekle_query(self,ids,passw)

    self.remove(self.kayit_Table)
    self.giris_ekrani()
    
def kullanici_kayit(event,self):
    self.remove(self.main_Table)
    self.kayit_ekrani()

def kullanici_giris(event,self):
    ids = self.main_IdEntry.get_text()
    passw = self.main_PassEntry.get_text()
    kullanici_giris_query(self,ids,passw)
    
def log_out(event,self):
    self.remove(self.notebook)
    self.giris_ekrani()

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

def kullanici_ekle_query(self,ids,passw):
        self.cursor.execute("INSERT INTO users(USERNAME,PASSWORD) Values(?,?)",(ids,passw))
        self.con.commit()