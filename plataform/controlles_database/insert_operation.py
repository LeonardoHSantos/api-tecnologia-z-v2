# from plataform.controlles_database.conn import connetion_db
# from plataform  import var_data_process

# def insert_database(obj_update_operation):
#     try:
#         conn = connetion_db()
#         cursor = conn.cursor()
        
#         option_id = obj_update_operation["option_id"]
#         active = obj_update_operation["active"]
#         open_time = obj_update_operation["open_time"]
#         expiration_time = obj_update_operation["expiration_time"]
#         direction = obj_update_operation["direction"]
#         status_alert = obj_update_operation["status_alert"]

#         comando_update = f'UPDATE app_estrategias_2_operacoesiqoption_testeAlert SET option_id = "{option_id}", open_time = "{open_time}", direction = "{direction}", status_alert = "{status_alert}", expiration_time = "{expiration_time}" WHERE expiration_alert_timestamp = "{expiration_time}" and active = "{active}"'
#         cursor.execute(comando_update)
#         conn.commit()
#         print(f"OPERATION/UPDATE FINISH -----> {comando_update}")
#         cursor.close()
#         conn.close()
#         print("DATABASE CLOSE CONNECTION")

#     except Exception as e:
#         print(f"********** Erro 'insert_database/UPDATE' update database: {e}")
#         cursor.close()
#         conn.close()
        




# # def insert_database(obj_operation):
# #     try:
# #         conn = connetion_db()
# #         cursor = conn.cursor()
# #         padrao = var_data_process.ESTRATEGIA
# #         print(obj_operation, f"Padrão: {padrao}")
# #         option_id = obj_operation["option_id"]
# #         open_time = obj_operation["open_time"]
# #         expiration_time = obj_operation["expiration_time"]
# #         direction = obj_operation["direction"]
# #         active = obj_operation["active"]
# #         mercado = obj_operation["mercado"]
# #         resultado = obj_operation["resultado"]
        

# #         comando_query = f'SELECT * FROM app_estrategias_2_operacoesiqoption WHERE option_id = "{option_id}"'
# #         cursor.execute(comando_query)
# #         result = cursor.fetchall()
# #         print(f">>>> Total registros: {len(result)}")

# #         comando = f'INSERT INTO app_estrategias_2_operacoesiqoption (option_id, open_time, expiration_time, direction, active, mercado, resultado, padrao) VALUES ("{option_id}", "{open_time}", "{expiration_time}", "{direction}", "{active}", "{mercado}", "{resultado}", "{padrao}")'
# #         # comando = f'INSERT INTO app_estrategias_2_operacoesiqoption (option_id, open_time, expiration_time, direction, active, mercado, resultado, padrao) VALUES ("{option_id}", "{open_time}", "{expiration_time}", "{direction}", "{active}", "teste M5", "{resultado}", "{padrao}")'
# #         if len(result) == 0:
# #             cursor.execute(comando)
# #             conn.commit()
# #             print(f" ---------  inserido - {comando} --------- ")
# #             cursor.close()
# #             conn.close()
# #         else:
# #             print(comando)

# #     except Exception as e:
# #         print(f" ---> Erro insert database: {e}")
# #         cursor.close()
# #         conn.close()
# #         print("Conexão encerrada")