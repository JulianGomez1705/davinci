from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# 1. Importación Simple de Rutas (Necesario para Uvicorn en el directorio davinci)
from davinci.rutas import simulation, team, project

# 2. Inicialización de la app
app = FastAPI(title="Tanque de Guerra de Leonardo da Vinci API")

# 3. Archivos estáticos y plantillas HTML (DEBEN DEFINIRSE ANTES DE USAR RUTAS)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# 4. Inclusión de Routers
app.include_router(simulation.router, prefix="/simulation", tags=["Simulation"])
app.include_router(team.router, prefix="/team", tags=["Team"])
app.include_router(project.router, prefix="/project", tags=["Project"])

# 5. Endpoint Home
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Bienvenido al proyecto del tanque de guerra de Leonardo da Vinci"})