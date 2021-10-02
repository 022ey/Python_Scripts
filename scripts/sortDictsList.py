from operator import itemgetter
def sortDictsList():
  return sorted(l, key=itemgetter('name'), reverse=True)
