def old_macdonald(s):
    first=s[0]
    inbetween=s[1:3]
    fourth=s[3]
    rem=s[4:]
    return first.upper()+inbetween+fourth.upper()+rem   
    


print(old_macdonald("macdonald"))