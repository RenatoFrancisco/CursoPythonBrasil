from Cpf_cnpj import Documento

exemplo_cnpj = '35379838000112'
exemplo_cpf = '32007832062'

# print(CpfCnpj(exemplo_cnpj, 'cnpj'))
# print(CpfCnpj(exemplo_cpf, 'cpf'))

documento = Documento.cria_documento(exemplo_cnpj)
documento2 = Documento.cria_documento(exemplo_cpf)
print(documento)
print(documento2)
