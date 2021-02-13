def check_permutation(s1,s2):
    if len(s1) != len(s2):return False
    mappings = {}
    for i in s1:
        if i in mappings:
            mappings[i] +=1
        else:
            mappings[i] = 1
    
    for i in s2:
        if i not in mappings or mappings[i]==0:return False
        else:mappings[i]-=1
    
    return True


s1 = 'abcc'
s2 = 'bcca'

print(check_permutation(s1,s2))