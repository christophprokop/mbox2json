#!/usr/bin/env python3

"""
usage: ./json2ics.py $json > $ics
       ./json2ics.py /tmp/cfp.all.json > /tmp/ics
convert json containing tuebix 2016 papers to ics
"""

import json
import sys
from ics import Calendar, Event
from datetime import timedelta, datetime

workshopstarttimes = [
        datetime(2016, 5, 2, 8, 0),
        datetime(2016, 5, 2, 10, 0),
        datetime(2016, 5, 2, 12, 0),
        datetime(2016, 5, 2, 14, 0),
        datetime(2016, 5, 3, 8, 0),
        datetime(2016, 5, 3, 10, 0),
        datetime(2016, 5, 3, 12, 0),
        datetime(2016, 5, 3, 14, 0),
        datetime(2016, 5, 4, 8, 0),
        datetime(2016, 5, 4, 10, 0),
        datetime(2016, 5, 4, 12, 0),
        datetime(2016, 5, 4, 14, 0),
        datetime(2016, 5, 5, 8, 0),
        datetime(2016, 5, 5, 10, 0),
        datetime(2016, 5, 5, 12, 0),
        datetime(2016, 5, 5, 14, 0),
        datetime(2016, 5, 6, 8, 0),
        datetime(2016, 5, 6, 10, 0),
        datetime(2016, 5, 6, 12, 0),
        datetime(2016, 5, 6, 14, 0)
        ]

def json2ics(inputfile):
    """ convert json containing tuebix 2016 papers to ics """
    cal = Calendar()
    with open(inputfile) as data_file:
        data = json.load(data_file)
    count = 1
    for talk in data:
        event = Event()
        #e.begin = datetime(2016, 5, 2, 6, 0) + timedelta(seconds=count * timedelta(15, 0, 0).total_seconds())
        #e.begin = datetime(2016, 5, 2, 10, 0) + timedelta(seconds=timedelta(minutes=120).total_seconds() * count)
        event.name = talk["titel"]
        if talk["type"]["workshop"]:
            event.begin = workshopstarttimes[count]
            count += 1
            event.duration = timedelta(hours=2)
            cal.events.append(event)
    with open("/tmp/ics.workshop", 'w') as my_file:
        my_file.writelines(cal)

json2ics(sys.argv[1])
