from kivy.app import App
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader


def sound_play():
    sound = SoundLoader.load('sources/sounds/chik.wav')
    sound.play()

class MyApp(App):
    def build(self):
        return Button(text = "Chik chik",
                      font_size=50,
                      on_press=self.btn_press,
                      )



    def btn_press(self, instance):
        print("Кнопка нажата")
        instance.text= "Я нажата"
        sound_play()




if __name__ == '__main__':
    MyApp().run()
