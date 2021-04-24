print("***   WELCOME TO COVID-19 RISK PREDICTION PROGRAM USER INTERFACE!   ***\n\n"
"(Please answer all the questions by typing YES or NO. The program is not case sensitive.)\n")

while True :
  age = input('Are you a cigarette addict older than 75 years old? ').lower()
  if age == 'no' :
    age=False
    break
  elif age == 'yes' :
    age = True
    break
  else :
    print(' - Pleae enter only one of YES or NO phrases.')

while True :
  chronic = input('Do you have a severe chronic disease? ').lower()
  if chronic == 'no' :
    chronic = False
    break
  elif chronic == 'yes' :
    chronic = True
    break
  else :
    print(' - Pleae enter only one of YES or NO phrases.')

while True :
  immune = input('Is your immune system too weak? ').lower()
  if immune == 'no' :
    immune = False
    break
  elif immune == 'yes' :
    immune = True
    break
  else :
    print(' - Pleae enter only one of YES or NO phrases.')

risk = age or chronic or immune
if (risk == True) :
  print("\nWatch out! You are IN risky group.")
else :
  print("\nCongratulations! You are NOT IN risky group :)")
