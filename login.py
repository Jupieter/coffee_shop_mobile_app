import os
import json
os.environ['KIVY_NO_CONSOLELOG'] = '1'

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.card import MDCard

import requests

Builder.load_file('kv/login.kv')

class LoginCard(MDCard):
	pass

'''
	def logger(self):
		user = self.root.ids.user.text
		password = self.root.ids.password.text
		self.root.ids.welcome_label.text =(f'Hi {user, password}!')
		x = {'email':user, 'password':password}
		sends = json=x
		print(sends)
		store = requests.post('http://127.0.0.1:8000/c_app/login/', data=sends).json()
		print(store)
		self.root.ids.data_label.text = f'sends {store}!'

	def clear(self):
		self.root.ids.welcome_label.text = "WELCOME"		
		self.root.ids.user.text = ""		
		self.root.ids.password.text = ""	

	def on_touch_down(self):
			print('Touch is a double tap !')
	
'''
