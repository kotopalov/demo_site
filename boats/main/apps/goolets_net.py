
import requests
from bs4 import BeautifulSoup
class GooletsNet:

    url = 'https://www.goolets.net/yacht-rentals?page=0'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/122.0.0.0 Safari/537.36"
    }

    @classmethod
    def get_data(cls):
        response = requests.get(cls.url, headers=cls.headers)

        soup = BeautifulSoup(response.text, 'html')
        wrapper_list = soup.find('div',
                                 attrs={"class": "goolets--list-wrapper"})

        goolets_items = wrapper_list.find_all('div',
                                              attrs={"class": "goolets-item"})

        columns = ["name", "price", "location", "length", "cabins", "crew", "href", "img"]
        rows = []

        for item in goolets_items:
            # .select_one() search by CSS-selector
            name = item.select_one('h2').text.strip() if item.select_one(
                'h2') else None
            price = item.select_one(
                '.price p:nth-of-type(2)').text.strip() if item.select_one(
                '.price p:nth-of-type(2)') else None
            info_text = item.select_one(
                '.text .link').text.strip() if item.select_one(
                '.text .link') else ""
            href = item.select_one('a.stretched-link')[
                'href'].strip() if item.select_one('a.stretched-link') else None
            img = item.select_one('.image img')[
                'src'].strip() if item.select_one('.image img') else None

            # Divide info_text по " | " if necessary
            info_parts = [part.strip() for part in
                          info_text.split('|')] if info_text else []

            # took values form из info_parts
            location = info_parts[0] if len(info_parts) > 0 else None
            length = info_parts[1] if len(info_parts) > 1 else None
            cabins = info_parts[2] if len(info_parts) > 2 else None
            crew = info_parts[3] if len(info_parts) > 3 else None

            rows.append([name, price, location, length, cabins, crew, href, img])

        return {"columns": columns, "rows": rows}