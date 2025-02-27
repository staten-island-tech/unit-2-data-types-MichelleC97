""" text = input("The red cat sat on the mat. Why are you so sad cat? Don't ask that.")
def input(S,s):
    def input(T,t):
        if text == (S,s < T,t):
            print('English')
        elif text == (S,s > T,t):
            print('French')
        elif text == (S,s = T,t):
            print('French') """




""" language = ("text")
def input(English):
    def input(French):
        def input(S,T):
            def input(s,t):
                for text in range(S<T):
                    print(English)
                for text in range(S>T):
                    print(French)
                for text in range(S=T):
                    print(French)
 """
""" 
S = 0
T = 0

sentence  = input("the cats sits on the stairs.")

for i in sentence:
    if i == " ":
        S += 1
    if i == ".":
        T += 1

if T > S:
    print("English")
elif S > T:
    print("French")
elif S == T:    
    print("French") """



some_text = "The quick brown fox jumped over the lazy dog"
more_text = ["T","h","e"]
def lang(text):
    french = 0
    english = 0
    for letter in text:
        if letter == "s" or letter == "S":
            french = french +1
        # elif letter in ["t","T"]:
        elif letter.lower() == "t":
            english = english +1
        if french>= english:
            print("French")
        else:
            print("English")
lang(some_text)