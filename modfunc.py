def count_findredc_in_recs (recs,findredc):
    cnt = 0
    for ele in recs:
        found = True
        for k in findredc:
            if k not in ele or findredc[k] != ele[k]:
                found = False
                break
        if found:
            cnt = cnt + 1
    return cnt

def prints_findredc_in_recs (recs, findredc):
    A = []
    for ele in recs:
        found = True
        for k in findredc:
            if k not in ele or findredc[k] != ele[k]:
                found = False
                break
        if found:
            A.append(ele)
    return A


def changing_recs_with_findredc(recs, findredc, replace):
    A = []
    for ele in recs:
        found = True
        for i in findredc:
            if i not in ele or findredc[i] != ele[i]:
                found = False
                break
        if found:
            A.append(ele)
            ele.update(replace)
    return A