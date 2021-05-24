from random import choice, randrange


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n, repeat=False):
    no, adv, adj = nouns.copy(), adverbs.copy(), adjectives.copy()
    jokes = []
    jokes_list = min(no, adv, adj)


    while n and len(jokes_list):
        num = randrange(len(jokes_list))
        if repeat:
            jokes.append(f"{no.pop(num)} {adv.pop(num)} {adj.pop(num)}")
        else:
            jokes.append(f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")
        n -= 1
    return jokes


print(get_jokes(1))