from fastapi import FastAPI, HTTPException, Depends, status, Query
from pydantic import BaseModel
from typing import Optional
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets
import math

class Tarefa(BaseModel):
    id: Optional[int] = None
    nome_tarefa: str
    descricao_tarefa: str
    tarefa_concluida: bool = False

app = FastAPI()
security = HTTPBasic()

def verificar_usuario(credentials: HTTPBasicCredentials = Depends(security)):
    usuario_valido = secrets.compare_digest(credentials.username, "admin")
    senha_valida = secrets.compare_digest(credentials.password, "admin")
    
    if not (usuario_valido and senha_valida):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

lista_tarefas: list[Tarefa] = []
id_contador = 0

@app.post("/tarefas")
def post_tarefas(tarefa: Tarefa, usuario: str = Depends(verificar_usuario)):
    global id_contador
    id_contador += 1
    tarefa.id = id_contador
    lista_tarefas.append(tarefa)
    return {"message": "Tarefa adicionada com sucesso!", "id": id_contador, "tarefa": tarefa}

@app.get("/tarefas")
def get_tarefas(
    page: int = Query(default=1, ge=1, description="Número da página"),
    size: int = Query(default=10, ge=1, le=100, description="Quantidade de tarefas por página"),
    limit: Optional[int] = Query(default=None, ge=1, le=100, description="Alias para size"),
    order_by: Optional[str] = Query(default=None, description="Campo para ordenação ('nome', 'descricao', 'id')"),
    usuario: str = Depends(verificar_usuario)
):
    # Aplica a ordenação antes da paginação
    if order_by:
        campo = order_by.lower()
        if campo in ("nome", "nome_tarefa"):
            tarefas_ordenadas = sorted(lista_tarefas, key=lambda x: x.nome_tarefa.lower())
        elif campo in ("descricao", "descricao_tarefa"):
            tarefas_ordenadas = sorted(lista_tarefas, key=lambda x: x.descricao_tarefa.lower())
        elif campo == "id":
            tarefas_ordenadas = sorted(lista_tarefas, key=lambda x: x.id or 0)
        elif campo in ("concluida", "tarefa_concluida", "status"):
            tarefas_ordenadas = sorted(lista_tarefas, key=lambda x: x.tarefa_concluida)
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Campo de ordenação '{order_by}' inválido. Escolha entre: 'nome', 'descricao' ou 'id'."
            )
    else:
        tarefas_ordenadas = lista_tarefas

    limite = limit if limit is not None else size
    total_tarefas = len(tarefas_ordenadas)
    total_paginas = math.ceil(total_tarefas / limite) if total_tarefas > 0 else 1
    start = (page - 1) * limite
    end = start + limite

    return {
        "pagina_atual": page,
        "itens_por_pagina": limite,
        "total_tarefas": total_tarefas,
        "total_paginas": total_paginas,
        "Lista de tarefas": tarefas_ordenadas[start:end],
    }

@app.put("/tarefas/{nome_tarefa}")
@app.put("/tarefas")
def put_tarefas(nome_tarefa: str, usuario: str = Depends(verificar_usuario)):
    for tarefa in lista_tarefas:
        if tarefa.nome_tarefa == nome_tarefa:
            tarefa.tarefa_concluida = True
            return {"message": "Tarefa atualizada com sucesso!", "tarefa": tarefa}
    raise HTTPException(status_code=404, detail="Tarefa não encontrada na lista")

@app.delete("/tarefas/{nome_tarefa}")
@app.delete("/tarefas")
def delete_tarefas(nome_tarefa: str, usuario: str = Depends(verificar_usuario)):
    for i, tarefa in enumerate(lista_tarefas):
        if tarefa.nome_tarefa == nome_tarefa:
            del lista_tarefas[i]
            return {"message": "Tarefa removida com sucesso!"}
    raise HTTPException(status_code=404, detail="Tarefa não encontrada na lista")
