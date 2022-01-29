def checkStringIsIp(var):
    try:
        result = [0<=int(x)<256 for x in re.split('\.',re.match(r'^\d+\.\d+\.\d+\.\d+$',var).group(0))].count(True)==4
        return result
    except (AttributeError, SyntaxError):
        return "Variable passed is not a string"
