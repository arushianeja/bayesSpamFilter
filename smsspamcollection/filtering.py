def populate_third_dict(good, bad, word, ngood, nbad):
    g = 0
    b = 0
    if word in good:
        g = 2 * good[word]
    if word in bad:
        b = bad[word]


    if (g+b >= 5):
        returnVal = max(0.01, (min (0.99, min(1, b/nbad)/(min(1, (g/ngood)+ min(1, (b/nbad)))))))
        return returnVal
    else:
        return 0.4
