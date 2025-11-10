from fastapi import APIRouter

router = APIRouter(prefix="/project", tags=["Proyecto"])

@router.get("/")
def get_project_info():
    return {
        "titulo": "Tanque de Guerra de Leonardo da Vinci",
        "descripcion": "Análisis físico y matemático del tanque de guerra diseñado por Leonardo da Vinci.",
        "materias_relacionadas": ["Física 2", "Cálculo Vectorial"],
        "objetivos": [
            "Analizar el diseño y movimiento del tanque",
            "Simular fuerzas aplicadas y energía requerida"
        ]
    }
