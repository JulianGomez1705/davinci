from pydantic import BaseModel

class SimulationInput(BaseModel):
    masa: float
    fuerza: float
    coef_rozamiento: float
    tiempo: float

class SimulationOutput(BaseModel):
    aceleracion: float
    velocidad_final: float
    distancia_recorrida: float
