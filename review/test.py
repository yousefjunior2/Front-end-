invaluse= open("values.text","rt")
outvaluse= open("output.text","wt")
print("start with done")
sum=0
for line in invaluse:
    sum += int(line)
    print(line.rstrip(), file=outvaluse)
print("sum ="+ str(sum), file=outvaluse)
outvaluse.close()