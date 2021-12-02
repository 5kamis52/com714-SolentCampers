from enums import CamperType
import csv
import os

class Camper:
  def __init__(self, id, size):
    self.id = id
    for e in CamperType:
      if e.name == size:
        size = e.value
        break
    self.size = size

  def writeCamperData(self):
    header = ['id', 'type']

    if os.path.isfile('data/campers.csv'):
      f = open('data/campers.csv', 'a', newline='', encoding='utf-8')
      writer = csv.writer(f)
      writer.writerow([self.id, self.size])
      f.close()
    else:
      f = open('data/campers.csv', 'w', newline='', encoding='utf-8')
      writer = csv.writer(f)
      writer.writerow(header)
      writer.writerow([self.id, self.size])
      f.close()