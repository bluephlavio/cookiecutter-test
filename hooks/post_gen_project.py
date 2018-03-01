import os.path

n = {{ cookiecutter.number }}

for i in range(n):
	dir = 'tex'
	filename = os.path.join(dir, f'problem{i+1}.tex')
	with open(filename, 'w') as f:
		f.write('')
	
