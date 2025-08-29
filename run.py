from infra.repository.pessoas_repository import PessoasRepository

repo = PessoasRepository()

data = repo.select()

print(data)