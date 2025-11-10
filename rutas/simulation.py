from fastapi import APIRouter
from app.schemas.schemas import SimulationInput, SimulationOutput
from app.services.calculations import simular_movimiento

router = APIRouter(prefix="/simulation", tags=["Simulación"])

@router.post("/run", response_model=SimulationOutput)
def run_simulation(data: SimulationInput):
    """
    Simula el movimiento del tanque de guerra según los datos físicos ingresados.
    """
    return simular_movimiento(data)
