import random
def primt(arg):
    newString=""
    if(type(arg) is str):
        word_list = arg.split()
        for word in word_list:
            limit=len(word)
            random_position=random.randint(1, limit-1)
            newWord=word[:random_position] + "m" + word[random_position:] + " "
            newString+=newWord
        print(newString)
    else:
        print(arg)
