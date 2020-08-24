def poker_star(no_of_card:'int', no_of_player:'int', sequence_cardsA:'list', sequence_cardsB:'list') -> 'Match Winner':
    """returns winning player name 
    Input:
        no_of_card : int no of cards each player has
        no_of_player : int total no of player playing the game
        sequence_cardsA : list
        sequence_cardsB : list
    Output: winner of the match
    """
     if len(sequence_cardsA) != len (sequence_cardsB) :
         raise ValueError("No Of Cards Should be same")
    else:
        pass

    a = ['acehearts','kinghearts','queenhearts','jackhearts','10hearts']
    b = ['10clubs','9clubs','8clubs','7clubs','6clubs']
    c = ['queenclubs','queenhearts','queenspades','queendiamonds','5clubs']
    d = ['acediamonds','acespades','acediamonds','kingspades','kingdiamonds']
    e = ['kinghearts','8hearts','6hearts','4hearts','2hearts']
    f = ['8diamonds','7clubs','6diamonds','5spades','4diamonds']
    g = ['queenclubs','queenhearts','queenspades','7diamonds','2spades']
    h = ['jackdiamonds','jackspades','9spades','9diamonds','5clubs']
    i = ['kinghearts','kingspades','9daimonds','8spades','4hearts']
    j = ['acehearts','queenclubs','6hearts','4spades','2diamonds']

    if no_of_player == 2:
        if no_of_card == 3:
            if sequence_cardsA == a[0:3]:
                p = "Player A is winner"
            elif sequence_cardsA == b[0:3] and sequence_cardsB != a[0:3] :
                p = "Player A is winner"
            elif sequence_cardsA == c[0:3] and ( sequence_cardsB != a[0:3] or sequence_cardsB != b[0:3] ):
                p = "Player A is winner"
            elif sequence_cardsA == d[0:3] and (sequence_cardsB != a[0:3] or sequence_cardsB != b[0:3] or sequence_cardsB != c[0:3]):
                p = "Player A is winner"
            elif sequence_cardsA == e[0:3] and (sequence_cardsB != a[0:3] or sequence_cardsB != b[0:3] or sequence_cardsB != c[0:3] or sequence_cardsB != d[0:3] ):
                p = "Player A is winner"
            elif sequence_cardsA == f[0:3] and (sequence_cardsB != a[0:3] or sequence_cardsB != b[0:3] or sequence_cardsB != c[0:3] or sequence_cardsB != d[0:3] or sequence_cardsB != e[0:3]):
                p = "Player A is winner"
            elif sequence_cardsA == g[0:3] and (sequence_cardsB == h[0:3] or sequence_cardsB == i[0:3] or sequence_cardsB == j[0:3]):
                p = "Player A is winner"
            elif sequence_cardsA == h[0:3] and (sequence_cardsB == i[0:3] or sequence_cardsB == j[0:3]):
                p = "Player A is winner"
            elif sequence_cardsA ==i[0:3] and sequence_cardsB == j[0:3]:
                p = "Player A is winner"
            else:
                p = "Player B is winner"
        elif no_of_card == 4:
            if sequence_cardsA == a[0:4]:
                p = "Player A is winner"
            elif sequence_cardsA == b[0:4] and sequence_cardsB!=a[0:4] :
                p = "Player A is winner"
            elif sequence_cardsA == c[0:4] and (sequence_cardsB!=a[0:4] or sequence_cardsB!=b[0:4]):
                p = "Player A is winner"
            elif sequence_cardsA == d[0:4] and (sequence_cardsB!=a[0:4] or sequence_cardsB!=b[0:4] or sequence_cardsB!=c[0:4]):
                p = "Player A is winner"
            elif sequence_cardsA == e[0:4] and (sequence_cardsB!=a[0:4] or sequence_cardsB!=b[0:4] or sequence_cardsB!=c[0:4] or sequence_cardsB!=d[0:4]):
                p = "Player A is winner"
            elif sequence_cardsA == f[0:4] and (sequence_cardsB!=a[0:4] or sequence_cardsB!=b[0:4] or sequence_cardsB!=c[0:4] or sequence_cardsB!=d[0:4] or sequence_cardsB!=e[0:4]):
                p = "Player A is winner"
            elif sequence_cardsA == g[0:4] and (sequence_cardsB == h[0:4] or sequence_cardsB==i[0:4] or sequence_cardsB==j[0:4]):
                p = "Player A is winner"
            elif sequence_cardsA == h[0:4] and (sequence_cardsB == i[0:4] or sequence_cardsB==j[0:4]):
                p = "Player A is winner"
            elif sequence_cardsA ==i[0:4] and sequence_cardsB == j[0:4]:
                p = "Player A is winner"
            else:
                p="Player B is winner"
        elif no_of_card == 5:
            if (sequence_cardsA == a) and (sequence_cardsB != b or sequence_cardsB != c or sequence_cardsB != d or sequence_cardsB != e or sequence_cardsB != f or sequence_cardsB != g or sequence_cardsB != h or sequence_cardsB != i or sequence_cardsB != j):
                p = "Player A is winner"
            elif (sequence_cardsA == b) and (sequence_cardsB != a) :
                p="Player A is winner"
            elif (sequence_cardsA == c) and (sequence_cardsB!=a or sequence_cardsB!=b):
                print("hello2")
                p = "Player A is winner"
            elif sequence_cardsA == d and (sequence_cardsB!=a or sequence_cardsB!=b or sequence_cardsB!=c):
                p = "Player A is winner"
            elif sequence_cardsA == e and (sequence_cardsB!=a or sequence_cardsB!=b or sequence_cardsB!=c or sequence_cardsB!=d):
                p = "Player A is winner"
            elif sequence_cardsA == f and (sequence_cardsB!=a or sequence_cardsB!=b or sequence_cardsB!=c or sequence_cardsB!=d or sequence_cardsB!=e):
                p = "Player A is winner"
            elif sequence_cardsA == g and (sequence_cardsB == h or sequence_cardsB==i or sequence_cardsB==j):
                p = "Player A is winner"
            elif sequence_cardsA == h and (sequence_cardsB == i or sequence_cardsB==j):
                p = "Player A is winner"
            elif sequence_cardsA ==i and sequence_cardsB == j:
                p = "Player A is winner"
            else:
                p="Player B is winner"
        else:
            p="please enter correct number of card"
    else:
        p="please enter correct number of players"
    return p
