import sys
sys.stdin = open('input.txt','r')
T = int(input())
for tc in range(1,T+1):
    M, A = map(int,input().split())
    p1 = list(map(int,input().split()))
    p2 = list(map(int,input().split()))
    AP = [[0] * 11 for i in range(11)]
    di1 = [0, 0, -1, 0, 1]
    dj1 = [0, 1, 0, -1, 0]
    di2 = [0, 0, -1, 0, 1, 0, -2, 0, 2, 1, -1, -1, 1]
    dj2 = [0, 1, 0, -1, 0, 2, 0, -2, 0, 1, 1, -1, -1]
    di3 = [0, 0, -1, 0, 1, 0, -2, 0, 2, 1, -1, -1, 1, 0, -3, 0, 3, 2, 1, -1, -2, -2, -1, 1, 2]
    dj3 = [0, 1, 0, -1, 0, 2, 0, -2, 0, 1, 1, -1, -1, 3, 0, -3, 0, 1, 2, 2, 1, -1, -2, -2, -1]
    di4 = [0, 0, -1, 0, 1, 0, -2, 0, 2, 1, -1, -1, 1, 0, -3, 0, 3, 2, 1, -1, -2, -2, -1, 1, 2, 0, -4, 0, 4, 3, 2, 1, -1,
           -2, -3, -3, -2, -1, 1, 2, 3]
    dj4 = [0, 1, 0, -1, 0, 2, 0, -2, 0, 1, 1, -1, -1, 3, 0, -3, 0, 1, 2, 2, 1, -1, -2, -2, -1, 4, 0, -4, 0, 1, 2, 3,
           3, 2, 1, -1, -2, -3, -3, -2, -1]
    APlist = [[0] * 11 for i in range(11)]
    for n in range(A):
        a = list(map(int,input().split()))
        j = a[0]
        i = a[1]
        c = a[2] #범위
        P = a[3] #파워

        if c == 1:
            for k in range(5):
                ni = i + di1[k]
                nj = j + dj1[k]
                if 0<=ni<11 and 0<=nj<11:

                    if AP[ni][nj] == 0:
                        AP[ni][nj] = P
                        APlist[ni][nj] = n
                    elif type(AP[ni][nj]) == tuple:
                        AP[ni][nj] += tuple([P])
                        if P >= max(AP[ni][nj]):
                            APlist[ni][nj] = n
                    else:
                        if P>= AP[ni][nj]:
                            APlist[ni][nj] = n
                        AP[ni][nj] = (P,AP[ni][nj])

        elif c==2:
            for k in range(13):
                ni = i + di2[k]
                nj = j + dj2[k]

                if 0<=ni<11 and 0<=nj<11:
                    if AP[ni][nj] == 0:
                        AP[ni][nj] = P
                        APlist[ni][nj] = n
                    elif type(AP[ni][nj]) == tuple:
                        AP[ni][nj] += tuple([P])
                        if P >= max(AP[ni][nj]):
                            APlist[ni][nj] = n
                    else:
                        if P>= AP[ni][nj]:
                            APlist[ni][nj] = n
                        AP[ni][nj] = (P,AP[ni][nj])

        elif c==3:
            for k in range(25):
                ni = i + di3[k]
                nj = j + dj3[k]

                if 0<=ni<11 and 0<=nj<11:
                    if AP[ni][nj] == 0:
                        AP[ni][nj] = P
                        APlist[ni][nj] = n
                    elif type(AP[ni][nj]) == tuple:
                        AP[ni][nj] += tuple([P])
                        if P >= max(AP[ni][nj]):
                            APlist[ni][nj] = n
                    else:
                        if P>= AP[ni][nj]:
                            APlist[ni][nj] = n
                        AP[ni][nj] = (P,AP[ni][nj])


        else:
            for k in range(41):
                ni = i + di4[k]
                nj = j + dj4[k]

                if 0<=ni<11 and 0<=nj<11:
                    if AP[ni][nj] == 0:
                        AP[ni][nj] = P
                        APlist[ni][nj] = n
                    elif type(AP[ni][nj]) == tuple:
                        AP[ni][nj] += tuple([P])
                        if P >= max(AP[ni][nj]):
                            APlist[ni][nj] = n
                    else:
                        if P>= AP[ni][nj]:
                            APlist[ni][nj] = n
                        AP[ni][nj] = (P,AP[ni][nj])

    # for i in range(11):
    #     print(AP[i])
    gi = [0,-1,0,1,0]
    gj = [0,0,1,0,-1]
    i1, j1 = 1,1
    i2, j2 = 10,10
    tp = AP[i1][j1] + AP[i2][j2]
    count = 0
    for m in range(M):
        i1 = i1+gi[p1[m]]
        j1 = j1+gj[p1[m]]
        i2 = i2 + gi[p2[m]]
        j2 = j2 + gj[p2[m]]
        # print(m, AP[i1][j1], AP[i2][j2])
        # print(i1,j1)
        # print(i2,j2)
        # tp = tp + AP[i1][j1] + AP[i2][j2]
        result = 0
        if type(AP[i1][j1]) == tuple and type(AP[i2][j2]) == tuple:
            l1 = list(AP[i1][j1])
            l2 = list(AP[i2][j2])
            l1.sort()
            l2.sort()
            # print(l1)
            if l1[-1] == l2[-1]:
                result = max((l1[-1]+l2[-2]),(l2[-1] + l1[-2]))
            else:
                result = l1[-1] + l2[-1]
        elif type(AP[i1][j1]) == tuple:
            v = list(AP[i1][j1])
            # print(v)
            v.sort()

            if v[-1] == AP[i2][j2]:
                if APlist[i1][j1] == APlist[i2][j2]:
                    result = AP[i2][j2] + v[-2]
                else:
                    result = AP[i2][j2] + v[-1]
            else:
                result = v[-1] + AP[i2][j2]
        elif type(AP[i2][j2]) == tuple:
            h = list(AP[i2][j2])
            h.sort()
            if h[-1] == AP[i1][j1]:
                if APlist[i1][j1] == APlist[i2][j2]:
                    result = AP[i1][j1] + h[-2]
                else:
                    result = AP[i1][j1] + h[-1]
            else:
                result = h[-1] + AP[i1][j1]
        else:
            if AP[i1][j1] == AP[i2][j2]:
                if APlist[i1][j1] == APlist[i2][j2]:
                    result = AP[i2][j2]
                else:
                    result = AP[i1][j1] + AP[i2][j2]
            else:
                result = AP[i1][j1] + AP[i2][j2]
        tp += result


    print(tp)
