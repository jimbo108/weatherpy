import datetime
import time
import os
from urllib2 import urlopen, URLError, HTTPError

def data_parse(pathname):
    with open(pathname) as f:
        content = f.readlines()
    return content

def main():
    pathname = "/home/james/private/weatherpy/199701FLG"
    rawfile = data_parse(pathname)
    wm = weather_month(pathname)
    return 1

class weather_day:
    def __init__(self, tmax, tmin, date):
        self.tmax = tmax
        self.tmin = tmin
        self.date = date

class weather_month:
    elements = []
    days = []
    month_and_year = None
    temp_elements = []
    def __init__(self, filepath):
        self.lines = data_parse(filepath)
        self.temp_elements = []
        a = 0
        for j in self.lines:
            if a == 0:
                try:
                    self.month_and_year = j
                except ValueError:
                    print "Error parsing month and year."
            if a > 5:
                print(j.strip().split(","))
                self.temp_elements.append(j.strip().split(","))
            if a > 34:
                break
            a = a + 1
        for element in self.temp_elements:
            if len(element) > 2 and len(element[0]) is not 0:
                try:
                    if len(element[0]) == 1:
                        element[0] = '0' + element[0]
                    print(str(element))
                    string_date = element[0] + "/" + self.month_and_year
                    string_date = string_date.strip()
                    print("string_date is " + string_date)
                    real_date = time.strptime(string_date, "%d/%m/%Y")
                    self.days.append(weather_day(float(element[1].translate(None, '*')), float(element[2].translate(None, '*')), real_date))
                except ValueError:
                    self.days.append(weather_day(None, None, real_date))
                    print "Error parsing temperature."
                    print "string_date that failed is " + string_date
        self.elements.append(self.temp_elements)
        print("done with __inti__")

class weather_year:
    months = []
    def __init__(self, filepath_dict):
        for month_index in range(0,5):
            self.months.append(weather_month(filepath_dict[month_index]))


FILE_EXTENSION_STRING = '.tar.gz'
START_YEAR = 1997
END_YEAR = 2006
URL_BEGINNING = 'https://www.ncdc.noaa.gov/orders/qclcd/'
for year in range(START_YEAR, END_YEAR):
    str_year = str(year)
    for month in range(1, 12):
        str_month = str(month)
        if len(str_month) == 1:
            str_month = '0' + str_month
        url_end = URL_BEGINNING + str_year + str_month + FILE_EXTENSION_STRING





path_1997_FLG_folder = "1997FLG/"
month_path_array = [ path_1997_FLG_folder + "199701FLG", path_1997_FLG_folder + "199702FLG",
path_1997_FLG_folder + "199703FLG", path_1997_FLG_folder + "199704FLG",
path_1997_FLG_folder + "199705FLG", path_1997_FLG_folder + "199706FLG"]
wy = weather_year(month_path_array)
for month in wy.months:
    for day in month.days:
        print("Tmax is " + str(day.tmax) + ", Tmin is " + str(day.tmin))
