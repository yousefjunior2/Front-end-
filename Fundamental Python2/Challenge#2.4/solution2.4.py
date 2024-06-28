import re
dialouge="almdrasa is your way to learn programming the right way. almdrasa badges motivatestudents to do more.almdrasa quizes help students practice on what they have learned through the course. almdrasa courses are one of a kind because they were made by professionals. almdrasa look and feel is one of a kind, almdrasa wishes you a good learning. thanks."

contaner= re.sub("almdrasa \w{4,}","Almdrasa",3,dialouge)
print(contaner)
