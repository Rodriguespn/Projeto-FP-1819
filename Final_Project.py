#Pedro Rodrigues, n90531

# Celula
    
class celula:
    '''class celula: {-1, 0, 1} -> celula
        
        A classe celula recebe um numero do conjunto {-1, 0, 1} e cria um objeto com a caracteristica "estado",
        cujo o seu valor corresponde ao numero introduzido. Caso o argumento nao esteja nesse intervalo,
        gera um erro com a mensagem ('cria_celula: argumento invalido')'''  
    
    def __init__(self, estado):  
        if estado in (-1,0,1):
            self._est = estado             
        else:
            raise ValueError('cria_celula: argumento invalido.')
            
    def estado(self):
        '''estado: celula -> {-1, 0, 1}
    
        O metodo "estado" recebe uma celula devolve o numero correspondente ao estado em que se encontra essa celula.'''
        
        return self._est
    
    def inverte(self):
        '''inverte: celula -> celula
    
        O metodo "inverte" recebe uma celula e devolve a celula resultante de inverter o estado da celula inicial.
        uma celula inativa torna-se ativa; uma celula ativa torna-se inativa e uma celula no estado incerto 
        mantem-se no mesmo estado.'''
        
        if self.estado() in (0,1):
            self._est = 1 - self._est # Se self._est == 0, 1-0 = 1; se self._est == 1, 1-1 = 0
        return self
    
    def str_cel(self):
        '''celula_para_str: celula -> cad. caracteres

        O metodo "str_cel" recebe uma celula e devolve uma cadeia de caracteres que representa o estado
        dessa celula. Se o seu estado for "-1", e representado por 'x'.'''
    
        if self.estado() == -1:       # Se o estado da celula for indefinido, devolvemos um 'x'
            return 'x'
        else:
            return str(self.estado())
    
cria_celula = celula                  # "cria_celula" corresponde a classe "celula"

obter_valor = celula.estado           # "obter_valor" corresponde ao metodo "estado" da classe "celula"

inverte_estado = celula.inverte       # "inverte_estado" corresponde ao metodo "inverte" da classe "celula"

celula_para_str = celula.str_cel      # "celula_para_str" corresponde ao metodo "str_cel" da classe "celula"

def eh_celula(cel):
    '''eh_celula: universal -> logico
    
    A funcao "eh_celula" recebe um argumento universal e devolve True apenas se esse argumento for do tipo "celula",
    e False caso contrario.'''
    
    return isinstance(cel, celula)    

def celulas_iguais(c1, c2):
    '''celulas_iguais: celula x celula -> logico
    
    A funcao "celulas_iguais" recebe duas celulas e devolve True apenas se as duas celulas tiverem o mesmo estado.
    Caso contrario, devolve False.'''
    
    return eh_celula(c1) and eh_celula(c2) and obter_valor(c1) == obter_valor(c2)     
    
# Coordenada

class coordenada:
    '''class coordenada: natural x natural -> coordenada
        
        A classe coordenada recebe dois numeros do conjunto {0, 1, 2} e cria um objeto com as caracteristicas "linha" e
        "coluna", cujo os seus valores correspondem, respetivamente, ao primeiro e segundo numero introduzidos. Caso algum
        dos argumentos nao esteja nesse conjunto, gera um erro com a mensagem ('cria_coordenada: argumento invalido')'''
    
    def __init__(self, linha, coluna):
        if linha in (0, 1, 2) and coluna in (0, 1, 2):   # Decidi que a coordenada (2,0) e aceite como coordenada, apesar
            self._ln = linha                             # de corresponder a uma posicao vazia no tabuleiro fisico
            self._cl = coluna
        else:
            raise ValueError("cria_coordenada: argumentos invalidos.")
    
    def linha(self):
        '''coordenada_linha: coordenada -> natural

        O metodo "coordenada_linha" recebe uma coordenada e devolve o numero natural correspondente a linha dessa coordenada.'''
        return self._ln
         
    def coluna(self):
        '''coordenada_coluna: coordenada -> natural
        
        O metodo "coordenada_coluna" recebe uma coordenada e devolve o natural correspondente a coluna dessa coordenada'''
    
        return self._cl
    
    def str_coord(self):
        '''coordenada_para_str: coordenada -> cad. caracteres
        
        O metodo "str_coord" recebe uma coordenada e devolve a cadeia de caracteres que representa o seu argumento.
        A coordenada correspondente a linha l e coluna c e representada pela cadeia de carateres '(l, c)'.'''
        
        return '(' + str(self.linha()) + ', ' + str(self.coluna()) + ')'
        
