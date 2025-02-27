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

S = 0
T = 0

sentence  = input("the cat is sitting.")

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
    print("French")