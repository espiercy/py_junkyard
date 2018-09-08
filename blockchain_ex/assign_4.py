#Write a normal function that accepts another function as an argument. Output the result of that other function in your “normal” function.

#ok, here goes my normal function
def normal_function(another_function, *pass_to_another_function, my_var=1.0):
    for arg in pass_to_another_function:
        updated_var = another_function(arg)
        #this works for me -- it's still more less demonstrating what was requested in the assignment.
        print(f'{my_var:-^20.2f} {updated_var}')


def func_i_pass(passed_parm):
    return str(passed_parm).upper() + ' from in func.'

#demonstrate with default my_var
normal_function(func_i_pass, 'to upper')

#demo custom my_var
normal_function(func_i_pass, 'in func passed', my_var=1.1)

#pass it a lambda instead
normal_function(lambda a : a * 2, 'twice ')

#can take multiple params, but NEED to declare my_var if it is to be used
normal_function(lambda a : a * 2, *['twice too ', 'also twice '], my_var=1.2)