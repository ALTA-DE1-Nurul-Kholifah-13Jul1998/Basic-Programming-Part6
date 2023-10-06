def caesar(offset, input_str):
    alp = "abcdefghijklmnopqrstuvwxyz"
    pattern = ""

    for i in input_str:
        if i in alp:
            index = (alp.index(i) + offset)%26
            pattern+=alp[index]
        else:
            pattern+=i

    return pattern

if __name__ == '__main__':
    print(caesar(3, "abc"))  # Output: "def"
    print(caesar(2, "alta")) # cnvc
    print(caesar(10, "alterraacademy")) # kvdobbkkmknowi
    print(caesar(1, "abcdefghijklmnopqrstuvwxyz")) # bcdefghijklmnopqrstuvwxyza
    print(caesar(1000, "abcdefghijklmnopqrstuvwxyz")) # mnopqrstuvwxyzabcdefghijkl