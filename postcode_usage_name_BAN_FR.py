# coding=utf-8

import re

black = ['à', 'di', 'au', 'aux', 'des', 'l', 'sous', 'et', 'du', 'les', 'd', 'lès', 'la', 'le', 'en', 'de', 'sur', 'saint', 'sainte']

# Adelans-et-le-Val-de-Bithaine -> Adelans-et-le-Val-de-Bithaine, adelans-et-le-val, adelans
# Return full name first
def subpart_generator(name):
  if '-' not in name:
    return (name,)

  s = name.lower().replace('\'', ' ').split('-')
  l = map(lambda i: s[i] not in black and not s[i][0].isdigit() and '-'.join(s[0:i+1]), range(len(s)-2, -1, -1))
  l = list(filter(lambda i: i, l))
  if len(l) > 0:
    l.insert(0, name)
    return l
  else:
    return (name,)


def get_labels(result):
  ret = []
  for city in subpart_generator(result.city):
    # Most complet first
    if result.type in ['city', 'town', 'village']:
      ret.extend(([result.postcode, city], [result.postcode], [city]))
    elif result.type in ['street', 'locality']:
      ret.extend(([result.name, result.postcode, city], [result.name, result.postcode], [result.name, city]))
    elif result.type == 'housenumber':
      ret.extend(([result.housenumber, result.name, result.postcode, city], [result.housenumber, result.name, result.postcode], [result.housenumber, result.name, city]))
  return list(map(lambda a: ' '.join(a), ret))
