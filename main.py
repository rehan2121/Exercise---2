# Author : Rehan Pathan
# Help By: NoOne

import time

current_hour = time.localtime().tm_hour

user_name = input("What is your name? ")

if (current_hour < 12):
  print("\nGood Morning", user_name, "Sir\n")

elif (current_hour < 16):
  print("\nGood Afternoone", user_name, "Sir\n")

elif (current_hour < 20):
  print("\nGood Night", user_name, "Sir\n")

else:
  print("Replaced Error Message")
