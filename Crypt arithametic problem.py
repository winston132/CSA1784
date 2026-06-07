from itertools import permutations

for p in permutations(range(10), 8):
    S,E,N,D,M,O,R,Y = p

    if S != 0 and M != 0:
        SEND  = 1000*S + 100*E + 10*N + D
        MORE  = 1000*M + 100*O + 10*R + E
        MONEY = 10000*M + 1000*O + 100*N + 10*E + Y

        if SEND + MORE == MONEY:
            print("Solution:", {'S':S,'E':E,'N':N,'D':D,
                                'M':M,'O':O,'R':R,'Y':Y})
            print("SEND + MORE = MONEY")
            print(MONEY)
            break