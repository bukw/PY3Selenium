from datetime import datetime

# today = datetime.strptime(datetime.now(),"%Y%m%d")
print(datetime.now().strftime("%Y%m%d"))

td = datetime.now()
month_week = int(datetime(td.year, td.month, td.day).strftime("%W")) - int(datetime(td.year, td.month,1).strftime("%W")) +1
print(month_week)
week_day = td.strftime("%w")
print(day)
# /html/body/div[3]/div[2]/div[2]/div[2]/form[1]/div[3]/p[1]/span/div/div/div/div/div/table/tbody/tr[1]/td[4]/span