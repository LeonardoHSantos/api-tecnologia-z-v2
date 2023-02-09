from plataform import urls_iqoption, constants, var_data_process
from plataform.http_plataform import prepare_message

from plataform.wss.channels_wss import Channels_WSS


class MessageWSS:
    def send_wss_ssid(ssid):
        name = "ssid"
        msg = prepare_message.prepare_message_send_wss(name=name, data=ssid, request_id="")
        print("----------------------------------- msg enviada")
        print(msg)
        urls_iqoption.WSS_OBJ.wss.send(msg)
        MessageWSS.send_msg_config_user_initial()
        return 

    def send_msg_config_user_initial():
        lista_config = [
            {"name": "subscribeMessage", "msg": {"name": "portfolio.position-changed", "version": "2.0", "params": {"routingFilters": {"instrument_type": "cfd", "user_balance_id": constants.ID_ACCOUNT_PRACTICE}}}, "request_id": ""},
            {"name": "subscribeMessage", "msg": {"name": "portfolio.position-changed", "version": "2.0", "params": {"routingFilters": {"instrument_type": "forex", "user_balance_id": constants.ID_ACCOUNT_PRACTICE}}}, "request_id": ""},
            {"name": "subscribeMessage", "msg": {"name": "portfolio.position-changed", "version": "2.0", "params": {"routingFilters": {"instrument_type": "crypto", "user_balance_id": constants.ID_ACCOUNT_PRACTICE}}}, "request_id": ""},
            {"name": "subscribeMessage", "msg": {"name": "portfolio.position-changed", "version": "2.0", "params": {"routingFilters": {"instrument_type": "digital-option", "user_balance_id": constants.ID_ACCOUNT_PRACTICE}}}, "request_id": ""},
            {"name": "subscribeMessage", "msg": {"name": "portfolio.position-changed", "version": "2.0", "params": {"routingFilters": {"instrument_type": "turbo-option", "user_balance_id": constants.ID_ACCOUNT_PRACTICE}}}, "request_id": ""},
            {"name": "subscribeMessage", "msg": {"name": "portfolio.position-changed", "version": "2.0", "params": {"routingFilters": {"instrument_type": "binary-option", "user_balance_id": constants.ID_ACCOUNT_PRACTICE}}}, "request_id": ""},
            {"name": "subscribeMessage", "msg": {"name": "portfolio.order-changed", "version": "1.0", "params": {"routingFilters": {"instrument_type": "cfd"}}}, "request_id": ""},
            {"name": "subscribeMessage", "msg": {"name": "portfolio.order-changed", "version": "1.0", "params": {"routingFilters": {"instrument_type": "forex"}}}, "request_id": ""},
            {"name": "subscribeMessage", "msg": {"name": "portfolio.order-changed", "version": "1.0", "params": {"routingFilters": {"instrument_type": "crypto"}}}, "request_id": ""},
            {"name": "subscribeMessage", "msg": {"name": "portfolio.order-changed", "version": "1.0", "params": {"routingFilters": {"instrument_type": "digital-option"}}}, "request_id": ""},
            {"name": "subscribeMessage", "msg": {"name": "portfolio.order-changed", "version": "1.0", "params": {"routingFilters": {"instrument_type": "turbo-option"}}}, "request_id": ""},
            {"name": "subscribeMessage", "msg": {"name": "portfolio.order-changed", "version": "1.0", "params": {"routingFilters": {"instrument_type": "binary-option"}}}, "request_id": ""},
            {"name": "sendMessage", "msg": {"name": "get-initialization-data", "version": "3.0", "body": {}}, "request_id": "get-underlying-list"}
        ]
        for i in range(len(lista_config)):
            print(lista_config[i])
            urls_iqoption.WSS_OBJ.wss.send(prepare_message.prepare_message_list_ready(lista_config[i]))

    def send_messages_actives_open():
        try:
            msg = {"name": "sendMessage", "msg": {"name": "get-initialization-data", "version": "3.0", "body": {}}, "request_id": "get-underlying-list"}
            urls_iqoption.WSS_OBJ.wss.send(prepare_message.prepare_message_list_ready(msg))
        except Exception as e:
            print("#########################")
            print(e)

    def send_message_get_candles(estrategia, timeframe, amount, name_estragy):
        Channels_WSS.get_candles(timeframe, amount, name_estragy)
        
    def send_message_open_operation(active, direction, name_estrategy):
        msg = Channels_WSS.open_operation_plataform(active=active, direction=direction, name_estrategy=name_estrategy)
        print("\n\n\n -------------------------------------------- msg para operação")
        print(msg)
        urls_iqoption.WSS_OBJ.wss.send(msg)
        print("operação enviada")
        print("-------------------------------------------- \n\n\n\n")

    def send_message_open_operation_alert(obj_analysis, status_alert):
        msg = Channels_WSS.open_operation_plataform_alert(obj_analysis, status_alert)
        print("\n\n\n -------------------------------------------- msg para operação")
        print(msg)
        urls_iqoption.WSS_OBJ.wss.send(msg)
        print("operação enviada")
        print("-------------------------------------------- \n\n\n\n")
    
    def send_message_get_result_operations(tt_operations):
        Channels_WSS.get_results_operations(tt_operations)
    






