from board import Board

def hill_climbing(board):
    heuristicV =[]
    hV =[]
    map =board.get_map()
    counter = 0
    c =0

    for row in map:
        h = board.get_fitness()
        heuristicV.append(h)
        for index in row:
            queenI = row.index(1)
            hV.append(queenI)
            print("Index: ",queenI)
            if c !=queenI:
                board.flip(counter,c)
                board.flip(counter,queenI)
                board.show_map()
                h = board.get_fitness()
                heuristicV.append(h)
                hV.append(c)
            c+=1
        minH = min(heuristicV)
        minI = heuristicV.index(minH)
        new = hV[minI]
        for i in row:
            if i==1:
                board.flip(counter,i)
        board.flip(counter,new)
        counter+=1
        c=0
    counter =0
    print ("\nhue",heuristicV)







if __name__ == '__main__':
    test = Board(5)
    test.show_map()
    print(test.get_fitness())
    print(test.get_map())
    hill_climbing(test)
    test.show_map()
    print(test.get_map())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
