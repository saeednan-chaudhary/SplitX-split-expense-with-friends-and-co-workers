# The final product

# DATABASE USING SQLITE3
import sqlite3
connection= sqlite3.connect('Splitx.db')
cursor=connection.cursor()
cursor.execute('''  CREATE TABLE IF NOT EXISTS
 users(Id INTEGER PRIMARY KEY AUTOINCREMENT, 
 name NOT NULL
 )
 ''')



# 1----
# building a database to store user's data
UsersDatabase={}

# Function for adding the users
def adduser_func():
    print("\n\nLet's add your friends and co-workers to split bills.\nPress 0 to stop.\n")

    while True:
        name = input("Add your companion name: ").strip()

        if name == "0":
            break
        if name:
           cursor.execute(
              "INSERT INTO users (name) VALUES (?)",
                          (name,) 
                          )
           connection.commit()
           print(name,'has been added')
           

# -----------------------------------------------------------------------------
#  2----
# dash board_____input total amount
# T_amount =total amount
def split_menu():
    
        # cursor.execute("""CREATE TABLE IF NOT EXISTS bill(id INTEGER AUTOINCREMENT,
# bill_name TEXT NOT NULL,
# amount INTEGER NOT NULL 
# )
# """)

  def direct_split():
      
    cursor.execute("SELECT id, name FROM users")
    users = cursor.fetchall()

    if not users:
        print("----Add at least two user before splitting the amount.")
    else:
        number_of_people = len(users)
        T_amount=input("Enter the amount : ")
        while True:
          try:
            T_amount=int(T_amount)
            print(f'no.of persons: {number_of_people}')
            print(f"Amount per person = {T_amount / number_of_people:.2f}")
            return
          except:
            T_amount=input("\n----Try number like 500.\nEnter the amount : ")

  def bill_split():
      cursor.execute("SELECT id, name FROM users")
      users = cursor.fetchall()
      number_of_people = len(users)
      while True:
          try:
              Ebill = int(input("Enter the Electricity bill: "))
              gbill = int(input("Enter the gas bill: "))
              wbill = int(input("Enter the water bill: "))
              wfbill = int(input("Enter the wifi bill: "))
          except ValueError:
              print("----Please enter whole numbers only, like 25.")
              continue

          total_bill = Ebill + gbill + wbill + wfbill
          print(f"\n-Your total bill is: {total_bill:.2f}")
          print(f"--Amount per person = {total_bill / number_of_people:.2f}")
          break






  while True:

    menu=input("0 = Go back 1 = Direct split  2 = Bill split :")
    if menu=="1":
      direct_split()
    if menu=="2":
      bill_split()
    if menu == "0":
       break  






# -----------------------------------------------------------------------------
# 3----



# ---------------------------remove user    
def remove_user():
  
  user_id = input("Enter the ID of the user to remove (or 0 to cancel): ").strip()

  if user_id == "0":
      return

  if not user_id.isdigit():
      print("Please enter a numeric ID.")
      return

  cursor.execute("DELETE FROM users WHERE id = ?", (int(user_id),))
  connection.commit()

  if cursor.rowcount > 0:
      print("User removed.")
  else:
      print("No user found with that ID.")
# -------------------------------------------------------------------show list
def show_users_list():
  cursor.execute('SELECT Id, name FROM users ORDER BY Id')
  users= cursor.fetchall()
  if not users:
    print("----No users have been found")
    return
  for user_id, name in users:
    print(f'{user_id}:{name}')
# -----------------------------------------------------------------------menu
def show_lists():
  while True:
    menu=input("1 = Show Users   2 = Remove Users  :")
    if menu=='0':
          break 
    else: 
      if menu=="1":
        show_users_list()
      if menu=="2":
        remove_user()
    


# -----------------------------------------------------------------------------

# 4----
  # Welcoming the guest

  
print ("             Hey There, Welcome to SplitX\n")

print("Press the following keys to move around.")
while True:
  start_sys=input("\n1 = Add User 2 = Go to split 3 = Show user's list 4 = Quit:")
  if start_sys=="1":
      adduser_func()



  # if already added pass
  if start_sys=='2':
    split_menu()

  if start_sys=='3':
    show_lists()

  if start_sys=='4':
     print("----goodbye")
     break  

connection.close()