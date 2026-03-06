import os

class Algorithm_manager():
    def __init__(self, path_manager):
        self.path_manager = path_manager
        self.sort_dir = self.path_manager.get_sort_dir()
        self.graph_dir = self.path_manager.get_graph_dir()
    def get_sort_algo(self):
        if not os.path.exists(self.sort_dir):
            return []
        results = []
        for file_name in os.listdir(self.sort_dir):
            full_path = os.path.join(self.sort_dir, file_name)
            if os.path.isfile(full_path) and file_name.endswith(".py"):
                results.append(os.path.splitext(file_name)[0])
        return results
    def get_graph_algo(self):
        if not os.path.exists(self.graph_dir):
            return []
        results = []
        for file_name in os.listdir(self.graph_dir):
            full_path = os.path.join(self.graph_dir, file_name)
            if os.path.isfile(full_path) and file_name.endswith(".py"):
                results.append(os.path.splitext(file_name)[0])
        return results