import requests, bs4

res = requests.get('https://nostarch.com')
res.raise_for_status()

exampleFile = open('example.html')

noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')

# print(noStarchSoup.select('p')[0].getText())
print(noStarchSoup)