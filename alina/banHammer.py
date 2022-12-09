import difflib

def banHammer(message, data, percentage=0.7):
    for element in data:
        for word in message.split():
            matcher = difflib.SequenceMatcher(None, word.lower(), element.lower())
            # print(f'{round(matcher.ratio(), 2)} ----- {word}----{element}')
            if (round(matcher.ratio(), 2) > percentage):
                return True
    return False

def spamHammer(message, data, percentage=0.7):
    for element in data:
        matcher = difflib.SequenceMatcher(None, message.lower(), element.lower())
        if (round(matcher.ratio(), 2) > percentage):
            return True
    return False

# def symbolSpam(word, amount=3):
#     if len(word) <= 2:
#         return False
#     else:
#         letter = ''
#         for i in range(len(word)):
#             if letter == '':                
#                 letter = word[i]
#             elif word[i] == letter:
#                 letter = word[i]
#                 amount -= 1
#         if amount <= 0:
#             return True