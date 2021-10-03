from operator import itemgetter
def sortDictsList(keyName):
  return sorted(l, key=itemgetter(keyName), reverse=True)
