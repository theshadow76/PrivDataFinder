import argparse
from rich.pretty import pprint as print
import json
import re
import time

# locals
from src.google.getdata import SearchData
from src.extract.getwebsitesdata import Extract

parser = argparse.ArgumentParser(
    prog="Private Data Finder",
    description="Private Data Finder is to find data like BTC Private keys or AWS secret keys online",
    epilog="END"
)


parser.add_argument("--searchgoogle", help="Search in google")
parser.add_argument("--regex", help="REGEX List file where there are a list of REGEX to try and see if we get any matches")
parser.add_argument("--dorks", help="The dorks file path")

args = parser.parse_args()

def main():
    searchgoogle = args.searchgoogle
    regex = args.regex
    dorksfile = args.dorks
    if searchgoogle == "true":
        try: # This means dorksfile is a valid file
            dorks = []
            droks = None
            regex2 = None
            with open(regex, "r") as f:
                regex2 = json.load(f)
            with open(dorksfile, "r") as f:
                droks = f.read()
            dorks = droks.split("\n")
            for dork in dorks:
                googlesearch = SearchData()
                data = googlesearch.Search(str(dork))
                ### REGEX ###
                validation_results = {}
                data_to_check = data
                for key, regex in regex2.items():
                    for data2 in data_to_check:
                        match = re.search(regex, data2)  # Check if key exists
                        validation_results[key] = bool(match)
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
    else:
        print("You need to select a option")

if __name__ == '__main__':
    main()