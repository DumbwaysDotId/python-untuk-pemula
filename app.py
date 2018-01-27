# if else conditional

age = raw_input("Please input your age: ")

#validation
if age.isdigit() == False:
    print("Please input correct age format")
else:
    age = int(age)

    if age < 13:
      print("You are not allowed to watch this movie!")
    elif age >= 13:
      print("You are allowed to watch this movie")
