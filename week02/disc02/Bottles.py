bottles = 99
take = 1

def pass_it(around):
    bottles = 98
    return take

remaining = bottles - pass_it(bottles)
bottles = remaining

# 1) What determines how many different frames appear in an environment diagram?
# a) The number of functions defined in the code
# b) The number of call expressions in the code
# c) The number of return statements in the code
# d) The number of times user-defined functions are called when running the code
# Answer: d)

# 2) What happens to the return value of pass_it(bottles)?
# a) It is used as the new value of remaining in the global frame
# b) It is used as the new value of bottles in the global frame
# c) It is used as the new value of pass_it in the global frame
# d) None of the above
# Answer: a)

# 3) What effect does the line bottles = 98 have on the global frame?
# a) It temporarily changes the value bound to bottles in the global frame.
# b) It permanently changes the value bound to bottles in the global frame.
# c) It has no effect on the global frame.
# Answer: c)