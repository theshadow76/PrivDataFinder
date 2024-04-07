import argparse
from rich.pretty import pprint as print

# locals
from src.google.getdata import SearchData

parser = argparse.ArgumentParser(
    prog="Private Data Finder",
    description="Private Data Finder is to find data like BTC Private keys or AWS secret keys online",
    epilog="END"
)

parser.add_argument("--searchgoogle")

args = parser.parse_args()

def main():
    searchgoogle = args.searchgoogle
    if searchgoogle == "true":
        googlesearch = SearchData()
        print(googlesearch.Search("BTC"))
    else:
        print("You need to select a option")

if __name__ == '__main__':
    main()