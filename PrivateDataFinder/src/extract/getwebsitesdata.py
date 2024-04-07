from bs4 import BeautifulSoup
import requests

class Extract:
    def __init__(self) -> None:
        pass
    def GetData(self, websites):
        for web in websites:
            r = requests.get(web)
            soup = BeautifulSoup(r.text, "lxml")
            data = soup.find("body")
            with open("TEMP-google-data.txt", "a") as f:
                f.write(data.text)
        return "Done"