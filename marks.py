import sys
if len(sys.argv)==4:
    m1 = float(sys.argv[1])
    m2 = float(sys.argv[2])
    m3 = float(sys.argv[3])

else:
    m1 = m2 = m3 =80

total = m1+m2+m3
if total<120:
    print("Status : fail")
else:
    print("Status  :Pass")
print("Total marks:",total)