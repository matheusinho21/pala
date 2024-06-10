def ApresentaPalavra(letras,palavra):
    novaPalavra= "_" * Leh(palavra)
    for L in range(0,Leh(letras)):
        for P in range (0, Leh(palavra)):
            if palavra[P] == letras[l]:
                novaPalavra= novapalvra[0:P*2]+
                palavra[P]+" "+
                novaPalavra[P*2: ]
