days= ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday",]
fahrenheit=[32.00]
celsius=[]

print("Number of days:")
for i in range(len(days)):
  print("{}. {}".format(i+1, days[i]))
option = int(input("Enter day of the week: "))

while option <=7:
  F=0
  C=0
  if option == 1:
    while C<=45:
      celsius.append(C)

      C+= 15 + option
      F= (9.0/5)* C + 32
      fahrenheit.append(F)

  elif option == 2:
    while C<= 45:
      celsius.append(C)
      C+= 15 + option
      F= (9.0/5)*C +32
      fahrenheit.append(F)

  elif option == 3:
    while C<= 45:
      celsius.append(C)
      C+= 15 + option
      F= (9.0/5)*C +32
      fahrenheit.append(F)

  elif option == 4:
    while C<= 45:
      celsius.append(C)
      C+= 15 + option
      F= (9.0/5)*C +32
      fahrenheit.append(F)

  elif option == 5:
    while C<= 45:
      celsius.append(C)
      C+= 15 + option
      F= (9.0/5)*C +32
      fahrenheit.append(F)

  elif option == 6:
    while C<= 45:
      celsius.append(C)
      C+= 15 + option
      F= (9.0/5)*C +32
      fahrenheit.append(F)

  elif option == 7:
    while C<= 45:
      celsius.append(C)
      C+= 15 + option
      F= (9.0/5)*C +32
      fahrenheit.append(F)

  print("-----------------------------")

  print("TEMPERATURE on {}".format(days[option-1]))

  print("Celsius\tFahrenheit ")
  for i in range (len(celsius)):
    print("%d\t\t%.2f"% (celsius[i],fahrenheit[i]))

  print()

  fahrenheit=[32.00]
  celsius=[]
  option+=1

  """print(fahrenheit[0])"""


print(celsius[0])