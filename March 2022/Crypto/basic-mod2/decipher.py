i=y=0
datas = [268, 413, 110, 190, 426, 419, 108, 229, 310, 379, 323, 373, 385, 236, 92, 96, 169, 321, 284, 185, 154, 137, 186]
modulo = []
reverse_modulo = []
alpha = {1:"A", 2:"B", 3:"C", 4:"D", 5:"E", 6:"F", 7:"G", 8:"H", 9:"I", 10:"J", 11:"K", 12:"L", 13:"M", 14:"N", 15:"O", 16:"P", 17:"Q", 18:"R", 19:"S", 20:"T", 21:"U", 22:"V", 23:"W", 24:"X", 25:"Y", 26:"Z", 27:"0", 28:"1", 29:"2", 30:"3", 31:"4", 32:"5", 33:"6", 34:"7", 35:"8", 36:"9", 37:"_"}

#Calculate modulo 41
for i in datas:
    modulo.append(i%41)
    #print(alpha[i%41], end="")

#Calculate reverse modulo
def modInverse(a, m):
    for x in range(1, m):
        if (((a % m) * (x % m)) % m == 1):
            return x
    return -1

for a in modulo:
    reverse_modulo.append(modInverse(a, 41))

for y in reverse_modulo:
    print(alpha[y], end="")
