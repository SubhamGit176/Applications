#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 12:11:27 2020

@author: subham
"""

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
import requests
import json


class MyInput(GridLayout):
    def __init__(self,**kwargs):
        super(MyInput,self).__init__(**kwargs)
        self.cols=1
        self.add_widget(Label(text="City : "))
        self.city = TextInput(multiline=False)
        self.add_widget(self.city)
        c = self.city
        api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
        url = api_address + self.city
        api_request = requests.get(url)
        api = api_request.json()
        self.add_widget(Label(text=api['weather'][0]['description'])

class MyApp(App):
    def build(self):
        return MyInput()
    
if __name__ == "__main__":
    MyApp().run()

