from enums import CampRegion
import csv
import os

class Camp:
  def __init__(self, id, name, region):
    self.id = id
    self.name = name
    
    for e in CampRegion:
      if e.name == region:
        region = e.value
        break

    self.region = region

  def writeCampData(self):     
    header = ['id', 'name', 'region']

    if os.path.isfile('data/camps.csv'):
      f = open('data/camps.csv', 'a', newline='', encoding='utf-8')
      writer = csv.writer(f)
      writer.writerow([self.id, self.name, self.region])
      f.close()
    else:
      f = open('data/camps.csv', 'w', newline='', encoding='utf-8')
      writer = csv.writer(f)
      writer.writerow(header)
      writer.writerow([self.id, self.name, self.region])
      f.close()