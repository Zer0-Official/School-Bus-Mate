version = '0.0.0'

import kivy
from kivy.metrics import dp
from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.theming import ThemeManager
from kivy.uix.widget import Widget
from kivy.factory import Factory
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from os import walk
from kivymd.uix.button import MDFlatButton
from kivymd.uix.snackbar import Snackbar
# from myfirebase import MyFirebase
from datetime import datetime
import kivy.utils
from kivy.utils import platform
import requests
import json
import traceback
from kivy.graphics import Color, RoundedRectangle
import random

theme = 'Light'

class LoginScreen(Screen):
    pass

class LoginType(Screen):
    pass

class HomeScreen(Screen):
    pass

class SeatScreen(Screen):
    pass

class RouteScreen(Screen):
    pass

class ReportScreen(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class MainApp(MDApp):
    dialog = None
    def build(self):
        # Window.clear_color = (1,1,171/255,1)
        self.theme_cls.theme_style = theme
        self.theme_cls.primary_palette = 'Amber'
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"Item {i}",
                "height": dp(56),
                "on_release": lambda x=f"Item {i}": self.menu_triDot(x),
             } for i in range(5)
        ]
        self.menu = MDDropdownMenu(
            items=menu_items,
            width_mult=4,
        )
        return Builder.load_file('main.kv')

# Dialogs
    def warning_box(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text="Please go to (site) for this account type.",
                buttons=[
                    MDFlatButton(
                        text="OK", text_color=self.theme_cls.primary_color,
                        on_release= self.dialog_close
                    ),
                ],
            )
        self.dialog.open()

    def dialog_close(self, *args):
        self.dialog.dismiss(force=True)

# Snackbars
    def snackCreate(self):
        Snackbar(
            text="Student Account Created!",
            snackbar_x="10dp",
            snackbar_y="10dp",
            size_hint_x=(
                Window.width - ((10) * 2)
            ) / Window.width
        ).open()

# Hidden Feature
    def snackMrJ(self): #Please Use Hidden Ft.
        Snackbar(
            text= 'What is the cat hair!?',
            snackbar_x="10dp",
            snackbar_y="10dp",
            size_hint_x=(
                Window.width - (dp(10) * 2)
            ) / Window.width
        ).open()

# Left Action Menu
    def triDotMenu(self, button):
        self.menu.caller = button
        self.menu.open()
    def menu_triDot(self, text_item):
        self.menu.dismiss()
        Snackbar(text=text_item).open()



if __name__ == '__main__':
    MainApp().run()
