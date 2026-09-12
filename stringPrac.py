s = "0zracee"
t = "0zjracee"

ss = []
tt = []
for i in s:
    ss.append(i)
for i in t:
    tt.append(i)
ss.sort()
tt.sort()

if ss==tt:
    print("True")
else:
    print("False")
