from plataform import var_data_process
from plataform.constants import NAME_TABLE_OPERATIONS
from plataform.controlles_database.conn import connetion_db

from logs_api.logs_api import logging_api

def update_database_alert(obj_update_operation):
    try:
        conn = connetion_db()
        cursor = conn.cursor()
        
        option_id = obj_update_operation["option_id"]
        active = obj_update_operation["active"]
        open_time = obj_update_operation["open_time"]
        expiration_time = obj_update_operation["expiration_time"]
        direction = obj_update_operation["direction"]
        status_alert = obj_update_operation["status_alert"]
        resultado = obj_update_operation["resultado"]
        padrao = var_data_process.ESTRATEGIA
        id_table = 0


        try:
            comando_query = f'SELECT * FROM {NAME_TABLE_OPERATIONS} WHERE active = "{active}" and expiration_alert_timestamp = "{expiration_time}"'
            cursor.execute(comando_query)
            result = cursor.fetchall()
            print(f"####### TT REGISTROS: {len(result)}")
        except Exception as e:
            print(f"**** ------->> Erro query: {e}")
            logging_api(process_log="error", log=f"Module: update_database_alert --> Erro QUERY: {e}")

        if len(result) == 1:
            try:
                comando_update = f'UPDATE {NAME_TABLE_OPERATIONS} SET option_id = "{option_id}", open_time = "{open_time}", direction = "{direction}", status_alert = "{status_alert}", expiration_time = "{expiration_time}", resultado = "{resultado}" WHERE expiration_alert_timestamp = "{expiration_time}" and active = "{active}" and id >= {id_table}'
                cursor.execute(comando_update)
                conn.commit()
                print(f"OPERATION/UPDATE FINISH -----> {comando_update}")
                logging_api(process_log="info", log=f"Module: update_database_alert --> OPERATION/UPDATE FINISH: {comando_update}")

            except Exception as e:
                print(f"Erro UPDATE/OPERATION: {e}")
                logging_api(process_log="error", log=f"Module: update_database_alert --> Erro UPDATE OPERATION: {e}")
        else:
            comando_insert = f'INSERT INTO {NAME_TABLE_OPERATIONS} (option_id, active, open_time, expiration_time, direction, status_alert, resultado) VALUES ("{option_id}", "{active}", "{open_time}", "{expiration_time}", "{direction}", "{status_alert}", "{resultado}")'
            cursor.execute(comando_insert)
            conn.commit()
            print(f"OPERATION/INSERT FINISH -----> {comando_insert}")
            logging_api(process_log="info", log=f"Module: update_database_alert --> OPERATION/INSERT FINISH: {comando_insert}")
        cursor.close()
        conn.close()
        print("DATABASE CLOSE CONNECTION")

    except Exception as e:
        print(f"********** Erro 'insert_database/UPDATE' update database: {e}")
        cursor.close()
        conn.close()
        logging_api(process_log="error", log=f"Module: update_database_alert --> Erro insert_database/UPDATE: {e}")
    

def update_database_results_operation(obj_operation):
    print(" -------------- inicio update -------------- ")
    print("************************* resultados")
    print(obj_operation)
    try:
        conn = connetion_db()
        cursor = conn.cursor()
        status_alert = "closed-operation"
        for i in range(len(obj_operation)):
            try:
                option_id = obj_operation["id_operation"][i]
                resultado = obj_operation["results"][i]
                comando = f'''
                UPDATE {NAME_TABLE_OPERATIONS} SET
                resultado = "{resultado}", status_alert = "{status_alert}"
                WHERE option_id = "{option_id}"
                '''
                cursor.execute(comando)
                conn.commit()
                print(f"------>> {i} - Dados atualizados: {option_id} | {resultado}")
                logging_api(process_log="info", log=f"Module: update_database_results_operation --> UPDATE DATA: {comando}")
            except Exception as e:
                print(f"---> {i} - Erro durante a atualização do registro: {i}")
                logging_api(process_log="error", log=f"Module: update_database_results_operation --> Erro durante a atualização do registro {i}: {e} | object: {obj_operation}")
        cursor.close()
        conn.close()
        print("Fim da atualização. Database desconectado.")
    except Exception as e:
        print(f"Erro ao atualizar banco de dados: {e}")
        cursor.close()
        conn.close()
        print("** Conexão encerrada **")
        logging_api(process_log="error", log=f"Module: update_database_results_operation --> Erro ao atualizar banco de dados: {e}")