values = [10, 5, 6, 0, 9, 8, "hello", 2]

for value in values:
    try:
        print( 10 / int(value) )
    except ZeroDivisionError as e:
        pass
    except ValueError as e:
        print("Hello World")
        raise
    else:
        print("No exception")
        
    

