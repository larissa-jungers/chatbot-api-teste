from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# estrutura de dados para as mensagens usando pydantic | definição do formato da mensagem recebida
class Mensagem(BaseModel):
    id_usuario: str
    conteudo: str

# rota GET para testar funcionamento da API
@app.get("/")
def home():
        return {"mensagem": "API rodando com sucesso!"}

# rota POST que recebe uma mensagem e imprimeno terminal
@app.post("/mensagem")
def receber_mensagem(mensagem: Mensagem):
        print(f"Mensagem recebida do usuário {mensagem.id_usuario}: {mensagem.conteudo}")
        return {"status": "ok", "recebido": mensagem.dict()}