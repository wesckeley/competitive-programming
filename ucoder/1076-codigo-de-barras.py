# 00 101
# 03 0101111
# 10 0110011
# 17 0010011
# 24 0100001
# 31 0100011
# 38 0111001
# 45 01010
# 50 1010000
# 57 1000100
# 64 1001000
# 71 1110100
# 78 1110010
# 85 1110010
# 92 101

ean13_offset = [0,3,10,17,24,31,38,45,50,57,64,71,78,85,92]
ean13_size = [3,7,7,7,7,7,7,5,7,7,7,7,7,7,3]

ean13_mapping = { 
    '0001101': 0, '0100111': 0, '1110010': 0,
    '0011001': 1, '0110011': 1, '1100110': 1,
    '0010011': 2, '0011011': 2, '1101100': 2,
    '0111101': 3, '0100001': 3, '1000010': 3,
    '0100011': 4, '0011101': 4, '1011100': 4,
    '0110001': 5, '0111001': 5, '1001110': 5,
    '0101111': 6, '0000101': 6, '1010000': 6,
    '0111011': 7, '0010001': 7, '1000100': 7,
    '0110111': 8, '0001001': 8, '1001000': 8,
    '0001011': 9, '0010111': 9, '1110100': 9
    }

ean13_parity = { 
    '0001101': '1', '0100111': '0',
    '0011001': '1', '0110011': '0',
    '0010011': '1', '0011011': '0',
    '0111101': '1', '0100001': '0',
    '0100011': '1', '0011101': '0',
    '0110001': '1', '0111001': '0',
    '0101111': '1', '0000101': '0',
    '0111011': '1', '0010001': '0',
    '0110111': '1', '0001001': '0',
    '0001011': '1', '0010111': '0'
    }

ean13_first = {
    '111111': 0,
    '110100': 1,
    '110010': 2,
    '110001': 3,
    '101100': 4,
    '100110': 5,
    '100011': 6,
    '101010': 7,
    '101001': 8,
    '100101': 9
    }

while(True):
    try:
        line = input()
    except EOFError:
        break

    ean13 = [line[ean13_offset[i]:ean13_offset[i]+ean13_size[i]] for i in range(15)]
    
    ean13_code = ""

    first = ""
    for i in range(1,7):
        first += ean13_parity[ean13[i]]
    ean13_code += chr(ean13_first[first] + ord('0'))    
    ean13_code += chr(ean13_mapping[ean13[1]] + ord('0'))
    ean13_code += '-'
    
    for i in range(2,7):
        ean13_code += chr(ean13_mapping[ean13[i]] + ord('0'))
    ean13_code += '-'

    for i in range(8,13):
        ean13_code += chr(ean13_mapping[ean13[i]] + ord('0'))
    ean13_code += '-'

    ean13_code += chr(ean13_mapping[ean13[13]] + ord('0'))

    ean13_check = ean13_first[first] + ean13_mapping[ean13[2]] + ean13_mapping[ean13[4]] +\
        ean13_mapping[ean13[6]] + ean13_mapping[ean13[9]] + ean13_mapping[ean13[11]]

    ean13_check += 3 * (ean13_mapping[ean13[1]] + ean13_mapping[ean13[3]] + ean13_mapping[ean13[5]] +\
        ean13_mapping[ean13[8]] + ean13_mapping[ean13[10]] + ean13_mapping[ean13[12]])        
    
    ean13_check %= 10
    ean13_check = 10 - ean13_check
    ean13_check %= 10

    if ean13_check != ean13_mapping[ean13[13]]:
        print("barcode incorreto: lido = {0} esperado = {1}".format(ean13_mapping[ean13[13]], ean13_check))
    else:
        print(ean13_code)