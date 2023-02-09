from dateutil import tz
from datetime import datetime, timedelta


def timesTemp_converter(timestamp):
    timestamp_convert = datetime.strptime(datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
    timestamp_convert = timestamp_convert.replace(tzinfo=tz.gettz('GMT'))
    return str(timestamp_convert.astimezone(tz.gettz('America/Sao Paulo')))[:-6]

def datetime_now_sao_paulo():
    return datetime.now(tz=tz.gettz("America/Sao Paulo")).strftime("%d/%m/%Y %H:%M:%S")

def convert_timestamp_sao_paulo(timestamp):
    timestamp_convert = datetime.strptime(datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
    timestamp_convert = timestamp_convert.replace(tzinfo=tz.gettz('GMT'))
    return str(timestamp_convert.astimezone(tz.gettz('America/Sao Paulo')))[:-6]

def timesTemp_converter_to_obj(timestamp):
    return datetime.fromtimestamp(timestamp).strftime("%d/%m/%Y %H:%M:%S")

def time_date_now():
    return datetime.now()

def expiration_operation_5m_alert():
    time_expirations = time_date_now()

    dia = time_expirations.day
    mes = time_expirations.month
    ano = time_expirations.year
    hora = time_expirations.hour
    minuto = time_expirations.minute

    hora_atual = None

    if minuto >= 0 and minuto < 5:
        hora_atual = datetime(year=ano, month=mes, day=dia, hour=hora, minute=10, second=0)
        print(f"\n\n\n\n-------->> 0--5 -- Expiração do candle: {hora_atual}")
        hora_atual = int(hora_atual.replace(microsecond=0).timestamp())
        print("---> ", hora_atual)
        return hora_atual
    elif minuto >= 5 and minuto < 10:
        hora_atual = datetime(year=ano, month=mes, day=dia, hour=hora, minute=15, second=0)
        print(f"\n\n\n\n-------->> 5--10 -- Expiração do candle: {hora_atual}")
        hora_atual = int(hora_atual.replace(microsecond=0).timestamp())
        print("---> ", hora_atual)
        return hora_atual
    elif minuto >= 10 and minuto < 15:
        hora_atual = datetime(year=ano, month=mes, day=dia, hour=hora, minute=20, second=0)
        print(f"\n\n\n\n-------->> 10--15 -- Expiração do candle: {hora_atual}")
        hora_atual = int(hora_atual.replace(microsecond=0).timestamp())
        print("---> ", hora_atual)
        return hora_atual
    elif minuto >= 15 and minuto < 20:
        hora_atual = datetime(year=ano, month=mes, day=dia, hour=hora, minute=25, second=0)
        print(f"\n\n\n\n-------->> 15--20 -- Expiração do candle: {hora_atual}")
        hora_atual = int(hora_atual.replace(microsecond=0).timestamp())
        print("---> ", hora_atual)
        return hora_atual
    elif minuto >= 20 and minuto < 25:
        hora_atual = datetime(year=ano, month=mes, day=dia, hour=hora, minute=30, second=0)
        print(f"\n\n\n\n-------->> 20--25 -- Expiração do candle: {hora_atual}")
        hora_atual = int(hora_atual.replace(microsecond=0).timestamp())
        print("---> ", hora_atual)
        return hora_atual
    elif minuto >= 25 and minuto < 30:
        hora_atual = datetime(year=ano, month=mes, day=dia, hour=hora, minute=35, second=0)
        print(f"\n\n\n\n-------->> 25--30 -- Expiração do candle: {hora_atual}")
        hora_atual = int(hora_atual.replace(microsecond=0).timestamp())
        print("---> ", hora_atual)
        return hora_atual
    elif minuto >= 30 and minuto < 35:
        hora_atual = datetime(year=ano, month=mes, day=dia, hour=hora, minute=40, second=0)
        print(f"\n\n\n\n-------->> 30--35 -- Expiração do candle: {hora_atual}")
        hora_atual = int(hora_atual.replace(microsecond=0).timestamp())
        print("---> ", hora_atual)
        return hora_atual
    elif minuto >= 35 and minuto < 40:
        hora_atual = datetime(year=ano, month=mes, day=dia, hour=hora, minute=45, second=0)
        print(f"\n\n\n\n-------->> 35--40 -- Expiração do candle: {hora_atual}")
        hora_atual = int(hora_atual.replace(microsecond=0).timestamp())
        print("---> ", hora_atual)
        return hora_atual
    elif minuto >= 40 and minuto < 45:
        hora_atual = datetime(year=ano, month=mes, day=dia, hour=hora, minute=50, second=0)
        print(f"\n\n\n\n-------->> 40--45 -- Expiração do candle: {hora_atual}")
        hora_atual = int(hora_atual.replace(microsecond=0).timestamp())
        print("---> ", hora_atual)
        return hora_atual
    elif minuto >= 45 and minuto < 50:
        hora_atual = datetime(year=ano, month=mes, day=dia, hour=hora, minute=55, second=0)
        print(f"\n\n\n\n-------->> 45--50 -- Expiração do candle: {hora_atual}")
        hora_atual = int(hora_atual.replace(microsecond=0).timestamp())
        print("---> ", hora_atual)
        return hora_atual
    elif minuto >= 50 and minuto < 55:
        hora_atual = datetime(year=ano, month=mes, day=dia, hour=hora, minute=0, second=0) + timedelta(hours=+1)
        print(f"\n\n\n\n-------->> 55--55 -- Expiração do candle: {hora_atual}")
        hora_atual = int(hora_atual.replace(microsecond=0).timestamp())
        print("---> ", hora_atual)
        return hora_atual
    elif minuto >= 55:
        hora_atual = datetime(year=ano, month=mes, day=dia, hour=hora, minute=5, second=0) + timedelta(hours=+1)
        print(f"\n\n\n\n-------->> 55--00 -- Expiração do candle: {hora_atual}")
        hora_atual = int(hora_atual.replace(microsecond=0).timestamp())
        print("---> ", hora_atual)
        return hora_atual
