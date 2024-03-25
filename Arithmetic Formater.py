def arithmetic_arranger(problems, show_answer=False):
    arranged_problems = ''
    for problem in problems:
        if '+' in problem:
            operator_index = problem.find('+')
            first_number = problem[:operator_index]
            second_number = problem[operator_index + 1:]
            operator = '+'
        elif '-' in problem:
            operator_index = problem.find('-')
            first_number = problem[:operator_index]
            second_number = problem[operator_index + 1:]
            operator = '-'
        else:
            return "Error: Operator not found in problem"
        arranged_problems += f"{first_number.strip()} {operator} {second_number.strip()}\n"

    return arranged_problems

print(arithmetic_arranger(["32+698", "3801-2", "45+43", "123 +49"]))


