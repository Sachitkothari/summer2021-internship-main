from datetime import datetime

def compareMonths(launchDate: str):
    h=datetime.strptime(launchDate,'%Y-%m-%d').month
    k = datetime.today().month
    return (k-h)