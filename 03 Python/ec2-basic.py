print("Welcome to Aws Resource creation")
instance_type = str(input("Enter the instance type: "))

if instance_type == "t2.micro":
    print("creating instance of type: ", instance_type)
    print("Please Pay 2$. ")
elif instance_type == "t2.small":
    print("creating instance of type: ", instance_type)
    print("Please Pay 5$. ")
elif instance_type == "t2.medium":
    print("creating instance of type: ", instance_type)
    print("Please Pay 10$. ")

else:
    print("Sorry!!!, You not authorised create instance type other than : ", instance_type)