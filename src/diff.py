import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import os, pathlib
import tqdm

import parse


def get_graph_big3():

    big_3 = ("Djokovic Novak", "Nadal Rafael", "Federer Roger")

    points1 = np.zeros(100)
    points2 = np.zeros(100)
    start_date = datetime(2015, 1, 1)
    end_date = datetime(2023, 11, 1)
    n1 = 0
    n2 = 0



    while start_date < end_date:
        rank = parse.get_top_100(start_date.year, start_date.month, start_date.day)
        print(start_date)
        if all(b in rank['player'].values[:3] for b in big_3):
            points1 += rank['points'].values
            n1 += 1
        else:
            points2 += rank['points'].values
            n2 += 1

        start_date += timedelta(weeks=10)
        
    points1 /= n1
    points2 /= n2

    perc1 = np.round(sum(points1[:4])/sum(points1),4)
    perc2 = np.round(sum(points2[:4])/sum(points2),4)

    plt.subplot(2,1,1)
    plt.title(f"Big 3 - {perc1}")
    plt.stairs(points1, np.arange(len(points1)+1))

    plt.subplot(2,1,2)
    plt.title(f"No big 3 - {perc2}")
    plt.stairs(points2, np.arange(len(points2)+1))
    breakpoint()


if __name__ == '__main__':

    get_graph_big3()