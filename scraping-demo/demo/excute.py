import os
from datetime import datetime

import requests
from bs4 import BeautifulSoup


class Titles(object):

    def __init__(self):
        self.url = 'http://jiandan.net/' + datetime.now().strftime('%Y/%m/%d')
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'}
        self.path = 'E:\jiandan'

    def get_today_title(self):
        res = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(res.text, 'lxml')
        all_a = soup.select('#content > div > div.indexs > h2 > a')
        for a in all_a:
            value = '{0},{1}'.format(a.text, a['href'])
            self.create_dir(self.path, value)

    def create_dir(self, path, value):
        os.chdir(self.path)
        date = datetime.now().strftime('%Y-%m-%d')
        file_name = date + '.txt'
        file = open(file_name, 'a')
        file.write(value + '\n')
        file.close()



if __name__=='__main__':
    Titles().get_today_title()