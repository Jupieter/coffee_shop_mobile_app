import os
os.environ['KIVY_NO_CONSOLELOG'] = '1'
cwd = os.getcwd()
print(cwd)
os.environ['KIVY_HOME'] = cwd + '/conf'

import sqlite3


from kivy.lang import Builder
from kivy.clock import Clock
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
from kivy.properties import StringProperty, ListProperty, ObjectProperty
from kivymd.uix.list import OneLineIconListItem
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivy.uix.recycleview import RecycleView

from login import LoginCard
from item_drawer import ItemDrawer

# class ItemDrawer(OneLineIconListItem):
#     icon = StringProperty()
#     text_color = ListProperty((0, 0, 0, 1))

login_card = ObjectProperty()
conn = 'dataDB'

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
    print('recycle 1')
    def __init__(self, **kwargs):
        super(MyRecycleView, self).__init__(**kwargs)
        print('recycle 2')
        self.load_data()
        print('recycle 3')
        Clock.schedule_interval(self.load_data, 3)

    def load_data(self, *args):
        conn = sqlite3.connect('coffe_app.db')
        active_token = 'semmi se'
        # active_token = conn.execute("SELECT token from tokens")
        # print('tok: ', active_token)
        # for row in active_token:
        #     print ("token = ", row[0])
        #     print(row)
        #     if row == "":
        #         print('semmi se')


class TestNavigationDrawer(MDApp):
    def build(self):
        print('main 1')
        # Create Database Or Connect To One
        conn = sqlite3.connect('coffe_app.db')
        # Create A Cursor
        cur = conn.cursor()
        sql1 = """CREATE TABLE if not exists act_tokens(
            id INT PRIMARY KEY NOT NULL,
            act_token TEXT)"""
        cur.execute(sql1)
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Brown"  # "Purple", "Red"
        return Builder.load_file('kv/main.kv')
    
    def on_start(self):
        print('main 2')
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
            
        self.root.ids.box_login.add_widget(LoginCard())
        print('main login_card')

        self.root.ids.box_home.add_widget(MyRecycleView())
        print('main home recycle')
        

if __name__ == '__main__':
    print('0')
    TestNavigationDrawer().run()