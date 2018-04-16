#!/usr/bin/env python
import os
import time
import json
import requests

SCHEDULE_JSON_URL = "https://us.pycon.org/2018/schedule/conference.json"

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
    return schedule