cria_coordenada = coordenada                 # "cria_coordenada" corresponde a classe "coordenada"

coordenada_linha = coordenada.linha          # "coordenada_linha" corresponde ao metodo "linha" da classe "coordenada"
    
coordenada_coluna = coordenada.coluna        # "coordenada_coluna" corresponde ao metodo "coluna" da classe "coordenada"

coordenada_para_str = coordenada.str_coord   # "coordenada_para_str" corresponde ao metodo "str_coord" da classe "coordenada"

def eh_coordenada(arg):
    '''eh_coordenada: universal -> logico
    
    A funcao "eh_coordenada" recebe um argumento universal e devolve True apenas no caso em que o seu argumento
    é do tipo coordenada.'''
    
    return isinstance(arg, coordenada)

def coordenadas_iguais(c1, c2):
    '''coordenadas_iguais: coordenada x coordenada -> logico
    
    A funcao "coordenadas_iguais" recebe duas coordenadas e devolve True apenas se essas coordenadas representarem
    coordenadas iguais, ou seja representam a mesma posicao.'''
    
    return  eh_coordenada(c1) and eh_coordenada(c2) and (coordenada_linha(c1) == coordenada_linha(c2)) and (coordenada_coluna(c1) == coordenada_coluna(c2))

# Tabuleiro

# Construtores
def tabuleiro_inicial():
    '''tabuleiro_inicial: {} -> tabuleiro
    
    A funcao "tabuleiro_inicial" nao recebe argumentos e devolve o tabuleiro inicial do jogo, ou seja, o
    tabuleiro representado pela string '((-1,-1,-1),(0,0,-1),(0,-1))'.'''
    
    return str_para_tabuleiro('((-1,-1,-1),(0,0,-1),(0,-1))')

def str_para_tabuleiro(st):
    '''str_para_tabuleiro: cad. caracteres -> tabuleiro

    A funcao "str_para_tabuleiro" recebe uma cad. de caracteres e devolve o tabuleiro correspondente a essa cad. de
    caracteres. A cad. de caracteres introduzida corresponde a um tuplo de 3 tuplos, os dois primeiros com 3
    elementos e o ultimo com 2 elementos. Os elementos destes tuplos sao obtidos do conjunto {0, 1, -1}.
    Caso o argumento nao seja valido, gera um erro com a mensagem ('str_para_tabuleiro: argumentos invalidos.')'''
    
    if isinstance(st, str) and eh_tabuleiro_proj1(eval(st)):   # A funcao "eh_tabuleiro_proj1" foi definida no projeto 1
        tab = transf_tuplo_lista(eval(st))                     # Um tabuleiro e uma lista de 3 listas de objetos correspondentes
        for ln in range(len(tab)):                             # a classe "celula", as 2 primeiras com 3 celulas e a ultima com
            for cl in range(len(tab[ln])):                     # apenas 2 celulas
                tab[ln][cl] = cria_celula(tab[ln][cl])         
        return tab
    else:
        raise ValueError("str_para_tabuleiro: argumento invalido.")
        
# Seletores        
def tabuleiro_dimensao(t):
    '''tabuleiro_dimensao: tabuleiro -> natural
    
    A funcao "tabuleiro_dimensao" recebe um tabuleiro e devolve o numero correspondente ao numero de linhas
    (e,como o tabuleiro e quadrado, tambem ao numero de colunas) existentes no tabuleiro'''
    
    return len(t)

def tabuleiro_celula(t, coord):
    '''tabuleiro_celula: tabuleiro x coordenada -> celula

    A funcao "tabuleiro_celula" recebe um tabuleiro e uma coordenada e devolve a celula presente na coordenada do tabuleiro'''
    
    return t[coordenada_linha(corrige_coord(coord))][coordenada_coluna(corrige_coord(coord))]         

# Modificadores
def tabuleiro_substitui_celula(t, cel, coord):
    '''tabuleiro_substitui_celula: tabuleiro x celula x coordenada -> tabuleiro
    
    A funcao "tabuleiro_substitui_celula" recebe um tabuleiro, uma celula e uma coordenada e devolve o tabuleiro
    que resulta de substituir a celula , existente na coordenada introduzida do tabuleiro, pela nova celula. Caso um dos 
    argumentos introduzidos nao seja do tipo correto, gera um erro com a mensagem
    ("tabuleiro_substitui_celula: argumentos invalidos.")'''

    if eh_tabuleiro(t) and eh_celula(cel) and eh_coordenada(coord):               
        t[coordenada_linha(corrige_coord(coord))][coordenada_coluna(corrige_coord(coord))] = cel
        return t
    else:
        raise ValueError("tabuleiro_substitui_celula: argumentos invalidos.")

