import time


class HandleInput:
    def __init__(self):
        self.now = time.localtime(time.time())
        self.today_str = time.strftime('%Y-%m-%d %H%M%S', self.now)
        self.today_value = time.strftime('%Y-%m-%d', self.now)
        self.output_file_name = str(self.today_str).replace(" ", "_") + ".xls"
        self.input_path = "tasks.txt"
        self.ret_array = []
        with open(self.input_path) as f:
            l = f.readlines()
            for item in l:
                self.ret_array.append(item)
