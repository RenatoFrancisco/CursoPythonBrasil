import requests
from acesso_cep import BuscaEndereco

cep = 25870145
objeto_cep = BuscaEndereco(cep)

print(objeto_cep.acessa_via_cep())