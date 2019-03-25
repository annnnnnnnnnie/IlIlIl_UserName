def baseb(n, b):
    e = n//b
    q = n%b
    if n == 0:
        return '0'
    elif e == 0:
        return str(q)
    else:
        return baseb(e, b) + str(q)

def Encode(string):
  print("encoding")
  encoded = ""
  for character in string:
    print(character)
    asciiNumber = int(str(ord(character)).zfill(3))
    asciiNumber = baseb(asciiNumber, 3)
    print("asciiNumber in base 3 is ", str(asciiNumber).zfill(5))
    print(EncodeString(str(asciiNumber).zfill(5)))
    encoded += EncodeString(str(asciiNumber).zfill(5)   )
    print(str(ord(character)).zfill(3)+"\n")
  print("\n\n" + encoded + "\n")
  return encoded

def EncodeString(string):
  encoded = ""
  for character in string:
    if character == "0":
      encoded += "|"
    elif character == "1":
      encoded += "I"
    else:
      encoded += "l"
  return encoded

def Decode(string):
    decoded =""
    for i in range(0, len(string) //5):
        decoded += DecodeString(string[i*5:(i*5+5)])
        
    return decoded

def DecodeString(string):
    print(string)
    decoded = ""
    for character in string:
        if character == "|":
          decoded += "0"
        elif character == "I":
          decoded += "1"
        else:
          decoded += "2"

    asciiNumber = ter2dec(decoded)
    print(asciiNumber)
    return chr(int(asciiNumber))
def ter2dec(string):
    a = 0
    for i in range(0,5):
        a+= (int(string[i]))* (3 ** (5-i-1))
    return a
def Main():
	while(1):
		print("e-encode, d-decode, x-exit")
		command = input()
		if(command == 'e'):
			print("Please type the string")
			encoded = Encode(str(input()))
			print("Encoded:", encoded)
		elif(command == 'd'):
			print("Please type the code")
			print("Decoded: \n"+Decode(str(input())))
		elif(command == 'x'):
			print("Exiting...")
			break
		else:
			print("Invalid command\n")
			print("e-encode, d-decode, x-exit")
	return

Main()

