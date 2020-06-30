def printPicnic(items, left, right):
    print('PICNIC ITEMS'.center(left + right, '-'))
    for k, v in items.items():
        print(k.ljust(left,'.') + str(v).rjust(right))

picitems = {'sand': 5, 'apples': 22, 'cips': 55}
printPicnic(picitems, 12 ,6)