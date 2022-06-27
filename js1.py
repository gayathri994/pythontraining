import json
with open('dic1.json',"r") as fd:
    jsondata = fd.read()

    re = json.loads(jsondata)

def gng(recs,findredc):
    cnt = 0
    for ele in recs:
        found = True
        for k in findredc:
            if k not in ele or findredc[k] != ele[k]:
                found = False
                break
        if found:
            cnt = cnt + 1
    print(cnt)
gng(re,{"fname": "abc01", "lname": "xyz02"})
gng(re,{"fname": "abc02", "lname": "xyz02"})
gng(re,{"fname": "abc02", "lname": "xyz02", "age": "43"})
