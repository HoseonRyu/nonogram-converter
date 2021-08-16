def make_clue(l):
    l_ = l+[0]
    list_ = []
    cnt = 0
    for i in l_:
        if i == 0:
            if cnt != 0:
                list_.append(cnt)
                cnt = 0
        else:
            cnt += 1
    if len(list_)==0:
        return [0]
    return list_


def make_clues(ls):
    outs = []
    for l in ls:
        outs.append(make_clue(l))
    return outs


def result(rows, cols):
    row_clues = make_clues(rows)
    col_clues = make_clues(cols)

    row_clues = crop(row_clues)
    if row_clues is None:
        return None

    col_clues = crop(col_clues)
    if col_clues is None:
        return None

    h = len(row_clues)
    w = len(col_clues)

    max_r_c = 12
    max_c_c = 5

    h_tot = h + max_c_c
    w_tot = w + max_r_c

    arr = []
    for i in range(h_tot):
        arr.append([])
        for j in range(w_tot):
            arr[i].append(0)

    for i in range(h):
        lst = row_clues[i]
        leng = len(lst)
        for j in range(leng):
            arr[i+max_c_c][max_r_c-leng+j] = lst[j]

    for i in range(w):
        lst = col_clues[i]
        leng = len(lst)
        for j in range(leng):
            arr[max_c_c-leng+j][i+max_r_c] = lst[j]

    return arr


def crop(clues):
    if sum([sum(l) for l in clues]) == 0:
        return None
    clues = clues[::-1]
    while sum(clues[0]) == 0:
        clues.pop(0)
    clues = clues[::-1]
    while sum(clues[0]) == 0:
        clues.pop(0)
    return clues