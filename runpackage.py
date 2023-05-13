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

def processDirCSVs():
    files = glob.glob('pu_[0-9]*-[0-9]*.csv')
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
    start = datetime.today().replace(day=1) #first day of month
    end = datetime.today() + timedelta(days=1)
    print("Start: " + start.strftime('%Y-%m-%d'))
    print("End: " + end.strftime('%Y-%m-%d'))
    print("\n")
    getPower.getPowerUsage(start, end)

