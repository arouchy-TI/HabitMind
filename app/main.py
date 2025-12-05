from fastapi import FastAPI

app = FastAPI(
    title="HabitMind API",
    description="Api - plataforma inteligente de gestao de habitos",
    version="0.1.0",
)

@app.get("/")
def root():
    return {"message" : "Bem vindo a minha Aplicacao de Habitos!"}

