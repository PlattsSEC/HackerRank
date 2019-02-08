def minimumBribes(q):
    bribe_count = 0
    back_index = len(q) - 1
    curr_sticker = len(q)

    while q != list(range(1,len(q)+1)):
        skips = 0
        if q[back_index] != curr_sticker:
            back_index -= 1
        else:
            while q.index(q[back_index]) != curr_sticker - 1:
                if skips < 2:
                    q[back_index], q[back_index + 1] = q[back_index + 1], q[back_index]
                    skips += 1
                    back_index += 1
                    bribe_count += 1
                else:
                    return('too chaotic')
            curr_sticker -= 1
            
    return bribe_count