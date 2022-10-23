key = [4,3,2,2,1,4,2,0,2,1,0,4,3]

message = "To any recruit that picks up this canteen, immediately DROP 20!"

"=============================================================================="
#ENCRYPTION

encrypted = ""
for i in range(len(message)):

  encrypted += chr(ord(message[i])+ key[i%len(key)])

#ENCRYPTED MESSAGE: Xr"co}"rgdrylx#vjbx"pkdkw#ys"vimu ebnxhiq."jqoefjaxhp|"FSSR 41!

print(encrypted)




"=============================================================================="
#DECRYPTION





original = ""

for i in range(len(encrypted)):
  a = ord(encrypted[i])
  b = key[i% len(key)]
  original += chr(a-b)


print(original)


