import websocket
from time import sleep
from datetime import datetime

from logs_api.logs_api import logging_api

from plataform import urls_iqoption, constants, var_data_process
from plataform.wss.send_message_wss import MessageWSS
from plataform.http_plataform.prepare_message import prepare_response

# operações sem alerta
# from plataform.controllers_proccess_data.process_analytics_data import ProcessData

# operações com alerta
from plataform.controllers_proccess_data.controllers_pre_analysis_data import AnalyzeData
from plataform.controllers_proccess_data.process_analytics_data_alert import ProcessData_Alert



from plataform.controllers_proccess_data.process_actives_open import process_open_actives
from plataform.controllers_proccess_data.process_data_operations import ProcessDataOperations


class WebSocket_client_app:
    def __init__(self):
        self.wss = websocket.WebSocketApp(
            url=urls_iqoption.URL_WSS,
            on_open=self.on_open,
            on_close=self.on_close,
            on_message=self.on_message,
            on_error=self.on_error
        )

    def on_message(self, message):
        message = prepare_response(message)

        if message["name"] == "initialization-data":
            process_open_actives(message["msg"])

        elif message["name"] == "candles":
            print(f">>>>> recebimento de candles --- estratégia: {message['request_id']} ")
            AnalyzeData.analizy_data_operation(message)
            
            
        elif message["name"] == "api_game_getoptions_result":
            ProcessDataOperations.process_results_operations(message["msg"]["result"])
        else:
            # print(message)

            ################### operações com alertas antecipados ###################
            dt = datetime.now()
            if dt.second == 31 and dt.minute in constants.LISTA_MINUTES_OPERATIONS_M5_V1_ALERT:
                var_data_process.TYPE_OPERATION = "pre-analysis"
                MessageWSS.send_messages_actives_open()
                var_data_process.ESTRATEGIA = "PADRAO-M5-V1"
                # amount = 5
                amount = 7 # alterado 07/02/2023
                MessageWSS.send_message_get_candles(estrategia="P-M5-2", timeframe=60*5, amount=amount, name_estragy=var_data_process.ESTRATEGIA)
                logging_api(process_log="info", log=f"Active Websocket Analysis: Datetime: {dt} | PADRAO-M5-V1 - P-M5-2 | pre-analysis ")
                sleep(1)
            elif dt.second == 50 and dt.minute in constants.LISTA_MINUTES_OPERATIONS_M5_V1_ALERT:
                var_data_process.TYPE_OPERATION = "activate-operation"
                MessageWSS.send_messages_actives_open()
                var_data_process.ESTRATEGIA = "PADRAO-M5-V1"
                logging_api(process_log="info", log=f"Active Websocket Analysis: Datetime: {dt} | PADRAO-M5-V1 - P-M5-2 | activate-operation ")
                # amount = 5
                amount = 7 # alterado 07/02/2023
                MessageWSS.send_message_get_candles(estrategia="P-M5-2", timeframe=60*5, amount=amount, name_estragy=var_data_process.ESTRATEGIA)
                sleep(1)

            elif dt.second == 31 and dt.minute in constants.LISTA_MINUTES_OPERATIONS_M5_V2_ALERT:
                var_data_process.TYPE_OPERATION = "pre-analysis"
                MessageWSS.send_messages_actives_open()
                var_data_process.ESTRATEGIA = "PADRAO-M5-V2"
                MessageWSS.send_message_get_candles(estrategia="P-M5-3", timeframe=60*5, amount=6, name_estragy=var_data_process.ESTRATEGIA)
                logging_api(process_log="info", log=f"Active Websocket Analysis: Datetime: {dt} | PADRAO-M5-V2 - P-M5-3 | pre-analysis ")
                sleep(1)
            
            elif dt.second == 50 and dt.minute in constants.LISTA_MINUTES_OPERATIONS_M5_V2_ALERT:
                var_data_process.TYPE_OPERATION = "activate-operation"
                MessageWSS.send_messages_actives_open()
                var_data_process.ESTRATEGIA = "PADRAO-M5-V2"
                MessageWSS.send_message_get_candles(estrategia="P-M5-3", timeframe=60*5, amount=6, name_estragy=var_data_process.ESTRATEGIA)
                logging_api(process_log="info", log=f"Active Websocket Analysis: Datetime: {dt} | PADRAO-M5-V2 - P-M5-3 | activate-operation ")
                sleep(1)

           
            elif dt.second == 1:
                var_data_process.LISTA_REQUEST_ID.clear()
                print(f"\n\n *********************** Lista request_id limpa: {len(var_data_process.LISTA_REQUEST_ID)} *********************** \n\n")
                sleep(1)
            elif dt.second == 10:
                MessageWSS.send_message_get_result_operations(15)
                sleep(1)

            if message["name"] == "profile":
                constants.ID_ACCOUNT_REAL = message["msg"]["balances"][0]["id"]
                constants.ID_ACCOUNT_PRACTICE = message["msg"]["balances"][1]["id"]
                print("----------------->>>")
                print(f"ID account REAL: {constants.ID_ACCOUNT_REAL}")
                print(f"ID account PRACTICE: {constants.ID_ACCOUNT_PRACTICE}")
                logging_api(process_log="info", log=f"### CONNECTED AND AUTHENTICATED WITH IQ_OPTION | {datetime.now()} ###")

            elif message["name"] == "option-opened":
                ProcessDataOperations.process_open_operation(message=message)
            
                print("\n\n\n\n\n ------------------- request id encontrado -------------------")
                print(f"------->>>> Lista request_id: {var_data_process.LISTA_REQUEST_ID}")
                print("\n\n\n--------------------- operação aberta ------------------\n\n\n")
                

            elif message["name"] == "option" and int(message["status"]) != 2000:
                ProcessDataOperations.operations_errors(message)
                logging_api(process_log="warning", log=f"{datetime.now()} - TRANSACTION REFUSED BY IQ_OPTION: {message}")
        

                

    def on_open(self):
        urls_iqoption.STATUS_CONN_WSS = True
        print(f"### Conexão estabelecida com a corretora. Status Conn: {urls_iqoption.STATUS_CONN_WSS} ###")
        logging_api(process_log="info", log=f"### CONNECTION ESTABLISHED WITH IQ_OPTION |{datetime.now()} ###")
        
    def on_close(self):
        urls_iqoption.STATUS_CONN_WSS = False
        self.wss.close()
        print(f"### Conexão encerrada com a corretora. Status Conn: {urls_iqoption.STATUS_CONN_WSS} ###")
        logging_api(process_log="warning", log=f"### CONNECTION CLOSED WITH IQ_OPTION |{datetime.now()} ###")
    def on_error(self, error):
        print(f"### Erro: {error}. ###")
        logging_api(process_log="error", log=f"### ERROR WITH THE CONNECTION |{datetime.now()} ###")