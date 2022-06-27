import json
with open('dic1.json',"r") as fd:
    jsondata = fd.read()
    re = json.loads(jsondata)
def gng(recs,findredc,replace):
    A=[]
    for ele in recs:
        found = True
        for i in findredc:
            if i not in ele or findredc[i] != ele[i]:
                found = False
                break
        if found:
            A.append(ele)
            ele.update(replace)
    print(A)
gng(re,{"fname": "abc02", "lname": "xyz02"},{"address": "214 xyz11 rd, abc11 city, MD, 21774"})
