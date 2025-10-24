from pydantic import BaseModel

class Tank(BaseModel):
    nombre: str = "Tanque de Leonardo da Vinci"
    masa: float  # en kg
    radio_rueda: float  # en metros
    fuerza_motriz: float  # en N
    coeficiente_rozamiento: float  # sin unidad

class Force(BaseModel):
    tipo: str
    magnitud: float
    direccion: str
