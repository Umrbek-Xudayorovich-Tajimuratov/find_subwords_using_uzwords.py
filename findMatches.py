

def findMatches(word, words):
    matches = []
    for check_word in words:
        if set(check_word).issubset(set(word)) and word != check_word and len(check_word) > 3:
            if all(list(word).count(i) >= list(check_word).count(i) for i in list(word)):
                matches.append(check_word)

    return matches