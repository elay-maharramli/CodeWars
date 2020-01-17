from string import digits
def string_clean(s):
    """
    Function will return the cleaned string
    """
    # Your code here
    res = s.translate(None, digits)
    return res
