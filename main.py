import input_module
import logic_module
import output_module

def start():
    score = input_module.get_input()
    grade = logic_module.calculate_grade(score)
    output_module.display_grade(score, grade)

if __name__ == "__main__":
    start()
