b = [' '] * 9

for i in range(9):
    p = 'X' if i % 2 == 0 else 'O'
    print(b[0],'|',b[1],'|',b[2])
    print('-----')
    print(b[3],'|',b[4],'|',b[5])
    print('-----')
    print(b[6],'|',b[7],'|',b[8])

    n = int(input(f"Player {p}'s turn (1-9): ")) - 1
    b[n] = p

    if (b[0]==b[1]==b[2]==p or b[3]==b[4]==b[5]==p or
        b[6]==b[7]==b[8]==p or b[0]==b[3]==b[6]==p or
        b[1]==b[4]==b[7]==p or b[2]==b[5]==b[8]==p or
        b[0]==b[4]==b[8]==p or b[2]==b[4]==b[6]==p):
        print(p, "wins!")
        break