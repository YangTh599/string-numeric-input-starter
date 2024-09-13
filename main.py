# Thayer Yang
# 13 SEP 2024
# String & Numeric Input 

# Task 1

first_name = input("What is your first name?\n")
program = input("What program do you take at CTC?\n")

print(first_name.capitalize()+" is a student at CTC. They are doing "+program)




# Task 2

age = int(input("How old are you?\n")) 

while isinstance(age, int) == False:
    print("Please enter an integer.")
    age = int(input("How old are you?\n"))
    if isinstance(age, int) == True:
        break


print(first_name+" is "+str(age)+" years old. In 10 years they'll be "+str(age+10)+" years old.")





# Task 3
num_of_family = int(input("How many family members do you have?\n"))
while isinstance(num_of_family, int) == False:
    print("Please enter an integer.")
    age = int(input("How many family members do you have?\n"))
    if isinstance(num_of_family, int) == True:
        break
print(f"{first_name} has {str(num_of_family)} family members in their family.")




# Task 4
# Comment
# Comment

cm_constant = 2.54
height_in = float(input("How tall are you in inches.\n"))
while isinstance(height_in, int) == False or isinstance(height_in, float) == False:
    print("Please enter an integer.")
    height_in = int(input("How many family members do you have?\n"))
    if isinstance(height_in, int) == True or isinstance(height_in, float) == True:
        break

print(first_name+" is "+str(height_in)+" inches tall which means they are "+str(cm_constant*height_in)+" cm tall.")



# Task 5
# Comment
# Comment





# Part 5
# Comment
# Comment
