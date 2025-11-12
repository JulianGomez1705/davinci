from fastapi import APIRouter, HTTPException
import math
from models import SuperficieEntrada, SuperficieResultado

router = APIRouter()

@router.post("/superficie", response_model=SuperficieResultado)
async def calcular_superficie(datos: SuperficieEntrada):
    tipo = datos.tipo.lower()

    if tipo == "esfera":
        if datos.radio is None:
            raise HTTPException(status_code=400, detail="Se requiere el radio para la esfera")
        volumen = (4/3) * math.pi * datos.radio**3
        area = 4 * math.pi * datos.radio**2
        cortes = {"x": datos.radio, "y": datos.radio, "z": datos.radio}

    elif tipo == "cono":
        if datos.radio is None or datos.altura is None:
            raise HTTPException(status_code=400, detail="Se requieren radio y altura para el cono")
        volumen = (1/3) * math.pi * datos.radio**2 * datos.altura
        generatriz = math.sqrt(datos.radio**2 + datos.altura**2)
        area = math.pi * datos.radio * (datos.radio + generatriz)
        cortes = {"x": datos.radio, "y": datos.radio, "z": datos.altura}

    elif tipo == "cilindro":
        if datos.radio is None or datos.altura is None:
            raise HTTPException(status_code=400, detail="Se requieren radio y altura para el cilindro")
        volumen = math.pi * datos.radio**2 * datos.altura
        area = 2 * math.pi * datos.radio * (datos.radio + datos.altura)
        cortes = {"x": datos.radio, "y": datos.radio, "z": datos.altura}

    elif tipo == "elipsoide":
        if datos.eje_mayor is None or datos.eje_menor is None or datos.altura is None:
            raise HTTPException(status_code=400, detail="Se requieren eje_mayor, eje_menor y altura para el elipsoide")
        volumen = (4/3) * math.pi * datos.eje_mayor * datos.eje_menor * datos.altura
        p = 1.6
        area = 4 * math.pi * (((datos.eje_mayor**p * datos.eje_menor**p) +
                               (datos.eje_mayor**p * datos.altura**p) +
                               (datos.eje_menor**p * datos.altura**p)) / 3) ** (1/p)
        cortes = {"x": datos.eje_mayor, "y": datos.eje_menor, "z": datos.altura}

    elif tipo == "paraboloide":
        if datos.radio is None or datos.altura is None:
            raise HTTPException(status_code=400, detail="Se requieren radio y altura para el paraboloide")
        volumen = (1/2) * math.pi * datos.radio**2 * datos.altura
        area = math.pi * datos.radio * (math.sqrt(datos.radio**2 + 4 * datos.altura**2) / 2 + datos.altura)
        cortes = {"x": datos.radio, "y": datos.radio, "z": datos.altura}

    else:
        raise HTTPException(status_code=400, detail="Tipo de superficie no reconocido")

    return SuperficieResultado(
        tipo=tipo,
        volumen=round(volumen, 3),
        area_superficial=round(area, 3),
        cortes_ejes=cortes
    )
