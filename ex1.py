import datetime as dt

def ex1(birth, ref):
    birthdate = dt.datetime.strptime(birth, "%d/%m/%Y")
    refdate = dt.datetime.strptime(ref, "%d/%m/%Y")
    return (refdate - birthdate).days // 365.25