#its a leap year calculation program
year = int(input("Which year do you want to check? "))

#Write your code below this line 👇
if year % 4 == 0 :
  if year % 100 == 0:
    if year % 400 == 0:
      print("its a leap year")
    else:
      print("its not a leap year")
  else:
    print("its a leap year")
else:
  print("its not a leap year")
