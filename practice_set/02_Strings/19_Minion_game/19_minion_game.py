
"""
example

word = banana

how many substrings can be formed from one position (for stuart : using consonants)
ex.
    position 0 --> 6 (b,ba,ban,bana,banan,banana)
    position 1 --> 0 words as this is a vowel
    position 2 --> 4 (n,na,nan,nana)
    position 3 --> 0 words as this is a vowel
    position 4 --> 2 (n,na)
    position 5 --> 0 words as this is a vowel

    so total points for stuart = 6+4+2 = 12

ex for kevin

    position 0 --> 0 words as this is a consonants
    position 1 --> 5 (a,an,ana,anan,anana)
    position 2 --> 0 words as this is a consonants
    position 3 --> 3 (a,an,ana) 
    position 4 --> 0 words as this is a consonants
    position 5 --> 1 (a)

    so total points for kevin = 5+3+1 = 9

"""


def minion_game(string):

    s_points = 0
    k_points = 0 

    #for consonant(stuart)
    for index,i in enumerate(string):
        if i!='A' and i!='E' and i!='I' and i!='O' and i!='U' :
            #calculate possible words
            s_points += (len(string) - index)
        else:
            k_points += (len(string) - index)


    if s_points == k_points:
        print("Draw ")
    elif s_points > k_points:
        print("Stuart" , s_points)
    elif s_points < k_points:
        print("Kevin" , k_points)



if __name__ == '__main__':
    s = input()
    minion_game(s)