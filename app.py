from fastapi import FastAPI, HTTPException

app = FastAPI()

lista_tarefas = {}

@app.post("/adiciona")
def post_tarefas(nome_tarefa: str, descricao_tarefa: str, tarefa_concluida: bool = False):
    id_tarefa = len(lista_tarefas) + 1
    nova_tarefa = {
        "nome_tarefa": nome_tarefa,
        "descricao_tarefa": descricao_tarefa,
        "tarefa_concluida": tarefa_concluida
    }
    lista_tarefas[id_tarefa] = nova_tarefa
    return {"message": "Tarefa adicionada com sucesso!", "id": id_tarefa, "tarefa": nova_tarefa}

@app.get("/tarefas")
def get_tarefas():
    return {"Lista de tarefas": lista_tarefas}

@app.put("/atualiza")
def put_tarefas(nome_tarefa: str):
    for id_tarefa, tarefa in lista_tarefas.items():
        if tarefa["nome_tarefa"] == nome_tarefa:
            tarefa["tarefa_concluida"] = True
            return {"message": "Tarefa atualizada com sucesso!", "id": id_tarefa, "tarefa": tarefa}
    
    raise HTTPException(status_code=404, detail="Tarefa não encontrada na lista")

@app.delete("/remove")
def delete_tarefas(nome_tarefa: str):
    for id_tarefa, tarefa in lista_tarefas.items():
        if tarefa["nome_tarefa"] == nome_tarefa:
            del lista_tarefas[id_tarefa]
            return {"message": "Tarefa removida com sucesso!"}
    
    raise HTTPException(status_code=404, detail="Tarefa não encontrada na lista")
