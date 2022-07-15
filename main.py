import os
os.environ['KIVY_NO_CONSOLELOG'] = '1'
cwd = os.getcwd()
print(cwd)
os.environ['KIVY_HOME'] = cwd + '/conf'

import sqlite3
import requests

from kivy.lang import Builder
from kivy.clock import Clock
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
from kivy.properties import StringProperty, ListProperty, ObjectProperty
from kivymd.uix.list import OneLineIconListItem
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivy.uix.recycleview import RecycleView

from login import LogInCard
from item_drawer import ItemDrawer

# class ItemDrawer(OneLineIconListItem):
#     icon = StringProperty()
#     text_color = ListProperty((0, 0, 0, 1))

active_token = 'Semmi'

class ContentNavigationDrawer(MDBoxLayout):
    pass

class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        '''Called when tap on a menu item.'''

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color

#recycle view for home screen
class MyRecycleView(RecycleView):
    print('Recycle 1')
    def __init__(self, **kwargs):
        super(MyRecycleView, self).__init__(**kwargs)
        print('Recy Token', active_token)
        Clock.schedule_interval(self.load_data, 3)


    def load_token(self, *args):
        conn = sqlite3.connect('coffe_app.db')
        active_tok = conn.execute("SELECT act_token from act_tokens")
        for row in active_tok:
            active_token = row[0]
            print ("token = ", active_token)
        print('recycle 3')
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
            # print(self.data)


class TestNavigationDrawer(MDApp):
    def build(self):
        print('Build 0')
        self.create_db()
        
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Brown"  # "Purple", "Red"
        return Builder.load_file('kv/main.kv')
    
    def create_db(self):
        print('CREATE START DB')
        # Create Database Or Connect To One
        conn = sqlite3.connect('coffe_app.db')
        cur = conn.cursor()
        sql = """CREATE TABLE if not exists act_tokens(
            id INT PRIMARY KEY NOT NULL,
            act_token TEXT,
            act_expiry TEXT)"""
        cur.execute(sql)
        sql = """INSERT OR IGNORE INTO 
                act_tokens (id, act_token) VALUES (?, ?)"""
        data1 = (1,'a1')    
        cur.execute(sql, data1)
        conn.commit()

        sql = """CREATE TABLE if not exists act_users(
            id INT PRIMARY KEY NOT NULL,
            act_user TEXT,
            act_pass TEXT)"""
        cur.execute(sql)
        sql = """INSERT OR IGNORE INTO 
                act_users (id, act_user, act_pass) 
                VALUES (?, ?, ?)"""
        data2 = (1,'a@a.com','abc123')    
        cur.execute(sql, data2)
        conn.commit()
        conn.close()
    
    def on_start(self):
        print('on_start')
        icons_item = {
            "folder": "My files",
            "account-multiple": "Shared with me",
            "star": "Starred",
            "history": "Recent",
            "checkbox-marked": "Shared with me",
            "upload": "Upload",
        }
        # print(icons_item)
        for icon_name in icons_item.keys():            
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item[icon_name])
            )
        log = LogInCard()
        log.act_token_db('Empty', 'Empty')
        self.root.ids.screen4.add_widget(LogInCard())
        
        print('main login')

        self.root.ids.box_home.add_widget(MyRecycleView())
        print('main home recycle')
    
    def on_stop(self):
        print('Finish')
    
    def on_resume(self):
        print('resume')
        

if __name__ == '__main__':
    print('START MAIN')
    TestNavigationDrawer().run()

