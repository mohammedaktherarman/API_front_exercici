def alumne_schema(alumne) -> dict:
    return {
        "NomAlumne": alumne[0],
        "Cicle": alumne[1],
        "Curs": alumne[2],
        "Grup": alumne[3],
        "DescAula": alumne[4]
    }

def alumnes_schema(alumnes) -> list:
    return [alumne_schema(alumne) for alumne in alumnes]
