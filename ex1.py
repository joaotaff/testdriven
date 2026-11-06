import datetime as dt
import re

def ex1(birth, ref):
    if not re.match(r"^\d{2}/\d{2}/\d{4}$", birth):
        raise ValueError("Invalid birthdate format")
    if not re.match(r"^\d{2}/\d{2}/\d{4}$", ref):
        raise ValueError("Invalid reference date format")
    birthdate = dt.datetime.strptime(birth, "%d/%m/%Y")
    refdate = dt.datetime.strptime(ref, "%d/%m/%Y")
    if birthdate > refdate:
        raise ValueError("Birthdate after reference date")
    return (refdate - birthdate).days // 365.25