import requests
from bs4 import BeautifulSoup

url = input("Enter  a website URL:")

try:
    response = requests.get(url)
    response.raise_for_status()

except requests.exceptions.RequestException as e:
    print("Error fecting the URL:",e)    
    exit()

soup = BeautifulSoup(response.text,'htmal.parser')

print("\n Heading found on the page:\n")
for tag in ['h1','h2','h3']:
    for heading in soup.find_all(tag):
        print(f"{tag.upper()}:{heading.text.strip()}")