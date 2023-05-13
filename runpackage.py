import os
from datetime import datetime, timedelta
import pandas
import math
from fastavro import writer, reader, parse_schema, schema, validate
import json
import glob
import pytz
from datetime import datetime, timedelta
import transformCSV
import getPower

def pu_csv2Avro(files):
    parsed_schema = schema.load_schema("pu.avsc")
    for f in files:
      pu = transformCSV.csvToJsonPower(f)
      start = datetime.fromtimestamp(pu[0]["Epoch"])
      end = datetime.fromtimestamp(pu[-1]["Epoch"])
      fileName = "pu_" + start.strftime("%Y%m%d") + "-" + (end).strftime("%Y%m%d") + ".avro"
      with open(fileName, 'wb') as out:
          writer(out, parsed_schema, pu )
          print(fileName)

def getCurrentMonthsUsage():
    start = ( datetime.today().replace(day=1) ) + timedelta(days=-1) #last day of last month
    end = datetime.today() + timedelta(days=2)
    print("Start: " + start.strftime('%Y-%m-%d'))
    print("End: " + end.strftime('%Y-%m-%d'))
    print("\n")
    return getPower.getPowerUsage(start, end)

def getSpecficMonthsUsage(gMonth, gYear):
    start = datetime.today().replace(day=1, month=gMonth, year=gYear) #first day of month
    end = (start + timedelta(days=32)).replace(day=2)
    print("Start: " + start.strftime('%Y-%m-%d'))
    print("End: " + end.strftime('%Y-%m-%d'))
    getPower.getPowerUsage(start, end)

for i in range(1, 6):
    print(str(i) + ' 2023')
    getSpecficMonthsUsage(i, 2023)

#pu_csv2Avro([file])

#files = glob.glob('pu_[0-9]*-[0-9]*.csv')