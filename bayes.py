##get only strong and confirmed, split by strand
with open('OperonSet.txt') as oset:
	with open('operonf.txt', 'w') as outf, open('operonr.txt', 'w') as outr:
		for line in oset:
			if '#' in line[0:1]:
				continue
			if 'Confirmed' in line or 'Strong' in line:
				if 'forward' in line:
					outf.write(line)
				else:
					outr.write(line)
					
with open('operonf.txt') as forward:
	operonsf = []
	for line in forward:
		k = line.split('\t')
		operonsf.append(k[0:6])
	operonsf.sort(key=lambda x:int(x[1]))
	
with open('operonr.txt') as reverse:
	operonsr = []
	for line in reverse:
		k = line.split('\t')
		operonsr.append(k[0:6])
	operonsr.sort(key=lambda x:int(x[1]))

with open('GeneProductSet.txt') as genes:
	genetable = {}
	for line in genes:
		if '#' in line[0:1]:
			continue
		k = line.split('\t')
		if k[3] != '':
			genetable[k[1]] = [int(k[3]), int(k[4])]
		
def distance(a, b, genetable):
	if genetable[a][0] > genetable[b][0]:
		return genetable[a][0] - genetable[b][1]
	else:
		return genetable[b][0] - genetable[a][1]
	
opdist = []

for op in operonsf:
	prevg = ''
	for g in op[5].split(','):
		if prevg != '':
			opdist.append(distance(prevg, g, genetable))
		prevg = g
		
for op in operonsr:
	prevg = ''
	for g in op[5].split(','):
		if prevg != '':
			opdist.append(distance(prevg, g, genetable))
		prevg = g
		
opdist.sort()

ndist = []
prevg = ''
for op in operonsf:
	if prevg != '':
		ndist.append(distance(prevg, op[5].split(',')[0], genetable))
	prevg = op[5].split(',')[-1]
	
prevg = ''
for op in operonsr:
	if prevg != '':
		ndist.append(distance(prevg, op[5].split(',')[0], genetable))
	prevg = op[5].split(',')[-1]

ndist.sort()

print(ndist)
print(opdist)