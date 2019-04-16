#Pedro Rodrigues, n90531

def eh_tabuleiro(t):
    '''Funcao eh_tabuleiro: universal -> booleano

    A funcao "eh_tabuleiro" recebe qualquer argumento e devolve True se o argumento for um tabuleiro, isto e,
se for um tuplo composto por 3 tuplos, onde os elementos de cada tuplo sao apenas -1, 0 ou 1 e que
os dois primeiros tem 3 elementos cada um e o ultimo tem apenas 2 elementos. Caso contrario, devolve False.'''
    
    if isinstance(t,tuple) and len(t) == 3 and isinstance(t[0] and t[1] and t[2],tuple) and len(t[0]) == len(t[1])== 3 and len(t[2])==2:
        
        for i in range(len(t)):       # Para otimizar, se encontrar um elemento dentro de t 
            for j in t[i]:            # que nao pertenca ao tuplo "estados", devolve
                if j not in (-1,0,1): # logo "false", nao precisando de percorrer
                    return False      # o tuplo todo, se nao for necessario                      
        return True
        
    else:
        return False

def tabuleiro_str(tuplo):
    '''Funcao tabuleiro_str: tabuleiro -> cad.caracteres

    A funcao "tabuleiro_str" recebe um tabuleiro e devolve a cadeia de caracteres que o representa, numa perpestiva de
45 graus.
    Se o argumento dado nao for um tabuleiro, a função gera um erro com a mensagem "tabuleiro_str: argumento invalido"'''
    
    def novo_tabuleiro():
        '''Funcao novo_tabuleiro: sem argumentos -> cad.caracteres
        
        A funcao novo_tabuleiro nao recebe argumentos e devolve uma cadeia de caracteres que representa uma versao "default"
(todas as posicoes sao x) de um tabuleiro de jogo'''
        
        return '+-------+\n|...x...|\n|..x.x..|\n|.x.x.x.|\n|..x.x..|\n+-------+'
    
    def transf_str_lista(tabuleiro_str):
        '''Funcao transf_str_lista: cad.caracteres -> lista
        
        A funcao transf_str_lista recebe uma cadeia de caracteres correpsondente a uma representacao se um tabuleiro
e devolve a lista com os elementos da cad.caracteres, separados individualmente'''
        list_tab=[]    
        for els in tabuleiro_str:
            list_tab = list_tab + [els]
        return list_tab
    
    def constroi_str(lista):
        '''Funcao constroi_str: lista -> cad.caracteres
        
        A funcao constroi_str recebe uma lista, em que os seus elementos sao todos caracteres, e devolve a cad. de caracteres
resultante de todos caracteres da lista juntos '''
        tabuleiro_str = ''                          # Como o tabuleiro tem uma rotacao de 45graus, decidi percorrer o tuplo
        for els in lista:                           # desde a ultima posicao [-1] ate a primeira posicao [-len(tuplo)]. 
            tabuleiro_str = tabuleiro_str + els     # Cada "estado" dos qubits no tabuleiro estao a distancia de 9 posicoes
        return tabuleiro_str                        # do proximo estado no tuplo.Por exemplo, quando se chega ao final de
                                                    # tuplo_inicial[0], a nossa ultima posicao analisada da lista foi
    if eh_tabuleiro(tuplo):                         # list_tab[32] e a posicao seguinte que queremos analisar e list_tab[25]
        tabuleiro= novo_tabuleiro()                 # 32-25=7 e isto repete-se.
# Posicao do tabuleiro onde aparece o primeiro "x"   
        pos=14                                      # Devido a instrucao "pos += 9", quando o ciclo for acaba, o valor         
        list_tab = transf_str_lista(tabuleiro)      # de "pos" tem 9 unidades a mais que o desejado.
                                                    # Como explicado acima, a proxima posicao a analisar esta 7 posicoes
        for els in tuplo:                           # atras da ultima analisada, mas como "pos" tem +9 valores que a posicao
            for i in range(1,len(els)+1):           # da ultima posicao analisada, subtraimos 9+7=16
                if els[-i] != -1:                    
                    list_tab[pos]= str(els[-i])
                pos= pos + 9
            pos= pos - 16                            
        return constroi_str(list_tab)                
                                                     
                                                     
    else:                                            
        raise ValueError("tabuleiro_str: argumento invalido") 
        
def tabuleiros_iguais(t1,t2):
    '''Funcao tabuleiros_iguais: tabuleiro x tabuleiro -> booleano
    
    A funcao tabuleiros_iguais recebe dois tabuleiros e devolve True se estes forem iguais. Caso contrario devolve False.
    Se algum dos argumentos dados nao for um tabuleiro, gera um erro com a mensagem "tabuleiros_iguais: um dos argumentos
nao e tabuleiro"'''
    
    if eh_tabuleiro(t1) and eh_tabuleiro(t2):
        return t1==t2
    
    else:
        raise ValueError("tabuleiros_iguais: um dos argumentos nao e tabuleiro")
        
