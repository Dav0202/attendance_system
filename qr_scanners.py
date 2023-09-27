import ast
import cv2
import numpy as np
from pyzbar.pyzbar import decode
from filestorage import FileStorage

data = []

def decoder(image):
    gray_img = cv2.cvtColor(image,0)
    barcode = decode(gray_img)

    for obj in barcode:
        points = obj.polygon
        (x,y,w,h) = obj.rect
        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image, [pts], True, (0, 255, 0), 3)

        barcodeData = obj.data.decode("utf-8")
        barcodeType = obj.type
        string = "Data " + str(barcodeData) + " | Type " + str(barcodeType)
        data.append(ast.literal_eval(barcodeData))

def scan():
    fs = FileStorage()
    fs.reload()
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        decoder(frame)
        cv2.imshow('Image', frame)
        code = cv2.waitKey(10)
        if data:
            verfi = data[0]['id']
            fs.incr(verfi)
            fs.save()
            break
        elif code == ord('q'):
            break

#if __name__ == "__main__":
#    scan()    
# end main


"""import cv2
import ast
file = 'qr_pngs' + "\\" + 'Dele' + ".png"
img = cv2.imread(file)
detector = cv2.QRCodeDetector()
data, bbox, straight_qrcode = detector.detectAndDecode(img)
if data is not None:
    dic_data = ast.literal_eval(data)
    print(dic_data['first_name'],dic_data['last_name'])
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()"""