import math
from app.schemas.schemas import SimulationInput, SimulationOutput

def simular_movimiento(data: SimulationInput) -> SimulationOutput:
    # Fuerza neta
    fuerza_neta = data.fuerza - (data.coef_rozamiento * data.masa * 9.81)
    aceleracion = fuerza_neta / data.masa
    velocidad_final = aceleracion * data.tiempo
    distancia = 0.5 * aceleracion * data.tiempo ** 2

    return SimulationOutput(
        aceleracion=aceleracion,
        velocidad_final=velocidad_final,
        distancia_recorrida=distancia
    )