def tabuleiro_inverte_estado(t, coord):
    '''tabuleiro_inverte_estado: tabuleiro x coordenada -> tabuleiro
    
    A funcao "tabuleiro_inverte_estado" recebe um tabuleiro, uma celula e uma coordenada e devolve o tabuleiro
    que resulta de inverter o estado da celula presente na coordenada coor do tabuleiro. A sua funcao deve
    verificar a correcao dos argumentos, gera um erro com a mensagem 
    ("tabuleiro_inverte_estado: argumentos invalidos.")'''
    
    if eh_tabuleiro(t) and eh_coordenada(coord):
        c = coord   # Como vou alterar destrutivamente "coord", e vou precisar dos valores iniciais mais tarde, copio esse objeto para "c" 
        inverte_estado(tabuleiro_celula(t, coord))
        t[coordenada_linha(corrige_coord(c))][coordenada_coluna(corrige_coord(c))] = cria_celula(obter_valor(tabuleiro_celula(t, c)))
        return t
    else:
        raise ValueError("tabuleiro_inverte_estado: argumentos invalidos.")

# Reconhecedores
def eh_tabuleiro(arg):
    '''eh_tabuleiro: universal -> logico
    
    A funcao "eh_tabuleiro" recebe um argumento e devolve True apenas no caso do argumento dado ser do tipo tabuleiro.'''
    
    if verifica_tab(arg):
        for i in range(len(arg)):             # Para otimizar, se encontrar um elemento dentro de arg 
            for j in arg[i]:                  # que nao seja do tipo celula, devolve
                if not eh_celula(j):          # logo False, nao precisando de percorrer
                    return False              # a lista toda, se nao for necessario      
                        
        return True
    else:
        return False

# Transformador
def tabuleiro_para_str(tab):
    '''tabuleiro_para_str: tabuleiro -> cad. caracteres
    
    A funcao "tabuleiro_para_str" recebe um tabuleiro e devolve a cadeia de caracteres que o representa.'''
    
    def tabuleiro_limpo():
        '''Funcao novo_tabuleiro: sem argumentos -> cad.caracteres
        
        A funcao "tabuleiro_limpo" nao recebe argumentos e devolve uma cadeia de caracteres, em que na posicao dos estados
        das celulas, esta a notacao "%s", que significa que a string vai aguardar pelo valores a serem introduzidos nessa posicao'''
        
        return '+-------+\n|...%s...|\n|..%s.%s..|\n|.%s.%s.%s.|\n|..%s.%s..|\n+-------+'
    
    def estados_por_ordem(tab):
        '''Funcao novo_tabuleiro: tabuleiro -> tuplo
        
        A funcao "estados_por_ordem" recebe um tabuleiro e devolve um tuplo em que os seus elementos sao cad. de caracteres
        que representam o estado de cada celula do tabuleiro, por ordem que os estados aparecem na cad. de caracteres que
        que representa o tabuleiro.'''
        
        estados_ordenados = ()
        pos = ((0, 2), (0, 1), (1, 2), (0, 0), (1, 1), (2, 1), (1, 0), (2, 0)) # Tuplo que contem as coordenadas das celulas 
                                                                               # no tabuleiro, pela ordem que aparecem na cad. 
                                                                               # de caracteres que representa o tabuleiro
        for el in pos:
            coord = cria_coordenada(el[0], el[1])                              # Vou buscar ao tabuleiro a celula na coordenada (coord)
                                                                               # e adiciono-a ao tuplo estados_ordenados
            estados_ordenados += (celula_para_str(tab[coordenada_linha(coord)][coordenada_coluna(coord)]),)
        return estados_ordenados
                             
    return tabuleiro_limpo() % estados_por_ordem(tab)

# Teste
def tabuleiros_iguais(t1, t2):
    '''Funcao tabuleiros_iguais: tabuleiro x tabuleiro -> booleano
    
    A funcao tabuleiros_iguais recebe dois tabuleiros e devolve True apenas se estes forem iguais.
    Caso contrario devolve False'''
                                                                                                       # Dois tabuleiros sao iguais se a sua representacao de 
    return eh_tabuleiro(t1) and eh_tabuleiro(t2) and tabuleiro_para_str(t1) == tabuleiro_para_str(t2)  # cad. de caracteres for igual
                                                             
