def wordsAmount(message, length=3):
    message = message.split()
    if len(message) <= length:
        return True
    else:
        return False