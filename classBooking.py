import os, csv

from enums import CampRegion

class Booking:
    def __init__(self, id, campID, camperID, regionID, bookingDate):
        self.id = id
        self.campID = campID
        self.camperID = camperID

        for e in CampRegion:
            if e.name == regionID:
                regionID = e.value
                break

        self.regionID = regionID
        self.bookingDate = bookingDate

    def writeBookingData(self):
        header = ['id', 'camp', 'van', 'ragion', 'book_date']

        if os.path.isfile('data/bookings.csv'):
            f = open('data/campers.csv', 'a', newline='', encoding='utf-8')
            writer = csv.writer(f)
            writer.writerow([self.id, self.campID, self.camperID, self.regionID, self.bookingDate])
            f.close()
        else:
            f = open('data/bookings.csv', 'w', newline='', encoding='utf-8')
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerow([self.id, self.campID, self.camperID, self.regionID, self.bookingDate])
            f.close()