import hashlib
def sha256(text):
 return hashlib.sha256(text.encode()).hexdigest()

text=input("Enter the text:")
sha2561=sha256(text)
print("Orginal text value:",text)
print("Hash value of the text:",sha2561)

change=text[:-1]+"x"
print("This is the change text:",change)
changehash=sha256(change)
print("Change text hash:",changehash)

if sha2561==changehash:
 print("this state that it dosenot follow the avalance property")
else: 
 print("It satisfy the avalance rule")


 text1=input("Enter the same text to check the deterministic:")
 deterministic=sha256(text1)
 print("this is the output of the same text :",deterministic)