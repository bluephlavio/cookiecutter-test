import os.path

TEX_DIR = 'tex'
TEMPLATE = '''
\documentclass[preview,border=0.5cm]{standalone}
\begin{document}

\end{document}
'''

n = {{ cookiecutter.number_of_problems }}

for i in range(n):
	problem = os.path.join(TEX_DIR, f'problem{i+1}.tex')
	solution = os.path.join(TEX_DIR, f'solution{i+1}.tex')
	with open(problem, 'w') as f:
		f.write(TEMPLATE)
	with open(solution, 'w') as f:
		f.write(TEMPLATE)
