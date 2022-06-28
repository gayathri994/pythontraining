import json
with open('pra.json', "r") as fd:
     jsondata = fd.read()
     re = json.loads(jsondata)
class myclass():
     def prints_findredc_in_recs(self,recs,findredc):
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
cal = myclass()
if cal.prints_findredc_in_recs(re,{"fname": "abc02", "lname": "xyz02"})==[{'fname': 'abc02', 'lname': 'xyz02', 'age': '32', 'address': '112 xyz rd, abc city, MD, 21774'}, {'fname': 'abc02', 'lname': 'xyz02', 'age': '43', 'address': '113 xyz rd, abc city, MD, 21774'}]:
    print("test pass")
else:
    print("test fail")
