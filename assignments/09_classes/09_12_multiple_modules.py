print("make a separate file that imports the User and Admin classes from their respective modules") 
from User import User # pyright: ignore[reportMissingImports]
from Admin import Admin, Privileges # pyright: ignore[reportMissingImports]
print("create an instance of the Admin class") 
admin_user = Admin("David", "Wilson") 
print("call the describe_user method") 
admin_user.describe_user()
print("call the show_privileges method from the Privileges class") 
admin_user.privileges.show_privileges()
# This code imports the User class from one module and the Admin and Privileges classes from another module.
# It then creates an instance of the Admin class and calls methods to describe the user
# and show their privileges. 