from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

class Tarefa(BaseModel):
    nome_tarefa: str
    descricao_tarefa: str
    tarefa_concluida: bool = False

app = FastAPI()

lista_tarefas: list[Tarefa] = []
id_contador = 0

@app.post("/tarefas")
def post_tarefas(tarefa: Tarefa):
    global id_contador
    id_contador += 1
    id_tarefa = id_contador
    lista_tarefas.append(tarefa)
    return {"message": "Tarefa adicionada com sucesso!", "id": id_tarefa, "tarefa": tarefa}

@app.get("/tarefas")
def get_tarefas():
    return {"Lista de tarefas": lista_tarefas}

@app.put("/tarefas/{nome_tarefa}")
@app.put("/tarefas")
def put_tarefas(nome_tarefa: str):
    for tarefa in lista_tarefas:
        if tarefa.nome_tarefa == nome_tarefa:
            tarefa.tarefa_concluida = True
            return {"message": "Tarefa atualizada com sucesso!", "tarefa": tarefa}
    raise HTTPException(status_code=404, detail="Tarefa não encontrada na lista")

@app.delete("/tarefas/{nome_tarefa}")
@app.delete("/tarefas")
def delete_tarefas(nome_tarefa: str):
    for i, tarefa in enumerate(lista_tarefas):
        if tarefa.nome_tarefa == nome_tarefa:
            del lista_tarefas[i]
            return {"message": "Tarefa removida com sucesso!"}
    raise HTTPException(status_code=404, detail="Tarefa não encontrada na lista")
