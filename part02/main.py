from part02.account_user import User


def run():
  wrong_email = True
  """for key, value in {
    "Welcome": "Welcome to Dario's Flight Club.\nWe find the best flight deals and email you.",
    "Question 1": input("What is you first name?\n"),
    "Question 2": input("What is your last name?\n"),
    "Question 3": input("What is your email address?\n"),
    "Question 4": input("Type your email again.\n"),
    "You're in": "You're in the club!"
  }.items():
    if value != input():
      print(key)
"""
  print("Welcome to Dario's Flight Club.\nWe find the best flight deals and email you.")
  first_name = input("What is you first name?\n")
  last_name = input("What is your last name?\n")  
  while wrong_email:
    email=input("What is your email address?\n")
    verify_email=input("Type your email again.\n")
  
    if email == verify_email:
      user = User(first_name, last_name, email)
      user.user_register()
      print("You're in the club!")
      wrong_email = False
    else:
      print("The emails aren't the same. Re-type the emails.")