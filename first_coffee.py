from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ObjectProperty
import time

import requests
import sqlite3


presentation = Builder.load_file('kv/first_coffee.kv')

class FirstCoffe(MDCard): # the.boss@staff.com    Enter1
	print('LogInCard 0')
	def __init__(self, **kwargs):
		super(FirstCoffe, self).__init__(**kwargs)



#class TestApp(MDApp):
#        
#        def build(self):
#            return presentation
#
#if __name__ == '__main__':
#    TestApp().run()                
