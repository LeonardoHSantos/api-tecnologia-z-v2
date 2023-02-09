from plataform.controlles_database.conn import connetion_db
from plataform.constants import NAME_TABLE_OPERATIONS


def insert_operation_alert_database(obj_alert, status_alert):
    try:
        conn = connetion_db()
        cursor = conn.cursor()

        alert_datetime = obj_alert["alert_datetime"]
        active = obj_alert["active"]
        direction = obj_alert["direction"]
        padrao = obj_alert["padrao"]
        name_estrategy = obj_alert["name_estrategy"]
        mercado = obj_alert["mercado"]
        expiration = obj_alert["expiration"]
        expiration_timestamp = obj_alert["expiration_timestamp"]

        comando_query = f'SELECT * FROM {NAME_TABLE_OPERATIONS} WHERE active = "{active}" and expiration_alert_timestamp = "{expiration_timestamp}"'
        
        cursor.execute(comando_query)
        result = cursor.fetchall()
        print(f"####### TT REGISTROS: {len(result)}")
        if len(result) == 0:
            comando = f'INSERT INTO {NAME_TABLE_OPERATIONS} (alert_datetime, active, direction, padrao, name_estrategy, mercado, expiration_alert, expiration_alert_timestamp, status_alert) VALUES ("{alert_datetime}", "{active}", "{direction}", "{padrao}", "{name_estrategy}", "{mercado}", "{expiration}", "{expiration_timestamp}", "{status_alert}")'
            cursor.execute(comando)
            conn.commit()
            print(f" ---------  alerta inserido - {comando} --------- ")

        cursor.close()
        conn.close()
    except Exception as e:
        print(f" ---> Erro insert alert database: {e}")
        cursor.close()
        conn.close()
        print("Conexão encerrada")