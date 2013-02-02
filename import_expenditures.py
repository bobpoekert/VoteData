import json, re
outf = open('contributions.tsv', 'a+')
inf = open('independent_expenditure_by_senator_2012.json', 'r')
input_data = json.load(inf)

def parse_dollar_amount(s):
    s = re.sub('[^\d]+', '', s, 1)
    dollars, cents = s.split('.')
    dollars = dollars.replace(',', '')
    return int(dollars) * 100 + int(cents)

i = 0
for member, contribs in input_data.iteritems():
    for contrib in contribs['contributions']:
        i += 1
        if i % 1000 == 0:
            print i
        org_name = contrib['spe_nam']
        amount = parse_dollar_amount(contrib['exp_amo'])
        outf.write('%s\t%d\t%s\n' % (org_name, amount, member))
