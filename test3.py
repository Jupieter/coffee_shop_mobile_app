import os
os.environ['KIVY_NO_CONSOLELOG'] = '1'
cwd = os.getcwd()
print(cwd)
os.environ['KIVY_HOME'] = cwd + '/conf'

from kivy.lang import Builder

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
from kivy.properties import StringProperty, ListProperty
from kivymd.uix.list import OneLineIconListItem
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.card import MDCard

from login import LoginCard
from item_drawer import ItemDrawer
# class ItemDrawer(OneLineIconListItem):
#     icon = StringProperty()
#     text_color = ListProperty((0, 0, 0, 1))

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


class TestNavigationDrawer(MDApp):
    def build(self):
        print('zero')
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Brown"  # "Purple", "Red"
        return Builder.load_file('kv/test3.kv')
    
    def on_start(self):
        print('here')
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
            
        self.root.ids.box_login.add_widget(
            LoginCard(
                line_color=(0.2, 0.2, 0.2, 0.8),         
                )
            )




TestNavigationDrawer().run()