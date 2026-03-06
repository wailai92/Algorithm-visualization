import os
import sys

class Path_manager():
    def __init__(self):
        self.base_dir = self.get_base_dir()
    def get_base_dir(self):
        if getattr(sys, 'frozen', False):
            return os.path.dirname(sys.executable)
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    def get_sort_dir(self):
        return os.path.join(self.base_dir, "algorithm", "sort")
    def get_graph_dir(self):
        return os.path.join(self.base_dir, "algorithm", "graph")