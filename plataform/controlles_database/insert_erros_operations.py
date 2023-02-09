from plataform.controlles_database.conn import connetion_db

def insert_error_database(date_time, message, active, status):
    try:
        conn = connetion_db()
        cursor = conn.cursor()
        
        comando = f'''
        INSERT INTO operations_errors
        (date_time, message, active, status_operation)
        VALUES
        ("{date_time}", "{message}", "{active}", {status})
        '''
        cursor.execute(comando)
        conn.commit()
        print(f" ---------  erro inserido - {date_time}, {message}, {active}, {status}  --------- ")
        cursor.close()
        conn.close()
        return
       
    except Exception as e:
        print(f" ---> Erro insert error database: {e}")
        cursor.close()
        conn.close()
        print("Conexão encerrada")