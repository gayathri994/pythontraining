import json
with open('pra.json', "r") as fd:
     jsondata = fd.read()
     re = json.loads(jsondata)
class myclass():
     def changing_recs_with_findredc (self,recs,findredc,replace):
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
cal = myclass()
if cal.changing_recs_with_findredc(re,{"fname": "abc02", "lname": "xyz02"},{"address": "214 xyz11 rd, abc11 city, MD, 21774"})==[{'fname': 'abc02', 'lname': 'xyz02', 'age': '32', 'address': '214 xyz11 rd, abc11 city, MD, 21774'}, {'fname': 'abc02', 'lname': 'xyz02', 'age': '43', 'address': '214 xyz11 rd, abc11 city, MD, 21774'}]:
    print("test pass")
else:
    print("test fail")

