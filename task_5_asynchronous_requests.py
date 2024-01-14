import requests
from bs4 import BeautifulSoup

base_url = "https://kinogo.inc/films-2023/page/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
    " Chrome/106.0.0.0 YaBrowser/22.11.0.2419 Yowser/2.5 Safari/537.36"
}


def make_request(url):
    response = requests.get(url, headers=headers)
    page = BeautifulSoup(response.text, "html.parser")
    movie_cards = page.find_all("div", class_="shortstory")

    for movie in movie_cards:
        name = movie.find("h2", class_="zagolovki").text
        with open("movies_asynchron.txt", "a") as file:
            file.write(f"{name}\n")


def main():
    # synchronously go through each page
    for page in range(1, 101):
        print(f"Page {page}")
        url = base_url + str(page) + "/"
        make_request(url)


if __name__ == "__main__":
    main()
