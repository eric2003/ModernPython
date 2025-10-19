import logging

values = [10, 5, 6, 0, 9, 8, "hello", 2]

logging.basicConfig(filename='myapp.log', level=logging.INFO)

for value in values:
    try:
        print( 10 / int(value) )
        raise AttributeError
    except (ValueError, ZeroDivisionError) as e:
        pass
    except AttributeError as e:
        print("Hello World")
        continue
    except Exception as e:
        logging.exception(e)
        
    

