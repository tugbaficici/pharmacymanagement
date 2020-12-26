import cv2,gi
from pyzbar import pyzbar
from pynput.keyboard import Key, Controller
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

#installation
#sudo apt-get install libzbar0
#pip3 install opencv-python
#pip3 install Pillow
#pip3 install pynput

# Her frame'in incelenmesi
def read_barcodes(frame,self):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y , w, h = barcode.rect
        #1
        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
        #2
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)
        #3
        self.yakalanan=barcode_info
    return frame

# Kameranın açılıp framelerin yakalanması
def main(self):
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()

    while ret:
        ret, frame = camera.read()
        frame = read_barcodes(frame,self)
        cv2.imshow('Barcode/QR code reader', frame)
        if (self.yakalanan != '') or (cv2.waitKey(1) & 0xFF == 27):
            break
        
    #3
    camera.release()
    cv2.destroyAllWindows()

# Yakalanan verinin maine gönderilmesi
def QRdanEkle(self):
    self.yakalanan = ''
    main(self)
    print("yakalanan:"+self.yakalanan)
    return self.yakalanan

