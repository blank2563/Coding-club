def beginner():
    menu = {'Carbonara' : 18.99, 
            'Spaghetti' : 17.49, 
            'Pizza'     : 24.99, 
            'Gnochi'    : 14.99, 
            'Risotto'   : 22.49, 
            'Lasagna'   : 49.99, 
            'Tiramisu'  : 11.99, 
            'Gelato'    : 7.99}
    price = 0

    
    while True:
        print('Please enter your order')
        item = input()
        if item == '0':         # Check for end of order
            break
        elif item in menu:      # Check that item is available
            price += menu[item]
        else:                   # Wrong input, outputing error message
            print("Sorry, our restaurant don't make that food.")
            
    print(f"Your order's total is ${round(price * 1.15, 2)}.")

def intermediate():
    menu = {'Carbonara' : 18.99, 
            'Spaghetti' : 17.49, 
            'Pizza'     : 24.99, 
            'Gnochi'    : 14.99, 
            'Risotto'   : 22.49, 
            'Lasagna'   : 49.99, 
            'Tiramisu'  : 11.99, 
            'Gelato'    : 7.99}
    
    drink = {'Water'    : 1.99, 
             'Juice'    : 3.99, 
             'Soda'     : 2.49} 
    
    alcohol = {'Beer'       : 4.99, 
               'Red wine'   : 9.99, 
               'White wine' : 11.99}
    price = 0
    
    print('How old are you?')
    age = int(input())
    
    if age < 19 and age > 0:        # Minor, can'd order alcohol
        menu.update(drink)
    elif age >= 19 and age < 120:   # Old enough to order alcohol
        menu.update(drink)
        menu.update(alcohol)
    else:                           # User entered an age that's either less than 0 or way too large, terminate program
        return(print("Human can't live that long/you seems to be an unborn baby, get out of my restaurant!!!"))
    
    while True:
        print('Please enter your order')
        item = input()
        if item == '0':         # Check for end of order
            break
        elif item in menu:      # Check that item is available
            price += menu[item]
        elif item in alcohol:   # Check for minor trying to buy alcohol
            print('You are too young to be ordering this drink.')
        else:                   # Wrong input, outputing error message
            print("Sorry, our restaurant don't make that food.")
            
    print(f"Your order's total is ${round(price * 1.15, 2)}.")

def advance():
    menu = {'Carbonara' : 18.99, 
            'Spaghetti' : 17.49, 
            'Pizza'     : 24.99, 
            'Gnochi'    : 14.99, 
            'Risotto'   : 22.49, 
            'Lasagna'   : 49.99, 
            'Tiramisu'  : 11.99, 
            'Gelato'    : 7.99}
    
    drink = {'Water'    : 1.99, 
             'Juice'    : 3.99, 
             'Soda'     : 2.49}
    
    alcohol = {'Beer'       : 4.99, 
               'Red wine'   : 9.99, 
               'White wine' : 11.99}
    price = 0
    order = []
    
    print('How old are you?')
    age = int(input())
    
    if age < 19 and age > 0:        # Minor, can'd order alcohol
        menu.update(drink)
    elif age >= 19 and age < 120:   # Old enough to order alcohol
        menu.update(drink)
        menu.update(alcohol)
    else:                           # User entered an age that's either less than 0 or way too large, terminate program
        return(print("Human can't live that long/you seems to be an unborn baby, get out of my restaurant!!!"))
    
    while True:
        print('Please enter your order')
        item = input()
        if item == '0':         # Check for end of order
            break
        elif item in menu:      # Check that item is available
            price += menu[item]
            order.append(item)
        elif item in alcohol:   # Check for minor trying to buy alcohol
            print('You are too young to be ordering this drink.')
        else:                   # Wrong input, outputing error message
            print("Sorry, our restaurant don't make that food.")
            
    print(f"Your order's total is ${round(price * 1.15, 2)}.")
    print(f"Items in your order are: {', '.join(order)}")

