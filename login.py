from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivy.properties import ObjectProperty

import requests
import sqlite3

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
		conn = sqlite3.connect('coffe_app.db')	
		cur = conn.cursor()
		sql = '''INSERT OR IGNORE INTO act_tokens 
				(id, act_token) 
				VALUES 
				(1, 'a1')'''
		# sql = """UPDATE tokens SET token = ? WHERE id=1"""
		sql2 = """UPDATE act_tokens SET act_token = ? WHERE id = 1"""
		data = 'a1s2d3f4'
		print('2')
		# cur.execute(sql2, data)
		print('3 ', sql, 'data:', data)
		conn.commit()
		cur.close()	
		print('END')