def symbolSpam(word, amount=3):
    if len(word) <= 2:
        return False
    else:
        letter = ''
        for i in range(len(word)):
            if letter == '':                
                letter = word[i]
            elif word[i] == letter:
                letter = word[i]
                amount -= 1
        if amount <= 0:
            return True