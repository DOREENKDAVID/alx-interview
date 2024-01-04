# UTF-8 Validation

# Resources
Read or watch:

- [UTF-8](https://intranet.alxswe.com/rltoken/oqFi6P1hNvp9aSuNv---IQ)
- [Characters, Symbols, and the Unicode Miracle](https://intranet.alxswe.com/rltoken/d--jVK8sBSlhkosu7pFzdw)



#Tasks
0. UTF-8 Validation
mandatory
Write a method that determines if a given data set represents a valid UTF-8 encoding.

Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer
