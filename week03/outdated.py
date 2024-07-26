flag = False
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

while not flag:
    date = input('Date: ').strip()
    try:
        month, day, year = date.split('/')
        try:
            month = int(month)
            if int(day) <= 31 and month < 13:
                print(f'{year}-{"%02d" % int(month)}-{"%02d" % int(day)}')
                flag = True
        except:
            flag = False
    except:
        month, day, year = date.split(' ')
        try:
            day = int(day[:-1])
            if day <= 31:
                print(f'{year}-{"%02d" % int(months.index(month) + 1)}-{"%02d" % day}')
                flag = True
        except:
            flag = False
