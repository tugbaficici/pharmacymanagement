def hasta_vericekme_query(self):
        self.cursor.execute("SELECT * FROM patients")
        hasta_list = self.cursor.fetchall()
        self.hasta_listesi = list()
        for i in list(hasta_list):
            gecici_liste = list()
            for j in i:
                gecici_liste.append(str(j))
            
            self.hasta_listesi.append(gecici_liste)
    
def ts_vericekme_query(self):
        self.cursor.execute("SELECT NAME,ACTIVE,SELLCOUNT FROM medicines ORDER BY SELLCOUNT DESC")
        ts_list = self.cursor.fetchall()
        self.ts_listesi = list()
        for i in list(ts_list):
            gecici_liste = list()
            for j in i:
                gecici_liste.append(str(j))
            
            self.ts_listesi.append(gecici_liste)

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
            self.cursor.execute("SELECT * FROM factorystock")
        else:
            self.cursor.execute("SELECT * FROM factorystock WHERE FACTORY=?",(facname,))
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