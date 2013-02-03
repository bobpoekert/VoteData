import json, codecs

name_to_id = json.load(codecs.open('name_to_id_map.json', 'r', 'UTF-8'))

id_to_name = (
    ('%s,%s' % (r['name']['last'], r['name']['first']), r['id']['bioguide']) for r in name_to_id)

res = codecs.open('name_to_id.tsv', 'w', 'UTF-8')

for k, v in id_to_name:
    res.write('%s\t%s\n' % (k, v))
