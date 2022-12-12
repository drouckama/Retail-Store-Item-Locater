import cv2
from pyzbar import pyzbar
import winsound
from tkinter import messagebox
class Test(object):
    def __init__(self, bc):
        self.bc = bc
    def setBc(self, bc):
        self.bc = bc
        return
    def getBc(self):
        return self.bc
    def cutBc(self, bc):
        bc = str(bc)
        s = []
        z = ""
        for i in range(len(bc)):
            s.append(bc[i])
        s.pop(0)
        s.pop(0)
        for i in range(len(s)):
            z += str(s[i])
        print (z)
        return z
            
        
        
        
bc = Test(0000000000)
    
def check(barcode):
    fpRef = open("planoguide.txt", "r")
    x = 0
    while True:
        line = fpRef.readline()
        if line == "":
            fpRef.close()
            if x == 0:
                messagebox.showinfo(title = "Error", message = "Item not found!")
                fpRef.close()
            break
        line = line.strip()
        word = line.split()
        if barcode == word[0]:
            messagebox.showinfo(title = (word[4]), message = (word[2], "Row", word[3], "Item"))
            x += 1
            fpRef.close()
            break
    return
def read_barcodes(frame):
    barcodes = pyzbar.decode(frame)    
    for barcode in barcodes:
        barcode_info = barcode.data.decode('utf-8')
        #print(barcode_info)
        bc.setBc(barcode_info)
        #print(bc.getBc(), "a")
        
        #winsound.PlaySound("sound2.wav", winsound.SND_ASYNC)
    return frame
def main():
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    while ret:
        print(pyzbar.decode(frame))
        ret, frame = camera.read()
        frame = read_barcodes(frame)
        cv2.imshow('Big Lots Box Finder', frame)
        if pyzbar.decode(frame) != []:
            print(bc.getBc())
            break
        if cv2.waitKey(1) & 0xFF == 27:
            exit()
            break
    camera.release()
    cv2.destroyAllWindows()
    w = bc.getBc()
    x = bc.cutBc(w)
    bc.setBc(x)
    check(bc.getBc())
while True:
    main()



