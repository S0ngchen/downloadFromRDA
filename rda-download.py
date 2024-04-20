#!/usr/bin/env python
""" 
Python script to download selected files from rda.ucar.edu.
After you save the file, don't forget to make it executable
i.e. - "chmod 755 <name_of_script>"
"""

url = 'https://data.rda.ucar.edu/ds083.2/grib2/'    # EXAMPLE url
import sys, os
from urllib.request import build_opener
from datetime import datetime, timedelta
import time
import urllib
import random


start_time = datetime.strptime('YYYYMMDD_HH_MM', '%Y%m%d_%H_%M')    # start time, format: YYYYMMDD_HH_MM
end_time = datetime(2023, 12, 31, 0, 0, 0)
time_list = (start_time + timedelta(hours=6*i) for i in range(int((end_time - start_time).total_seconds()) // (3600*6 + 1)))
time_list_formatted = (time.strftime('%Y%m%d_%H_%M') for time in time_list)
filelist = (f'{url}{time[0:4]}/{time[0:4]}.{time[4:6]}/fnl_{time}.grib2' for time in time_list_formatted)


opener = build_opener()
i = 1
for file in filelist:
    if i <= 30:
        i += 1
    else:
        i = 1
    ofile = os.path.basename(file)
    sys.stdout.write("downloading " + ofile + " ... ")
    sys.stdout.flush()
    infile = opener.open(file)
    outfile = open(ofile, "wb")
    outfile.write(infile.read())
    outfile.close()
    sys.stdout.write("done\n")

