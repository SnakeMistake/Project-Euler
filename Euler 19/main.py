#This code correctly finds the number of Sundays between 1/1/1900 and 12/31/2000, but the Euler challenge asks us to disregard the two Sundays that occur in 1900 and start at 1901.  I also didn't realize the entire year of 2000 was considered to be part of the 20th century.
today = {
  "month":"jan",
  "day":1,
  "year":1900,
  "weekday":"mon"
}
counter = 0
print(today)
days_in_months = {
  "jan":31,
  "feb":28,
  "mar":31,
  "apr":30,
  "may":31,
  "jun":30,
  "jul":31,
  "aug":31,
  "sept":30,
  "oct":31,
  "nov":30,
  "dec":31,
}
months_list = [  "jan","feb","mar","apr","may","jun","jul","aug","sept","oct","nov","dec"]
weekday_list = ["mon", "tues", "wed", "thurs", "fri", "sat", "sun"]


def next_day(date):
  if date['day'] == 28 and date['month'] == 'feb':
    if date['year']%400 ==0:
      date['day'] = (date['day']+1)
    elif date['year']%4 ==0 and date['year']%100 != 0:
      date['day'] = (date['day']+1)
    else:
      date['day'] = 1
      next_month(date)
  elif date['day'] < days_in_months[date["month"]]:
    date['day'] = (date['day']+1)
  else:
    date['day'] = 1
    next_month(date)
    
def next_month(date):
  if months_list.index(date["month"]) <11:
    date['month'] = months_list[months_list.index(date["month"])+1]
  else:
    date['month'] = 'jan'
    next_year(date)

def next_weekday(date):
  if weekday_list.index(date['weekday']) < 6:
    date['weekday'] = weekday_list[weekday_list.index(date['weekday'])+1]
  else:
    date['weekday'] = "mon"
    
def sunday_check(date, counter):
  if date['weekday'] == 'sun' and date['day'] ==1:
    print("FOUND ONE!")
    counter += 1
    print(f"Counter: {counter}")
    print(today)
  return counter
  
def next_year(date):
  date['year'] = (date['year'] +1)

while not today['year'] == 2001:
  next_day(today)
  next_weekday(today)
  counter = sunday_check(today, counter)
  
