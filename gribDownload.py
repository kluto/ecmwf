#!/usr/bin/env python
from ecmwfapi import ECMWFDataServer
    
server = ECMWFDataServer()

server.retrieve({
    "class": "ei",
    "dataset": "interim",
    "date": "2015-07-01/to/2015-07-31",
    "expver": "1",
    "grid": "0.75/0.75",
    "levtype": "sfc",
    "param": "167.128",
    "step": "0",
    "stream": "oper",
    "time": "00:00:00/06:00:00/12:00:00/18:00:00",
    "type": "an",
    "target": "/home/tpk/testTemp.grib",
})