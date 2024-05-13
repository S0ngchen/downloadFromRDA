#!/usr/bin/env python
""" 
Python script to download selected files from rda.ucar.edu.
After you save the file, don't forget to make it executable
i.e. - "chmod 755 <name_of_script>"
"""

url = 'https://data.rda.ucar.edu/ds083.2/grib2/'    # EXAMPLE url
"""
This example url comes from the original download script you downloaded.
"""
import sys, os
from urllib.request import build_opener
from datetime import datetime, timedelta
import time
import urllib
import random


start_time = datetime.strptime('YYYYMMDD_HH_MM', '%Y%m%d_%H_%M')
# start time, format: YYYYMMDD_HH_MM, may be changed in different situations
# PLEASE DO NOT CHANGE THE VARIABLE NAME
end_time = datetime(2023, 12, 31, 0, 0, 0)  # end time
time_list = (start_time + timedelta(hours=6*i) for i in range(int((end_time - start_time).total_seconds()) // (3600*6 + 1)))    # steps in ds083.2 is 6 hours, may be changed in different situations 
time_list_formatted = (time.strftime('%Y%m%d_%H_%M') for time in time_list)
# here should be changed if the format of start time was changed
filelist = (f'{url}{time[0:4]}/{time[0:4]}.{time[4:6]}/fnl_{time}.grib2' for time in time_list_formatted)    # EXAMPLE url, may be changed in different situations
"""
The desired download format can be found in the original download script
For EXAMPLE, the format of url provided here is 'https://data.rda.ucar.edu/ds083.2/grib2/YYYY/MM/fnl_YYYYMMDD_HH_MM.grib2'. As for ds083.3, the example url may be 'https://data.rda.ucar.edu/ds083.3/YYYY/YYYYMM/gdas1.fnl0p25.YYYYMMDDHH.fXX.grib2'.(XX here means XX hours later)
"""


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

