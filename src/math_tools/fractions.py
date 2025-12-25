def decimal_to_fraction(num):
    s = str(num)
    if '.' not in s:
        return f"{num}/1"
    
    splits = s.split('.')
    decimal_places = len(splits[1])
    numer = int(10 ** decimal_places * num)
    denom = int(10 ** decimal_places)
    
    ls = []
    limit = max(numer, denom)
    for i in range(1, limit + 1):
        if numer % i == 0 and denom % i == 0:
            ls.append(i)
            
    if not ls:
        return f"{numer}/{denom}"
        
    final_numer = int(numer / ls[-1])
    final_denom = int(denom / ls[-1])
    result = f'{final_numer}/{final_denom}'
    print(result)
    return result

if __name__ == "__main__":
    decimal_to_fraction(46.23)
    decimal_to_fraction(1.25)
