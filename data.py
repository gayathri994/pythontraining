from modfunc import count_findredc_in_recs
import json
with open('recdata.json',"r") as fd:
    jsondata = fd.read()
    re = json.loads(jsondata)
if count_findredc_in_recs(re,{"fname": "abc01", "lname": "xyz02"})==1:
    print("test pass")
else:
    print("test fail")
if count_findredc_in_recs(re,{"fname": "abc02", "lname": "xyz02"})==2:
    print("test pass")
else:
    print("test fail")
if count_findredc_in_recs(re,{"fname": "abc02", "lname": "xyz02","age":"43"})==1:
    print("test pass")
else:
    print("test fail")

