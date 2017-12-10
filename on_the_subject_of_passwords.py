words = ['about','after','again','below','could','every','first','found','great','house','large','learn','never',
         'other','place','plant','point','right','small','sound','spell','still','study','their','there','these',
         'thing','think','three','water','where','which','would','world','write']
tmp = []

for x in range(1, 6):
    val = list(input("Enter set {} of words> ".format(x)))[:6]
    for i in words:
        for letter in val:
            z = i[x-1]
            if letter in z:
                tmp.append(i)
                break

    words = tmp
    tmp = []

print("The word is {}".format(str(words)))
