print("make a seperate file that imports the Admin, User, and Privileges classes") 
from Admin import Admin, User, Privileges # pyright: ignore[reportMissingImports]
print("create an instance of the Admin class") 
admin_user = Admin("Charlie", "Brown") 
print("call the describe_user method") 
admin_user.describe_user()
print("call the show_privileges method from the Privileges class") 
admin_user.privileges.show_privileges()
# This code imports the User, Privileges, and Admin classes from another file named Admin.py
# It then creates an instance of the Admin class and calls methods to describe the user
# and show their privileges. 