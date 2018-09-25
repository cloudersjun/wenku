# -*- coding: utf-8 -*-
import logging
import sys
from datetime import timedelta
import re
import json

reload(sys)
sys.setdefaultencoding('utf8')
logging.basicConfig(filename='logger.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s : %(levelname)s : %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filemode='w'
                    )


class HandleParse:
    def __init__(self, response):
        self.response = response

    def parse(self):
        ret = ""
        # logging.info("parse:{}", self.response.text())
        te = self.response.xpath("//p/text()").extract()
        for s in te:
            ret += s
        logging.info(ret)
        return ret
