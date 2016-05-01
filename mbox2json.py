#!/usr/bin/env python3

"""
usage: ./mbox2json $CFPMBOX
convert mbox containing tuebix 2016 papers to json
"""

import mailbox
import re
import sys

def mbox2json(inputfile):
    """convert mbox containing tuebix 2016 papers to json"""
    count = 0
    for message in mailbox.mbox(inputfile):
        payload = message.get_payload()
        jsonblock = re.match(r"""Hallo.+?================= <json> =================.+?(\{.+?\})\n\n.+?================= </json> =================""", payload, re.DOTALL)
        name = re.match(r""".+?"name"\: "(.+?)",""", payload, re.DOTALL)
        namestripped = name.groups()[0].replace(' ','')
        title = re.match(r""".+?"titel"\: "(.+?)",""", payload, re.DOTALL)
        titlestripped = title.groups()[0].replace(' ','')
        #"name": "Ingo Blechschmidt", 
        if jsonblock:
            jsonpart = jsonblock.groups()[0].replace('\n', ' ')
            print("{"+str(count)+"-"+namestripped+"-"+titlestripped+":"+jsonpart+"}\n")
            count += 1
    return

mbox2json(sys.argv[1])
