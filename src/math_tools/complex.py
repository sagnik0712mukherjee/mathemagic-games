def analyze_complex(z):
    s = str(z)
    s = s.replace('j', 'i').strip()
    re, im = "0", "0"
    if '-' in s:
        ls = s.split('-')
        re = ls[0]
        im = ls[1].replace('i', '')
        im = '-' + im
        if im == '': im = '1'
        elif im == '-': im = '-1'
    elif '+' in s:
        ls = s.split('+')
        re = ls[0]
        im = ls[1].replace('i', '')
        if im == '': im = '1'
    
    print(f'The complex number is {z} where the Real part is {re} and Imaginary part is {im}')
    return re, im

def complex_math_ops(z1, z2):
    def extract_parts(z):
        s = str(z).replace('j', 'i')
        if '-' in s:
            l = s.split('-')
            re = float(l[0])
            im_str = l[1].replace('i','')
            im = -float(im_str) if im_str else -1.0
        elif '+' in s:
            l = s.split('+')
            re = float(l[0])
            im_str = l[1].replace('i','')
            im = float(im_str) if im_str else 1.0
        else:
            re = float(s)
            im = 0.0
        return re, im

    re1, im1 = extract_parts(z1)
    re2, im2 = extract_parts(z2)
    
    add = f'{re1 + re2} + {im1 + im2}i'
    sub = f'{re1 - re2} + {im1 - im2}i'
    mul = f'{re1*re2 + (-im1)*im2} + {(re1*im2)+(re2*im1)}i'
    # Fixed the division logic slightly for clarity, though keeping original intent
    div = f'{((re1*re2) + (-im1)*(-im2))/(re2**2 + im2**2)} + {((re1*(-im2))+(re2*im1))/(re2**2 + im2**2)}i'
    
    return {'Sum': add, 'Difference': sub, 'Product': mul, 'Ratio': div}

if __name__ == "__main__":
    z1 = '2 + 12i'
    z2 = '1 - i'
    analyze_complex(z1)
    print(complex_math_ops(z1, z2))
