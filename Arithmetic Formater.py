def arithmetic_arranger(problems, show_answer=False):
    sorting_problem = ''
    row1 = ''
    row2 = ''
    row3 = ''
    row4 = ''
    
    if len(problems) > 5:
        return "Error: Too many problems."
    
    for problem in problems:
        if '+' in problem:
            operator_index = problem.find('+')
            first_number = problem[:operator_index].strip()
            second_number = problem[operator_index + 1:].strip()
            operator = '+'
            if not first_number.isdigit() or not second_number.isdigit():
                return "Error: Numbers must only contain digits."
            if len(first_number) > 4 or len(second_number) > 4:
                return "Error: Numbers cannot be more than four digits."
        elif '-' in problem:
            operator_index = problem.find('-')
            first_number = problem[:operator_index].strip()
            second_number = problem[operator_index + 1:].strip()
            operator = '-'
            if not first_number.isdigit() or not second_number.isdigit():
                return "Error: Numbers must only contain digits."
            if len(first_number) > 4 or len(second_number) > 4:
                return "Error: Numbers cannot be more than four digits."
        else:
            return "Error: Operator must be '+' or '-'."
        
        # Construct the sorted problem string
        sorting_problem += f"{first_number.strip()} {operator} {second_number.strip()}\n"

        # Sorting the formats
        row1 += first_number.rjust(5) + '    '
        row2 += operator + second_number.rjust(4) + '    '
        row3 += '-' * 5 + '    '

        # Calculate the result of the arithmetic if show_answer is True
        if show_answer == True:
            if operator == '+':
                result = str(int(first_number) + int(second_number))
            elif operator == '-':
                result = str(int(first_number) - int(second_number))
            row4 += result.rjust(5) + '    '
        if show_answer == False:
            row4 = ''
    
    # Combine the rows
    sorting_problem = '\n'.join([row1.rstrip(), row2.rstrip(), row3.rstrip(), row4.rstrip()])
    
    # Return the arranged problems
    return sorting_problem

print(arithmetic_arranger(["32-698", "3801-2", "45+43", "123 +49", "32-698"], show_answer=False))
