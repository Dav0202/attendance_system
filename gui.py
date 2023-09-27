from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
import qr_gen

user_data = []

class QrGen(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.3)
        self.window.pos_hint = {"center_x":0.5, "center_y":0.5}
        
        #self.window.add_widget(Image(source="pic.jpg",))
        self.firstname = Label(text="Enter your FirstName",
                               font_size = 18,
                               color = '#00FFCE')
        
        self.userfirst = TextInput(multiline=False,)
        self.window.add_widget(self.firstname)
        self.window.add_widget(self.userfirst)
        
        self.lastname = Label(text="Enter your Lastname",
                               font_size = 18,
                               color = '#00FFCE')
        
        self.userlast = TextInput(multiline=False,)
        
        self.window.add_widget(self.lastname)
        self.window.add_widget(self.userlast)
        
        self.display1 = Label(
                               font_size = 18,
                               color = '#00FFCE'
        )
        self.window.add_widget(self.display1)
        
        self.button = Button(text="Generate",
                             size_hint = (1, 0.8),
                             bold = True,
                             background_color = '#00FFCE',
                             background_normal = "")
        
        self.button.bind(on_press = self.callback)
        self.window.add_widget(self.button)

        return self.window
    
    def callback(self, instance):
        user_data.append(self.userfirst.text)
        user_data.append(self.userlast.text)
        qr_gen.generate(user_data)
        App.get_running_app().stop

        Window.close()
    
if __name__ == "__main__":
    QrGen().run()