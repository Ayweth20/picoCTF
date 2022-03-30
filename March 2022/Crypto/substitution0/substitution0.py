given_alphabet ='EKSZJTCMXOQUDYLFABGPHNRVIW'
english_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

message = '''
EKSZJTCMXOQUDYLFABGPHNRVIW

Mjbjhfly Ujcbeyz eblgj, rxpm e cbenj eyz gpepjui exb, eyz kblhcmp dj pmj kjjpuj
tbld e cuegg segj xy rmxsm xp reg jysulgjz. Xp reg e kjehpxthu gsebekejhg, eyz, ep
pmep pxdj, hyqylry pl yephbeuxgpg—lt slhbgj e cbjep fbxwj xy e gsxjypxtxs flxyp
lt nxjr. Pmjbj rjbj prl blhyz kuesq gflpg yjeb lyj jvpbjdxpi lt pmj kesq, eyz e
ulyc lyj yjeb pmj lpmjb. Pmj gseujg rjbj jvsjjzxycui mebz eyz culggi, rxpm euu pmj
effjebeysj lt khbyxgmjz cluz. Pmj rjxcmp lt pmj xygjsp reg njbi bjdebqekuj, eyz,
peqxyc euu pmxycg xypl slygxzjbepxly, X slhuz mebzui kuedj Ohfxpjb tlb mxg lfxyxly
bjgfjspxyc xp.

Pmj tuec xg: fxslSPT{5HK5717H710Y_3N0UH710Y_59533E2J}'''.upper()

decrypted_message = ''

for letter in message:
    
    try:  # We don't want ponctuation to be part of this transformation
        decrypted_message +=english_alphabet[given_alphabet.index(letter)]
    except:
        decrypted_message+=letter 

print(decrypted_message)

 '''
 We get the following output: 
 
 ABCDEFGHIJKLMNOPQRSTUVWXYZ

HEREUPON LEGRAND AROSE, WITH A GRAVE AND STATELY AIR, AND BROUGHT ME THE BEETLE
FROM A GLASS CASE IN WHICH IT WAS ENCLOSED. IT WAS A BEAUTIFUL SCARABAEUS, AND, AT
THAT TIME, UNKNOWN TO NATURALISTS—OF COURSE A GREAT PRIZE IN A SCIENTIFIC POINT
OF VIEW. THERE WERE TWO ROUND BLACK SPOTS NEAR ONE EXTREMITY OF THE BACK, AND A
LONG ONE NEAR THE OTHER. THE SCALES WERE EXCEEDINGLY HARD AND GLOSSY, WITH ALL THE
APPEARANCE OF BURNISHED GOLD. THE WEIGHT OF THE INSECT WAS VERY REMARKABLE, AND,
TAKING ALL THINGS INTO CONSIDERATION, I COULD HARDLY BLAME JUPITER FOR HIS OPINION
RESPECTING IT.

THE FLAG IS: PICOCTF{5UB5717U710N_3V0LU710N_59533A2E}
'''