def transf_tuplo_lista(tuplo):
    '''Funcao transf_tuplo_lista: tuplo -> lista

    A funcao transf_tuplo_lista recebe um tuplo e devolve uma lista com exatamente os mesmos elementos do tuplo inicial'''
    
    lst = []
    for el in tuplo:
        lst += [list(el)]
    return lst
        
def porta_x(tuplo, lado):
    ''' Funcao porta_x: tabuleiro x {"E", "D"} -> tabuleiro
    
    A funcao porta_x recebe um tabuleiro e um caracter ('E' ou 'D') e devolve o tabuleiro correspondente a altertar os 
estados dos QuBits da parte parte inferior do tabuleiro (de 1 para 0 e vice-versa, em caso de ser -1 mantem-se o estado)
do lado indicado no segundo argumento. Caso um dos argumentos nao seja valido, isto e, o primeiro nao ser um tabuleiro
ou o segundo nao ser um dos caracteres apresentados acima, gera um erro com a mensagem "porta_x: um dos argumentos e
invalido"'''
    
    if eh_tabuleiro(tuplo) and lado in ('E', 'D'):
        lst = transf_tuplo_lista(tuplo)
            
        if lado == 'E':
            for elemento in range(len(lst[1])):                    # Como queremos mudar os estados de 1 para 0 e vice-versa, 
                if lst[1][elemento] in (0,1):                      # quando o estado for 0, abs(0-1) = 1 e quando for 1, 
                    lst[1][elemento] = abs(lst[1][elemento] - 1)   # abs(1-1) = 0       
        else:
            for elemento in range(len(lst)):                       # De modo a evitar uma condicao extra para
                if lst[elemento][-2] in (0,1):                     # lista_nova[2], que so tem 2 elementos,
                    lst[elemento][-2] = abs(lst[elemento][-2] - 1) # decidi que fica mais facil se considerarmos
                                                                   # as posicoes na lista por [-3, -2, -1]
        return tuple(lst[0]),tuple(lst[1]), tuple(lst[2])
    
    else:
        raise ValueError("porta_x: um dos argumentos e invalido")
        
def porta_z(tuplo, lado):
    '''Funcao porta_z: tabuleiro x {"E", "D"} -> tabuleiro
    
    A funcao porta_z recebe um tabuleiro e um caracter ('E' ou 'D') e devolve o tabuleiro correspondente a altertar os 
estados dos QuBits da parte parte superior do tabuleiro (de 1 para 0 e vice-versa, em caso de ser -1 mantem-se o estado)do 
lado indicado no segundo argumento. 
    Caso um dos argumentos nao seja valido, isto e, o primeiro nao ser um tabuleiro ou o segundo nao ser um dos caracteres 
apresentados acima, gera um erro com a mensagem "porta_z: um dos argumentos e invalido"'''
    
    if eh_tabuleiro(tuplo) and (lado == 'E' or lado == 'D'):
        lst = transf_tuplo_lista(tuplo)
        
        if lado == 'E':                             # O raciocinio utilizado na funcao porta_z e ao da funcao porta_x
            for elemento in range(len(lst[0])):
                if lst[0][elemento] in (0,1):
                    lst[0][elemento] = abs(lst[0][elemento] - 1)
                    
        else:
            for elemento in range(len(lst)):
                if lst[elemento][-1] in (0,1):
                    lst[elemento][-1] = abs(lst[elemento][-1] - 1)
                    
        return tuple(lst[0]),tuple(lst[1]), tuple(lst[2])
    else:
        raise ValueError("porta_z: um dos argumentos e invalido")
        
def porta_h(tuplo, lado):
    '''Funcao porta_h: tabuleiro x {"E", "D"}-> tabuleiro
    
    A funcao porta_h recebe um tabuleiro e um caracter ('E' ou 'D') e devolve o tabuleiro correspondente a trocar os estados
dos QuBits da parte inferior do tabuleiro com os da parte superior do tabuleiro, do lado indicado no segundo argumento.
    Caso um dos argumentos nao seja valido, isto e, o primeiro nao ser um tabuleiro ou o segundo nao ser um dos caracteres
apresentados acima, gera um erro com a mensagem "porta_h: um dos argumentos e invalido"'''
    
    if eh_tabuleiro(tuplo) and (lado == 'E' or lado == 'D'):
        lst = transf_tuplo_lista(tuplo)
        
        if lado == 'E':
            lst[0], lst[1] = lst[1], lst[0]      # Se o lado escolhido for a esquerda, queremos trocar os dois primeiros
                                                 # tuplos do tabuleiro.
        else:                                    # Se for direita, queremos trocar os elementos na ultima e penultima posicao
            for el in lst:                       # de todos os tuplos do tablueiro.
                el[-2], el[-1] = el[-1], el[-2]
                    
        return tuple(lst[0]),tuple(lst[1]), tuple(lst[2])
    else:
        raise ValueError("porta_h: um dos argumentos e invalido")

