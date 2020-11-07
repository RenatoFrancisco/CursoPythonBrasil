from validate_docbr import CPF, CNPJ

class Documento:

    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)

        return DocCnpj(documento)

class DocCpf:

    def __init__(self, documento):
        documento = str(documento)
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError('CPF inválido!')

    def __str__(self):
        return self.format_cpf()

    def valida(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        raise ValueError('Quantidade de dígitos inválida')
    
    def format_cpf(self):
        marcara = CPF()
        return marcara.mask(self.cpf)

class DocCnpj:
    def __init__(self, documento):
        documento = str(documento)
        if self.valida(documento):
            self.cnpj =  documento
        else:
            raise ValueError('CNPJ inválido!')

    def __str__(self):
        return self.format_cnpj()

    def valida(self, cnpj):
        if len(cnpj) == 14:
            validador = CNPJ()
            return validador.validate(cnpj)
        raise ValueError('Quantidade de dígitos inválidas')

    def format_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
