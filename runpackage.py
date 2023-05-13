import getPower.getPowerUsage
from datetime import datetime, timedelta

start = datetime.today().replace(day=1) #first day of month
end = (start + timedelta(days=32)).replace(day=1) #first day of next month

print("Start: " + start.strftime('%Y-%m-%dT00:00:00'))
print("End: " + end.strftime('%Y-%m-%dT00:00:00'))
print("\n")
getPowerUsage(start, end)