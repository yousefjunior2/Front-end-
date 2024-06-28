# valuesfile = open("values.txt","rt")
# outputfile = open("output.txt","wt")
# print("start")
# sum=0
# for line in valuesfile:
#     sum += int(line)
#     print(line.rstrip(), file=outputfile)
# print("sum:" + str(sum), file=outputfile)
# outputfile.close()
# print("I am done")
valuesfile= open("values.txt","rt")
outputfile= open("output.txt","wt")
print("start")
sum=0
for line in valuesfile:
    sum += int(line) 
    print(line.rstrip(),file=outputfile)
print("sum:"+ str(sum), file=outputfile)
outputfile.close()