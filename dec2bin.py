
def bin2dec1(binary,decimal,idx):
    if idx:
        binary=binary>>1
        if decimal % 2:
            binary |= 0b1000000000000000
        decimal=int(decimal/2)
        idx-=1
        return bin2dec1(binary,decimal,idx)
    else:
        return binary
if __name__ == '__main__':
    for a in range(0,10000,3):
        c=bin2dec1(0,a,16)
        print(f'{a:>3} je ve dvojkové soustavě: {c:>16b}')