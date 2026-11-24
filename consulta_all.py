from sqlalchemy import select
from configuracion import SessionLocal
from crear_base_entidades import Clinica, Consultorio, Veterinario, HistoriaClinica

session = SessionLocal()

try:
    print("=== TODAS LAS CLÍNICAS ===")
    clinicas = session.execute(select(Clinica)).scalars().all()
    for c in clinicas:
        print(f"ID: {c.id} | Nombre: {c.nombre_comercial} | Responsable: {c.veterinario_responsable}")

    print("\n=== TODOS LOS CONSULTORIOS ===")
    consultorios = session.execute(select(Consultorio)).scalars().all()
    for cons in consultorios:
        print(f"ID: {cons.id} | {cons.nombre_o_numero} | Especialidad: {cons.especialidad_principal} | Clínica ID: {cons.clinica_id}")

    print("\n=== TODOS LOS VETERINARIOS ===")
    veterinarios = session.execute(select(Veterinario)).scalars().all()
    for v in veterinarios:
        print(f"ID: {v.id} | {v.nombres} {v.apellidos} | Licencia: {v.licencia_profesional} | Correo: {v.correo}")

    print("\n=== TODAS LAS HISTORIAS CLÍNICAS ===")
    historias = session.execute(select(HistoriaClinica)).scalars().all()
    for h in historias:
        print(f"ID: {h.id} | Mascota: {h.nombre_mascota} | Fecha: {h.fecha_atencion} | Diagnóstico: {h.diagnostico_principal}")
finally:
    session.close()