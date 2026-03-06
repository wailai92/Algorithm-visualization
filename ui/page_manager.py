from ui.component.button import Button
from ui.main_page import Main_page
from ui.sort_page import Sort_page
from ui.graph_page import Graph_page
from ui.setting_page import Setting_page

class Page_manager():
    def __init__(self):
        pass
    def switch_page(self, page_name):
        if page_name == "main":
            return Main_page(self)
        if page_name == "sort":
            return Sort_page(self)
        if page_name == "graph":
            return Graph_page(self)
        if page_name == "setting":
            return Setting_page(self)