from infra.configs.connection import DBConnectionHandlerS
from infra.entities.pessoas import Pessoas

class PessoasRepository:
    def select(self):
        with DBConnectionHandlerS() as db:
            data = db.session.query(Pessoas).all()
            return data
    
    def insert(self, cpf, nome, telefone):
        with DBConnectionHandlerS() as db:
            data_insert = Pessoas(nome = nome,
                                  cpf = cpf,
                                  telefone = telefone)
            db.session.add(data_insert)
            return data_insert
        
    def delete_by_nome(self, nome):
        with DBConnectionHandlerS() as db:
            db.session.query(Pessoas).filter(Pessoas.nome==nome).delete()

    def update_telefone_by_nome(self, nome, telefone):
        with DBConnectionHandlerS() as db:
            db.session.query(Pessoas).filter(Pessoas.nome==nome).update({"telefone": telefone})