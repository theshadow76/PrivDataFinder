import argparse
from rich.pretty import pprint as print

# locals
from src.google.getdata import SearchData

parser = argparse.ArgumentParser(
    prog="Private Data Finder",
    description="Private Data Finder is to find data like BTC Private keys or AWS secret keys online",
    epilog="END"
)

googlesearch = SearchData()
print(googlesearch.Search("BTC"))