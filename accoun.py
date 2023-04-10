#dic = {'accountno' : '1234567890'}
def AccValidation(event):
    if len(event['accountno']) == 10 :
        return True
    else :
        return False