# Porta X
def porta_x(t, lado):
    '''porta_x: tabuleiro x {'E', 'D'} -> tabuleiro

    A funcao "porta_x" recebe um tabuleiro e um lado, dentro de ('E', 'D') e devolve o tabuleiro resultante de aplicar
    a porta x a celula inferior do qubit da esquerda, ou da direita, conforme lado seja 'E' ou 'D', respetivamente.
    Caso algum dos argumentos nao seja valido, gera um erro com a mensagem ("porta_x: argumentos invalidos.")'''
    
    def porta_x_esq(tab):
        '''porta_x_esq: tabuleiro -> tabuleiro
        
        A funcao "porta_x_esq" recebe um tabuleiro e devolve o tabuleiro correspondente de aplicar a porta x a celula inferior
        do qubit da esquerda'''
        
        for cl in range(3):                       
            tab = tabuleiro_inverte_estado(tab, cria_coordenada(1, cl))  
        return tab
    
    def porta_x_dir(tab):
        '''porta_x_dir: tabuleiro -> tabuleiro
        
        A funcao "porta_x_dir" recebe um tabuleiro e devolve o tabuleiro correspondente de aplicar a porta x a celula inferior
        do qubit da direita'''
        
        for ln in range(3):                       
            tab = tabuleiro_inverte_estado(tab, cria_coordenada(ln, 1)) 
        return tab
    
    if eh_tabuleiro(t) and lado in ('E', 'D'):  
        if lado == 'E':
            return porta_x_esq(t)
        else:
            return porta_x_dir(t)     
    else:
        raise ValueError("porta_x: argumentos invalidos.")

    
# Porta Z
def porta_z(t, lado):
    '''porta_z: tabuleiro x {'E', 'D'} -> tabuleiro
    
    A funcao "porta_z" recebe um tabuleiro e um lado, dentro de ('E', 'D') e devolve o tabuleiro resultante de aplicar
    a porta z a celula superior do qubit da esquerda, ou da direita, conforme lado seja 'E' ou 'D', respetivamente.
    Caso algum dos argumentos nao seja valido, gera um erro com a mensagem ("porta_z: argumentos invalidos.")'''

    def porta_z_esq(tab):
        '''porta_z_esq: tabuleiro -> tabuleiro
        
        A funcao "porta_z_esq" recebe um tabuleiro e devolve o tabuleiro correspondente de aplicar a porta z a celula superior
        do qubit da esquerda'''
        
        for cl in range(3):                          
            tab = tabuleiro_inverte_estado(tab, cria_coordenada(0, cl))
        return tab
    
    def porta_z_dir(tab):
        '''porta_z_dir: tabuleiro -> tabuleiro
        
        A funcao "porta_z_dir" recebe um tabuleiro e devolve o tabuleiro correspondente de aplicar a porta z a celula superior
        do qubit da direita'''
        
        for ln in range(3):                               
            tab = tabuleiro_inverte_estado(tab, cria_coordenada(ln,2))
        return tab
    
    if eh_tabuleiro(t) and lado in ('E', 'D'):  
        if lado == 'E':
            return porta_z_esq(t)
        else:
            return porta_z_dir(t)
    else:
        raise ValueError("porta_z: argumentos invalidos.")


# Porta_H        
def porta_h(t, p):
    '''porta_h: tabuleiro -> {'E', 'D'} -> tabuleiro
    
    A funcao "porta_h" recebe um tabuleiro e um lado, dentro de ('E', 'D') e devolve o tabuleiro resultante de aplicar
    a porta h a esquerda, ou da direita, conforme lado seja 'E' ou 'D', respetivamente.
    Caso algum dos argumentos nao seja valido, gera um erro com a mensagem ("porta_h: argumentos invalidos.")'''
    
    if eh_tabuleiro(t) and p in ('E', 'D'):

        if p == 'E':
            t[0], t[1] = t[1], t[0]              # Se o lado escolhido for a esquerda, queremos trocar os dois primeiros
                                                 # tuplos do tabuleiro.
        else:                                    # Se for direita, queremos trocar os elementos na ultima e penultima posicao
            for el in t:                         # de todos os tuplos do tablueiro.
                el[-2], el[-1] = el[-1], el[-2]
                    
        return t
    else:
        raise ValueError("porta_h: argumentos invalidos.")
    
    
