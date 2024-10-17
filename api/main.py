from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from db_alumne import (llistaAlumne,idAlumne,afegirAlumne,existeixAula,actualizaAlumne,borrarAlumne,llistaAlumne2)
from alumnes import alumnes_schema, alumne_schema
from alumnes2 import alumnes_schema2

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class tablaAlumne(BaseModel):
    NomAlumne: str
    Cicle: str
    Curs: str
    Grup: str
    DescAula: str

@app.get("/alumne/list", response_model=List[tablaAlumne])
def llista():
    alumnes = llistaAlumne()
    return alumnes_schema(alumnes)

@app.get("/alumne/", response_model=List[tablaAlumne])
def llistaParametres(orderby: str | None = None,contain: str | None = None,skip: int = 0,limit: int | None = None,):

    alumnes = llistaAlumne(orderby=orderby, contain=contain, skip=skip, limit=limit)
    return alumnes_schema(alumnes)

@app.get("/alumne/show/{id}", response_model=dict)
def mostra(id: int):
    alumne = idAlumne(id)
    if alumne is None:
        return {"message": "El alumne no existeix"}
    return alumne_schema(alumne)

class Alumne(BaseModel):
    IdAula: int
    NomAlumne: str
    Cicle: str
    Curs: str
    Grup: str

@app.post("/alumne/add", response_model=dict)
def afegir(alumne: Alumne):
    if not existeixAula(alumne.IdAula):
        raise HTTPException(status_code=400, detail="IdAula no existeix.")
    id = afegirAlumne(alumne.IdAula, alumne.NomAlumne, alumne.Cicle, alumne.Curs, alumne.Grup)
    return {"message": "S'ha afegit correctament", "IdAlumne": id}

class AlumneUpdate(BaseModel):
    IdAula: int
    NomAlumne: str
    Cicle: str
    Curs: str
    Grup: str

@app.put("/alumne/update/{id}", response_model=dict)
def actualizar(id: int, alumne: AlumneUpdate):
    result = actualizaAlumne(id, alumne.IdAula, alumne.NomAlumne, alumne.Cicle, alumne.Curs, alumne.Grup)
    return result

@app.delete("/alumne/delete/{id}", response_model=dict)
def borrar(id: int):
    result = borrarAlumne(id)
    return result

@app.get("/alumne/listAll", response_model=list)
def llistaTot():
    alumnes = llistaAlumne2()
    return alumnes_schema2(alumnes)
