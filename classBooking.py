import os, csv

class Booking:
    def __init__(self, id, campID, camperID, regionID, bookingDate, campingDate):
        self.id = id
        self.campID = campID
        self.camperID = camperID
        self.regionID = regionID
        self.bookingDate = bookingDate
        self.campingDate = campingDate

    def writeBookingData(self):
        header = ['id', 'camp', 'van', 'ragion', 'book_date', 'camp_date']

        if os.path.isfile('data/bookings.csv'):
            f = open('data/campers.csv', 'a', newline='', encoding='utf-8')
            writer = csv.writer(f)
            writer.writerow([self.id, self.campID, self.camperID, self.regionID, self.bookingDate, self.campingDate])
            f.close()
        else:
            f = open('data/bookings.csv', 'w', newline='', encoding='utf-8')
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerow([self.id, self.campID, self.camperID, self.regionID, self.bookingDate, self.campingDate])
            f.close()