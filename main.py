def modeSelect():
  print("-----------------------------------")
  print("")
  print("Please select an option")
  print("")
  print("(1) Restoring Division Method")
  print("(2) Non-Restoring Division Method")
  print("")
  print("-----------------------------------")
  mode = int(input("\n"))
  print("\n")
  return mode

def twosComp(num):
  #1's Complement
  for i in range(len(num)):
    num[i] = "1" if num[i] == "0" else "0"

  #Creating "1" for whatever byte size needed
  one = ["0" for i in range(len(num))]
  one[-1] = "1"

  return addition(num, one)[0]

def addition(num1, num2, E="0"):
  #while len(num1) < len(num2):
    #num1.insert(0, E)
  #Bringing E back into the equation
  if len(num1) < len(num2):
    num1.insert(0, E)
    
  result = ["0" for i in num1] #Generate empty list
  carry = False
  i = len(num1)-1

  #Going from left to right
  while i >= 0:
    if carry:
      if num1[i] == num2[i]:
        result[i] = "1"
        if num1[i] == "0":
          carry = False
      else:
        result[i] = "0"
    else:
      if num1[i] == num2[i]:
        result[i] = "0"
        if num1[i] == "1":
          carry = True
      else:
        result[i] = "1"
    i -= 1

  num1.pop(0) #Because Python lists are fun
    
  return (result, carry)

def checkOverflow(A, compB, E):
  carry = addition(A, compB, E)[1]
  return True if carry else False
  
def restoring(divisor, dividend):
  #Divide by 0 check
  if "1" not in divisor:
    print("Divide By 0 Error")
    return
  
  
  B = list(divisor)
  n = len(dividend)
  temp = list(dividend)
  E = temp.pop(0)
  A = temp[:n//2] #First half
  Q = temp[n//2:] #Second half
  addSubCount = 0
  iterations = 0

  #Overflow check
  compB = twosComp(B)
  if not checkOverflow(A, compB, E):
    print("Error: Overflow")
    return
      

  #Table formatting
  print("\n")
  print("E |            A               |             Q              |   Operation")
  print("\n")
  print(E, "|", A, "      |", Q, "      |   Initial Values")
  print("\n")

  #Division Algorithm
  for i in range(len(Q)):
    iterations += 1
    #Left Shift
    E = A.pop(0)
    A.append(Q.pop(0))
    Q.append("_")
    print(E, "|", A, "      |", Q, "      |   Shift left")

    #Check Sign Bit
    prev = A.copy()
    if E != "0": #Add 
      A = addition(A, compB, E)[0]
      E = A.pop(0)
      print(E, "|", A, "      |", Q, "      |   Add")
    else: #Subtract
      A = addition(A, compB, E)[0]
      E = A.pop(0)
      print(E, "|", A, "      |", Q, "      |   Subtract")
    addSubCount += 1
    
    #Check Sign Bit Again
    if E == "0": #Success
      Q.pop()
      Q.append("1") #Q0 = 1
      print(E, "|", A, "      |", Q, "      |   Set Q0 = 1")
    else: #Not a success
      Q.pop()
      Q.append("0") #Q0 = 0
      A = prev #Restoring
      print(E, "|", A, "      |", Q, "      |   Restore")
      print("")

  #Signs must match
  if divisor[0] != dividend[0]:
    Q.insert(0, "1")

  print("\n\n")
  print("Remainder:", A)
  print("Quotient: ", Q)
  print("Iterations:", iterations)
  print("Additions/Subtractions:", addSubCount)
  return

def nonRestoring(divisor, dividend):
#Divide by 0 check
  if "1" not in divisor:
    print("Divide By 0 Error")
    return
  
  B = list(divisor)
  n = len(dividend)
  temp = list(dividend)
  E = temp.pop(0)
  A = temp[:n//2] #First half
  Q = temp[n//2:] #Second half
  iterations = 0
  addSubCount = 0

  #Overflow check
  compB = twosComp(B)
  if checkOverflow(A, compB, E):
    print("Error: Overflow")
    return
      
  #Table formatting
  print("\n")
  print("E |            A               |             Q              |   Operation")
  print("\n")
  print(E, "|", A, "      |", Q, "      |   Initial Values")
  print("\n")

  #Division Algorithm
  for i in range(len(Q)):
    iterations += 1
    #Left Shift
    E = A.pop(0)
    A.append(Q.pop(0))
    Q.append("_")
    print(E, "|", A, "      |", Q, "      |   Shift left")

    #Check Sign Bit
    prev = A.copy()
    if E != "0": #Add 
      A = addition(A, B, E)[0]
      E = A.pop(0)
      print(E, "|", A, "      |", Q, "      |   Add")
    else: #Subtract
      A = addition(A, compB, E)[0]
      E = A.pop(0)
      print(E, "|", A, "      |", Q, "      |   Subtract")
    addSubCount += 1
      
    #Check Sign Bit Again
    if E == "0": #Success
      Q.pop()
      Q.append("1") #Q0 = 1
      print(E, "|", A, "      |", Q, "      |   Set Q0 = 1")
    else: #Not a success
      Q.pop()
      Q.append("0") #Q0 = 0
      print(E, "|", A, "      |", Q, "      |   Set Q0 = 0")
      print("")

  #Signs must match
  if E == "1":
    A = addition(A, B, E)

  print("\n\n")
  print("Remainder:", A)
  print("Quotient: ", Q)
  return

def main():

  mode = modeSelect()

  divisor = input("Please enter the divisor \n")
  dividend = input("Please enter the dividend \n")

  if mode == 1:
    #Restoring
    restoring(divisor, dividend)
  if mode == 2:
    #Non-Restoring
    nonRestoring(divisor, dividend)

if __name__ == "__main__":
  main()