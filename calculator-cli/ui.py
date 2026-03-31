from operation import decode_operation
from exceptions import BadInputException


def ui() -> None:
    """
    main ui worker for the calculator
    """
    
    print("_____________ Calculator _____________")
    print("Enter 'q' to exit\n")
    
    while True:
        user_input = input("What operation? ")
        
        # exit condition
        if user_input == "q":
            return
        
        try:
            operation = decode_operation(user_input)
        except Exception as e:
            print(e)
            print()
            continue
            
        print(f"Operation decoded as {operation}")
        print()

        try:
            num1 = take_input(1)
            num2 = take_input(2)
            print()
        except BadInputException as e:
            print(e)
            print()
            continue
        
        result: float = operation.operate(num1, num2)
        print(f"Result is {round(result, 4)}\n")
        continue
        

def take_input(input_number: int) -> float:
    """
    function for taking input from the cli
    
    Args:
        input_number: the input number to ask to the user
        
    Returns:
        the input taken from the user
        
    Raises:
        BadInputException: in case of invalid input
    """
    
    user_input = input(f"Enter number {input_number}: ")
    
    try:
        return float(user_input)
    except:
        raise BadInputException("Invalid input, must be a number.")
    
