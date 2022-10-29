import requests


def main(event, context):
    url = "https://www.google.com/"
    res = requests.get(url)
    
    return res.status_code