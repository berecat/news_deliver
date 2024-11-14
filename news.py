import requests
import json 
import os 
from dotenv import load_dotenv
load_dotenv()
NEWS_TOKEN = os.getenv("NEWS_API_TOKEN")


# INITIALIZE PARAMS
url = "https://api.newscatcherapi.com/v2/search"
# url = "https://api.newscatcherapi.com/v2/latest_headlines"
search_people = ["Elon Musk", "Joe Biden", "Tim Cook", "Jerome Powell"]
countries = ["SE", "US"]
# topics : news sport tech world finance politics business economics 
# entertainment beauty travel music food science gaming energy
topics = ["tech", "world", "finance", "politics", "business", "economics", "science"]

# to and from 
to = "1 day ago"
frm = "1 day ago"

# api token
headers = {
    "x-api-key": NEWS_TOKEN
}

def make_query_OR(li : list()):
    if (len(li) <= 0): return ""
    ret = f"\"{li[0]}\""
    for s in li[1::]:
        ret += f" OR \"{s}\""
    return ret

def find_news():
    querystring = {"q":make_query_OR(search_people), "from_rank":100, "lang":"en", "sort_by":"relevancy", "from":"2 days ago", "page":"1"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    out_file = open("text1.json", "w")
    # json.dump(response.json(), out_file, indent=4)
    if (response.status_code == 200):
        json.dump(response.json(), out_file, indent=4)
    else:
        print("RESPONSE STATUS CODE NOT 200")
        out_file.write("")
    out_file.close()

if __name__ == "__main__":
    find_news()



