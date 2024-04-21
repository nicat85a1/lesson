import requests
from bs4 import BeautifulSoup

username = input("İstifadəçi adını daxil edin: ")

def check_username(username):
    sites = {
        "Instagram":f"https://instagram.com/{username}",
    }
    
    results = []
    for site, url in sites.items():
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            if soup.find("meta", property="og:type", content="profile"):
                results.append(f"✅{site} tapıldı: {url}✅")
            else:
                results.append(f"⚠️{site} tapılmadı⚠️")
        else:
            results.append(f"⚠️{site} tapılmadı⚠️")
    
    return "\n".join(results)

print(check_username(username))