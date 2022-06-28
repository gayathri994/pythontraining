import json
with open('pra.json', "r") as fd:
    jsondata = fd.read()
    re = json.loads(jsondata)
class myclass():
    def count_findredc_in_recs(self,recs,findredc):
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
cal = myclass()
if cal.count_findredc_in_recs(re,{"fname": "abc01", "lname": "xyz02"})==1:
    print("test pass")
else:
    print("test fail")
if cal.count_findredc_in_recs(re,{"fname": "abc02", "lname": "xyz02"})==2:
    print("test pass")
else:
    print("test fail")
if cal.count_findredc_in_recs(re,{"fname": "abc02", "lname": "xyz02","age":"43"})==1:
    print("test pass")
else:
    print("test fail")