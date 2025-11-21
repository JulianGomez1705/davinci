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


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "title": "Proyecto Tanque de Guerra de Da Vinci",
            "info_davinci": "Leonardo da Vinci, genio del Renacimiento (1452–1519), fue un artista, científico e inventor. Su diseño más conocido es el Tanque de Guerra (Armoured Car), un vehículo blindado propulsado por la fuerza humana, que representa su audaz mezcla de arte e ingeniería militar.",
            "imagen_url": "/static/davinci_tank.jpg" # Usaremos esta URL para la imagen
        }
    )