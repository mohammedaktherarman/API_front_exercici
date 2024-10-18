from client import db_client

def llistaAlumne(orderby: str | None = None, contain: str | None = None, skip: int = 0, limit: int | None = None):
    try:
        conn = db_client()
        cur = conn.cursor()

        values = []

        query = """ select a.NomAlumne, a.Cicle, a.Curs, a.Grup, b.DescAula from alumne a join aula b on a.IdAula = b.IdAula"""

        containExisteix = contain != None

        if containExisteix:
            query = query + " where a.NomAlumne like %s"
            containValue = f"%{contain}%"
            values.append(containValue)

        orderbyExisteix = orderby != None 

        if orderbyExisteix and orderby == "asc":
            query = query + " order by a.NomAlumne asc"
        elif orderbyExisteix and orderby == "desc":
            query = query + " order by a.NomAlumne desc"

        limitExisteix = limit != None

        if limitExisteix:
            query = query + " limit %s offset %s"
            values.append(limit)
            values.append(skip)
        else:
            if skip > 0:
                query = query + " limit 100 offset %s"  
                values.append(skip)


        values = tuple(values)
        cur.execute(query, values)
        alumnes = cur.fetchall()

    finally:
        conn.close()
    
    return alumnes

def idAlumne(id: int):
    try:
        conn = db_client()
        cur = conn.cursor()

        query = "select * from alumne where IdAlumne = %s"
        values = (id)

        cur.execute(query, values)
        alumne = cur.fetchone()

    finally:
        conn.close()

    return alumne

def actualizaAlumne(id, IdAula, NomAlumne, Cicle, Curs, Grup):
    try:
        conn = db_client()
        cur = conn.cursor()

        query = "update alumne set IdAula = %s, NomAlumne = %s, Cicle = %s, Curs = %s, Grup = %s where IdAlumne = %s"
        values = (IdAula, NomAlumne, Cicle, Curs, Grup, id)

        cur.execute(query, values)
        conn.commit()

    except Exception as e:
        return {"status": -1, "message": f"Error: {e}"}
    
    finally:
        conn.close()

    return {"status": 0, "message": "S'ha modificat correctament"}

def borrarAlumne(id):
    try:
        conn = db_client()
        cur = conn.cursor()

        query = "delete from alumne where IdAlumne = %s"
        
        values = (id)

        cur.execute(query, values)
        conn.commit()

    except Exception as e:
        return {"status": -1, "message": f"Error: {e}"}
    
    finally:
        conn.close()

    return {"status": 0, "message": "S'ha esborrat correctament"}

def llistaAlumne2():
    try:
        conn = db_client()
        cur = conn.cursor()

        query = """ select a.IdAlumne, a.IdAula, a.NomAlumne, a.Cicle, a.Curs, a.Grup, b.DescAula, b.Edifici, b.Pis from alumne a join aula b on a.IdAula = b.IdAula """

        cur.execute(query)
        alumnes = cur.fetchall()

    finally:
        conn.close()

    return alumnes




def afegirAula(DescAula: str, Edifici: str, Pis: str):
    try:
        conn = db_client()
        cur = conn.cursor()

        query = "insert into aula (DescAula, Edifici, Pis) values (%s, %s, %s)"
        values = (DescAula, Edifici, Pis)

        cur.execute(query, values)
        conn.commit()

        return cur.lastrowid
    
    except Exception as e:
        return {"status": -1, "message": f"Error: {e}"}
    
    finally:
        conn.close()


def afegirAlumne(DescAula: str, NomAlumne: str, Cicle: str, Curs: str, Grup: str):
    try:
        conn = db_client()
        cur = conn.cursor()

        query = "insert into alumne (IdAula, NomAlumne, Cicle, Curs, Grup) values ((select IdAula from aula where DescAula = %s), %s, %s, %s, %s)"
        values = (DescAula, NomAlumne, Cicle, Curs, Grup)

        cur.execute(query, values)
        conn.commit()

        return cur.lastrowid
    
    except Exception as e:
        return {"status": -1, "message": f"Error: {e}"}
    
    finally:
        conn.close()


def existeixAula(DescAula: str) -> bool:
    try:
        conn = db_client()
        cur = conn.cursor()

        query = "select count(*) from aula where DescAula = %s"
        values = (DescAula,) 

        cur.execute(query, values)
        count = cur.fetchone()[0]

        return count > 0
    
    finally:
        conn.close()


def existeixAlumne(NomAlumne: str, Cicle: str, Curs: str, Grup: str) -> bool:
    try:
        conn = db_client()
        cur = conn.cursor()

        query = """select count(*) from alumne where NomAlumne = %s and Cicle = %s and Curs = %s and Grup = %s"""
        values = (NomAlumne, Cicle, Curs, Grup)
        
        cur.execute(query, values)
        count = cur.fetchone()[0]

        return count > 0
    
    finally:
        conn.close()