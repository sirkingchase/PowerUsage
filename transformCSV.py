import os
from datetime import datetime, timedelta
import pandas
import math
from fastavro import writer, reader, parse_schema, schema, validate
import json
import glob
import pytz
cst = pytz.timezone('US/Central')

def csvToJsonPower(f):
    print (f)
    recordArr = []
    powerRange = [i for i in range(0,26)]
    df = pandas.read_csv(f, usecols=powerRange)
    for index, row in df.iterrows():
        rowDate = row["Date/Time"] #1 Apr 23
        for i in range(1, 25):
            kwh = row[i]
            if not isinstance(kwh, str) and not math.isnan(kwh):
                dt_object = datetime.strptime(rowDate + ' ' + str(i-1), '%d %b %Y %H')
                #print(str(cst.localize(dt_object)) + ' vs. ' + str(cst.localize(dt_object).astimezone(pytz.UTC)))
                #print(str(dt_object.timestamp()) + ' vs. ' + str(cst.localize(dt_object).astimezone(pytz.UTC).timestamp()))
                record = { "Epoch": cst.localize(dt_object).timestamp(), "kwh": kwh, "DateTime": str(cst.localize(dt_object)) }
                recordArr.append(record)
    return recordArr


#files = glob.glob('pu_[0-9]*-[0-9]*.csv')
#
#for f in files:
#  pu = csvToJsonPower(f)
#  start = datetime.fromtimestamp(pu[0]["Epoch"])
#  end = datetime.fromtimestamp(pu[-1]["Epoch"])
#  fileName = "pu_" + start.strftime("%Y%m%d") + "-" + (end).strftime("%Y%m%d") + ".avro"
#  with open(fileName, 'wb') as out:
#      writer(out, parsed_schema, pu )
#      print(fileName)

## Reading
#with open(fileName, 'rb') as fo:
#    for record in reader(fo):
#        print(record)