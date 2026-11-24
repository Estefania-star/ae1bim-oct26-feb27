from datetime import date
from configuracion import SessionLocal
from crear_base_entidades import Clinica, Consultorio, Veterinario, HistoriaClinica

session = SessionLocal()

try:
    # 1. Clínicas
    clinica_1 = Clinica(
        nombre_comercial="VetVida Centro",
        direccion="Av. Principal 102 y Calle Norte",
        veterinario_responsable="Dra. Valeria Mendoza",
    )
    clinica_2 = Clinica(
        nombre_comercial="Huellas del Sur",
        direccion="Av. del Pacífico Km 3",
        veterinario_responsable="Dr. Andrés Cedeño",
    )
    session.add_all([clinica_1, clinica_2])
    session.flush()

    # 2. Consultorios
    cons_1 = Consultorio(
        nombre_o_numero="Consultorio 101",
        especialidad_principal="Medicina General",
        clinica_id=clinica_1.id,
    )
    cons_2 = Consultorio(
        nombre_o_numero="Consultorio 102",
        especialidad_principal="Cirugía y Traumatología",
        clinica_id=clinica_1.id,
    )
    cons_3 = Consultorio(
        nombre_o_numero="Consultorio A",
        especialidad_principal="Dermatología y Vacunación",
        clinica_id=clinica_2.id,
    )
    session.add_all([cons_1, cons_2, cons_3])
    session.flush()

    # 3. Veterinarios
    vet_1 = Veterinario(
        nombres="Camila Sofía",
        apellidos="Rojas Paredes",
        correo="camila.rojas@vetvida.com",
        licencia_profesional="VET-2021-001",
        consultorio_id=cons_1.id,
    )
    vet_2 = Veterinario(
        nombres="Mateo Alejandro",
        apellidos="Zambrano Vera",
        correo="mateo.zambrano@vetvida.com",
        licencia_profesional="VET-2020-045",
        consultorio_id=cons_2.id,
    )
    vet_3 = Veterinario(
        nombres="Lucía Fernanda",
        apellidos="Salazar Ortiz",
        correo="lucia.salazar@huellassur.com",
        licencia_profesional="VET-2022-089",
        consultorio_id=cons_3.id,
    )
    session.add_all([vet_1, vet_2, vet_3])
    session.flush()

    # 4. Historias Clínicas
    historias = [
        HistoriaClinica(
            fecha_atencion=date(2026, 11, 10),
            diagnostico_principal="Gastroenteritis leve",
            tratamiento_prescrito="Dieta blanda por 5 días y probióticos",
            nombre_mascota="Max",
            veterinario_id=vet_1.id,
        ),
        HistoriaClinica(
            fecha_atencion=date(2026, 11, 12),
            diagnostico_principal="Fractura en pata delantera derecha",
            tratamiento_prescrito="Inmovilización con férula y analgésicos",
            nombre_mascota="Luna",
            veterinario_id=vet_2.id,
        ),
        HistoriaClinica(
            fecha_atencion=date(2026, 11, 15),
            diagnostico_principal="Dermatitis alérgica por pulgas",
            tratamiento_prescrito="Antiparasitario tópico y baño medicado",
            nombre_mascota="Rocky",
            veterinario_id=vet_3.id,
        ),
        HistoriaClinica(
            fecha_atencion=date(2026, 11, 18),
            diagnostico_principal="Control anual y refuerzo de vacuna séxtuple",
            tratamiento_prescrito="Aplicación de vacuna y desparasitación interna",
            nombre_mascota="Nala",
            veterinario_id=vet_1.id,
        ),
    ]
    session.add_all(historias)
    session.commit()
    print("Datos insertados correctamente en la base de datos.")

except Exception as e:
    session.rollback()
    print("Error al poblar la base de datos:", e)
finally:
    session.close()