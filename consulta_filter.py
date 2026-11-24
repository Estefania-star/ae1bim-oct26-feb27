from sqlalchemy import select
from configuracion import SessionLocal
from crear_base_entidades import Veterinario, HistoriaClinica

session = SessionLocal()

try:
    print("=== VETERINARIOS CON LICENCIA QUE EMPIEZA POR 'VET-2021' ===")
    vets_2021 = session.execute(
        select(Veterinario).where(Veterinario.licencia_profesional.like("VET-2021%"))
    ).scalars().all()
    for v in vets_2021:
        print(f"{v.nombres} {v.apellidos} - Licencia: {v.licencia_profesional}")

    print("\n=== HISTORIAS CLÍNICAS DE LA MASCOTA 'Luna' ===")
    historias_luna = session.execute(
        select(HistoriaClinica).where(HistoriaClinica.nombre_mascota == "Luna")
    ).scalars().all()
    for h in historias_luna:
        print(f"Mascota: {h.nombre_mascota} | Diagnóstico: {h.diagnostico_principal} | Tratamiento: {h.tratamiento_prescrito}")
finally:
    session.close()