import parse
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from datetime import datetime

def get_single_graph(year, month, day):

    rankings = parse.get_top_100(year, month, day)
    rank = rankings['rank']
    points = rankings['points']

    data = []
    for i in range(len(rank)):
        for _ in range(points[i]):
            data.append(rank[i]+1)

    plt.title("ATP Top 100 points distribution")
    counts, bins, patches = plt.hist(data, bins=100, color='royalblue')
    perc = np.round(sum(counts[:4])/sum(counts),4)
    for i in range(4):
        patches[i].set_color("navy")
    plt.annotate(text=f"{100*perc:.2f}%", xy=(50, 10000))
    plt.show()



def make_animation():

    date1 = datetime(2011, 1, 1)
    date2 = datetime(2016, 1, 1)
    data = parse.make_data_total(date1, date2)


    # Crea il grafico di base
    fig, ax = plt.subplots()


    # Funzione per creare gli istogrammi
    def update_hist(frame):
        ax.clear()
        c, b, p = ax.hist(data[frame], bins=100)  # Modifica il numero di bin se necessario
        perc = np.round(sum(c[:4])/sum(c),4)
        for i in range(4):
            p[i].set_color("navy")
        ax.annotate(text=f"{100*perc:.2f}%", xy=(50, 10000))
        ax.set_ylim(0, 16e3)
        ax.set_title(f'Istogramma {frame+1}')

    # Crea l'animazione
    ani = animation.FuncAnimation(fig, update_hist, frames=len(data), interval=200)

    # Salva l'animazione come file video
    ani.save('istogrammi.mp4', writer='ffmpeg')  # Assicurati di avere ffmpeg installato nel tuo sistema

    # Mostra l'animazione (opzionale)
    plt.show()





if __name__ == '__main__':

    make_animation()

    