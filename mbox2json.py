#!/usr/bin/env python3

"""
usage: ./mbox2json.py $MBOX > $MBOX.json
       ./mbox2json.py ../cfp/cfp.all > /tmp/cfp.all.json
convert mbox containing tuebix 2016 papers to json
"""
#TODO:
    # not json compatible ? Zeichensalat aus: /^(\d\d)\.(\d\d)\.(\d{4})$/
    # json ends with comma },] but should be without }]

import mailbox
import re
import sys

def mbox2json(inputfile):
    """convert mbox containing tuebix 2016 papers to json"""
    print ('[')
    for message in mailbox.mbox(inputfile):
        payload = message.get_payload()
        jsonblock = re.match(r"""Hallo.+?================= <json> =================.+?(\{.+?\})\n\n.+?================= </json> =================""", payload, re.DOTALL)
        if jsonblock:
            jsonpart = jsonblock.groups()[0].replace('\n', ' ')
            print(jsonpart+",")
    print ("]")

mbox2json(sys.argv[1])
