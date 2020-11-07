from validate_docbr import CPF, CNPJ

class CpfCnpj:

    def __init__(self, documento, tipo_documento):
        documento = str(documento)
        self.tipo_documento =  tipo_documento

        if self.tipo_documento == 'cpf':
            if self.cpf_eh_valido(documento):
                self.cpf = documento
            else:
                raise ValueError('CPF inválido!')
        elif self.tipo_documento == 'cnpj':
            if self.cnpj_eh_valido(documento):
                self.cnpj =  documento
            else:
                raise ValueError('CNPJ inválido!')
        else:
            raise ValueError('Documento inválido!')

    def __str__(self):
        if self.tipo_documento == 'cpf':
            return self.format_cpf()
        return self.format_cnpj()

    def cpf_eh_valido(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        raise ValueError('Quantidade de dígitos inválida')
    
    def cnpj_eh_valido(self, cnpj):
        if len(cnpj) == 14:
            validador = CNPJ()
            return validador.validate(cnpj)
        raise ValueError('Quantidade de dígitos inválidas')

    def format_cpf(self):
        marcara = CPF()
        return marcara.mask(self.cpf)

    def format_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)