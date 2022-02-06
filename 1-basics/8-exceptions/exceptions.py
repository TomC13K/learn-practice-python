
# EXCEPTIONS  - comment/uncomment one to test
try:                                            # try to run code
    print(x)
    #print("a")
except:                                         # error handling
    print("exception occured")
else:                                           # execute code when no error
    print("code executed without errors- ALL good")
finally:                                        # execute always
    print("finally statement always runs - FINISHED")


# Handling specific error
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("some other error")

