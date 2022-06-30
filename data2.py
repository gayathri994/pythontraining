from modfunc import changing_recs_with_findredc
import json
with open('recdata.json',"r") as fd:
    jsondata = fd.read()
    re = json.loads(jsondata)
if changing_recs_with_findredc(re,{"fname": "abc02", "lname": "xyz02"},{"address": "214 xyz11 rd, abc11 city, MD, 21774"})==[{'fname': 'abc02', 'lname': 'xyz02', 'age': '32', 'address': '214 xyz11 rd, abc11 city, MD, 21774'}, {'fname': 'abc02', 'lname': 'xyz02', 'age': '43', 'address': '214 xyz11 rd, abc11 city, MD, 21774'}]:
    print("test pass")
else:
    print("test fail")

