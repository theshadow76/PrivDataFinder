import argparse
from rich.pretty import pprint as print
import json
import re
import time

# locals
from src.google.getdata import SearchData
from src.extract.getwebsitesdata import Extract
from src.github.searchgh import SearchGitgub

parser = argparse.ArgumentParser(
    prog="Private Data Finder",
    description="Private Data Finder is to find data like BTC Private keys or AWS secret keys online",
    epilog="END"
)


parser.add_argument("--searchgoogle", help="Search in google")
parser.add_argument("--regex", help="REGEX List file where there are a list of REGEX to try and see if we get any matches")
parser.add_argument("--dorks", help="The dorks file path")
parser.add_argument("--searchgithub", type=bool, help="Search in Github")
parser.add_argument("--ghtoken")
parser.add_argument("--ghquery")

args = parser.parse_args()

def main():
    searchgoogle = args.searchgoogle
    regex = args.regex
    dorksfile = args.dorks
    searchgithub = args.searchgithub
    ghtoken = args.ghtoken
    ghquery = args.ghquery
    if searchgoogle == "true":
        try: # This means dorksfile is a valid file
            dorks = []
            droks = None
            regex2 = None
            with open(str(regex), "r", encoding="utf8") as f:
                regex2 = json.load(f)
            with open(dorksfile, "r", encoding="utf8") as f:
                droks = f.read()
            try:
                dorks = droks.split("\n")
            except Exception as e:
                print(e)
            for dork in dorks:
                googlesearch = SearchData()
                data = googlesearch.Search(str(dork))
                ### REGEX ###
                validation_results = {}
                data_to_check = data
                for key, regex in regex2.items():
                    for data2 in data_to_check:
                        try:
                            match = re.search(regex, str(data2))  # Check if key exists
                            validation_results[key] = bool(match)
                        except Exception as e:
                            print(f"Something went wrong trying to validate: {e}")
                if "True" in validation_results:
                    with open("validations.txt", "a") as f:
                        f.write(f"{str(validation_results)}\n")
                else:
                    print("No match")
                time.sleep(5)
                

        except Exception as e:
            if dorksfile is None:
                googlesearch = SearchData()
                extract = Extract()
                data = googlesearch.Search("BTC")
                extract.GetData(data)
            else:
                print(f"Something went wrong: {e}")
    elif searchgithub:
        links = []
        try:
            resulsts = SearchGitgub(token=ghtoken, query=ghquery)['items']
            for result in resulsts:
                links.append(result['html_url'])
            extract = Extract()
            extract.GetData(websites=links, isgithub=True)
            try:
                ### REGEX ###
                validation_results = {}
                data_to_check = None
                regex3 = None
                try:
                    with open("TEMP-github-data.txt", "r", encoding="utf8") as f:
                        data_to_check = f.read()
                except Exception as e:
                    print(f"Something happend opening the github file: {e}")
                try:
                    with open(regex, "r", encoding="utf8") as f:
                        regex3 = json.load(f)
                except Exception as e:
                    print(f"Something happened opening regex: {e}")
                try:
                    data3 = data_to_check.split("\n")
                except Exception as e:
                    print(f"Something happened spliting: {e}")
                for key, regex in regex3.items():
                    for data2 in data3:
                        try:
                            match = re.search(regex, str(data2))  # Check if key exists
                            validation_results[key] = bool(match)
                            print(f"{key} | {validation_results[key]}")
                        except Exception as e:
                            print(f"Something went wrong trying to validate: {e}")
                if "True" in validation_results:
                    with open("validations.txt", "a") as f:
                        f.write(f"{str(validation_results)}\n")
                else:
                    print("No match | searching for AWS creds now")
                    pattern = re.compile(r"AWS_(ACCESS_KEY_ID|SECRET_ACCESS_KEY)=([A-Z0-9+/]{20}|[A-Za-z0-9/+=]{40})")
                    text = None
                    with open("TEMP-github-data.txt", "r", encoding="utf8") as f:
                        text = f.read()
                    for line in text.splitlines():
                        match = pattern.search(line)
                        if match:
                            key_type = match.group(1)
                            key_value = match.group(2)
                            print(f"Pothential key! | Type={key_type} | Value={key_value}") 
            except Exception as e:
                print(f"Something went wrong in regex: {e}")
        except Exception as e:
            print(f"Something went wrong in githubsearch: {e}")
    else:
        print("You need to select a option")

if __name__ == '__main__':
    main()