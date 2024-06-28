inp_strings=open("strings_input.txt")
out_strings=open("strings_output.txt","wt")
print("starting")
result=""
for line in inp_strings:
    if line.strip() =="I":
        result += " " + line.strip()
    elif line.strip() =="Almdrasa":
        result += " " + line.strip()
    else:    
     result += " " + line.strip().lower()
print(result)
print(result.strip(),file=out_strings)
out_strings.close()
# in_strings=open("strings_input")
# stringsfile=open("strings_output","wt")
# print("starting")
# answer=""
# for index,line in enumerate(in_strings):
#     if index == 0:
#         answer += " " + line.strip()
#     elif index == 2:
#         answer += " " + line.strip()    
#     else:    
#      answer += " " + line.strip().lower()
# print(answer)
# print(answer.strip(),file=stringsfile)
# stringsfile.close()