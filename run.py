import sys
from collections import defaultdict

def main():
    orig_stdout = sys.stdout
    f = open('successor-predecessor-frequencies.txt', 'w')
    sys.stdout = f
    K = int(sys.argv[2])


    words = []
    with open(sys.argv[1]) as file:
        for line in file:
            line = line.strip()
            line = line+' '
            words.append(line)

    words.sort()
    originals = [word.strip() for word in words]
    back_words = [word[::-1] for word in words]
    #Forward
    words = algorithm(words, K)
    places = placespaces(words)
    for place in places:
        print(place)

    #Backwards
    back_words = algorithm(back_words, K)
    back_places = placespaces(back_words)
    back_places = [word[::-1] for word in back_places]

    print("=" *30 + "Right to Left" + "=" *30)
    for bplace in back_places:
        print(bplace)

    lex = createLexicon(places, originals)
    #print(lex)

    sig = createSignatures(lex)
    f = open('TomSawyerSignatures.txt', 'w')
    sys.stdout = f
    for i, (key, values) in enumerate(sig.items()):
        if i >20:
            break
        else:
            print(key + " " + str(len(values)) + " ", end='')
            for e, value in enumerate(values):
                if e > 2:
                    break
                else:
                    print(value + " ", end ='')
        print()


    sys.stdout = orig_stdout
    f.close()

def createLexicon(words, originals):
    Lexicon = {}
    for word in words:
        if ' ' in word.strip():
            word = word.split()
            key = ''.join(word[:len(word)-1])
            value = word[-1]
            Lexicon.setdefault(key, [])
            if key in originals and "NULL" not in Lexicon[key]:
                Lexicon[key].append("NULL")
            Lexicon[key].append(value)

        else:
            Lexicon[word] = "NULL"

    for key, value in Lexicon.items():
        if value is not 'NULL':
            value = '='.join(value)
            Lexicon[key] = value
    return Lexicon

def createSignatures(Lexicon):
    Signatures = {}
    for key, value in Lexicon.items():
        for key_i, value_i in Lexicon.items():
            Signatures.setdefault(value, [])
            if value_i == value and key_i not in Signatures[value]:
                Signatures[value].append(key_i)
    return Signatures

def algorithm(words, K):
    ret = []
    for i, word in enumerate(words):
        space_indicies = []
        for j in range(len(word)):
            lst = []
            if j < K:
                continue
            else:
                for word_j in words:
                    if j >= len(word_j):
                        continue
                    if word[:j] == word_j[:j] and word_j[j] not in lst:
                        lst.append(word_j[j])
                    if len(lst) > 1:
                        space_indicies.append(j-1)
                        break
        ret.append((word, space_indicies))
    return ret

def placespaces(words):
    for e, (word, indicies) in enumerate(words):
        if len(indicies) == 0:
            words[e] = word
            continue
        for i in range(len(word) + len(indicies)):
            if len(words[e][1]) == 0:
                words[e] = words[e][0]
                break
            if i in words[e][1]:
                words[e][1].remove(i)
                words[e] = word[:i+1] + ' ' + word[i+1:], [idx+1 for idx in words[e][1]]
            word = words[e][0]

    return words

if __name__ == '__main__':
    main()