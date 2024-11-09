def permutacije(prvi, zadnji, niz):
    if prvi == zadnji:
        print(niz)
    else:
        for i in range(prvi, zadnji + 1):
            niz[i], niz[prvi] = niz[prvi], niz[i]
            permutacije(prvi + 1, zadnji, niz)
            niz[i], niz[prvi] = niz[prvi], niz[i]



niz = list(map(int, input("Unesite niz brojeva, odvojenih razmacima: ").split()))
permutacije(0, len(niz) - 1, niz)