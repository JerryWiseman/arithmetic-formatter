def exceptions(num1, num2, operator):
    try:
        int(num1)
    except:
        return "Error: Numbers must only contain digits."
    try:
        int(num2)
    except:
        return "Error: Numbers must only contain digits."
    try:
        if(len(num1)>4 or len(num2)>4):
            raise BaseException
    except:
        return "Error: Numbers cannot be more than four digits."
    try:
        if operator != '+' and operator != '-':
            raise BaseException
    except:
        return "Error: Operator must be '+' or '-'."
    return None


def arithmetic_arranger(problems, mode=False):   
    try:
        if len(problems) > 5:
            raise BaseException
    except:
        return "Error: Too many problems."
    
    row1 = row2 = row3 = row4 = ''
    space1 = '    '
    space2 = ' '
    problem1 = True
    for prob in problems:
        arr2 = prob.split()
        exception = exceptions(arr2[0],arr2[2],arr2[1])
        if exception != None:
            return exception
        if arr2[1] == '+':
            result = str(int(arr2[0]) + int(arr2[2]))
        else:
            result = str(int(arr2[0]) - int(arr2[2]))
        width = max(len(arr2[0]),len(arr2[2]))
        if problem1 == True:
            row1 += arr2[0].rjust(width+2)
            row2 += arr2[1] + space2 + arr2[2].rjust(width)
            row3 += '-'*(width+2)
            row4 += result.rjust(width+2)
            problem1 = False
        else:
            row1 += arr2[0].rjust(width+6)
            row2 += arr2[1].rjust(5) + space2 + arr2[2].rjust(width)
            row3 += space1 + '-'*(width+2)
            row4 += space1 + result.rjust(width+2)  
    if mode == True:      
        return row1 + '\n' + row2 + '\n' + row3 + '\n' + row4
    return row1 + '\n' + row2 + '\n' + row3 