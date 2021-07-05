import bs4
import pandas as pd

class Person:
  def __init__(self):
    self.rank = ""
    self.name = ""
    self.lang = ""
    self.exer = ""
    self.temps = ""
    self.ecole = ""

  def  to_string(self):
    return "rank:\t" + self.rank + "\tname:\t" + self.name + "\t\t\t\tlang:\t" \
    + self.lang + "\texer:\t" + self.exer + "\ttemps:\t" + self.temps + "\tecole:\t" + self.ecole

  def  to_csv(self):
    return self.rank + ";" + self.name + ";" + self.lang + ";" + self.exer + ";" + self.temps + ";" + self.ecole + "\n"

TOTAL_PAGE = 120

persons = []

for pageNum in range(2, TOTAL_PAGE + 1):

    page = open("./pages/battle_dev" + str(pageNum) + ".html", "r", encoding="utf-8")

    noStarchSoup = bs4.BeautifulSoup(page, 'html.parser')

    table_body = noStarchSoup.select('#form_data1 tbody')[0]
    table_rows = table_body.find_all('tr')

    for row in table_rows:
        header = row.find('th')
        cols = row.find_all('td')
        person = Person()
        person.rank = header.getText()
        person.name = cols[0].getText()
        person.lang = cols[1].getText()
        person.exer = cols[2].getText()
        person.temps = cols[3].getText()
        person.ecole = cols[4].getText()
        persons.append(person)

for person in persons:
    fileToSave = open('./data/data.csv', 'a', encoding='utf-8')
    fileToSave.write(person.to_csv())