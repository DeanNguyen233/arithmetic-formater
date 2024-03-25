def arithmetic_arranger(problems, show_answer=False):
    sorting_problem = ''
    row1 = ''
    row2 = ''
    row3 = ''
    row4 = ''
    
    # Sorting out all of the problem, seperate in between (string1, operator, string2) in 1 problem.
    for problem in problems:
        if '+' in problem:
            operator_index = problem.find('+')
            first_number = problem[:operator_index]
            second_number = problem[operator_index + 1:]
            operator = '+'
            if first_number != range(-9999,9999) or second_number != range(-9999,9999):
                return "Error: Numbers cannot be more than four digits."
        elif '-' in problem:
            operator_index = problem.find('-')
            first_number = problem[:operator_index]
            second_number = problem[operator_index + 1:]
            operator = '-'
            # This is to confirm the number can only be 4 digit maximum
            if first_number != range(-9999,9999) or second_number != range(-9999,9999):
                return "Error: Numbers cannot be more than four digits."
        else:
            return "Error: Operator must be '+' or '-'."
        
        sorting_problem += f"{first_number.strip()} {operator} {second_number.strip()}\n"
            #return "Error: Numbers must only contain digits."

    # Drawing out rows and input the number on that "rows"
    max_row_character = max(len(first_number), len(second_number))
    if max_row_character <= 4:
        row1 += first_number.rjust(max_row_character + 2) + '    '
        row2 += operator.ljust(max_row_character) + second_number.rjust(max_row_character + 1) + '    '
        row3 += '-'*(max_row_character + 2) + '    '

        # Calculate the result of the Arithmetic
        if show_answer == True:
            if operator == '+':
                result = str(int(first_number) + int(second_number))
            elif operator == '-':
                result = str(int(first_number) - int(second_number))
            else:
                return "Error: Operator must be '+' or '-'."
            row4 += result.rjust(max_row_character + 2) + '    '
    else:
        return "Error: Too many problems."
    return sorting_problem

print(arithmetic_arranger(["32+698", "3801-2", "45+43", "123 +49"]))


