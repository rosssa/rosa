ex_string = "옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷못옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷못옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷못옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷못옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷옷"

it = iter(ex_string)
n = 0
while True:
if '못' in it:
	n=n+1
	print('못이 %d개 있습니다' % n)
else:
	pass
