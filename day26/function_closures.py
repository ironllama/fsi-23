# 1. Write a function called 'more_power' that takes one integer argument, called
#     'total' which will be a running total of the power.
#     This function will return another function called 'whatever' that also
#     takes one integer argument, which be added to the 'total' and then will
#     print out the current value of 'total'. Everytime the enclosed function
#     is called, the total will increase.
#    Example:
#     enhance = more_power(1)
#     enhance(32)  # => TOTAL: 33
#     enhance(84)  # => TOTAL: 117
#     enhance(12)  # => TOTAL: 129
#     enhance(93)  # => TOTAL: 222
def more_power(total):
    def whatever(new_num):
        nonlocal total  # Since we're going to change 'total'
        total += new_num
        print("SO FAR:", total)
        
    return whatever

enhance = more_power(1)
enhance(32)
enhance(84)
enhance(12)
enhance(93)
