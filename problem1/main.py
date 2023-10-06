def compare(a, b):
    pattern = ""
    if len(a) >= len(b):
        
        if a.count(b) > 0:   # memeriksa berapa kali kemunculan string (b) ada di string (a)
            start_idx = a.index(b) 
            end_idx = start_idx + len(b)
            pattern = a[start_idx : end_idx]
    elif len(a) < len(b):
        if (b.count(a)) > 0:
            start_idx = b.index(a)
            end_idx = start_idx + len(a)
            pattern = b[start_idx : end_idx]

    return pattern

if __name__ == '__main__':
    print(compare("AKA", "AKASHI")) # AKA
    print(compare("KANGOORO", "KANG")) # KANG
    print(compare("KI", "KIJANG")) # KI
    print(compare("KUPU-KUPU", "KUPU")) # KUPU
    print(compare("ILALANG", "ILA")) # ILA