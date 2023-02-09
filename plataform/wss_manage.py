import threading

from logs_api.logs_api import logging_api

from plataform import urls_iqoption, constants
from plataform.wss.send_message_wss import MessageWSS
from plataform.wss.wss_client import WebSocket_client_app


class StartWebsocket:
    def start_connect_wss(ssid):
        urls_iqoption.WSS_OBJ = WebSocket_client_app()
        urls_iqoption.THREDING_WSS = threading.Thread(target=urls_iqoption.WSS_OBJ.wss.run_forever).start()

        try:
            while True:
                if urls_iqoption.STATUS_CONN_WSS == True:
                    break
            MessageWSS.send_wss_ssid(ssid)
            print(f"status >>> {urls_iqoption.STATUS_CONN_WSS}")
            while True:
                if constants.ID_ACCOUNT_REAL != None and constants.ID_ACCOUNT_PRACTICE != None:
                    print("------------")
                    break
            return
        except Exception as e:
            logging_api(process_log="error", log=f"Module: StartWebsocket.start_connect_wss | Error: {e}")
