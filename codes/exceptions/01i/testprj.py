import logging

values = [10, 5, 6, 0, 9, 8, "hello", 2]

logging.basicConfig(filename='myapp.log', level=logging.INFO)

for value in values:
    try:
        print( 10 / int(value) )
    except ValueError as e:
        print(str(e))
        logging.exception(e)
    except ZeroDivisionError as e:
        pass
    except Exception as e:
        logging.exception(e)
        
    

