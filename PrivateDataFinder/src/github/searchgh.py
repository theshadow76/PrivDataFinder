import requests

def SearchGitgub(token, query):
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",  # Replace <YOUR-TOKEN> with your actual token
        "X-GitHub-Api-Version": "2022-11-28"
    }
    url = f"https://api.github.com/search/code?q={query}" 

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        # Process the returned data
        return data
    else:
        print("An error occurred:", response.status_code)