#!/usr/bin/env python
import os
import time
import json
import requests

SCHEDULE_JSON_URL = "https://us.pycon.org/2017/schedule/conference.json"

def _download_schedule(output_file):
    resp = requests.get(SCHEDULE_JSON_URL, verify=False)
    resp.raise_for_status()
    with open(output_file, "w") as f:
        for block in resp.iter_content(4096):
            f.write(block)

def _get_schedule():
    data_file = os.path.join(os.path.dirname(__file__), "schedule.json")
    if not os.path.exists(data_file):
        _download_schedule(data_file)
    elif time.time() - os.path.getmtime(data_file) > 600:
        os.unlink(data_file)
        return get_schedule()

    with open(data_file) as f:
        return json.load(f)

def get_schedule():
    schedule = _get_schedule()
    return [
        {
            "abstract": "",
            "authors": [
                "Lorena Barba",
            ],
            "conf_key": 100000,
            "contact": [],
            "description": "Keynote",
            "duration": 40,
            "start": "2016-05-30T09:30:00",
            "end": "2016-05-30T010:10:00",
            "kind": "keynote",
            "license": "CC",
            "name": "Keynote",
            "released": True,
            "room": "Keynote",
            "tags": ""
        },
        {
            "abstract": "",
            "authors": [
                "Guido van Rossum",
            ],
            "conf_key": 100000,
            "contact": [],
            "description": "Python Language",
            "duration": 40,
            "start": "2016-05-31T09:00:00",
            "end": "2016-05-31T009:40:00",
            "kind": "keynote",
            "license": "CC",
            "name": "Python Language",
            "released": True,
            "room": "Keynote",
            "tags": ""
        },
        {
            "abstract": "",
            "authors": [
                "Parisa Tabriz",
            ],
            "conf_key": 100000,
            "contact": [],
            "description": "Keynote",
            "duration": 40,
            "start": "2016-05-31T09:40:00",
            "end": "2016-05-31T010:20:00",
            "kind": "keynote",
            "license": "CC",
            "name": "Keynote",
            "released": True,
            "room": "Keynote",
            "tags": ""
        },
        {
            "abstract": "",
            "authors": [
                "Van Lindberg",
            ],
            "conf_key": 100000,
            "contact": [],
            "description": "Python Software Foundation",
            "duration": 20,
            "start": "2016-06-01T09:00:00",
            "end": "2016-06-01T009:20:00",
            "kind": "keynote",
            "license": "CC",
            "name": "Python Software Foundation",
            "released": True,
            "room": "Keynote",
            "tags": ""
        },
        {
            "abstract": "",
            "authors": [
                "Cris Ewing",
            ],
            "conf_key": 100000,
            "contact": [],
            "description": "Keynote",
            "duration": 40,
            "start": "2016-06-01T09:20:00",
            "end": "2016-06-01T010:00:00",
            "kind": "keynote",
            "license": "CC",
            "name": "Keynote",
            "released": True,
            "room": "Keynote",
            "tags": ""
        },
        {
            "abstract": "",
            "authors": [
                "K Lars Lohn",
            ],
            "conf_key": 100000,
            "contact": [],
            "description": "Keynote",
            "duration": 40,
            "start": "2016-06-01T15:10:00",
            "end": "2016-06-01T015:50:00",
            "kind": "keynote",
            "license": "CC",
            "name": "Keynote",
            "released": True,
            "room": "Keynote",
            "tags": ""
        },
    ] + schedule
