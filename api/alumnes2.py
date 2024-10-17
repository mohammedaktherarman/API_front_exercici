def alumne_schema2(alumne) -> dict:
    return {
        "IdAlumne": alumne[0],
        "IdAula": alumne[1],
        "NomAlumne": alumne[2],
        "Cicle": alumne[3],
        "Curs": alumne[4],
        "Grup": alumne[5],
        "DescAula": alumne[6],
        "edifici": alumne[7],
        "pis": alumne[8]
    }

def alumnes_schema2(alumnes) -> list:
    return [alumne_schema2(alumne) for alumne in alumnes]
