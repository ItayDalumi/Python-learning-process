def person(**kwargs):
    print(kwargs) # the output is a dictionary of all the things we set in the function input
    print(type(kwargs)) # the type is dict
    
    if "age" in kwargs:
        print("person's age = ", kwargs.get("age"))

person(name="itay", age=16, hobbies="code") # returns: {'name': 'itay', 'age': 16, 'hobbies': 'code'}



#real world example:
def order_pizza(name, address, **toppings): #toppings is kwargs
    price = 10
    
    print("-------------------------")
    print("order:")
    print("-------------------------")
    
    print("name: " + name)
    print("adress: ", address)
    print("-------------------------")
    print("extras:")
    
    for i in toppings:
        print(i)
        price = price + 1
        
    print("-------------------------")
    print("total price =", price)

order_pizza("itay", "Israel wdwadawd", red_onion=True, Tomato=True)