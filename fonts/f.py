import os
import imageio

base = './play/bmp/'
prefix = 'play'
pngs = os.listdir(base)
for png in pngs:
	im = imageio.read(os.path.join(base, png))
	data = im.get_data(0)
	rows = data.shape[0]
	cols = data.shape[1]

	d = 'const PROGMEM unsigned char '+prefix+'_'+png[:-4]+'[] = {'
	d = d+'0x'+hex(cols)[2:]+','
	for r in range(0, rows):
		for c in range(0, cols, 2):
			firstNib = (int) ((255-data[r][c][0])/16)
			secondNib = (int) ((255-data[r][c+1][0])/16)

			firstNib = hex(firstNib)[2:]
			secondNib = hex(secondNib)[2:]
			if (r == rows-1) and (c == cols-2):
				d = d+'0x'+firstNib+secondNib+'};'
			else:
				d = d+'0x'+firstNib+secondNib+','
	print(d)