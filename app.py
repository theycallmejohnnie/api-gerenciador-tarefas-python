from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

class Tarefa(BaseModel):
    nome_tarefa: str
    descricao_tarefa: str
    tarefa_concluida: bool = False

app = FastAPI()

lista_tarefas = {}

@app.post("/tarefas")
def post_tarefas(tarefa: Tarefa):
    id_tarefa = len(lista_tarefas) + 1
    lista_tarefas[id_tarefa] = tarefa.dict()
    return {"message": "Tarefa adicionada com sucesso!", "id": id_tarefa, "tarefa": tarefa}

@app.get("/tarefas")
def get_tarefas():
    return {"Lista de tarefas": lista_tarefas}

@app.put("/tarefas/{id_tarefa}")
def put_tarefas(id_tarefa: int):
    if id_tarefa in lista_tarefas:
        lista_tarefas[id_tarefa]["tarefa_concluida"] = True
        return {"message": "Tarefa atualizada com sucesso!", "id": id_tarefa, "tarefa": lista_tarefas[id_tarefa]}
    raise HTTPException(status_code=404, detail="Tarefa não encontrada na lista")

@app.delete("/tarefas/{id_tarefa}")
def delete_tarefas(id_tarefa: int):
    if id_tarefa in lista_tarefas:
        del lista_tarefas[id_tarefa]
        return {"message": "Tarefa removida com sucesso!"}
    raise HTTPException(status_code=404, detail="Tarefa não encontrada na lista")
