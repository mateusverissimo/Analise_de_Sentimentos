import string

palavras_positivas = {"bom", "ótimo", "excelente", "maneiro", "gostei", "massa", "legal"}
palavras_negativas = {"ruim", "péssimo", "horrível", "te doido é", "chato", "sem condição", "jogar fora"}

comentarios = []

quantidade = int(input('Quantos comentários você deseja analisar?'))

for i in range(quantidade):
    comentario = input(f'Digite o comentário {i + 1}: ')
    comentarios.append(comentario)

for comentario in comentarios:
    score = 0
    palavras = comentario.lower().split()
    
    palavras = [palavra.strip(string.punctuation) for palavra in palavras]

    for palavra in palavras:
        if palavra in palavras_positivas:
            score += 1
        elif palavra in palavras_negativas:
            score -= 1
    
    if score == 1:
        print(f'{comentario} -> Positivo')
    elif score >= 2:
        print(f'{comentario} -> Muito Positivo')
    elif score == -1:
        print(f'{comentario} -> Negativo')
    elif score <= -2:
        print(f'{comentario} -> Muito Negativo')
    else:
        print(f'{comentario} -> Neutro')


