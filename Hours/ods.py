from pyexcel_ods import get_data
from pyexcel_ods import save_data


class CalcSheet:

    file_path = None
    data = None

    def __init__(self, file_path):
        self.file_path = file_path
        self.data = get_data(self.file_path)

    def close(self):
        save_data(self.file_path, self.data)
