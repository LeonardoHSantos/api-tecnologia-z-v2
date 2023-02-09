from plataform  import var_data_process, urls_iqoption, constants
from plataform.http_plataform import prepare_message
from plataform.http_plataform import data_times_expirations

import json

class Channels_WSS:
    def get_candles(timeframe, amount, estrategia):
        time_now = data_times_expirations.time_date_now()
       
        print(f"Horário: {time_now} | estratégia: {estrategia} | amount: {amount} --> Func.: Channels_WSS.get_candles")
       
        expiration = data_times_expirations.expiration_of_operation()[0]
        try:
            for i in range(len(var_data_process.LISTA_ATIVOS_ABERTOS["id"])):
                try:
                    id_active   = int(var_data_process.LISTA_ATIVOS_ABERTOS["id"][i])

                    try:
                        if estrategia == "PADRAO-M15-V1":
                            active_name = var_data_process.LISTA_ATIVOS_ABERTOS["P-M15-1"][i]
                        elif estrategia == "PADRAO-M5-V1":
                            active_name = var_data_process.LISTA_ATIVOS_ABERTOS["P-M5-2"][i]
                        elif estrategia == "PADRAO-M5-V2":
                            active_name = var_data_process.LISTA_ATIVOS_ABERTOS["P-M5-3"][i]

                    except Exception as e:
                        print(f" *** Channels_WSS.get_candles -->>  Erro validação de estratégia: {e}")


                    name = 'sendMessage'
                    msg = {
                        'name': 'get-candles',
                        'version': '2.0',
                        'body': {
                            'active_id': id_active,
                            'size': timeframe,
                            'to': expiration,
                            'count': amount,
                        }
                    }
                    request_id = active_name
                    msg = prepare_message.prepare_message_send_wss(
                        name=name,
                        data=msg,
                        request_id=request_id
                        )
                    print("<<*************************************>>")
                    print(msg)
                    urls_iqoption.WSS_OBJ.wss.send(msg)
                    print(f"{i} ---> mensagem enviada")
                except Exception as e:
                    print("erro >>> ", e)
        except Exception as e:
            print(e)

    def open_operation_plataform(active, direction, name_estrategy):
        name = "sendMessage"
        # expiration = data_times_expirations.expiration_of_operation()[0]
        # print(f"---------------- expiração de 1min: {expiration}")

        if name_estrategy == "P-M15-1":
            expiration = data_times_expirations.expiration_operation_15m()
        elif name_estrategy == "P-M5-2":
            expiration = data_times_expirations.expiration_operation_5m()
        elif name_estrategy == "P-M5-3":
            expiration = data_times_expirations.expiration_operation_5m()

        
        id_active  = var_data_process.LISTA_ATIVOS_ABERTOS[var_data_process.LISTA_ATIVOS_ABERTOS[name_estrategy] == active]["id"].values[0]
        var_data_process.MERCADO    = var_data_process.LISTA_ATIVOS_ABERTOS[var_data_process.LISTA_ATIVOS_ABERTOS[name_estrategy] == active]["mercado"].values[0]
        print(f"<>>>>>>> id active: {id_active} | mercado: {var_data_process.MERCADO} | estrategia: {var_data_process.ESTRATEGIA} | expiração: {expiration}")
        
        body = {
            "body": {
                "price": 1.5,
                "active_id": int(id_active),
                "expired": int(expiration),
                "direction": direction,
                "option_type_id": 3,
                "user_balance_id": constants.ID_ACCOUNT_PRACTICE
                },
                "name": "binary-options.open-option",
                "version": "1.0"
            }
        # request_id = f"{ativo}-{direcao}-{timeframe}"
        request_id = active
        return prepare_message.prepare_message_send_wss(name=name, data=body, request_id=request_id)

    def open_operation_plataform_alert(obj_analysis, status_alert):
        name = "sendMessage"
        print(f"-----------------------> dados para body send_msg: {obj_analysis}")
   
        id_active = obj_analysis["id_active"]
        # direction = obj_analysis["direction"]
        direction = "call"
        expiration_timestamp = obj_analysis["expiration_timestamp"]

        active = obj_analysis["active"]
        padrao = obj_analysis["padrao"]
        name_estrategy = obj_analysis["name_estrategy"]
        expiration = obj_analysis["expiration"]
        
        body = {
            "body": {
                "price": 1.5,
                "active_id": int(id_active),
                "expired": int(expiration_timestamp),
                "direction": direction,
                "option_type_id": 3,
                "user_balance_id": constants.ID_ACCOUNT_PRACTICE
                },
                "name": "binary-options.open-option",
                "version": "1.0"
            }
        request_id = [int(id_active), active, padrao, name_estrategy, expiration, expiration_timestamp, status_alert]
        if request_id not in var_data_process.LISTA_REQUEST_ID:
            tt_request_id = len(var_data_process.LISTA_REQUEST_ID)
            var_data_process.LISTA_REQUEST_ID.insert(tt_request_id, request_id)
   

        return prepare_message.prepare_message_send_wss(name=name, data=body, request_id=request_id)



    def get_results_operations(tt_operations):
        msg = json.dumps({"name": "api_game_getoptions", "msg": {"limit": tt_operations, "user_balance_id": constants.ID_ACCOUNT_PRACTICE}, "request_id": "info_operacoes"})
        urls_iqoption.WSS_OBJ.wss.send(msg)

