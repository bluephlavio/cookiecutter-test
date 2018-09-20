import os.path

TEX_DIR = 'tex'

n = {{ cookiecutter.number }}

for i in range(n):
	filename = os.path.join(TEX_DIR, f'problem{i+1}.tex')
	with open(filename, 'w') as f:
		f.write('')
