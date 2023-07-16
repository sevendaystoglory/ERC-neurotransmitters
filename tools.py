def normalize(num):
    try:
        num = int(num)
    except ValueError and TypeError:
        num = 50
    if num<0:
        return 0
    if num>100:
        return 100
    else:
        return num
    
def set_temp(dopamine):
    return(dopamine/100)    

