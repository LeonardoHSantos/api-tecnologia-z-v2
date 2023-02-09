import pandas as pd

from plataform .wss.send_message_wss import MessageWSS
from plataform import var_data_process
from plataform.module_times.converter_timestamp import timesTemp_converter

class ProcessData:
    def __init__(self, message):
        self.request_id = message["request_id"]
        self.data = message["msg"]["candles"]


    def process_data_version_1(self):
        print(f"--------> Início processamento de dados: {self.request_id}")

        
        if self.request_id in var_data_process.LISTA_ATIVOS_ABERTOS["P-M15-1"].values:
            
            name_estrategy = "P-M15-1"
            print(f"Processando dados: {self.request_id} | Nome da estratégia: {name_estrategy}")
            try:
                print(self.request_id)
                self.data = pd.DataFrame(self.data)
                try:
                    self.data[["open", "close", "min", "max"]] = self.data[["open", "close", "min", "max"]].astype(float, errors="raise")
                    print("pd convertido M15...")
                except Exception as e:
                    print(f"Erro conversão DataFrame: {e}")
                list_data = [
                    [], # status close
                    [], # active
                ]
                print("*********** início loop")
                for i in range(len(self.data["id"])):
                    # self.data["from"][i] = self.timesTemp_converter(self.data["from"][i])
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
                print("*********** fim loop") 
                print("---------------------------- df atualizado")
                self.data["status close"],self.data["active"] = list_data[0], list_data[1]
                index_inicio = 2
                # first_candle = df_amostra = self.data[self.data.index.values == 0]
                df_amostra = self.data[self.data.index.values >= index_inicio]
                print("<<< *************************")
                print(self.data)
                print(df_amostra)
                # print(first_candle)
                print("************************* >>>")
                cont_altas = df_amostra["status close"][df_amostra["status close"] == "alta"].count()
                cont_baixas = df_amostra["status close"][df_amostra["status close"] == "baixa"].count()
                print(cont_altas, cont_baixas)

                active = self.data["active"][0]
                direction = "---"
                try:
                    if self.data["status close"][1] == "alta" and cont_baixas >= 5:
                        direction = "call"
                    elif self.data["status close"][1] == "baixa" and cont_altas >= 5:
                        direction = "put"
                    print(f" ----------------  Fim análise df --> active: {active} | direction: {direction} ----------------")
                except Exception as e:
                    print(f"---> Erro durante validação alta/baixa: {e}")
                # MessageWSS.send_message_open_operation(active=active, direction="call", name_estrategy=name_estrategy)
                if direction != "---":
                    MessageWSS.send_message_open_operation(active=active, direction=direction, name_estrategy=name_estrategy)
                else:
                    print(f"Padrão sem confluência {self.request_id} | {direction}")

            except Exception as e:
                print(f"-- Erro processamento de dados {self.request_id}: ", e)

        elif self.request_id in var_data_process.LISTA_ATIVOS_ABERTOS["P-M5-2"].values:
            name_estrategy = "P-M5-2"
            print(f"Processando dados: {self.request_id} | Nome da estratégia: {name_estrategy}")
            try:
                print(self.request_id)
                self.data = pd.DataFrame(self.data)
                try:
                    self.data[["open", "close", "min", "max"]] = self.data[["open", "close", "min", "max"]].astype(float, errors="raise")
                    print("pd convertido M5...")
                except Exception as e:
                    print(f"Erro conversão DataFrame: {e}")
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
                print("*********** fim loop") 
                print("---------------------------- df atualizado M5")
                self.data["status close"],self.data["active"] = list_data[0], list_data[1]
                print("<<< *************************")
                print(self.data)
            
                active = self.data["active"][0]
                direction = "---"
                try:
                    if self.data["status close"][0] == "alta" and self.data["status close"][1] == "baixa" and self.data["status close"][2] == "baixa":
                        if self.data["status close"][3] == "alta" and self.data["status close"][4] == "alta":
                            direction = "put"
            
                    elif self.data["status close"][0] == "baixa" and self.data["status close"][1] == "alta" and self.data["status close"][2] == "alta":
                        if self.data["status close"][3] == "baixa" and self.data["status close"][4] == "baixa":
                            direction = "call"
                    print(f" ----------------  Fim análise direction: {direction} ----------------")
                except Exception as e:
                    print(f"---> Erro durante validação direção: {e}")
                # MessageWSS.send_message_open_operation(active=active, direction="call", name_estrategy=name_estrategy)
                if direction != "---":
                    MessageWSS.send_message_open_operation(active=active, direction=direction, name_estrategy=name_estrategy)
                else:
                    print(f"Padrão M5-V1 sem confluência {self.request_id} | {direction}")

            except Exception as e:
                print("-- Erro processamento de dados M5: ", e)

        elif self.request_id in var_data_process.LISTA_ATIVOS_ABERTOS["P-M5-3"].values:
            name_estrategy = "P-M5-3"
            print(f"Processando dados: {self.request_id} | Nome da estratégia: {name_estrategy}")
            try:
                print(self.request_id)
                self.data = pd.DataFrame(self.data)
                try:
                    self.data[["open", "close", "min", "max"]] = self.data[["open", "close", "min", "max"]].astype(float, errors="raise")
                    print("pd convertido M5-3...")
                except Exception as e:
                    print(f"Erro conversão DataFrame: {e}")
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
                print("*********** fim loop") 
                print("---------------------------- df atualizado M5 - v2")
                self.data["status close"],self.data["active"] = list_data[0], list_data[1]
                print("<<< *************************")
                print(self.data)
            
                active = self.data["active"][0]
                direction = "---"
                try:
                    if self.data["status close"][0] == "baixa" and self.data["status close"][1] == "alta" and self.data["status close"][2] == "baixa":
                        if self.data["status close"][3] == "baixa" and self.data["status close"][4] == "baixa" and self.data["status close"][5] == "baixa":
                            direction = "call"
            
                    elif self.data["status close"][0] == "alta" and self.data["status close"][1] == "baixa" and self.data["status close"][2] == "alta":
                        if self.data["status close"][3] == "alta" and self.data["status close"][4] == "alta" and self.data["status close"][5] == "alta":
                            direction = "put"
                    print(f" ----------------  Fim análise M5-V2 direction: {direction} ----------------")
                except Exception as e:
                    print(f"---> Erro durante validação direção: {e}")
                # MessageWSS.send_message_open_operation(active=active, direction="call", name_estrategy=name_estrategy)
                if direction != "---":
                    MessageWSS.send_message_open_operation(active=active, direction=direction, name_estrategy=name_estrategy)
                else:
                    print(f"Padrão  M5-V2 sem confluência {self.request_id} | {direction}")

            except Exception as e:
                print("-- Erro processamento de dados M5-V2: ", e)


