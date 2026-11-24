from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship
from configuracion import engine

Base = declarative_base()


class Clinica(Base):
    __tablename__ = "clinicas"

    id = Column(Integer, primary_key=True)
    nombre_comercial = Column(String(120), nullable=False)
    direccion = Column(String(200), nullable=False)
    veterinario_responsable = Column(String(120), nullable=False)

    consultorios = relationship(
        "Consultorio", back_populates="clinica", cascade="all, delete-orphan"
    )


class Consultorio(Base):
    __tablename__ = "consultorios"

    id = Column(Integer, primary_key=True)
    nombre_o_numero = Column(String(50), nullable=False)
    especialidad_principal = Column(String(100), nullable=False)
    clinica_id = Column(Integer, ForeignKey("clinicas.id"), nullable=False)

    clinica = relationship("Clinica", back_populates="consultorios")
    veterinarios = relationship(
        "Veterinario", back_populates="consultorio", cascade="all, delete-orphan"
    )


class Veterinario(Base):
    __tablename__ = "veterinarios"

    id = Column(Integer, primary_key=True)
    nombres = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    correo = Column(String(120), nullable=False)
    licencia_profesional = Column(String(60), nullable=False, unique=True)
    consultorio_id = Column(Integer, ForeignKey("consultorios.id"), nullable=False)

    consultorio = relationship("Consultorio", back_populates="veterinarios")
    historias_clinicas = relationship(
        "HistoriaClinica", back_populates="veterinario", cascade="all, delete-orphan"
    )


class HistoriaClinica(Base):
    __tablename__ = "historias_clinicas"

    id = Column(Integer, primary_key=True)
    fecha_atencion = Column(Date, nullable=False)
    diagnostico_principal = Column(String(250), nullable=False)
    tratamiento_prescrito = Column(String(250), nullable=False)
    nombre_mascota = Column(String(100), nullable=False)
    veterinario_id = Column(Integer, ForeignKey("veterinarios.id"), nullable=False)

    veterinario = relationship("Veterinario", back_populates="historias_clinicas")


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("Base de datos y tablas creadas con éxito.")