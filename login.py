from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivy.properties import ObjectProperty

import requests
import sqlite3

Builder.load_file('kv/login.kv')

active_token = "TOKEN1"





class LogInCard(MDCard):
	print('test 0')
	pass
	

	txt_inpt = ObjectProperty(None)
	def check_status(self, btn):
		print('test 2')
		print('button state is: {state}'.format(state=btn.state))
		# print('text input text is: {txt}'.format(txt=self.txt_inpt))

	def logger(self):
		print('START LOG')
		user = self.ids.user.text
		password = self.ids.password.text
		self.ids.welcome_label.text =(f'Hi {user, password}!')
		x = {'email':user, 'password':password}
		sends = json=x
		print(sends)
		store = requests.post('http://127.0.0.1:8000/c_app/login/', data=sends).json()
		tk_expiry = store['expiry']
		act_token = store['token']
		print(tk_expiry)
		print(act_token)
		# self.ids.data_label.text = f'sends {store}!'
		self.act_token_db(act_token)
		self.act_user_db(user, password)
		print('END LOG') # the.boss@staff.com    Enter1
	
	def act_token_db(self, act_token):
		print(act_token)
		conn = sqlite3.connect('coffe_app.db')	
		cur = conn.cursor()
		sql = """UPDATE act_tokens 
					SET act_token = ? 
					WHERE id = ?"""
		data = (act_token, 1)
		cur.execute(sql, data)
		conn.commit()
		conn.close()

	def act_user_db(self, act_user, act_pass):
		print(act_user, act_pass)
		conn = sqlite3.connect('coffe_app.db')	
		cur = conn.cursor()
		sql = """UPDATE act_users 
					SET act_user = ?, act_pass = ? 
					WHERE id = ?"""
		data = (act_user, act_pass, 1)
		cur.execute(sql, data)
		conn.commit()
		conn.close()

	def read_user(self):
		conn = sqlite3.connect('coffe_app.db')	
		cur = conn.cursor()
		# conn.execute("SELECT act_token from act_tokens")
		sql = """SELECT act_user FROM act_users WHERE id = 1"""
		print(sql)
		data = (1)
		users = cur.execute(sql)
		print('user: ', users)
		for row in users:
			user = row[0]
			print ("user = ", user)
		conn.close()
		return user


	def clear(self):
		print('Clear  !')
		self.ids.user.text = ""		
		self.ids.password.text = ""	
		self.ids.welcome_label.text = "WELCOME"		





	def testing(self):
		conn = sqlite3.connect('coffe_app.db')	
		cur = conn.cursor()
		sql = """INSERT OR IGNORE INTO 
			act_tokens (id, act_token) VALUES (?, ?)"""
		data1 = (1,'a1')
		cur.execute(sql, data1)
		conn.commit()
		conn.close()

	def testing2(self):
		conn = sqlite3.connect('coffe_app.db')	
		cur = conn.cursor()
		sql = """UPDATE act_tokens 
					SET act_token = ? 
					WHERE id = ?"""
		data = ('a1s2d3f4', 1)
		cur.execute(sql, data)
		conn.commit()
		conn.close()	

class LogOutCard(MDCard):
	print('test 0')
	pass