class MEM_WB:
    def __init__(self):
        self.data = None

    def read(self):
        return self.data

    def write(self, new_data):
        self.data = new_data

