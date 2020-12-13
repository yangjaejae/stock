import requests
from bs4 import BeautifulSoup as bs
import re

class Stock:

    def __init__(self):
        self.url_naver_fin = 'https://finance.naver.com/sise/sise_market_sum.nhn'
        self.url_naver_sise = 'https://finance.naver.com/item/sise.nhn?code=%s'
        self.top50_list = []

    def get_html(self, url):
        url = self.url_naver_fin
        html = requests.get(url).text
        html = html.replace('\n','')
        html = html.replace('\t','')
        html = html.replace(',','')
        html = html.replace('.','')
        soup = bs(html, 'html.parser')

        return soup

    def get_top50_list(self):
        top50_list = []
        soup = self.get_html(self.url_naver_fin)

        cost_table = soup.find('table', {'class': 'type_2'})
        trs = cost_table.find_all('tr')

        for idx, tr in enumerate(trs):
            a_tag = tr.find_all('a')
            if a_tag:
                p = re.compile('(?<==)[0-9]+')
                top50_list.append(p.search(str(a_tag[0])).group())

        print(top50_list)
        return top50_list

    def get_20_line(self, item):
        line_20 = 0
        soup = self.get_html(self.url_naver_sise % item)

        print(soup.find_all('body > table.type2'))
        # cost_table = soup.find('table', {'class': 'type2'})
        # print(cost_table)
        # trs = cost_table.find_all('tr')

        # print(trs)

        # return line_20