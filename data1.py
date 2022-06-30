from modfunc import prints_findredc_in_recs
import json
with open('recdata.json',"r") as fd:
    jsondata = fd.read()
    re = json.loads(jsondata)
if prints_findredc_in_recs(re,{"fname": "abc02", "lname": "xyz02"})==[{'fname': 'abc02', 'lname': 'xyz02', 'age': '32', 'address': '112 xyz rd, abc city, MD, 21774'}, {'fname': 'abc02', 'lname': 'xyz02', 'age': '43', 'address': '113 xyz rd, abc city, MD, 21774'}]:
    print("test pass")
else:
    print("test fail")
