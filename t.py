def cfDecodeEmail(encodedString):
    r = int(encodedString[:2],16)
    email = ''.join([chr(int(encodedString[i:i+2], 16) ^ r) for i in range(2, len(encodedString), 2)])
    return email

x = "aacec9cbd8d8c5c6c6eac9c3ded3c5cccbc6c8cfd8dedcc3c6c6cf84c9c5c7"

print(cfDecodeEmail(x))