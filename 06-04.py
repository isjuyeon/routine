paragraph="Bob hit a ball, the hit BALL flew far after it was hit."
banned=["hit"]
a=paragraph.split()
for i in banned:
    while i in paragraph:
        a.remove(i)
#여기서 i가 for문에서 while문으로 넘어갈 때 인식이 안되는 것 같은데 원래 그런건가요