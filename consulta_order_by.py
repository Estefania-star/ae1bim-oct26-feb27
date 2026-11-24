from sqlalchemy import select
from configuracion import SessionLocal
from crear_base_entidades import Clinica, HistoriaClinica

session = SessionLocal()

try:
    print("=== CLÍNICAS ORDENADAS POR NOMBRE COMERCIAL (A-Z) ===")
    clinicas_ordenadas = session.execute(
        select(Clinica).order_by(Clinica.nombre_comercial.asc())
    ).scalars().all()
    for c in clinicas_ordenadas:
        print(f"{c.nombre_comercial} - {c.direccion}")

    print("\n=== HISTORIAS CLÍNICAS ORDENADAS POR FECHA DE ATENCIÓN (RECIENTES PRIMERO) ===")
    historias_ordenadas = session.execute(
        select(HistoriaClinica).order_by(HistoriaClinica.fecha_atencion.desc())
    ).scalars().all()
    for h in historias_ordenadas:
        print(f"{h.fecha_atencion} | Mascota: {h.nombre_mascota} | Diagnóstico: {h.diagnostico_principal}")
finally:
    session.close()