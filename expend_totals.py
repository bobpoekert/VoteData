cont_file = open('contributions.tsv', 'r')

contributions = [e.replace('\n', '').split('\t') for e in cont_file]
contributions = [(e[0], int(e[1]), e[2]) for e in contributions]

totals = {}
for org, amt, member in contributions:
    k = (org, member)
    if k in totals:
        totals[k] += amt
    else:
        totals[k] = amt

outf = open('total_contributions.tsv', 'w')

for k, amt in totals.iteritems():
    org, member = k
    outf.write('%s\t%s\t%d\n' % (org, member, amt))
