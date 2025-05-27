
import requests
from bs4 import BeautifulSoup
class MBlueyachtsCom:

    url = 'https://m-blueyachts.com/luxury-yacht-charter/page/9'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/122.0.0.0 Safari/537.36"
    }

    @classmethod
    def get_data(cls):
        response = requests.get(cls.url, headers=cls.headers)

        soup = BeautifulSoup(response.text, 'html')

        thumbs = soup.find_all('li', attrs={"class": "rowthumb"})



        columns = ["name", "href", "img", "thumb-price", "thumb-pax", "thumb-feet"]
        rows = []

        for item in thumbs:
            data = [
                item.select_one(
                    '.thumb-name a').text.strip() if item.select_one(
                    '.thumb-name a') else None,
                item.select_one('.thumb-name a')[
                    'href'] if item.select_one('.thumb-name a') else None,
                item.select_one('.feat-thumb img')[
                    'src'] if item.select_one('.feat-thumb img') else None,
                item.select_one(
                    '.thumb-price').text.strip() if item.select_one(
                    '.thumb-price') else None,
                item.select_one(
                    '.thumb-pax').text.strip() if item.select_one(
                    '.thumb-pax') else None,
                item.select_one(
                    '.thumb-feet').text.strip() if item.select_one(
                    '.thumb-feet') else None,
            ]
            rows.append(data)

        return {"columns": columns, "rows": rows}