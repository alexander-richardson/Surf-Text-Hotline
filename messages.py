from spots import spotsdict


wrong = """
Wipeout! I don't know what you mean brother. Try texting 'kook' if you wanna ride this wave.
"""
kook = """
Pretty simple, text the name of the spot you want the conidtions to and you'll get it. Text 'spots'
to see what spots we cover.
"""
# spots = str(spotsdict.keys())
spots = ''.join(['* {}\n'.format(x) for x in spotsdict.keys()])

def formats(word):
    first = word.strip()
    second = first.upper()
    return second
