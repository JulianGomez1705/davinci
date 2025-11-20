from fastapi import APIRouter, HTTPException
from typing import Dict, Any, List

# CORRECCIÓN CLAVE: Usamos la importación ABSOLUTA desde el paquete raíz 'davinci'
# Esto requiere que hayas creado el archivo davinci/__init__.py
from davinci import schemas
from davinci.services.calculo_vectorial import clasificar_superficie_conica, calcular_valor_ecuacion

router = APIRouter()


@router.post("/clasificar_evaluar", response_model=Dict[str, Any], tags=["Calculo Vectorial"])
def clasificar_y_evaluar_superficie(
        # USAMOS EL PREFIJO 'schemas.' para referenciar los modelos Pydantic
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