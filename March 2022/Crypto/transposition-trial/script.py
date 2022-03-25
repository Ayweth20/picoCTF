s = 'heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V6E5926A}4'

n = 3
res = [s[i:i + n] for i in range(0, len(s), n)]

#print(res)
#res --> ['heT', 'fl ', 'g a', 's i', 'icp', 'CTo', '{7F', '4NR', 'P05', '1N5', '_16', '_35', 'P3X', '51N', '3_V', '6E5', '926', 'A}4']

for i in res:
    y = 0
    print(i[2] + i[0] + i[1], end="")
