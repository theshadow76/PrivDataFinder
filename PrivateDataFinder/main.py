import argparse
from rich.pretty import pprint as print

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
parser.add_argument("--dorks", "The dorks file path")

args = parser.parse_args()

def main():
    searchgoogle = args.searchgoogle
    regex = args.regex
    dorksfile = args.dorks
    if searchgoogle == "true":
        try: # This means dorksfile is a valid file
            dorks = []
            droks = None
            with open(dorksfile, "r") as f:
                droks = f.read()
            dorks = droks.split("\n")
            for dork in dorks:
                googlesearch = SearchData()
                data = googlesearch.Search(str(dork))
                ### REGEX ###
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