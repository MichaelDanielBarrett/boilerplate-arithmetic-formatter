# This is the boilerplate arithmetic arranger source by Michael Barrett done for the Scientific Computing with Python course for freecodecamp.org

# First I want to define the function with inputs

def arithmetic_arranger(problems, answer=False):

    # Start with defining some variables for identifying errors

    error = False
    toomanyproblemserror = False
    operatorerror = False
    operandtypeerror = False
    operandlengtherror = False

    if len(problems) > 5:
        error = True
        toomanyproblemserror = True

    # These are some lists I'll use in the for loop which analyzes the "problems" input
    
    first_number = list()
    second_number = list()
    operator = list()
    width = list()
    result = list()

    # And now for the analysis loop

    for i in problems:
        problem = i.split()
        problem_width = max(len(problem[0]), len(problem[2]))
        if problem[0].isdigit() == True:
            first_number.append(problem[0])
        else:
            error = True
            operandtypeerror = True
            break
        if problem[2].isdigit() == True:
            second_number.append(problem[2])
        else:
            error = True
            operandtypeerror = True
            break
        if problem_width < 5:
            width.append(2 + problem_width)
        else:
            error = True
            operandlengtherror = True
            break
        if problem[1] == '+':
            operator.append(problem[1])
            result.append(int(problem[0]) + int(problem[2]))
        elif problem[1] == '-':
            operator.append(problem[1])
            result.append(int(problem[0]) - int(problem[2]))
        else:
            error = True
            operatorerror = True
            break

    # Check for errors

    if error == True:
        if toomanyproblemserror == True:
            arranged_problems = 'Error: Too many problems.'
        elif operatorerror == True:
            arranged_problems = "Error: Operator must be '+' or '-'."
        elif operandtypeerror == True:
            arranged_problems = 'Error: Numbers must only contain digits.'
        elif operandlengtherror == True:
            arranged_problems = 'Error: Numbers cannot be more than four digits.'
    else:
    # It's time to start arranging things

        first_line = str()
        second_line = str()
        dash_line = str()
        answer_line = str()

        for i in range(len(problems)):
            x1 = width[i] - len(first_number[i])
            x2 = width[i] - (1 + len(second_number[i]))
            x3 = width[i] - len(str(result[i]))
            first_line += x1 * ' ' + first_number[i] + '    '
            second_line += operator[i] + x2 * ' ' + second_number[i] + '    '
            dash_line += width[i] * '-' + '    '
            answer_line += x3 * ' ' + str(result[i]) + '    '

        first_line = first_line.rstrip() + '\n'
        second_line = second_line.rstrip() + '\n'
        dash_line = dash_line.rstrip() + '\n'
        answer_line = answer_line.rstrip() + '\n'
    
    # Now we need to put it all together and return something

        if answer == True:
            arranged_problems = first_line + second_line + dash_line + answer_line.rstrip()
        elif answer == False:
            arranged_problems = first_line + second_line + dash_line.rstrip()

    # and the result
    
    return arranged_problems
