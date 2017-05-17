##get only strong and confirmed, split by strand
with open('OperonSet.txt') as oset:
	with open('operonf.txt', 'w') as outf:
		for line in oset:
			if '#' in line[0:1]:
				continue
			if 'Confirmed' in line or 'Strong' in line:
				outf.write(line)

## create a list of all operons				
with open('operonf.txt') as forward:
	operonsf = []
	for line in forward:
		k = line.split('\t')
		operonsf.append(k[0:6])
	operonsf.sort(key=lambda x:int(x[1]))

##create a dict with allgenes
with open('GeneProductSet.txt') as genes:
	genetable = {}
	for line in genes:
		if '#' in line[0:1]:
			continue
		k = line.split('\t')
		if k[3] != '':
			genetable[k[1]] = [int(k[3]), int(k[4])]

##simple function for calculating the distance between genes			
def distance(a, b, genetable):
	if genetable[a][0] > genetable[b][0]:
		return genetable[a][0] - genetable[b][1]
	else:
		return genetable[b][0] - genetable[a][1]

##distance list for genes in operon		
opdist = []

#populate the distance list in operon
for op in operonsf:
	prevg = ''
	for g in op[5].split(','):
		if prevg != '':
			opdist.append(distance(prevg, g, genetable))
		prevg = g
		
opdist.sort()

#create and popluate a distance list outside of operons
ndist = []
prevg = ''
prevs = ''
for op in operonsf:
	if prevg != '' and prevs == op[3]:
		ndist.append(distance(prevg, op[5].split(',')[0], genetable))
	prevg = op[5].split(',')[-1]
	prevs = op[3]

ndist.sort()

##show similar lists
print(ndist)
print(opdist)