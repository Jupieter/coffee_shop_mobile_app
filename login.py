from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivy.properties import ObjectProperty

import requests

Builder.load_file('kv/login.kv')
active_token = "TOKEN1"





class LoginCard(MDCard):
	print('test 0')
	pass
	

	print('test 1')
	txt_inpt = ObjectProperty(None)
	def check_status(self, btn):
		print('test 2')
		print('button state is: {state}'.format(state=btn.state))
		# print('text input text is: {txt}'.format(txt=self.txt_inpt))

	def logger(self):
		user = self.ids.user.text
		password = self.ids.password.text
		self.ids.welcome_label.text =(f'Hi {user, password}!')
		x = {'email':user, 'password':password}
		sends = json=x
		print(sends)
		store = requests.post('http://127.0.0.1:8000/c_app/login/', data=sends).json()
		print(store)
		self.ids.data_label.text = f'sends {store}!'

	def clear(self):
		print('Clear  !')
		self.ids.user.text = ""		
		self.ids.password.text = ""	
		self.ids.welcome_label.text = "WELCOME"		

	def testing(self):
		print('Touch  !')	
		active_token = "TOKEN Login"