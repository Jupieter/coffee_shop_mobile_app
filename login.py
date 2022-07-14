from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.gridlayout import MDGridLayout
from kivy.properties import ObjectProperty
import time

import requests
import sqlite3
# from main import MyRecycleView
# from main import active_token


Builder.load_file('kv/login.kv')



class LogInCard(MDCard): # the.boss@staff.com    Enter1
	print('LogInCard 0')
	def __init__(self, **kwargs):
		super(LogInCard, self).__init__(**kwargs)
		ld_user = self.load_user()
		# self.ids.user.text = ld_user
		print(ld_user)
	# pass
	

	txt_inpt = ObjectProperty(None)
	def check_status(self, btn):
		print('test 2')
		print('button state is: {state}'.format(state=btn.state))
		# print('text input text is: {txt}'.format(txt=self.txt_inpt))

	def log_out(self):
		active_token = self.load_token()
		print('LOG Token', active_token)
		token_str = 'Token ' + active_token
		hd_token = {'Authorization':token_str}
		store = requests.post('http://127.0.0.1:8000/c_app/logout/', headers=hd_token)
		print(hd_token)
		print(store)
		if store == 'Response [204]':
			self.ids.welcome_label.text =(f'Logged out!')
		

	def log_in(self):
		print('START LOG')
		self.ids.welcome_label.text =(f'LOG IN!')
		user = self.ids.user.textself.ids.user.text
		print(user)
		password = self.ids.password.text
		if user != "" or password != "" :
			x = {'email':user, 'password':password}
			sends = json=x
			print(sends)
			store = requests.post('http://127.0.0.1:8000/c_app/login/', data=sends).json()
			print(store)
			keys = []
			values = []
			for key in store.keys():
				print (key)
				keys.append(key)
			print ('key: ', keys[0] )
			if keys[0] == 'expiry':
				self.ids.welcome_label.text =(f'Logged {user}.')
				act_expiry = store['expiry']
				act_token = store['token']
				print(act_expiry)
				print(act_token)
				self.act_token_db(act_token, act_expiry)
				self.act_user_db(user, password)
				print('END LOG') 

			elif keys[0] == 'non_field_errors':
				x = store['non_field_errors']
				print('val: ', x)
				self.ids.welcome_label.text =(f' {x}')


			else:
				self.ids.welcome_label.text =(f'Hi /{user}/ wrong email or password!')
				print('WRONG LOG')
	
	def load_token(self, *args):
		conn = sqlite3.connect('coffe_app.db')
		active_tk = conn.execute("SELECT act_token from act_tokens")
		for row in active_tk:
			active_token = row[0]
		return active_token

	def load_user(self, *args):
		conn = sqlite3.connect('coffe_app.db')
		user = conn.execute("SELECT act_user from act_users")
		for row in user:
			active_user = row[0]
		return active_user

	def act_token_db(self, act_token, act_expiry):
		print(act_token)
		conn = sqlite3.connect('coffe_app.db')	
		cur = conn.cursor()
		sql = """UPDATE act_tokens 
					SET act_token = ?, act_expiry = ?
					WHERE id = ?"""
		data = (act_token, act_expiry, 1)
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



	def test1(self):
		print('tets 1')
		x= self.ids.items()
		print(x)

	def test2(self):
		print('tets 2')
		self.ids.test_btn.text = "Test 1"
		# self.remove_widget(self.root.ids.box_logout)


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

#class LogOutCard(MDCard):
#	print('LogOutCard 0')
#			# self.ids.data_label.text = f'sends {store}!'
#	pass