from infra.configs.base import Base
from sqlalchemy import Column, String, Integer

class Pessoas(Base):
    __tablename__ = "pessoas"

    cpf = Column(String, primary_key=True)
    nome = Column(String, nullable=False)
    telefone = Column(String, nullable=False)
    
    def __repr__(self):
        return f"Paciente (nome = {self.nome}, cpf = {self.cpf})"
