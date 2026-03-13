# maketrans() funtion is a string funtion which is use to make translation table
# The str.maketrans() method takes two strings of equal length and returns a translation table that maps each character of the first string with the corresponding character of the second string. Each character in the translation table is stored as a Unicode ordinal, a number that uniquely identifies the character.

small_letters = "abcdefghijklmnopqrstuvwxyz"
capital_letters = small_letters.upper()

table = str.maketrans(small_letters, capital_letters)
name = "aarush"
capital_name = name.translate(table)
print(capital_name)
# this was just for educational purpose but the better way is , capital_name = name.upper()
