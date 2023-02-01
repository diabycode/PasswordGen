from kivy.config import Config
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', 600)
Config.set('graphics', 'height', 200)

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.modalview import ModalView
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty

import clipboard as c
import random

from generator import PasswordGenerator


class MainWidgt(Widget):
    alpha_lenght =  ObjectProperty()
    digit_lenght = ObjectProperty()
    symbol_lenght = ObjectProperty()

    result_label = ObjectProperty()
    copy_button = ObjectProperty()

    customized = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_parent(self, widget, parent):
        self.deactive_input()

    def deactive_input(self):
        self.alpha_lenght.disabled = True
        self.digit_lenght.disabled = True
        self.symbol_lenght.disabled = True

    def active_input(self):
        self.alpha_lenght.disabled = False
        self.digit_lenght.disabled = False
        self.symbol_lenght.disabled = False

    def copy_button_click(self):
        c.copy(self.result_label.text)

    def customization(self, widget):
        if widget.state == "down":
            self.active_input()
            self.customized = True
            return
        self.deactive_input()
        self.customized = False

    def text_validated(self, widget):
        # print("alpha lenght: " + self.alpha_lenght.text)
        # print("digit lenght: " + self.digit_lenght.text)
        # print("symbol lenght: " + self.symbol_lenght.text)
        if not self.customized:
            alpha_len = random.randint(2, 9)
            digit_len = random.randint(2, 9)
            symbol_len = random.randint(2, 9)

            self.alpha_lenght.text = str(alpha_len)
            self.digit_lenght.text = str(digit_len)
            self.symbol_lenght.text = str(symbol_len)

        try:
            alpha_len_int = int(self.alpha_lenght.text)
            digit_len_int = int(self.digit_lenght.text)
            special_len_int = int(self.symbol_lenght.text)
        except:
            self.result_label.text = "Veuillez entrer des valeur numerique"
        else:
            pg = PasswordGenerator()
            passwd = pg.generate(alpha_len=alpha_len_int, digit_len=digit_len_int, special_len=special_len_int)
            self.copy_button.disabled = False
            if len(passwd) > 18:
                self.result_label.text = "Mot de passe trop long"
                self.copy_button.disabled = True
                return
            self.result_label.text = passwd


class MainApp(App):
    main = ObjectProperty(None)
    
    def build(self):
        self.main = MainWidgt()
        return self.main


if __name__ == "__main__":
    print(dir(TextInput))
    MainApp().run()

