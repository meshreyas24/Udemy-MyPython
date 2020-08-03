#more on strings

full_name = "\tJohnny\nsmith" #t for spacing n for new line
print(full_name)

first_name = "johnny"
last_name = "smith"

full_name = first_name + "  " + last_name #Joining Strings concatenate
print(full_name.title())

print(first_name.upper() + " " +last_name.upper()) #Upper Case / lower() for lower case

print(4+2) #Result 6
print("4" + "2") #Joining Strings concatenate #Result 42

message = "Hello, how are you doing today? What is going on at home ?"
message = message.lower()
print(message) #message in lower case

h_count = message.count("h")
print("Our Message has " + str(h_count) +"h's in it.") #Count of h in message








