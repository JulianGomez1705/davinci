from fastapi import APIRouter, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Dict, Any, List

from .. import schemas
from ..services.calculo_vectorial import clasificar_superficie_conica, calcular_valor_ecuacion

# Definición de router (asumo que está al inicio)
router = APIRouter()

# Las funciones get_calculo_vectorial_form y post_calculo_vectorial deben ser añadidas al final
# Se necesita una definición de templates, ya que no se puede importar directamente de main.py
try:
    from davinci.main import templates as templates_engine
except ImportError:
    templates_engine = Jinja2Templates(directory="templates")


@router.post("/clasificar_evaluar", response_model=Dict[str, Any], tags=["Calculo Vectorial"])
def clasificar_y_evaluar_superficie(
        ecuacion_data: schemas.EcuacionConica,
        puntos_evaluacion: List[schemas.PuntoEvaluacion]
):
    ecuacion_dict = ecuacion_data.model_dump()

    tipo_superficie = clasificar_superficie_conica(ecuacion_dict)

    resultados_evaluacion = []
    for punto in puntos_evaluacion:
        valor = calcular_valor_ecuacion(ecuacion_dict, punto.x, punto.y, punto.z)
        resultados_evaluacion.append({
            "punto": f"({punto.x}, {punto.y}, {punto.z})",
            "valor_en_ecuacion": valor,
            "esta_en_superficie": abs(valor) < 1e-6
        })

    return {
        "ecuacion_recibida": ecuacion_dict,
        "tipo_superficie": tipo_superficie,
        "evaluacion_puntos": resultados_evaluacion
    }


# **INICIO DEL CÓDIGO AÑADIDO PARA LAS VISTAS**

@router.get("/calculo_vectorial", response_class=HTMLResponse, tags=["Vistas"])
async def get_calculo_vectorial_form(request: Request):
    return templates_engine.TemplateResponse("calculo.html", {"request": request})


@router.post("/resultado_calculo", response_class=HTMLResponse, tags=["Vistas"])
async def post_calculo_vectorial(
        request: Request,
        A: float = Form(0.0), B: float = Form(0.0), C: float = Form(0.0),
        D: float = Form(0.0), E: float = Form(0.0), F: float = Form(0.0),
        G: float = Form(0.0), H: float = Form(0.0), I: float = Form(0.0),
        J: float = Form(0.0),
        punto_x: float = Form(0.0), punto_y: float = Form(0.0), punto_z: float = Form(0.0)
):
    ecuacion_data = {
        "A": A, "B": B, "C": C, "D": D, "E": E, "F": F,
        "G": G, "H": H, "I": I, "J": J
    }

    punto_data = schemas.PuntoEvaluacion(x=punto_x, y=punto_y, z=punto_z)
    puntos_evaluacion = [punto_data]

    try:
        # Llamamos a la función ya existente para el cálculo
        resultados = clasificar_y_evaluar_superficie(
            schemas.EcuacionConica(**ecuacion_data),
            puntos_evaluacion
        )

        return templates_engine.TemplateResponse("resultado.html", {"request": request, "resultados": resultados})

    except Exception as e:
        return templates_engine.TemplateResponse("error.html", {"request": request, "error_message": str(e)},
                                                 status_code=500)


