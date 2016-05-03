#!/usr/bin/env python3

"""
usage: ./json2ics.py $json
       ./json2ics.py /tmp/cfp.all.json
convert json containing tuebix 2016 papers to ics
"""

import json
import sys
from ics import Calendar, Event
from datetime import timedelta, datetime
#from pprint import pprint

icsfile = "/tmp/ics"

def json2ics(inputfile):
    """ convert json containing tuebix 2016 papers to ics """
    cal = Calendar()
    with open(inputfile) as data_file:
        data = json.load(data_file)
    next120 = datetime(2016, 5, 1, 8, 0)
    next55 = datetime(2016, 5, 4, 8, 0)
    next25 = datetime(2016, 5, 7, 10, 0)
    for talk in data:
        event = Event()
        event.name = talk["titel"]
        event.description = talk["name"] + "\n" + talk["inhalt"]
        # keep Ingo out and use him as a Joker at the end
        if talk["type"]["workshop"] and talk["name"] != "Ingo Blechschmidt":
            event.begin = next120
            event.end = next120 + timedelta(hours=2)
            next120 += timedelta(hours=2)
            if next120.hour > 15:
                next120 += timedelta(hours=16)
            cal.events.append(event)
            for cfptype, possible in talk["type"].items():
                if possible and cfptype != "workshop":
                    event.name += " ### " + cfptype
        elif talk["type"]["v55"] and talk["name"] != "Ingo Blechschmidt":
            event.begin = next55
            event.end = next55 + timedelta(hours=1)
            next55 += timedelta(hours=1)
            if next55.hour > 15:
                next55 += timedelta(hours=16)
            cal.events.append(event)
            for cfptype, possible in talk["type"].items():
                if possible and cfptype != "v55":
                    event.name += " ### " + cfptype
        elif talk["type"]["v25"] and talk["name"] != "Ingo Blechschmidt":
            event.begin = next25
            event.end = next25 + timedelta(minutes=30)
            next25 += timedelta(minutes=30)
            if next25.hour > 15:
                next25 += timedelta(hours=16)
            cal.events.append(event)
            for cfptype, possible in talk["type"].items():
                if possible and cfptype != "v25":
                    event.name += " ### " + cfptype

    with open(icsfile, 'w') as my_file:
        my_file.writelines(cal)

json2ics(sys.argv[1])
