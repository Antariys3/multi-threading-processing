import threading

import requests
from bs4 import BeautifulSoup

base_url = "https://klassmarket.ua/ru/aktsii/katalog-aktsionnykh-tovarov?page="
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
    " Chrome/106.0.0.0 YaBrowser/22.11.0.2419 Yowser/2.5 Safari/537.36"
}


def parsing_of_promotional_products(url):
    response = requests.get(url, headers=headers)
    page = BeautifulSoup(response.text, "html.parser")
    product_cards = page.find_all("div", class_="product-sale my-class")

    for product in product_cards:
        name = product.find("div", class_="product-ten__name").text
        price = product.find("div", class_="product-price-old__current").text
        with open("products.txt", "a") as file:
            file.write(f"{name} Цена: {price}\n")


if __name__ == "__main__":
    threads = []
    # create threads for simultaneous parsing of five pages
    for page in range(1, 5):  # Five is the maximum number of pages on this site
        url = base_url + str(page)
        t = threading.Thread(target=parsing_of_promotional_products, args=(url,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
