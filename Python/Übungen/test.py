import datetime

actualDate = str(datetime.datetime.now().date())
date1 = int(actualDate[:4])
date2 = date1 - 1
if int(actualDate[5:7]) >= 9:
    date1 += 1
    date2 += 1

print(str(date2) + "/" + str(date1))