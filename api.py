#bibliotecas
from flask import Flask, request
from datetime import datetime
import json

#inicia a api
app = Flask(__name__)

#home page

@app.route("/")
def homepage():
  return "A api delivery CocoBambu está funcionando!"

#endpoint 1
#cria novo pedido
@app.route("/api/create", methods = ['POST'])
def create():
    data = dict(request.args)
    data["timestamp"] = datetime.now().strftime("%Y/%m/%dT%H:%M:%S")
    data["entregue"] = False
    data["valor"] = float(data["valor"])
    f = open("pedidos.json", encoding="utf-8")
    dicionario = json.load(f)
    f.close()
    data["id"] = dicionario["nextId"]
    dicionario["nextId"] += 1
    dicionario["pedidos"].append(data)
    f = open("pedidos.json", "w", encoding="utf-8")
    json.dump(dicionario, f)
    f.close()
    return data

#endpoint2
#altera o pedido
@app.route("/api/alterarpedido", methods = ['POST'])
def alterarpedido():
  consulta = dict(request.args)
  consulta['id'] = int(consulta['id'])
  consulta['cliente'] = str(consulta['cliente'])
  consulta['produto'] = str(consulta['produto'])
  consulta['valor'] = float(consulta['valor'])
  consulta['entregue'] = bool(consulta['entregue'])
  f = open("pedidos.json", encoding="utf-8")
  dicionario = json.load(f)
  f.close()
  for i in range(len(dicionario["pedidos"])):
    try:
      if dicionario["pedidos"][i]["id"] ==     consulta['id']:
        dicionario["pedidos"][i]['cliente'] =  consulta['cliente']
        dicionario["pedidos"][i]['produto'] =  consulta['produto']
        dicionario["pedidos"][i]['valor'] =    consulta['valor']
        dicionario["pedidos"][i]['entregue'] = consulta['entregue']
        break
    except:
      pass
  else:
    return "Id not found"
  f = open("pedidos.json", "w", encoding="utf-8")
  json.dump(dicionario, f)
  f.close()
  return "Success"

#endpoint3
#muda o status entregue
@app.route("/api/entregue", methods = ['POST'])
def entregue():
  id_data = dict(request.args)
  id_data['id'] = int(id_data['id'])
  f = open("pedidos.json", encoding="utf-8")
  dicionario = json.load(f)
  f.close()
  for i in range(len(dicionario["pedidos"])):
    try:
      if dicionario["pedidos"][i]["id"] == id_data['id']:
        if str(id_data["entregue"]) == 'true':
          dicionario["pedidos"][i]["entregue"] = True
          break
        else:
          dicionario["pedidos"][i]["entregue"] = False
          break
    except:
      pass
  else:
    return "Id not found"
  f = open("pedidos.json", "w", encoding="utf-8")
  json.dump(dicionario, f)
  f.close()
  return "Success"


#endpoint4
#deleta clientes
@app.route("/api/delete", methods = ['POST'])
def delete():
  id = dict(request.args)["id"]
  f = open("pedidos.json", encoding="utf-8")
  dicionario = json.load(f)
  f.close()
  for i in range(len(dicionario["pedidos"])):
    try:
      if dicionario["pedidos"][i]["id"] == int(id):
        dicionario["pedidos"].pop(i)
        break
    except:
      pass
  else:
    return "Id not found"
  f = open("pedidos.json", "w", encoding="utf-8")
  json.dump(dicionario, f)
  f.close()
  return "Success"

#endpoint5
#informa dados do pedido
@app.route("/api/consultarpedido", methods = ['POST'])
def consultarpedido():
  id = dict(request.args)["id"]
  f = open("pedidos.json", encoding="utf-8")
  dicionario = json.load(f)
  f.close()
  for i in range(len(dicionario["pedidos"])):
    try:
      if dicionario["pedidos"][i]["id"] == int(id):
        return dicionario["pedidos"][i]
        break
    except:
      pass
  else:
    return "Id not found"
  f = open("pedidos.json", "w", encoding="utf-8")
  json.dump(dicionario, f)
  f.close()
  return "Success"
  
#endpoint6
#informa dados sobre o cliente
@app.route("/api/fregues", methods = ['POST'])
def fregues():
  nome = dict(request.args)["nome"]
  somador =  dict()
  f = open("pedidos.json", encoding="utf-8")
  dicionario = json.load(f)
  f.close()
  somador['soma'] = 0
  for i in range(len(dicionario["pedidos"])):
    try:
      if dicionario["pedidos"][i]["cliente"] == str(nome)and dicionario["pedidos"][i]["entregue"] == True:
        somador['soma'] += 1
    except:
      pass
  f = open("pedidos.json", "w", encoding="utf-8")
  json.dump(dicionario, f)
  f.close()
  return somador

#endpoint7
#informa a qnt de produtos
@app.route("/api/qntdproduto", methods = ['POST'])
def qntdproduto():
  produto = dict(request.args)["produto"]
  somador =  dict()
  f = open("pedidos.json", encoding="utf-8")
  dicionario = json.load(f)
  f.close()
  somador['soma'] = 0
  for i in range(len(dicionario["pedidos"])):
    try:
      if dicionario["pedidos"][i]["produto"] == str(produto)and dicionario["pedidos"][i]["entregue"] == True:
        somador['soma'] += 1
    except:
      pass
  f = open("pedidos.json", "w", encoding="utf-8")
  json.dump(dicionario, f)
  f.close()
  return somador

#rodar nossa api
app.run(host = '0.0.0.0')
