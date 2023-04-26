# Starting collection and new items to add
beachCollection = {'sand dollar': 3, 'seashell': 12, 'beach glass': 5, 'driftwood': 1}
bucketItems = ['seashell', 'seashell', 'coral', 'seashell']

def listCollection(beachCollection):
    print('Here are the current items in your beach collection:')

    for k, v in beachCollection.items():
        print(k + ' count: ' + str(v))



listCollection(beachCollection)
