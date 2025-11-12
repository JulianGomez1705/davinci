from pydantic import BaseModel
from typing import Optional

class Tanque(BaseModel):
    nombre: str = "Tanque de Leonardo da Vinci"
    masa: float
    radio_rueda: float
    fuerza_motriz: float
    coeficiente_rozamiento: float

class Fuerza(BaseModel):
    tipo: str
    magnitud: float
    direccion: str

class SuperficieEntrada(BaseModel):
    tipo: str
    radio: Optional[float] = None
    altura: Optional[float] = None
    eje_mayor: Optional[float] = None
    eje_menor: Optional[float] = None

class SuperficieResultado(BaseModel):
    tipo: str
    volumen: float
    area_superficial: float
    cortes_ejes: dict

