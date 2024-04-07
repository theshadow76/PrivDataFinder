from bs4 import BeautifulSoup
import requests

class Extract:
    def __init__(self) -> None:
        pass
    def GetData(self, websites: list = [], blacklist: list = ["youtube.com"], isgithub: bool = False):
        if isgithub:
            for web in websites:
                r = requests.get(f"{web}?raw=true")
                soup = BeautifulSoup(r.text, "lxml")
                data = soup.find("body")
                with open("TEMP-github-data.txt", "a", encoding="utf8", errors="ignore") as f:
                    f.write(data.text)
        else:
            for web in websites:
                if web not in blacklist:
                    r = requests.get(f"{web}")
                    soup = BeautifulSoup(r.text, "lxml")
                    data = soup.find("body")
                    with open("TEMP-google-data.txt", "a") as f:
                        f.write(data.text)
                return "Done"