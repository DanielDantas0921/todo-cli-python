import json

def read_json(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arquivo:
            dados = json.load(arquivo)
        print("File read successfully.")
        return dados 
    except FileNotFoundError:
        print("File not found.")
        return None

def write_json(nome_arquivo, dados):
    with open(nome_arquivo, "w") as arquivo:
        json.dump(dados, arquivo, indent=4)
    print("data saved successfully.")
