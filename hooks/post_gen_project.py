import os.path

TEX_DIR = 'tex'
TEMPLATE = '''
\\documentclass[preview,border=0.5cm]{standalone}
\\usepackage[utf8]{inputenc}
\\usepackage[italian]{babel}
\\begin{document}

\\end{document}
'''.strip()

NUMBER_OF_PROBLEMS = {{ cookiecutter.number_of_problems }}

for i in range(NUMBER_OF_PROBLEMS):
	problem = os.path.join(TEX_DIR, f'problem{i+1}.tex')
	solution = os.path.join(TEX_DIR, f'solution{i+1}.tex')
	with open(problem, 'w') as f:
		f.write(TEMPLATE)
	with open(solution, 'w') as f:
		f.write(TEMPLATE)
