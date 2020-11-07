from validate_docbr import CPF
from Cpf import Cpf

# cpf = '15616987913'

# objeto_cpf = Cpf(cpf)

# print(objeto_cpf)

cpf = CPF()
print(cpf.validate('012.345.678-90'))
print(cpf.validate('11111111111'))