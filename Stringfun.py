# Strings Function

name = "hitesh"

print(name.endswith("sh"))
print(name.startswith("h"))
print(name.capitalize())    #function should be case sensitive
print(name.upper())    
print(name.replace("hitesh", "nayak"))    

text = ("I", "code", "python")
result = (" ".join(text))
print(result)

word = input("Enter your name: ")
print(f"Good Afternoon, {word}")