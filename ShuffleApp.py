
import random                       
from datetime import datetime

filename = 'sortedbygroups.txt'     #Name of a file where the output will be saved
orderList = []                      #List of everything from "orders.txt" will be stored here

try:
  file = open("orders.txt", "r")        
except FileNotFoundError:           #code that grabs exception while not finding a file in a folder
  print("You need to have 'orders.txt' in the same folder as program.")


def Program():
  for line in file:                                     #Script that takes the content from
    stripped_line = line.strip()                        #"orders.txt" and appends line by line
    line_list = stripped_line.split()                   #whole content into the list named
    orderList.append(line_list)                         #"orderList" and closes the file.
  file.close()                                          #
  print('You have ' + str(len(orderList)) + ' orders')  #Prints a message about how many orders you have

  print("How many groups you have to work with?")       #Takes the info about the groups
  groups = int(input("ilość grup:"))                    #and stores it in "groups" variable

  random.shuffle(orderList)                             #Shuffles the content of "orderList"
  ef = len(orderList)/groups                            
  ammount = round(ef)                                   #First line calculates and second is rounding up
                                                        #the ammount of orders that groups should get

  with open(filename, 'a') as textfile:       #Makes a file named 'sortedbygroups.txt'
    for i in range(groups):
      textfile.write(f'Group{i + 1}:\n')      #Takes the number of iteration and adds 'Group' to it and writes it to the file
      for j in range(ammount):                #Checks the amount of orders, that group should have
        try:
          textfile.write(str(orderList[0]).strip("['']") + '\n')    #Writes the ammount of orders to the group above from the orderList list
          orderList.pop(0)                                          #erases first order on the list (The one that is added above)
        except:
          print('')                                                 #if any errors here, just skip

  if len(orderList) > 0:                                            #If there are some orders left in orderList
    with open(filename, 'a') as textfile:                           #it adds the rest to the last group made in the textfile named 'sortedbygroups.txt'
      for i in range(len(orderList)):                               
        textfile.write(str(orderList[0]).strip("['']") + '\n')
        orderList.pop(0)



  with open(filename, 'a') as textfile:                             #This part of code just adds timestamp
    now = datetime.now()                                            #when the file has been made
    today = now.strftime("%d/%m/%Y %H:%M:%S")
    textfile.write("Generated at: " + str(today) + '\n\n')
    textfile.close()

Program()


print('Press "ENTER" to exit...')
input()