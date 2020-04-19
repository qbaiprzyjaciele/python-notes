import requests as req
from bs4 import BeautifulSoup

subs = ['creepy']




def fetch_sub_content(sub_name):
    headers = {'Accept': 'application/json'}
    resp = req.get('https://reddit.com/r/creepy.json', { 'User-Agent': 'Chromium'})
    print(resp.status_code)
    if resp.status_code == 200:
        resp_mapped = map(lambda item: 
            {
                'title': item['data']['title'], 
                'img': item['data']['thumbnail'], 
                'created': item['data']['created_utc']
            }, 
            resp.json()['data']['children'])
        return resp_mapped
    elif resp.status_code == 429:
        print('Too many requests')
    else:
        print('Unsupported status code' + resp.status_code)


def get_image(url):
    print('not yet implemented')
    
mapped = fetch_sub_content('')
print(mapped)
