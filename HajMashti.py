# Problem Source: https://quera.org/problemset/209104

def HajMashti(var):
    if var[0] == 'Y':
        return 'Haji'
    
    elif var[1] == 'Y':
        return 'Karbalaee'
    
    elif var[2] == 'Y':
        return 'Mashti'
    
    else:
        return 'Agha'
    
var = input()
print(HajMashti(var))
            
