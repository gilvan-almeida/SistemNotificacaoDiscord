from datetime import datetime

def formatDate(dt: str | datetime) -> str:
    if  isinstance(dt, str):
        dt = datetime.fromisoformat(dt.replace("z",""))
    data = dt.strftime("%d/%m/%Y %H:%M")
    return data
        