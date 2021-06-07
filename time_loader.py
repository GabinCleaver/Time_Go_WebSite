from urllib.request import urlopen
import time


def get_load_time(url):

    if ("https" or "http") in url: 
        open_this_url = urlopen(url)
    else:
        open_this_url = urlopen("https://" + url)
    start_time = time.time()
    open_this_url.read()
    end_time = time.time()
    open_this_url.close()
    time_to_load = end_time - start_time

    return time_to_load


if __name__ == '__main__':
    try:
        url = input("Saisissez l'url dont vous souhaitez vérifier le temps de chargement : ")
        print(f"\nLe temps de chargement de {url} est de {get_load_time(url):.2} secondes.")
    except:
        print("Erreur dans la requête")