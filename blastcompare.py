
with open('ecolisq.txt') as ecoli:
	with open('ecolisq2.txt','w') as out:
		gd = ''
		for line in ecoli:
			tr =line.split('\t');
			if tr[0] != gd:
				gd = tr[0]
				out.write(line)
		

atumeb = open('atumesq.txt')
output = open('finalpairs.txt', 'w')

gene = ''
compare = ''
counter = 0;

for line in atumeb:
	tabrow = line.split('\t')
	if tabrow[0] != gene:
		gene = tabrow[0].lstrip().rstrip()
		compare = tabrow[1].lstrip().rstrip()
		with open('ecolisq2.txt') as ecolib:
			for ln in ecolib:
				etabrow = ln.split('\t')
				if compare in etabrow[0]:
					if gene in etabrow[1]:
						output.write(compare + '\t' + gene + '\n')
					break
	counter += 1
	print(counter)
		