import json
with open('dic1.json',"r") as fd:
    jsondata = fd.read()
    re = json.loads(jsondata)
def gng(recs, findredc):
    A = []
    for ele in recs:
        found = True
        for k in findredc:
            if k not in ele or findredc[k] != ele[k]:
                found = False
                break
        if found:
            A.append(ele)
    print(A)
gng(re,{"fname": "abc02", "lname": "xyz02"})