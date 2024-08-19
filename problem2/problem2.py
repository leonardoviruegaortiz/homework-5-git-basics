def date_format(date):
    year = date[6:10]
    month = date[0:2]
    day = date[3:5]
    date2 = (f'{year}-{month}-{day}')
    return date2
