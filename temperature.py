import requests
from selectorlib import Extractor

class Temperature:

    base_url = 'https://www.timeanddate.com/weather/'
    yml_path = 'temperature.yaml'

    headers = {
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    def __init__(self, country, city):
        self.county = country.replace(" ", "-")
        self.city = city.replace(" ", "-")

    def build_url(self):
        url = self.base_url + self.county + "/" + self.city
        return url

    def scrape(self):

        url = self.build_url()
        r = requests.get(url, headers = self.headers)
        c = r.text
        extractor = Extractor.from_yaml_file(self.yml_path)
        raw_result = extractor.extract(c)
        return raw_result



    def get(self):
        scraped_content = self.scrape()
        result = float(scraped_content['temp'].replace("\xa0°C",""))
        return result

if __name__ == '__main__':
    temperature = Temperature('Italy', 'Rome')
    print(temperature.get())
    print(temperature.build_url())


















