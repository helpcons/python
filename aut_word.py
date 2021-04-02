from docxtpl import DocxTemplate
import jinja2
import pandas as pd

# Carregando o template para auto preenchimento
'''
# Testando o código
doc = DocxTemplate('notas_template.docx')
contexto = {
    'rs_rj' : 'Rio de Janeiro'
}
doc.render(contexto)
doc.save('notas_saida1.docx')
'''
# 1 - Carregando as variável do excel
notas_dados = pd.read_excel('dados_estados.xlsx')

# 2 - Criando o dicionário de contexto
contexto = dict(zip(notas_dados['var'], notas_dados['valor']))
# Pareando os valores da lista 'var' com 'valor' com a função zip()
# Transformando em um dicionário dict()
# Não sei porque mas tive que instalar as libs xlrd e openpyxl para que o pandas pudesse lê meu dicionário.
#print(contexto)

# 3 - Salvando as informações do dicionário em um novo arquivo docx
doc = DocxTemplate('notas_template.docx')
doc.render(contexto)
doc.save('notas_saida2.docx')