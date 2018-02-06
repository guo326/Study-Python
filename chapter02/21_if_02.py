# exercise if

pocket = ['paper', 'handphone']
card = 1
if 'money' in pocket:
    print("택시")
else:
    if card:
        print("택시")
    else:
        print("걸어")

pocket = ['paper', 'handphone']
card = 1
if 'money' in pocket: print("택시")
elif card: print("택시")
else: print("걸어")

if 'money' in pocket: pass
else: print("걸어")
