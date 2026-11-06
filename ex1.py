import datetime as dt

def ex1(birth, ref):
    birthdate = dt.datetime.strptime(birth, "%d/%m/%Y")
    refdate = dt.datetime.strptime(ref, "%d/%m/%Y")
    if birthdate > refdate:
        raise ValueError("Birthdate after reference date")
    return (refdate - birthdate).days // 365.25