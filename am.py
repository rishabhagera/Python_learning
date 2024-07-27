dictionary1={
    "1":"one",
    "2":"two",
    "3":"three"
}

inp=input(">")
out=""
for i in inp:
        out+=dictionary1.get(i,"i")+" "
print(out)