from docx import Document
from docx.shared import Pt

# Criação do documento
doc = Document()

# Título do documento
doc.add_heading('Relatório de Dimensionamento do Sistema de Água Fria', 0)

# Adicionando o conteúdo com formatação
textoaf = """
Objetivo  
O objetivo deste relatório é apresentar o dimensionamento do sistema de água fria para a edificação, considerando as necessidades de vazão, as características das tubulações e os requisitos de pressão, em conformidade com as normas brasileiras vigentes.

Normas Técnicas  
O dimensionamento foi realizado com base nas seguintes normas brasileiras:

- NBR 5626:1998 – Instalação Predial de Água Fria
- NBR 11988:1993 – Rede de Distribuição Predial de Água Fria
- NBR 7198:1993 – Projeto de Instalações Hidrossanitárias
- NBR 13209:1994 – Tubos e Conexões de PVC para Água Fria

Essas normas foram utilizadas para garantir que o projeto atenda a todos os requisitos técnicos e de segurança necessários para a instalação de um sistema eficiente e sustentável de distribuição de água fria.

Metodologia de Cálculo  
O cálculo do sistema de água fria foi realizado com base nas vazões estimadas para cada ponto de consumo, levando em consideração o tipo de uso e as dimensões da edificação. Para o cálculo da perda de carga nas tubulações, utilizou-se o método de equações empíricas presentes na NBR 7198:1993, considerando o tipo de material das tubulações e o layout do sistema.

Resultados Obtidos  
O dimensionamento das tubulações foi feito considerando os seguintes parâmetros:

1. Vazão: As vazões foram determinadas com base no número de pontos de consumo e na necessidade de abastecimento de água para as diversas áreas da edificação.
2. Tubulações: Foram selecionadas tubulações de PVC conforme as especificações da NBR 13209:1994, que asseguram resistência, durabilidade e compatibilidade com o tipo de água fornecida.
3. Perda de Carga: A perda de carga foi calculada considerando o comprimento total das tubulações, o tipo de material utilizado e o número de conexões, de acordo com os métodos da NBR 7198:1993.
4. Pressão: A pressão mínima e máxima de operação foi verificada, garantindo que todas as extremidades do sistema recebam a pressão adequada para o bom funcionamento das instalações.

Conclusão  
O sistema de água fria projetado atende integralmente às exigências das normas NBR 5626:1998, NBR 11988:1993, NBR 7198:1993 e NBR 13209:1994, garantindo uma distribuição eficiente e segura de água para os usuários da edificação. O dimensionamento das tubulações e o cálculo da perda de carga asseguram que o sistema funcionará de maneira otimizada, minimizando desperdícios e assegurando a longevidade do sistema hidráulico.

Com o dimensionamento realizado, o projeto está pronto para ser executado, atendendo às normas de segurança e eficiência, além de garantir o conforto e a sustentabilidade do abastecimento de água fria.
"""

# Adicionando o texto ao documento com formatação de fonte
for par in textoaf.split("\n\n"):
    p = doc.add_paragraph(par)
    run = p.runs[0]
    run.font.name = 'Arial'  # Fonte Arial
    run.font.size = Pt(12)   # Tamanho da fonte 12

# Salvando o documento
doc.save("relatorio_agua_fria.docx")


print(textoaf)