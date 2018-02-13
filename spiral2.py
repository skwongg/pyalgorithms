def spiral(input_size):
    num_bank = range(1, input_size*input_size + 1)

    num_objs=0
    mat = []
    for i in range(0, input_size):
        sub_arr = []
        for j in range(0, input_size):
            sub_arr.append(0)
            num_objs+=1
        mat.append(sub_arr)
    xmax, xmin, ymax, ymin = len(mat[0]), 0, len(mat), 0
    right,left,up,down = True, False, False, False

    while num_bank:
        if right == True:
            for r in range(xmin, xmax):
                mat[xmin][r] = num_bank.pop(0)
            right=False
            down=True
            ymin+=1
        if down == True:
            for i in range(ymin, ymax):
                mat[i][ymax-1] = num_bank.pop(0)
            down=False
            left=True
            xmax-=1

        if left == True:
            for j in range((xmax - 1), (xmin - 1), -1):
                mat[ymax - 1][j] = num_bank.pop(0)
            left=False
            up = True
            ymax-=1

        if up == True:
            for u in range((ymax - 1), (ymin - 1), -1):
                mat[u][xmin] = num_bank.pop(0)
            up = False
            right=True
            xmin+=1

    return mat

print(spiral(5))
