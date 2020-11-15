import requests
from acesso_cep import BuscaEndereco

cep = '25800320'
objeto_cep = BuscaEndereco(cep)

bairro, localidade, uf = objeto_cep.acessa_via_cep()
print(bairro, localidade, uf)