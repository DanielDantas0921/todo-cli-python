import json
import os

def generate_id():
    caminho_dados = "tasks.json"
    # Verifica se o arquivo existe
    if os.path.exists(caminho_dados):
        with open(caminho_dados, "r") as arquivo:
            dados = json.load(arquivo)
            if len(dados)> 0:
               for __ in dados:
                generate_id = dados[-1]["id"] + 1
            else:
                generate_id = 1
    else:
        generate_id = 1

    return generate_id
