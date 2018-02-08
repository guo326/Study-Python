import sys

print(sys.path)

sys.path.append("C:\Python\exercise\chapter04/42_module/")

print(sys.path)

import mod2
print(mod2.sum(3, 4))
