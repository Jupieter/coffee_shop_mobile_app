from kivy.lang import Builder
from kivy.clock import Clock
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
		print('fk_test')
		magam = self
		x = self.ids
		print(x)
		Clock.schedule_once(magam.load_data, 0)
		Clock.schedule_interval(magam.load_data, 1) 
	
	def tik(self, *args):
		print('tik-tak')
	
	def load_token(self, *args):
		conn = sqlite3.connect('coffe_app.db')
		active_tok = conn.execute("SELECT act_token from act_tokens")
		for row in active_tok:
			active_token = row[0]
			print ("token = ", active_token)
		print('recycle 3')
		# Clock.schedule_interval(print('tik-tak'), 3)
		return active_token

	def load_data(self, *args):
		print('recycle 2')
		active_token = self.load_token()
		print('LOG Token', active_token)
		token_str = 'Token ' + active_token
		hd_token = {'Authorization':token_str}
		if active_token != 'Empty':
			store = requests.get('http://127.0.0.1:8000/c_app/todaytcoffee/', headers=hd_token).json()
			print(store)
			list_data = []
			for item in store:
				list_data.append({'text': item['c_make_date']})
			first_coffe = list_data[0]['text']
			print(first_coffe)
			# self.data = first_coffe
			# print(self.dat			
			fc_date = first_coffe[0:10]
			print(fc_date)
			fc_hour = first_coffe[11:13]
			fc_min = first_coffe[14:16]
			print(fc_hour,':',fc_min)
			date_time = [fc_date, fc_hour, fc_min]
			print(date_time)




#class TestApp(MDApp):
#        
#        def build(self):
#            return presentation
#
#if __name__ == '__main__':
#    TestApp().run()                
