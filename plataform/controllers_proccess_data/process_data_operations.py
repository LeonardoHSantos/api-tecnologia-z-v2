
import pandas as pd

from logs_api.logs_api import logging_api

from plataform.operations_threading.operation_threading_M5 import operation_threading_M5

from plataform.http_plataform.data_times_expirations import timesTemp_converter, time_sao_paulo


from plataform.controlles_database.insert_erros_operations import insert_error_database


############ alerts
from plataform.controlles_database.insert_alert_operations import insert_operation_alert_database
from plataform.controlles_database.update_operation import update_database_alert, update_database_results_operation



class ProcessDataOperations:
    def operations_errors(data):
        try:
            date_time = time_sao_paulo()
            message = data["msg"]
            active = data["request_id"]
            status = int(data["status"])
            insert_error_database(date_time, message, active, status)
        except Exception as e:
            print(f"***** Erro insert errors database: {e}")

    def process_open_operation(message):
        try:
            print("\n\n\n----------------------------------------- processando abertura de operacao -- Func.: ProcessDataOperations.process_open_operation")
            obj_update_operation = {
                "option_id" : str(message["msg"]["option_id"]),
                "active" : str(message["msg"]["active"]),
                "open_time" : str(message["msg"]["open_time"]),
                "expiration_time" : str(message["msg"]["expiration_time"]),
                "direction" : str(message["msg"]["direction"]),
                "status_alert" : str("active-operation"),
                "resultado": "em andamento"
            }
            print(f" ----------------- object operation: {obj_update_operation}")
            logging_api(process_log="info", log=f"Open operation: {obj_update_operation}")

            
            return update_database_alert(obj_update_operation)
        except Exception as e:
            print(f"Erro processamento abertura operação: {e}")

    def alert_operations(obj_alert, status_alert ):
        insert_operation_alert_database(
                obj_alert,
                status_alert
                )

    def process_results_operations(dados):
        lista_update = [
            [], # 0 - id_operacao
            [], # 1 - resultado
        ]
        registros = dados["closed_options"]
        print(registros)
        tt_registros = len(registros)
        for i in range(tt_registros):
            print("*****************************")
            id_operacao = registros[i]["id"][0]
            active = registros[i]["active"]
            active_id = registros[i]["active_id"]
            resultado = registros[i]["win"]
            try:
                if resultado == "win":
                    resultado = "win"
                elif resultado == "loose":
                    resultado = "loss"
                elif resultado == "em andamento":
                    resultado = "em andamento"
                elif resultado == "equals":
                    resultado == "empate"
                else:
                    resultado = resultado
            except Exception as e:
                print(f" **** Erro ao processar resultado: {e}")
                resultado = "resultado?"
            print(id_operacao, active, active_id, resultado)
            lista_update[0].append(id_operacao)
            lista_update[1].append(resultado)

        df_resultados = pd.DataFrame(list(zip(
            lista_update[0],
            lista_update[1],
        )), columns=["id_operation", "results"])
        update_database_results_operation(obj_operation=df_resultados)
    
    


