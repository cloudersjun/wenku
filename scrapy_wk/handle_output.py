# -*- coding: utf-8 -*-
import os
import sys

import xlsxwriter

reload(sys)
sys.setdefaultencoding('utf8')


class HandleOutput:
    def __init__(self, path, name, header, result_map, input_array):
        self.output_path = path
        self.output_file_name = name
        self.header = header
        self.result_map = result_map
        self.input_array = input_array

    def write(self):
        if not os.path.exists(self.output_path):
            os.mkdir(self.output_path)
        if os.path.exists(self.output_path + self.output_file_name):
            os.remove(self.output_path + self.output_file_name)
        f = open(self.output_path + self.output_file_name, 'a')
        f.write(self.result_map)
        f.close()
