str1 = "Az almafán almák teremnek."
print("A szöveg hossza:", len(str1))
print(type(len(str1)))

str2 = "terem"
print(str1.find(str2))

lower_str1 = str1.lower()
print(str1)
print(lower_str1)
print(str1.upper())
print(lower_str1.islower())
print(lower_str1.isupper())
print(str1.isupper())

print(str1.isalpha())
print(str2.isalpha())
print(str2.isalnum())
str3 = "user12"
print(str3.isalpha())
print(str3.isalnum())

