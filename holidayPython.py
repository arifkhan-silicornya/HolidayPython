# from datetime import date
import datetime
import holidays 
import json

from pytz import timezone
from datetime import date

class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,sort_keys=True, indent=4)


# today = date.today()
# print("Today's date:", today)
NewYorkYear = datetime.datetime.now(timezone('America/New_York')).date().year
ChicagoYear = datetime.datetime.now(timezone('America/Chicago')).date().year
ShanghaiYear = datetime.datetime.now(timezone('Asia/Shanghai')).date().year
ParisYear = datetime.datetime.now(timezone('Europe/Paris')).date().year
TokyoYear = datetime.datetime.now(timezone('Asia/Tokyo')).date().year
Hong_KongYear = datetime.datetime.now(timezone('Asia/Hong_Kong')).date().year
LondonYear = datetime.datetime.now(timezone('Europe/London')).date().year
IndiaYear = datetime.datetime.now(timezone('Asia/Kolkata')).date().year
TorontoYear = datetime.datetime.now(timezone('America/Toronto')).date().year
BerlinYear = datetime.datetime.now(timezone('Europe/Berlin')).date().year
RiyadhYear = datetime.datetime.now(timezone('Asia/Riyadh')).date().year
SeoulYear = datetime.datetime.now(timezone('Asia/Seoul')).date().year
ZurichYear = datetime.datetime.now(timezone('Europe/Zurich')).date().year
SydneyYear = datetime.datetime.now(timezone('Australia/Sydney')).date().year
Sao_PauloYear = datetime.datetime.now(timezone('America/Sao_Paulo')).date().year
JohannesburgYear = datetime.datetime.now(timezone('Africa/Johannesburg')).date().year
DhakaYear = datetime.datetime.now(timezone('Asia/Dhaka')).date().year
# todaydate = datetime.datetime.now(timezone('America/New_York')).time()


# a = datetime.datetime.now(timezone('Europe/Berlin'))
# v = datetime.datetime.now(timezone('Europe/Berlin')).today()
# v1 = datetime.datetime.now(timezone('America/New_York'))

# print("----------------")

# print(a)
# print(v)
# print(v1)




us_newYork_holidays = holidays.UnitedStates(state='NY',years = NewYorkYear)
us_Chicago_holidays = holidays.UnitedStates(state='IL',years = ChicagoYear)
china_holidays = holidays.China(years = ShanghaiYear)
France_holidays = holidays.France(years = ParisYear)
japan_holidays = holidays.Japan(years = TokyoYear)
HongKong_holidays = holidays.HongKong(years = Hong_KongYear)
uk_holidays = holidays.UnitedKingdom(years = LondonYear)
IndiaMumbai_holidays = holidays.India(prov="MH",years = IndiaYear)
Canada_holidays = holidays.Canada(years = TorontoYear)
Germany_holidays = holidays.Germany(prov="HE",years = BerlinYear)
SaudiArabia_holidays = holidays.SaudiArabia(years = RiyadhYear)
Korea_holidays = holidays.Korea(years = SeoulYear)
Swaziland_holidays = holidays.Swaziland(years = ZurichYear)
australia_holidays = holidays.Australia(years = SydneyYear)
br_holidays = holidays.Brazil(years = Sao_PauloYear)
SouthAfrica_holidays = holidays.SouthAfrica(years = JohannesburgYear)
bd_holidays = holidays.Bangladesh(years = DhakaYear)



state_array = [us_newYork_holidays,us_Chicago_holidays,china_holidays,France_holidays,japan_holidays,HongKong_holidays,uk_holidays,IndiaMumbai_holidays,Canada_holidays,Germany_holidays,SaudiArabia_holidays,Korea_holidays,Swaziland_holidays,australia_holidays,
br_holidays,SouthAfrica_holidays,bd_holidays]

city_array = ["New York","Chicago","Shanghai","Paris","Tokyo","Hong Kong","London","Mumbai","Toronto","Frankfurt am Main","Riyadh","Busan & Seoul","Zurich","Sydney","São Paulo","Sandton, Johannesburg","Dhaka"]


holidays = []
holidaysArray = []

Holiday = {}

i= 0
# Print all the holidays in year 2022
while(i < len(state_array)):
    for date,holiname in state_array[i].items():
        # print(date,holiname)
        holidays = [city_array[i],holiname,date]
        holidaysArray.append(holidays)
    i= i+1

i = 0

while(i < len(holidaysArray) ):
    j = 0
    while(j < len(holidays) ):
        
        print(holidaysArray[i][j])
        j = j+1
    
    i= i+1


# State Information every state

# {
# "id" : id,
# "Stock_Name" : name,
# "Country" : country,
# "State" : state,
# "TodayTime" : TodayTime,
# "TodayDate" : TodayDate,
# "TodayDay" : TodayDay,
# "TodayTimeString" : TodayTimeString,
# "startT" : startT,
# "endT" : endT,
# "weekOff1" : off1,
# "weekOff2" : off2,
# }

# Holiday = Object()
# me.name = "Onur"
# me.age = 35
# me.dog = Object()
# me.dog.name = "Apollo"

# print(me.toJSON())








#     date = '2010-01-05'
# holidayName = ''
# # The Holiday class will also recognize strings of any format
# # and int/float representing a Unix timestamp

# b = date in uk_holidays
# if b == True:
#     isHoliday = True
#     holidayName = uk_holidays.get(date)
# else:
#     isHoliday = False
#     holidayName = None

# # print('1/1/2024' in us_holidays)    # True
# # print(1388597660 in us_holidays)    # True

# print(isHoliday)
# print(holidayName)
