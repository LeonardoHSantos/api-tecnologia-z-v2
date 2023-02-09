import pandas as pd


from plataform import var_data_process

from plataform.http_plataform import data_times_expirations

from plataform.module_times.converter_timestamp import timesTemp_converter, datetime_now_sao_paulo, timesTemp_converter_to_obj

from plataform.module_times.converter_timestamp import expiration_operation_5m_alert

from logs_api.logs_api import logging_api

class ProcessData_Alert:
    def __init__(self, message):
        self.request_id = message["request_id"]
        self.data = message["msg"]["candles"]
    
    def process_data_version_1_alert(self, type_operation):

        
        if self.request_id in var_data_process.LISTA_ATIVOS_ABERTOS["P-M5-2"].values:
            name_estrategy = "P-M5-2"
            expiration_timestamp = expiration_operation_5m_alert()
            expiration = timesTemp_converter_to_obj(expiration_timestamp)
            alert_datetime = datetime_now_sao_paulo()
            try:
                id_active = var_data_process.LISTA_ATIVOS_ABERTOS[var_data_process.LISTA_ATIVOS_ABERTOS[name_estrategy] == self.request_id]["id"].values[0]
                active    = var_data_process.LISTA_ATIVOS_ABERTOS[var_data_process.LISTA_ATIVOS_ABERTOS["id"]           == id_active]["ativo"].values[0]
                mercado   = var_data_process.LISTA_ATIVOS_ABERTOS[var_data_process.LISTA_ATIVOS_ABERTOS["id"]           == id_active]["mercado"].values[0]
                padrao    = var_data_process.LISTA_ATIVOS_ABERTOS[var_data_process.LISTA_ATIVOS_ABERTOS["id"]           == id_active]["nome padrao v2"].values[0]
                
                print(f"Processando dados: {self.request_id} | Nome da estratégia: {name_estrategy} | ExpiraçãoTMST: {expiration_timestamp} | Expiração: {expiration} | Ativo: {active} | Mercado: {mercado}")
             
                self.data = pd.DataFrame(self.data)
                try:
                    self.data[["open", "close", "min", "max"]] = self.data[["open", "close", "min", "max"]].astype(float, errors="raise")
                    print("pd convertido M5...")
                except Exception as e:
                    print(f"Erro conversão DataFrame: {e}")
                    logging_api(process_log="error", log=f"Error: **** ProcessData_Alert | process_data_version_1_alert **** Erro conversão DataFrame M5-V1: {e}")
                list_data = [
                    [], # status close
                    [], # active
                ]
                print("*********** início loop")
                for i in range(len(self.data["id"])):
                    self.data["from"][i] = timesTemp_converter(self.data["from"][i])
                    list_data[1].append(self.request_id)
                    try:
                        if self.data["close"][i] > self.data["open"][i]:
                            list_data[0].append("alta")
                        elif self.data["close"][i] < self.data["open"][i]:
                            list_data[0].append("baixa")
                        else:
                            list_data[0].append("sem mov.")
                    except Exception as e:
                        print(f"Erro tratamento dataframe: {e}")
                        logging_api(process_log="error", log=f"Error: **** ProcessData_Alert | process_data_version_1_alert **** Erro tratamento dataframe M5-V1: {e}")
                print("*********** fim loop") 
                print("---------------------------- df atualizado M5")
                self.data["status close"],self.data["active"] = list_data[0], list_data[1]
                print("<<< *************************")
                print(self.data)
                logging_api(process_log="info", log=f"DataFrame atualizado M5 - v1:\n{self.data}")
            
                direction = "---"
                try:
                    if self.data["status close"][0] == "alta" and self.data["status close"][1] == "baixa" and self.data["status close"][2] == "baixa":
                        if self.data["status close"][3] == "alta" and self.data["status close"][4] == "alta":
                            if self.data["status close"][5] == "baixa": # condição adicionada 07/02/2023.
                                direction = "put"
            
                    elif self.data["status close"][0] == "baixa" and self.data["status close"][1] == "alta" and self.data["status close"][2] == "alta":
                        if self.data["status close"][3] == "baixa" and self.data["status close"][4] == "baixa":
                            if self.data["status close"][5] == "alta": # condição adicionada 07/02/2023.
                                direction = "call"
                    print(f" ----------------  Fim análise M5-V1-ALERT direction: {direction} ----------------")
                except Exception as e:
                    print(f"---> Erro durante validação direção: {e}")
                    logging_api(process_log="error", log=f"Error: **** ProcessData_Alert | process_data_version_1_alert **** Erro durante validação direção M5-V1: {e}")
                

                object_analyzed  = {
                    "alert_datetime": alert_datetime,
                    "id_active": id_active,
                    "active": active,
                    "mercado": mercado,
                    "direction": direction,
                    # "direction": "call",
                    "padrao": padrao,
                    "name_estrategy": name_estrategy,
                    "expiration": expiration,
                    "expiration_timestamp": expiration_timestamp,
                    "msg_active": f"Atenção Ativo: {active} | Mercado: {mercado} | Direção: {direction} | Padrão: {padrao} | Expiração: {expiration}",
                }
                print(f"----------->>> Mensagem M5-V1 pronta para envio: {object_analyzed}")
                logging_api(process_log="info", log=f"Mensagem M5-V1 pronta para envio: {object_analyzed}")
                return object_analyzed

            except Exception as e:
                print("-- Erro processamento de dados M5-V1: ", e)
                logging_api(process_log="error", log=f"Error: **** ProcessData_Alert | process_data_version_1_alert **** Erro de processamento de dados M5-V1: {e}")


        elif self.request_id in var_data_process.LISTA_ATIVOS_ABERTOS["P-M5-3"].values:
            name_estrategy = "P-M5-3"
            expiration_timestamp = expiration_operation_5m_alert()
            expiration = timesTemp_converter_to_obj(expiration_timestamp)
            alert_datetime = datetime_now_sao_paulo()
            try:

                id_active = var_data_process.LISTA_ATIVOS_ABERTOS[var_data_process.LISTA_ATIVOS_ABERTOS[name_estrategy] == self.request_id]["id"].values[0]
                active    = var_data_process.LISTA_ATIVOS_ABERTOS[var_data_process.LISTA_ATIVOS_ABERTOS["id"]           == id_active]["ativo"].values[0]
                mercado   = var_data_process.LISTA_ATIVOS_ABERTOS[var_data_process.LISTA_ATIVOS_ABERTOS["id"]           == id_active]["mercado"].values[0]
                padrao    = var_data_process.LISTA_ATIVOS_ABERTOS[var_data_process.LISTA_ATIVOS_ABERTOS["id"]           == id_active]["nome padrao v3"].values[0]
                

                print(f"Processando dados: {self.request_id} | Nome da estratégia: {name_estrategy} | ExpiraçãoTMST: {expiration_timestamp} | Expiração: {expiration} | Ativo: {active} | Mercado: {mercado}")
                
                
                self.data = pd.DataFrame(self.data)
                try:
                    self.data[["open", "close", "min", "max"]] = self.data[["open", "close", "min", "max"]].astype(float, errors="raise")
                    print("pd convertido M5-3...")
                except Exception as e:
                    print(f"Erro conversão DataFrame: {e}")
                    logging_api(process_log="error", log=f"Error: **** ProcessData_Alert | process_data_version_1_alert **** Erro conversão DataFrame M5-V2: {e}")
                list_data = [
                    [], # status close
                    [], # active
                ]
                print("*********** início loop")
                for i in range(len(self.data["id"])):
                    self.data["from"][i] = timesTemp_converter(self.data["from"][i])
                    list_data[1].append(self.request_id)
                    try:
                        if self.data["close"][i] > self.data["open"][i]:
                            list_data[0].append("alta")
                        elif self.data["close"][i] < self.data["open"][i]:
                            list_data[0].append("baixa")
                        else:
                            list_data[0].append("sem mov.")
                    except Exception as e:
                        print(f"Erro tratamento dataframe: {e}")
                        logging_api(process_log="error", log=f"Error: **** ProcessData_Alert | process_data_version_1_alert **** Erro tratamento dataframe M5-V2: {e}")
                print("*********** fim loop") 
                print("---------------------------- df atualizado M5 - v2")
                self.data["status close"],self.data["active"] = list_data[0], list_data[1]
                print("<<< *************************")
                print(self.data)
                logging_api(process_log="info", log=f"DataFrame atualizado M5 - v2:\n{self.data}")
            
                direction = "---"
                try:
                    if self.data["status close"][0] == "baixa" and self.data["status close"][1] == "alta" and self.data["status close"][2] == "baixa":
                        if self.data["status close"][3] == "baixa" and self.data["status close"][4] == "baixa" and self.data["status close"][5] == "baixa":
                            direction = "call"
                    elif self.data["status close"][0] == "alta" and self.data["status close"][1] == "baixa" and self.data["status close"][2] == "alta":
                        if self.data["status close"][3] == "alta" and self.data["status close"][4] == "alta" and self.data["status close"][5] == "alta":
                            direction = "put"
                    print(f" ----------------  Fim análise M5-V2-ALERT direction: {direction} ----------------")
                except Exception as e:
                    print(f"---> Erro durante validação direção: {e}")
                    logging_api(process_log="error", log=f"Error: **** ProcessData_Alert | process_data_version_1_alert **** Erro durante validação direção M5-V2: {e}")
                
                object_analyzed = {
                    "alert_datetime": alert_datetime,
                    "id_active": id_active,
                    "active": active,
                    "mercado": mercado,
                    "direction": direction,
                    # "direction": "call",
                    "padrao": padrao,
                    "name_estrategy": name_estrategy,
                    "expiration": expiration,
                    "expiration_timestamp": expiration_timestamp,
                    "msg_active": f"Atenção Ativo: {active} | Mercado: {mercado} | Direção: {direction} | Padrão: {padrao} | Expiração: {expiration}",
                }
                print(f"----------->>> Mensagem M5-V2 pronta para envio: {object_analyzed}")
                logging_api(process_log="info", log=f"Mensagem M5-V2 pronta para envio: {object_analyzed}")
                return object_analyzed

            except Exception as e:
                print("-- Erro processamento de dados M5-V2: ", e)
                logging_api(process_log="error", log=f"Error: **** ProcessData_Alert | process_data_version_1_alert **** Erro de processamento de dados M5-V2: {e}")


