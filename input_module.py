def get_input():
    try:
        return float(input("Enter student score: "))
    except ValueError:
        return None
