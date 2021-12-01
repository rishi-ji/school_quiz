#You just need to download this code on vsc and press "ctrl + `" and navigate it to "school.py" by typing "python school.py"
# or
#you can copy/paste code and run this on online python platform(s)
def give_options(x,y,z):
    print("a):", x)
    print("b):", y)
    print("c):", z)

print("Hello! Welcome to my Quiz" "\n" "One Questions carries 1 marks each")
ans = input("Are you ready to play (yes/no): ")
a ="Note: write options! Do not write answers."
score = 0
total_questions = 5

correct_ans =["a", "c", "b", "c","a"]

if ans.lower() == "yes":
    print(a)
    print("Question 1- What is the most popular and easy to use language? ")
    give_options("Python", "C", "Java" )
    ans=input("")
    if ans.lower() == correct_ans[0]:
        score=score+1
        print("Correct")
    else:
        print("Incorrect")
    print(a)
    print("Question 2- How to comment a line in python ")
    give_options("$", "//", "#")
    ans = input("")
    if ans.lower() == correct_ans[1]:
        score=score+1
        print("Correct")
    else:
        print("Incorrect")
    print(a)
    print("Question 3- What is the full form of AI in coding? ")
    give_options("Art Integrients", "Artificial Intelligence", "All Intelligence")
    ans = input("")
    if ans.lower() == correct_ans[2]:
        score=score+1
        print("Correct")
    else:
        print("Incorrect")
    print(a)
    print("Question 4- Who made python? ")
    give_options("Douglas Crockford", "Brendan Eich", "Guido van Rossum")
    ans = input("")
    if ans.lower() == correct_ans[3]:
        score=score+1
        print("Correct")
    else:
        print("Incorrect")

    print(a)
    print("Question 5- How to add multi line comment in python ")
    give_options("''' ''''", "/*", "#")
    ans = input("")
    if ans.lower() == correct_ans[4]:
        score=score+1
        print("Correct")
    else:
        print("Incorrect")

print('Congo, you got:',score,'points :)')

print('Do you want to play quiz of JavaScript also?(yes/no)')

def give_options1(x,y,z):
    print("i):", x)
    print("ii):", y)
    print("iii):", z)

print("Hello! Welcome to my Quiz" "\n" "One Questions carries 1 marks each")
ans = input("Are you ready to play (yes/no): ")
score1 = 0

correct_ans1 =["iii", "i", "ii", "iii"]

if ans.lower() == "yes":
    print(a)
    print("Question 1- Who made Java? ")
    give_options1("Douglas Crockford", "Guido van Rossum", "Brendan Eich")
    ans=input("")
    if ans.lower() == correct_ans1[0]:
        score1=score+1
        print("Correct")
    else:
        print("Incorrect")
    print(a)
    print("Question- When was JS made? ")
    give_options1("1995", "1999", "2000")
    ans = input("")
    if ans.lower() == correct_ans1[1]:
        score1=score+1
        print("Correct")
    else:
        print("Incorrect")
    print(a)
    print("Question- What is the full for of JS ")
    give_options1("Java Stop", "Java Script", "Java Screen")
    ans = input("")
    if ans.lower() == correct_ans1[2]:
        score1=score+1
        print("Correct")
    else:
        print("Incorrect")
    print(a)
    print("Question- What is used to comment a line in JS?")
    give_options1("///", "&&", "//")
    ans = input("")
    if ans.lower() == correct_ans1[3]:
        score1=score+1
        print("Correct")
    else:
        print("Incorrect")

print('Congo, you got:',score1,'points : in JS quiz)')


