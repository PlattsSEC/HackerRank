# Complete the function below.


def  function( x):
    try:
        if x >= 1 and x <= 1000:
            return x ** 2
            
    except ValueError:
        print("Input must be between 1 and 1000")
