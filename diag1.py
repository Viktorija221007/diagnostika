#Viktorija Štelmahere 18.10.24

Vecums = int(input("Ievadi savu vecumu: "))    #ievada vecumu

if Vecums < 13:                                #ja mazāks par 13...
    print("Tu esi bērns")                      #izvada šo
elif Vecums >= 20:                             #ja lielāks par 20...
    print("Tu esi pieaugušais")                #izvada šo
else:                                          #ja neviens no iepriekšējiem jeb starp 13 un 20...
    print("Tu esi tīnis")                      #izvada šo