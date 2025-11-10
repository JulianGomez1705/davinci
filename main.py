from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routes import simulation, team, project

app = FastAPI(title="Tanque de Guerra de Leonardo da Vinci API")

# Rutas (endpoints)
app.include_router(simulation.router)
app.include_router(team.router)
app.include_router(project.router)

# Archivos estáticos y plantillas HTML
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
def home():
    return {"message": "Bienvenido al proyecto del tanque de guerra de Leonardo da Vinci"}
