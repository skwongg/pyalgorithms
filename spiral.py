def spiral(mat):
    if not mat:
        return "Matrix not found"
    xmax, xmin, ymax, ymin = len(mat[0]), 0, len(mat), 0
    right,left,up,down = False, False, False, False

    num_objs = 0
    for obj in mat:
        num_objs+=len(obj)

    collec = []
    if not collec:
        right = True
    while len(collec) < num_objs:
        if right == True:
            for r in range(xmin, xmax):
                collec.append(mat[xmin][r])
            right=False
            down=True
            ymin+=1
        if down == True:
            for i in range(ymin, ymax):
                collec.append(mat[i][ymax-1])
            down=False
            left=True
            xmax-=1

        if left == True:
            for j in range((xmax - 1), (xmin - 1), -1):
                collec.append(mat[ymax - 1][j])
            left=False
            up = True
            ymax-=1

        if up == True:
            for u in range((ymax - 1), (ymin - 1), -1):
                collec.append(mat[u][xmin])
            up = False
            right=True
            xmin+=1

    return collec

mat = [ [1 ,2 ,3 ,4 ,21],
        [5 ,6 ,7 ,8 ,71],
        [9 ,10,11,12,38],
        [13,14,15,16,31],
        [13,14,15,16,31]
        ]

mat = [ [1, 2, 3, 4, 5 ],
        [6, 7, 8, 9, 10],
        [11,12,13,14,15],
        [16,17,18,19,20],
        [21,22,23,24,25],
      ]

print spiral(mat)
