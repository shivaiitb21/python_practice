def is_first_char_vowel(str):
    if str[0] in "aeiouAEIOU":
        return True
    else:
        return False

def is_first_char_consonant(str):
    if str[0] not in "aeiouAEIOU":
        return True
    else:
        return False

def vowel_count(str):
    count = 0
    for alphabet in str:
        if alphabet in "aeiouAEIOU":
           count +=1
    return count

def consonant_count(str):
    count = 0
    for alphabet in str:
        if alphabet not in "aeiouAEIOU":
            count +=1
    return count

def name_contain_love(str):
    is_love = False
    for alphabet in str:
        if alphabet in "love":
            is_love = True

    return is_love


print("LOVE CALCULATOR")
while True:
    YName = input("Enter your name: ")
    PName = input("Enter your partner name: ")
    point = 0

    if  not YName.isalpha() or len(YName)>20 or not PName.isalpha() or len(PName)>20:
        print("Enter name properly")
        continue

    if len(YName) == len(PName):
        point +=20
    if is_first_char_vowel(YName) and is_first_char_vowel(PName):
        point +=30
    if is_first_char_consonant(YName) and is_first_char_consonant(PName):
        point +=10
    if vowel_count(YName) == vowel_count(PName):
        point +=30
    if consonant_count(YName) == consonant_count(PName):
        point +=20
    if name_contain_love(YName) and name_contain_love(PName):
        point +=20

    print(f"Love match {point}%")
    if point == 100:
        print(f"MARRIAGE: {YName}'s and {PName}'s love can end up being really deep and end in wedding bells.")
    elif point >= 80:
        print("Deep Love:", YName, "and", PName, "will probably last longer, and are highly compatible.")
    elif point >= 60:
        print("High CHANCE:", YName, "and", PName, " there is a chance these two will fall in love.")
    elif point >= 40:
        print("Low Friends:", YName, "and", PName,
              "there is a chance these two will fall in love though there is also a great chance of break up.")
    elif point >= 30:
        print("Only Friends:", YName, "and", PName, "are meant to be friends")
    elif point >= 10:
        print("No Friends:", YName, "'s and", PName, "'s two will never be together, not even friends")
    else:
        print("super Enemies:", YName, "and", PName, "born to fight")

    user_chose = input("Want to play again?(yes/exit): ")
    if user_chose=="yes":
        continue
    else:
        break
