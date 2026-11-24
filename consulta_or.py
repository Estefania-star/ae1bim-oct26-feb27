from sqlalchemy import or_, select
from configuracion import SessionLocal
from crear_base_entidades import Consultorio, HistoriaClinica

session = SessionLocal()

try:
    print("=== CONSULTORIOS DE MEDICINA GENERAL O DERMATOLOGÍA ===")
    consultorios_or = session.execute(
        select(Consultorio).where(
            or_(
                Consultorio.especialidad_principal == "Medicina General",
                Consultorio.especialidad_principal == "Dermatología y Vacunación",
            )
        )
    ).scalars().all()
    for cons in consultorios_or:
        print(f"{cons.nombre_o_numero} | Especialidad: {cons.especialidad_principal}")

    print("\n=== HISTORIAS CLÍNICAS DE 'Max' O 'Rocky' ===")
    historias_or = session.execute(
        select(HistoriaClinica).where(
            or_(
                HistoriaClinica.nombre_mascota == "Max",
                HistoriaClinica.nombre_mascota == "Rocky",
            )
        )
    ).scalars().all()
    for h in historias_or:
        print(f"Mascota: {h.nombre_mascota} | Diagnóstico: {h.diagnostico_principal}")
finally:
    session.close()