from datetime import date
from sqlalchemy import and_, select
from configuracion import SessionLocal
from crear_base_entidades import Consultorio, HistoriaClinica

session = SessionLocal()

try:
    print("=== CONSULTORIO 'Consultorio 101' DE LA CLÍNICA ID 1 ===")
    consultorio_and = session.execute(
        select(Consultorio).where(
            and_(
                Consultorio.nombre_o_numero == "Consultorio 101",
                Consultorio.clinica_id == 1,
            )
        )
    ).scalars().all()
    for cons in consultorio_and:
        print(f"ID: {cons.id} | {cons.nombre_o_numero} | Especialidad: {cons.especialidad_principal}")

    print("\n=== HISTORIAS CLÍNICAS DESDE '2026-11-12' ASIGNADAS AL VETERINARIO ID 1 ===")
    historias_and = session.execute(
        select(HistoriaClinica).where(
            and_(
                HistoriaClinica.fecha_atencion >= date(2026, 11, 12),
                HistoriaClinica.veterinario_id == 1,
            )
        )
    ).scalars().all()
    for h in historias_and:
        print(f"{h.fecha_atencion} | Mascota: {h.nombre_mascota} | Vet ID: {h.veterinario_id} | Diagnóstico: {h.diagnostico_principal}")
finally:
    session.close()