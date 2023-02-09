from time import time
from dateutil import tz
from pytz import timezone
from datetime import datetime, timedelta


def timestamp_server():
    return datetime.fromtimestamp(time(), tz=timezone("UTC")).timestamp()

def timestamp_utc(tmst):
    return datetime.fromtimestamp(tmst, tz=timezone("UTC"))

def time_date_now():
    return datetime.now()

def time_date_now_UTC():
    return datetime.now(tz=tz.gettz("UTC"))

def timestamp_sao_paulo(tmst):
    return datetime.fromtimestamp(tmst, tz=timezone("America/Sao_Paulo"))

def time_sao_paulo():
    data = datetime.now(tz=tz.gettz("America/Sao Paulo"))
    data_hora = datetime.strptime(data.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
    return data_hora

# /////// time expiration
def expiration_of_operation():
    tmst = timestamp_server()
    time_now = time_date_now()
    timestamp = timestamp_utc(tmst)

    if time_now.hour == timestamp.hour:
        pass
    else:
        timestamp = timestamp_sao_paulo(tmst)

    year   = timestamp.year
    month  = timestamp.month
    day    = timestamp.day
    hour   = timestamp.hour
    minute = timestamp.minute
    second = timestamp.second

    if second < 30:
        minute = minute + 1
    else:
        minute = minute + 2
    
    expiration = datetime(
        year=year,
        month=month,
        day=day,
        hour=hour,
        minute=minute,
    )
    return int(expiration.timestamp()), expiration

def timesTemp_converter(timestamp):
    hora = datetime.strptime(datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
    hora = hora.replace(tzinfo=tz.gettz('GMT'))
    return str(hora.astimezone(tz.gettz('America/Sao Paulo')))[:-6]

def expiration_operation_5m():
    time_expirations = time_date_now()

    dia = time_expirations.day
    mes = time_expirations.month
    ano = time_expirations.year
    hora = time_expirations.hour
    minuto = time_expirations.minute

    hora_atual = None

    if minuto >= 0 and minuto < 5:
        hora_atual = datetime(year=ano, month=mes, day=dia, hour=hora, minute=5, second=0)
        print(f"\n\n\n\n-------->> 0--5 -- Expiração do candle: {hora_atual}")
        hora_atual = int(hora_atual.replace(microsecond=0).timestamp())
        print("---> ", hora_atual)
        return hora_atual
    elif minuto >= 5 and minuto < 10:
        hora_atual = datetime(year=ano, month=mes, day=dia, hour=hora, minute=10, second=0)
        print(f"\n\n\n\n-------->> 5--10 -- Expiração do candle: {hora_atual}")
        hora_atual = int(hora_atual.replace(microsecond=0).timestamp())
        print("---> ", hora_atual)
        return hora_atual
    elif minuto >= 10 and minuto < 15:
        hora_atual = datetime(year=ano, month=mes, day=dia, hour=hora, minute=15, second=0)
        print(f"\n\n\n\n-------->> 10--15 -- Expiração do candle: {hora_atual}")
        hora_atual = int(hora_atual.replace(microsecond=0).timestamp())
        print("---> ", hora_atual)
        return hora_atual
    elif minuto >= 15 and minuto < 20:
        hora_atual = datetime(year=ano, month=mes, day=dia, hour=hora, minute=20, second=0)
        print(f"\n\n\n\n-------->> 15--20 -- Expiração do candle: {hora_atual}")
        hora_atual = int(hora_atual.replace(microsecond=0).timestamp())
        print("---> ", hora_atual)
        return hora_atual
    elif minuto >= 20 and minuto < 25:
        hora_atual = datetime(year=ano, month=mes, day=dia, hour=hora, minute=25, second=0)
        print(f"\n\n\n\n-------->> 20--25 -- Expiração do candle: {hora_atual}")
        hora_atual = int(hora_atual.replace(microsecond=0).timestamp())
        print("---> ", hora_atual)
        return hora_atual
    elif minuto >= 25 and minuto < 30:
        hora_atual = datetime(year=ano, month=mes, day=dia, hour=hora, minute=30, second=0)
        print(f"\n\n\n\n-------->> 25--30 -- Expiração do candle: {hora_atual}")
        hora_atual = int(hora_atual.replace(microsecond=0).timestamp())
        print("---> ", hora_atual)
        return hora_atual
    elif minuto >= 30 and minuto < 35:
        hora_atual = datetime(year=ano, month=mes, day=dia, hour=hora, minute=35, second=0)
        print(f"\n\n\n\n-------->> 30--35 -- Expiração do candle: {hora_atual}")
        hora_atual = int(hora_atual.replace(microsecond=0).timestamp())
        print("---> ", hora_atual)
        return hora_atual
    elif minuto >= 35 and minuto < 40:
        hora_atual = datetime(year=ano, month=mes, day=dia, hour=hora, minute=40, second=0)
        print(f"\n\n\n\n-------->> 35--40 -- Expiração do candle: {hora_atual}")
        hora_atual = int(hora_atual.replace(microsecond=0).timestamp())
        print("---> ", hora_atual)
        return hora_atual
    elif minuto >= 40 and minuto < 45:
        hora_atual = datetime(year=ano, month=mes, day=dia, hour=hora, minute=45, second=0)
        print(f"\n\n\n\n-------->> 40--45 -- Expiração do candle: {hora_atual}")
        hora_atual = int(hora_atual.replace(microsecond=0).timestamp())
        print("---> ", hora_atual)
        return hora_atual
    elif minuto >= 45 and minuto < 50:
        hora_atual = datetime(year=ano, month=mes, day=dia, hour=hora, minute=50, second=0)
        print(f"\n\n\n\n-------->> 45--50 -- Expiração do candle: {hora_atual}")
        hora_atual = int(hora_atual.replace(microsecond=0).timestamp())
        print("---> ", hora_atual)
        return hora_atual
    elif minuto >= 50 and minuto < 55:
        hora_atual = datetime(year=ano, month=mes, day=dia, hour=hora, minute=55, second=0)
        print(f"\n\n\n\n-------->> 55--55 -- Expiração do candle: {hora_atual}")
        hora_atual = int(hora_atual.replace(microsecond=0).timestamp())
        print("---> ", hora_atual)
        return hora_atual
    elif minuto >= 55:
        hora_atual = datetime(year=ano, month=mes, day=dia, hour=hora, minute=0, second=0) + timedelta(hours=+1)
        print(f"\n\n\n\n-------->> 55--00 -- Expiração do candle: {hora_atual}")
        hora_atual = int(hora_atual.replace(microsecond=0).timestamp())
        print("---> ", hora_atual)
        return hora_atual

    # # hora_atual = datetime.now(tz=tz.gettz("UTC")) + timedelta(minutes=+15)
    # # print(f"\n\n\n\n-------->> Expiração do candle: {hora_atual}\n\n\n\n\n")
    # hora_atual = hora_atual.replace(hour=0, second=0, microsecond=0).timestamp()
    # return int(hora_atual)


def expiration_operation_15m():
    time_expirations = time_date_now_UTC()

    dia = time_expirations.day
    mes = time_expirations.month
    ano = time_expirations.year
    hora = time_expirations.hour
    minuto = time_expirations.minute

    hora_atual = None


    if minuto >= 0 and minuto < 15:
        hora_atual = datetime(year=ano, month=mes, day=dia, hour=hora, minute=15, second=0)
        print(f"\n\n\n\n-------->> 0--15 -- Expiração do candle: {hora_atual}")
        hora_atual = int(hora_atual.replace(microsecond=0).timestamp())
        print("---> ", hora_atual)
        return hora_atual
    elif minuto >= 15 and minuto < 30:
        hora_atual = datetime(year=ano, month=mes, day=dia, hour=hora, minute=30, second=0)
        print(f"\n\n\n\n-------->> 15--30 -- Expiração do candle: {hora_atual}")
        hora_atual = int(hora_atual.replace(microsecond=0).timestamp())
        print("---> ", hora_atual)
        return hora_atual
    elif minuto >= 30 and minuto < 45:
        hora_atual = datetime(year=ano, month=mes, day=dia, hour=hora, minute=45, second=0)
        print(f"\n\n\n\n-------->> 30--45 -- Expiração do candle: {hora_atual}")
        hora_atual = int(hora_atual.replace(microsecond=0).timestamp())
        print("---> ", hora_atual)
        return hora_atual
    elif minuto >= 45:
        hora_atual = datetime(year=ano, month=mes, day=dia, hour=hora, minute=0, second=0) + timedelta(hours=+1)
        print(f"\n\n\n\n-------->> 45--00 -- Expiração do candle: {hora_atual}")
        hora_atual = int(hora_atual.replace(microsecond=0).timestamp())
        print("---> ", hora_atual)
        return hora_atual
