def solution(l):
  l.sort(key=lambda s: map(int, s.split('.')))
  return l
