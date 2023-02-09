import json
import pandas as pd
from plataform import urls_iqoption, constants, var_data_process

from logs_api.logs_api import logging_api

def process_open_actives(dados):
        try:
            print("processando dados ativos abertos --------------------------------------------------")
            var_data_process.LISTA_ATIVOS_ABERTOS = None
            lista_ativos = [
                [], # 0 id
                [], # 1 name
                [], # 2 ticker
                [], # 3 is_suspended
                [], # 4 enabled
                [], # 5 padrão 15m
                [], # 6 padrão 5m
                [], # 7 mercado

                [], #  8 nome padrao 1
                [], #  9 nome padrao 2

                [], # 10 padrão 5m v2
                [], # 11 nome padrao 3

            ]
            for i in dados["binary"]["actives"]:
                try:
                    id   = dados["binary"]["actives"][i]["id"]
                    name = dados["binary"]["actives"][i]["name"]
                    ticker = dados["binary"]["actives"][i]["ticker"]

                    is_suspended = dados["binary"]["actives"][i]["is_suspended"]
                    enabled = dados["binary"]["actives"][i]["enabled"]
                    # print(id, name, ticker, is_suspended, enabled)
                    
                    if enabled == True and ticker in constants.PARIDADES.keys(): #and is_suspended == False:

                        lista_ativos[0].append(id)
                        lista_ativos[1].append(name)
                        lista_ativos[2].append(ticker)
                        lista_ativos[3].append(is_suspended)
                        lista_ativos[4].append(enabled)
                        lista_ativos[5].append(f"{ticker}-M15-V1-900")
                        lista_ativos[6].append(f"{ticker}-M5-V2-300")

                        if "OTC" in ticker:
                            lista_ativos[7].append("otc")
                        else:
                            lista_ativos[7].append("aberto")

                        lista_ativos[8].append("PADRAO-M15-V1")
                        lista_ativos[9].append("PADRAO-M5-V1")

                        lista_ativos[10].append(f"{ticker}-M5-V3-300")
                        lista_ativos[11].append("PADRAO-M5-V2")
                    
                except Exception as e:
                    print(e)
                    logging_api(process_log="error", log=e)
            if len(lista_ativos[0]) >= 1:

                df = pd.DataFrame(list(zip(
                        lista_ativos[0],
                        lista_ativos[1],
                        lista_ativos[2],
                        lista_ativos[3],
                        lista_ativos[4],
                        lista_ativos[5], lista_ativos[6], lista_ativos[7],
                        lista_ativos[8],
                        lista_ativos[9],
                        lista_ativos[10], lista_ativos[11],
                    )),
                    columns=[
                        "id", "nome", "ativo", "supenso", "status",
                        "P-M15-1", "P-M5-2", "mercado", "nome padrao v1",
                        "nome padrao v2",
                        "P-M5-3", "nome padrao v3"
                    ])
                print(df)
                var_data_process.LISTA_ATIVOS_ABERTOS = df
            else:
                var_data_process.LISTA_ATIVOS_ABERTOS = "nenhum ativo encontrado"
        except Exception as e:
            print(e)
            logging_api(process_log="error", log=e)