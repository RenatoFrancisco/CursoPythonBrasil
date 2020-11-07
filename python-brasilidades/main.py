import re

padrao = '[0-9][a-z][0-9]'
texto = '123, 1a2 aa1'
resposta =  re.search(padrao, texto)

print(resposta.group())

