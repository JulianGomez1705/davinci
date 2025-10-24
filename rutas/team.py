from fastapi import APIRouter

router = APIRouter(prefix="/team", tags=["Equipo"])

@router.get("/")
def get_team():
    return {
        "equipo": [
            {"nombre": "Juan V", "rol": "Análisis físico"},
            {"nombre": "Julián G", "rol": "Cálculo vectorial y simulaciones"},
            {"nombre": "Juan G", "rol": "Integración y visualización"},
        ]
    }
