# Which year do you want to check?
print('Please enter the year you want to check\n')
year = int(input())

if year%4==0:
  if year%100!=0:
    print('Leap year')
  else:
    if year%400==0:
      print('Leap year')
    else:
      print('Not leap year')
else:
  print('Not leap year')