recs = [{"fname": "abc01", "lname": "xyz02", "age": "32",
         "address": "111 xyz rd, abc city, MD, 21774"},
        {"fname": "abc02", "lname": "xyz02", "age": "32",
         "address": "112 xyz rd, abc city, MD, 21774"},
        {"fname": "abc02", "lname": "xyz02", "age": "43",
         "address": "113 xyz rd, abc city, MD, 21774"},
        {"fname": "abc03", "lname": "xyz02", "age": "22",
         "address": "114 xyz rd, abc city, MD, 21774"}
        ]
Findredc = {"fname": "abc02", "lname": "xyz02"}
A = []
for ele in recs:
    found = True
    for i in Findredc:
        if i not in ele or Findredc[i]!=ele[i]:
            found = False
            break
    if found:
        A.append(ele)
print(A)
