# while

"""
while <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    <수행할 문장3>
    ...
"""

treehit = 0
while treehit < 10:
    treehit = treehit + 1
    print("나무를 {0}번 찍었습죠" .format(treehit))
    if treehit == 10:
        print("나무 넘어가요")
