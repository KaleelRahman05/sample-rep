sub= ['tamil','english','maths','science','social']
tot = 0; avg = 0
for i in range(len(sub)):
    mark=int(input(f"enter marks for {sub[i]}: "))
    tot+=mark
    avg = tot/len(sub)
print("Your total is:",tot)
print("Your average is:",avg)
if tot >=490:
    print("Great work! keep it up ✔")
elif tot>=300 and tot<=400:
    print("good keep working!")
elif tot>=250 and tot<=300:
    print("this time you passed!")
elif tot<=230:
    print("failed...")
