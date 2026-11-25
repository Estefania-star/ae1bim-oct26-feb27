from sqlalchemy import select
from configuracion import SessionLocal
from crear_base_entidades import (
    Clinica,
    Consultorio,
    Veterinario,
    HistoriaClinica,
)

session = SessionLocal()

try:
    print("=== CLÍNICAS Y NÚMERO DE HISTORIAS CLÍNICAS ASOCIADAS ===")
    clinicas = session.execute(select(Clinica)).scalars().all()
    historias = session.execute(select(HistoriaClinica)).scalars().all()

    for c in clinicas:
        # Obtenemos los IDs de consultorios de esta clínica
        ids_consultorios = [
            cons.id for cons in c.consultorios
        ] if hasattr(c, "consultorios") else []

        # Si no tienes relationship configurada en el modelo, consultamos directo:
        if not ids_consultorios:
            consultorios_clinica = session.execute(
                select(Consultorio).where(Consultorio.clinica_id == c.id)
            ).scalars().all()
            ids_consultorios = [cons.id for cons in consultorios_clinica]

        veterinarios_clinica = session.execute(
            select(Veterinario).where(Veterinario.consultorio_id.in_(ids_consultorios))
        ).scalars().all() if ids_consultorios else []
        ids_veterinarios = [v.id for v in veterinarios_clinica]

        total_historias = sum(
            1 for h in historias if h.veterinario_id in ids_veterinarios
        )

        print(
            f"Clínica: {c.nombre_comercial} | Responsable: {c.veterinario_responsable} | "
            f"Historias clínicas asociadas: {total_historias}"
        )

    print("\n=== TODOS LOS CONSULTORIOS ===")
    consultorios = session.execute(select(Consultorio)).scalars().all()
    for cons in consultorios:
        print(
            f"ID: {cons.id} | {cons.nombre_o_numero} | "
            f"Especialidad: {cons.especialidad_principal} | Clínica ID: {cons.clinica_id}"
        )

    print("\n=== TODOS LOS VETERINARIOS ===")
    veterinarios = session.execute(select(Veterinario)).scalars().all()
    for v in veterinarios:
        print(
            f"ID: {v.id} | {v.nombres} {v.apellidos} | "
            f"Licencia: {v.licencia_profesional} | Correo: {v.correo}"
        )

    print("\n=== TODAS LAS HISTORIAS CLÍNICAS ===")
    for h in historias:
        print(
            f"ID: {h.id} | Mascota: {h.nombre_mascota} | "
            f"Fecha: {h.fecha_atencion} | Diagnóstico: {h.diagnostico_principal}"
        )
finally:
    session.close()