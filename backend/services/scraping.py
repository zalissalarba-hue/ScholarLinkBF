import requests
from bs4 import BeautifulSoup

def scrape_bourses(url):
    response = requests.get(url)
    response.raise_for_status()  # lève une erreur si le site est inaccessible

    soup = BeautifulSoup(response.text, "html.parser")

    # Exemple : récupérer tous les liens de bourses
    bourses = []
    for item in soup.select("div.bourse-item"):
        nom = item.select_one("h2").get_text(strip=True)
        email = item.select_one("span.email").get_text(strip=True)
        lien = item.select_one("a")["href"]

        bourses.append({
            "nom": nom,
            "email": email,
            "lien": lien
        })

    return bourses
