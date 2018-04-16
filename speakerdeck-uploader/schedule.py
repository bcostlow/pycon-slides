import json

def get_schedule():
    schedule = json.load(open("schedule.json"))
    return schedule
