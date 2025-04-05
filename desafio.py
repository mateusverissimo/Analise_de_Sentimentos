import re
import unicodedata


palavras_positivas = {"bom", "otimo", "excelente", "maneiro", "gostei", "massa", "legal"}
palavras_negativas = {"ruim", "pessimo", "horrivel", "te doido e", "chato", "sem condicao", "jogar fora"}
indicadores_ironicos = { "só que não", "aham", "sei", "legal né", "tá bom", "imagina", "uau", "topzera", "só que ruim"}
indicadores_construtivos = { "mas", "porém", "contudo", "todavia", "seria melhor", "sugiro", "precisa melhorar", "falta"}
indicadores_intensivos = {"muito", "demais", "super", "incrivelmente", "extremamente", "totalmente", "pra caramba"}


comentarios = []

quantidade = int(input('Quantos comentários você deseja analisar? '))

for i in range(quantidade):
    
#     comentarios exemplo
#     "Esse produto é top demais!",
#     "Excelente atendimento, voltarei a comprar.",
#     "Horrível, péssimo suporte ao cliente.",
#     "Achei legal, mas poderia ser melhor.",
#     "Maneiro demais! Ótimo.",
#     "Produto estranho, mas funciona.",
#     "Serviço maravilhoso!",
#     "Simplesmente lixo. Arrependido!",
#     "Parece bom, bom pra jogar fora!"

    comentario = input(f'Digite o comentário {i + 1}: ')
    formatacao = re.sub(r'[^\w\s]', '', comentario)

    formatacao = unicodedata.normalize('NFD', formatacao)
    formatacao = formatacao.encode('ascii', 'ignore').decode('utf-8')
    
    comentarios.append(formatacao)
    print(formatacao)

    for comentario in comentarios:
     score = 0
     score_ironico = 0
     score_construtivo = 0


     palavras = comentario.lower().split()

    for palavra in palavras:
        if palavra in palavras_positivas and palavra in palavras_negativas:
            if palavra in indicadores_ironicos and palavra not in indicadores_construtivos:
               score_ironico += 1
            elif palavra in indicadores_construtivos and palavra not in indicadores_ironicos:
               score_construtivo += 1
        else:
           










        #  if palavra in palavras_positivas:
        #     score += 1
        # elif palavra in palavras_negativas:
        #     score -= 1
    
# if score == 1:
#     print(f'{comentario} -> Positivo')
# elif score >= 2:
#     print(f'{comentario} -> Muito Positivo')
# elif score == -1:
#     print(f'{comentario} -> Negativo')
# elif score <= -2:
#     print(f'{comentario} -> Muito Negativo')
# else:
#     print(f'{comentario} -> Neutro')