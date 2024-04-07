import serpapi

def google(q):
    s = serpapi.search(q)
    return s

print(google("BTC"))