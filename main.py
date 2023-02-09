from plataform.http_plataform.auth_plataform import auth_user
from plataform.wss_manage import StartWebsocket
import config_db

from logs_api.logs_api import logging_api

auth = auth_user(config_db.USER_IQ, config_db.PASSWORD_IQ)

print(auth)
if auth[0] == 200:
    StartWebsocket.start_connect_wss(auth[1])
else:
    print(f"Credenciais incorretas. Tente novamente.")


# max = 3
# cont = 0
# while True:
#     if cont == max:
#         print("Você excedeu a quantidade máxima de tentativas. Verique sua conta.")
#         break
#     auth = auth_user(
#         str(input("Digite seu usuário (iqiotion): ")),
#         str(input("Digite sua senha (iqiotion): "))
#         )
#     print(auth)
#     if auth[0] == 200:
#         StartWebsocket.start_connect_wss(auth[1])
#         break
#     auth = None
#     cont += 1
#     print(f"Credenciais incorretas. Tente novamente. | Tentativas: {cont}/{max}")

