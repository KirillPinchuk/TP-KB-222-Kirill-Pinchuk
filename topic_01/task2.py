str = ".lock." # Видалення символів '.' з обох кінців рядка.
str = str.strip(".")
print(str)

str = "lock, local"
str = str.capitalize() # Перше слово з великої літери
print(str)

str = "lock, local"
str = str.title() # Всі слова з великої літери
print(str)

str = "lock" 
str = str.upper() # Всі слова великими літерами
print(str)

str = "LOCK"
str = str.lower() # Всі слова маленькими літерами
print(str)