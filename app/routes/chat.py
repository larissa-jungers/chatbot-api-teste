from fastapi import APIRouter, HTTPException
from app.models.session import Session

router = APIRouter()

# lista para simular banco de dados
sessions = []

# teste
@router.get("/ping")
async def ping():
        return {"message": "pong"}

# iniciar sessão
@router.post("/start-session")
async def start_session(technician_id: str, notes:str = None):
        session = Session.create(technician_id, notes)
        sessions.append(session)
        return session

# enviar mensagem
@router.post("/send-message")
async def send_message(technician_id: str, message: str):
    for session in sessions:
        if session.technician_id == technician_id:
            session.messages.append(message)
            return {"message": "Mensagem adicionada com sucesso."}
    raise HTTPException(status_code=404, detail="Sessão não encontrada.")

# ver histórico
@router.get("/history/{technician_id}")
async def get_history(technician_id: str):
    for session in sessions:
        if session.technician_id == technician_id:
            return {"messages": session.messages}
    raise HTTPException(status_code=404, detail="Sessão não encontrada.")