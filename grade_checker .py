def get_score():
    try:
        return float(input("Enter student score: "))
    except ValueError:
        print("Please enter a number.")
        return get_score()

def check_grade(score):
    if score >= 70: return "A"
    elif score >= 60: return "B"
    elif score >= 50: return "C"
    elif score >= 45: return "D"
    elif score >= 40: return "E"
    else: return "F"

def main():
    score = get_score()
    grade = check_grade(score)
    print(f"The grade is: {grade}")

if __name__ == "__main__":
    main()
