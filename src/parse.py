"""Module ot handle ranking downloads"""

import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import re
from datetime import datetime, timedelta, timezone, date
import numpy as np


def get_top_100(year, month, day):

    rank1 = get_ranking_page(year, month, day, page=1)
    rank2 = get_ranking_page(year, month, day, page=2)

    return pd.concat((rank1, rank2), ignore_index=True)


def get_ranking_page(year, month, day, page = 1):

    url = 'http://www.tennisexplorer.com/ranking/atp-men/' + str(year) + '?date=' + \
             str(year) + '-' + str(month) + '-' + str(day) +'&page=' + str(page)
    
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    html = response.read()

    soup = BeautifulSoup(html, "html.parser")
    
    table = soup.find("tbody", attrs={"class": "flags"})
    
    if table is None:
        return pd.DataFrame()
    

    trs = table.findAll('tr')
    result = pd.DataFrame()
        
    for tr in trs :

        player = tr.find("td" , attrs={"class": "t-name"}).text.strip() 
        rank = tr.find("td" , attrs={"class": "rank first"}).text.strip() 
        points = tr.find("td" , attrs={"class": "long-point"}).text.strip() 
        
        ## putting data together    
        dict = {'player' : player,
                 'rank' : int(rank.strip('.')), 
                 'points' : int(points)
                }
        
        data = pd.DataFrame([dict])
        result = pd.concat((result, data), ignore_index=True) 
    
    return result


def make_data_total(start_date: datetime, end_date: datetime):

    current_date = start_date
    data = []

    while current_date <= end_date:

        print(current_date)
        rankings = get_top_100(current_date.year, current_date.month, current_date.day)
        rank = rankings['rank']
        points = rankings['points']

        x = []
        for i in range(len(rank)):
            for _ in range(points[i]):
                x.append(rank[i]+1)
        
        data.append(x)

        current_date += timedelta(days=31)

    return data



if __name__ == '__main__':

    d1 = datetime(2023, 1, 1)
    d2 = datetime(2023, 3, 30)
    data = make_data_total(d1, d2)


    breakpoint()