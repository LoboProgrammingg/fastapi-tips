from fastapi import FastAPI

app = FastAPI(
    title="Mini CRM API",
    description="Uma API simples para gerenciar contatos.",
    version="0.1.0"
)

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Bem-vindo à API teste do FastAPI"}