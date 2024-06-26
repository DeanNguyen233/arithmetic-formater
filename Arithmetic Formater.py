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

        # Max length of the "----" row 3
        max_length = max(len(first_number), len(second_number))

        # Sorting the formats
        row1 += first_number.rjust(max_length + 2) + '    '
        row2 += operator + second_number.rjust(max_length + 1) + '    '
        row3 += '-' * (max_length + 2) + '    '

        # Calculate the result of the arithmetic if show_answer is True
        if show_answer == True:
            if operator == '+':
                result = str(int(first_number) + int(second_number))
            elif operator == '-':
                result = str(int(first_number) - int(second_number))
            row4 += result.rjust(max_length + 2) + '    '
        if show_answer == False:
            row4 = ''
    
    # Check different format if show_answer is True
    if show_answer == True:
        sorting_problem = row1.rstrip() + '\n' + row2.rstrip() + '\n' + row3.rstrip() + '\n' + row4.rstrip()
    if show_answer == False:
        sorting_problem = row1.rstrip() + '\n' + row2.rstrip() + '\n' + row3.rstrip() + row4.rstrip()
    
    # Return the arranged problems
    return sorting_problem

print(str(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)))
print(str("   32         1      45      123      988\n- 698    - 3801    + 43    +  49    +  40\n-----    ------    ----    -----    -----\n -666     -3800      88      172     1028"))
