import os


class TimestampCache:
    file_name = "\\.cache"
    file_path = os.path.dirname(os.path.abspath(__file__))

    def __init__(self):
        pass

    def save_timestamp(self, time_to_save):
        with open(self.file_path + self.file_name, 'w') as f:
            f.write(str(time_to_save))

    def load_timestamp(self):
        with open(self.file_path + self.file_name, 'r') as f:
            return float(f.read())
