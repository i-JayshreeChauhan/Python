
"""
The purpose of this code is to find if a post/comment is talking
about you or not

"""

c="jayshree"

comment = "hello world! we just had chat with Jayshree.and it was amazing.jAAYshree is a nice person"


#we have converted both to lower case and then we will check as this prog
#doesnt have concern with case(lower/upper) but with name being called in the comment

if(c.lower() in comment.lower()) :
    print("yes , this comment talks about you !")
else:
    print("No , this comment does not talk about you.")
