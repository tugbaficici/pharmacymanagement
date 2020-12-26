from deleteFonksiyonlar import *
from guncelleFonksiyonlar import *
from veriCekmeFonksiyonlar import *

# Tablo sağ tıklamasında gözüken menü fonksiyonu
def tablo_rightClick(treeview, event,tablename,self):
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

            menu = context_menu(self)
            menu.popup( None, None, None,None, event.button, event.get_time())
            return True

# Hasta tablosuna sol tıklandığında ilgili satırın alınmasını sağlayan fonksiyon
def tablo_leftClick(treeview,event,tablename,self):
        self.table_typeLeft = tablename
        if self.table_typeLeft == 'patients':
            pthinfo = treeview.get_path_at_pos(event.x, event.y)
            if pthinfo != None:
                path,col,cellx,celly = pthinfo
                treeview.grab_focus()
                treeview.set_cursor(path,col,0)
            selection = treeview.get_selection()
            (model, iter) = selection.get_selected()
            
            self.proceedPatTC = model[iter][1]
            self.proceedPatName = model[iter][2]
            self.proceedPatSurname = model[iter][3]
            self.proceedPatMail = model[iter][4]

# Fabrika tablosuna sol tıklandığında ilgili satırın alınmasını sağlayan fonksiyon
def tablo_leftClickFac(treeview,event,tablename,self):
        self.table_typeLeft = tablename
        if self.table_typeLeft == 'factories':
            pthinfo = treeview.get_path_at_pos(event.x, event.y)
            if pthinfo != None:
                path,col,cellx,celly = pthinfo
                treeview.grab_focus()
                treeview.set_cursor(path,col,0)
            selection = treeview.get_selection()
            (model, iter) = selection.get_selected()
            
            self.proceedPatFactory = model[iter][1]
            
# Fabrika tablosuna sağ tıklandığında menü çıkmasını sağlayan fonksiyon            
def tablo_rightClickFac(treeview, event,tablename,self):
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
        facilac_vericekme_query(self,model[iter][1])

        for i in range(len(self.facilac_listesi)):
            self.facilac_listmodel.append(self.facilac_listesi[i])

# Sağ tık menüsü
def context_menu(self): # Buton sağ tıkında açılan menü 
        menu = Gtk.Menu()

        menu_item_del = Gtk.MenuItem(label = "Sil")
        menu.append(menu_item_del)
        menu_item_del.connect("activate",onclick_Delete,self)

        menu_item_update = Gtk.MenuItem(label = "Güncelle")
        menu.append(menu_item_update)
        if self.table_type == 'patients':
            menu_item_update.connect("activate",hasta_guncelle,self)
        
        if self.table_type == 'medicines':
            menu_item_update.connect("activate",ilac_guncelle,self)

        if self.table_type == 'factories':
            menu_item_update.connect("activate",factory_guncelle,self)
        
        if self.table_type == 'cart':
            menu_item_update.connect("activate",cart_guncelle,self)
        
        if self.table_type == 'cart2':
            menu_item_update.connect("activate",cart_guncelle2,self)

        menu.show_all()

        return menu