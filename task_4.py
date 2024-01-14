from multiprocessing import Process

import requests
from bs4 import BeautifulSoup

base_url = "https://kinogo.inc/films-2023/page/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
    " Chrome/106.0.0.0 YaBrowser/22.11.0.2419 Yowser/2.5 Safari/537.36"
}


def parsing_movie_titles(url):
    response = requests.get(url, headers=headers)
    page = BeautifulSoup(response.text, "html.parser")
    movie_cards = page.find_all("div", class_="shortstory")

    for movie in movie_cards:
        name = movie.find("h2", class_="zagolovki").text
        with open("movies_process.txt", "a") as file:
            file.write(f"{name}\n")


if __name__ == "__main__":

    # We create processes for simultaneous page parsing. In this case 50 pages
    processes = []
    for page in range(1, 51):  # this site has a maximum of 113 pages
        url = base_url + str(page) + "/"
        process = Process(target=parsing_movie_titles, args=(url,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
