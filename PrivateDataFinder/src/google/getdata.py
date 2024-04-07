from googlesearch import search

class SearchData:
    def __init__(self) -> None:
        pass
    def Search(self, prompt: str = "Private Key"):
        # to search
        query = prompt
        data = []
        
        for j in search(query):
            print(f"Extracting {j} | Google Search")
            data.append(j)
        return data