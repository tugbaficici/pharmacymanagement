from veriCekmeFonksiyonlar import *

def patients_searchBar(searchentry,self):
        search_text = searchentry.get_text()

        self.cursor.execute("SELECT * FROM patients")
        list_Patients = self.cursor.fetchall()
        tc_Number = list()
        for i in range(len(list_Patients)):
            tc_Number.append(list_Patients[i][1])

        self.listmodel.clear()
        hasta_vericekme_query(self)

        for j in range(len(tc_Number)):
            if search_text in str(tc_Number[j]):
                self.listmodel.append(self.hasta_listesi[j])
    
def medicines_searchBar(searchentry,self):
        search_text = searchentry.get_text()
        self.cursor.execute("SELECT NAME FROM medicines")
        list_MedicineNames = self.cursor.fetchall()

        self.ilac_listmodel.clear()
        ilac_vericekme_query(self)

        for j in range(len(list_MedicineNames)):
            if search_text in str(list_MedicineNames[j]):
                self.ilac_listmodel.append(self.ilac_listesi[j])
    
def medicines_searchBar2(searchentry,self):
        search_text = searchentry.get_text()
        self.cursor.execute("SELECT NAME FROM medicines")
        list_MedicineNames = self.cursor.fetchall()

        self.facilac_listmodel.clear()
        facilac_vericekme_query(self,None)

        for j in range(len(list_MedicineNames)):
            if search_text in str(list_MedicineNames[j]):
                self.facilac_listmodel.append(self.facilac_listesi[j])
    
def factory_SearchBar(searchentry,self):
        search_text = searchentry.get_text()
        self.cursor.execute("SELECT NAME FROM factories")
        list_factoryNames = self.cursor.fetchall()

        self.factories_listmodel.clear()
        fabrika_vericekme_query(self)

        for j in range(len(list_factoryNames)):
            if search_text in str(list_factoryNames[j]):
                self.factories_listmodel.append(self.fabrika_listesi[j])