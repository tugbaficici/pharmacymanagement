from veriCekmeFonksiyonlar import *

# Sağ tık menüsündeki silme butonu görevi
def onclick_Delete(action,self):
        if self.table_type == 'patients':
            self.cursor.execute("DELETE FROM patients WHERE ID = ?",(self.secilen_Satir,))
            self.con.commit()
     
            self.listmodel.clear()
            hasta_vericekme_query(self)

            for i in range(len(self.hasta_listesi)):
                self.listmodel.append(self.hasta_listesi[i])
        
        if self.table_type == 'medicines':
            self.cursor.execute("DELETE FROM medicines WHERE ID = ?",(self.secilen_Satir,))
            self.con.commit()
     
            self.ilac_listmodel.clear()
            ilac_vericekme_query(self)

            for i in range(len(self.ilac_listesi)):
                self.ilac_listmodel.append(self.ilac_listesi[i])

        if self.table_type == 'factories':
            self.cursor.execute("DELETE FROM factories WHERE ID = ?",(self.secilen_Satir,))
            self.con.commit()
     
            self.factories_listmodel.clear()
            fabrika_vericekme_query(self)

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
        if self.table_type == 'cart2':
            for row in self.cartlistmodel2:
                if row[0] == self.secilen_Satir:
                    self.cartlistmodel2.remove(row.iter)
                    break
            for row2 in self.geciciliste2:
                if row2[0] == self.secilen_Satir:
                    self.geciciliste2.remove(row2)
                    break