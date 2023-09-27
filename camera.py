from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from pyzbar.pyzbar import decode
from filestorage import FileStorage
from kivy.core.window import Window
import ast
import cv2
import numpy as np

class CamApp(App):
    data = []

    def build(self):
        self.img1=Image()
        layout = BoxLayout()
        layout.add_widget(self.img1)
        #opencv2 stuffs
        self.capture = cv2.VideoCapture(0)
    #    cv2.namedWindow("CV2 Image")
        Clock.schedule_interval(self.update, 1.0/33.0)
        return layout

    def update(self, dt):
        fs = FileStorage()
        fs.reload()
        # display image from cam in opencv window
        ret, frame = self.capture.read()
        # convert it to texture
        buf1 = cv2.flip(frame, 0)
        buf = buf1.tobytes()
        texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr') 
        #if working on RASPBERRY PI, use colorfmt='rgba' here instead, but stick with "bgr" in blit_buffer. 
        texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        # display image from the texture
        self.img1.texture = texture1
        self.decoder(frame)
        code = cv2.waitKey(10)
        if self.data:
            verfi = self.data[0]['id']
            fs.incr(verfi)
            fs.save()
            #App.get_running_app().stop
            #Window.close()
        elif code == ord('q'):
            App.get_running_app().stop
            Window.close()


    def decoder(self, image):
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
            self.data.append(ast.literal_eval(barcodeData))


if __name__ == '__main__':
    CamApp().run()
    cv2.destroyAllWindows()