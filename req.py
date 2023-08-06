import requests
def get_data(keyword):
    url = f"https://newsapi.org/v2/everything?q={keyword}&sortBy=publishedAt&apiKey=0705f7e3a84d4d6bab81e47dfece97f5&language=en"
    data = requests.get(url)
    data = data.json()
    return data["articles"]
