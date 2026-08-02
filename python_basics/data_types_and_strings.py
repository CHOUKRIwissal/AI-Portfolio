# practice of python data types and string manipulation
name="wiso"
age=23
gpa=3.7
graduation=True
height = 3.6            
is_student = True     

print(f"\n My name is {name}, I'm {age} years old, and my graduation status is {graduation} with a GPA of {gpa}.")
print(f"\n Height: {height} -> {type(height)}")
print(f"\n Student: {is_student} -> {type(is_student)}")
height_in_cm = height * 30.48
print(f"\n Height in cm: {height_in_cm:.3f}")
print(f"\n Name length: {len(name)}")
print(f"\n Is {name} over 25? {age > 25}")

print(f"|{name:^10}|")   
print(f"|{name:<10}|")    
print(f"|{name:>10}|") 

# Get user input
your_name=str(input("ENTER YOUR NAME : "))
your_age=int(input("ENTER YOUR AGE : "))
your_age_months= your_age*12
your_age_upd= your_age + 10
print(f"\n HELLO {your_name}, your age in months is {your_age_months},after ten years your age gona be {your_age_upd} ")


sentence=str(input("ENTER A SENTENCE : "))
print(f"\n The length of the sentence is {len(sentence)} ")
print(f"\n The first character {sentence[0]} and last character {sentence[-1]}")
print (f"\n The sentence in Uppercase {sentence.upper()}")
print (f"\n The sentence in Lowercase {sentence.lower()}")
print(f"\n First 3 characters: {sentence[:3]}")
print(f"\n Characters 5-9: {sentence[5:10]}")
how_many_words_method1=sentence.count(" ") + 1
print(f"\n The sentence has {how_many_words_method1} words method 1 counting spaces")
words = sentence.split()
print(f"\n Split into words: {words}")
how_many_words_method2=len(words)
print(f"\n The sentence has {how_many_words_method2} words method 2 using split()")