# Jogo "Hello Quantum"
def hello_quantum(st):
    '''hello_quantum: cad. caracteres -> logico
    
    Função principal do jogo que permite jogar um jogo completo de Hello Quantum.
    A função hello_quantum recebe uma cadeia de caracteres contendo a descrição do
    tabuleiro objetivo e do numero maximo de jogadas. A funcao devolve verdadeiro
    se o jogador conseguir transformar o tabuleiro inicial no tabuleiro objetivo, nao
    ultrapassando o numero de jogadas indicado e devolve falso em caso contrario. O
    numero maximo de jogadas e apresentado imediatamente apos a descricao do tabuleiro
    objetivo, separado por ":"'''
    
    def descodifica_str(st):
        '''descodifica_str: cad. caracteres -> tuplo
        
        A funcao "descodifica_str" recebe uma cad. de caracteres que representa o tuplo que representa o tabuleiro objetivo,
        e o numero de jogadas maxima para alcancar esse mesmo tabuleiro, e devolve o tuplo em que na primeira posicao esta
        o tuplo que representa o tabuleiro e na segunda esta o numero de jogadas maxima.'''
        
        for el in range(len(st)):
            if ord(st[el]) == ord(':'):
                tab_final = str_para_tabuleiro(st[:el])
                jogadas_max = eval(st[el+1:])
        return (tab_final, jogadas_max)
    
    print('Bem-vindo ao Hello Quantum!')
    print('O seu objetivo e chegar ao tabuleiro:')
    tab_final, jogadas_max = descodifica_str(st)
            
    print(tabuleiro_para_str(tab_final))
    tab_jog = tabuleiro_inicial()
    print('Comecando com o tabuleiro que se segue:')
    print(tabuleiro_para_str(tab_jog))
    
    jogadas = 0
    while not tabuleiros_iguais(tab_jog, tab_final) and jogadas < jogadas_max:
        porta = str(input('Escolha uma porta para aplicar (X, Z ou H): '))
        lado = str(input('Escolha um qubit para analisar (E ou D): '))
        if porta == 'X':
            tab_jog = porta_x(tab_jog, lado)

        elif porta == 'Z':
            tab_jog = porta_z(tab_jog, lado)

        elif porta == 'H':
            tab_jog = porta_h(tab_jog, lado)

        print(tabuleiro_para_str(tab_jog))
        jogadas += 1
        
    if tabuleiros_iguais(tab_jog, tab_final):
        print('Parabens, conseguiu converter o tabuleiro em %s jogadas!' % str(jogadas))
        return True
    
    else:
        return False
           
# Funcoes do projeto1
    
def eh_tabuleiro_proj1(t):
    '''Funcao eh_tabuleiro_proj1: universal -> booleano

    A funcao "eh_tabuleiro_proj1" recebe qualquer argumento e devolve True se o argumento for um tabuleiro, isto e,
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
    
def transf_tuplo_lista(tuplo):
    '''Funcao transf_tuplo_lista: tuplo -> lista

    A funcao transf_tuplo_lista recebe um tuplo e devolve uma lista com exatamente os mesmos elementos do tuplo inicial'''
    
    lst = []
    for el in tuplo:
        lst += [list(el)]
    return lst

def corrige_coord(coord): 
    '''corrige_coord: coordenada -> coordenada
    
    A funcao "corrige_coord" recebe uma coordenada e, se essa cordenada estiver em ((2,1), (2,2)), devolve a coordenada correspondente a coordenada da coluna anterior
    dessa coordenada ((2,0) ou (2,1)). Caso nao pertenca, devolve a coordenada sem alteracoes'''
    
    def coord_fantasma(coord):
        '''coord_fantasma: coordenda -> logico

        A funcao "coord_fantasma" recebe uma coordenada e devolve True apenas se essa coordenada for (2,1) ou (2,2).
        Caso contrario, devolve False.'''

        return (coordenada_linha(coord), coordenada_coluna(coord)) in ((2, 1), (2, 2))
    
    if coord_fantasma(coord):
        return cria_coordenada(coordenada_linha(coord), coordenada_coluna(coord)-1)
    else:
        return coord

# funcoes auxiliares para o tabuleiro
def verifica_tab(arg):
    '''verifica_tab: universal -> logico
    
    A funcao "verifica_tab" recebe um argumento qualquer e devolve True apenas se esse argumento for do tipo "tabuleiro".
Caso contrario, devolve False.'''
    
    return isinstance(arg, list) and len(arg) == 3 and isinstance(arg[0] and arg[1] and arg[2], list)           and len(arg[0]) == len(arg[1])== 3 and len(arg[2])== 2

