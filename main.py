import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from davinci.rutas import simulation, team, project

app = FastAPI(title="Tanque de Guerra de Leonardo da Vinci API")

app.mount(
    "/static",
    StaticFiles(directory=os.path.join("davinci", "static")),
    name="static"
)
templates = Jinja2Templates(directory=os.path.join("davinci", "templates"))

app.include_router(simulation.router, prefix="/simulation", tags=["Simulation"])
app.include_router(team.router, prefix="/team", tags=["Team"])
app.include_router(project.router, prefix="/project", tags=["Project"])

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Bienvenido al proyecto del tanque de guerra de Leonardo da Vinci"})