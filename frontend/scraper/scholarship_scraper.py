import requests
from bs4 import BeautifulSoup

def scrape_scholarships():

    url = "https://example.com"

    response = requests.get(url)

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    offres = soup.find_all("a")

    for offre in offres:
        print(offre.text)