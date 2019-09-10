import os
import yaml
from invoke import task
from latest import render

ROOT = os.path.abspath(os.path.dirname(__file__))
CONFIG = os.path.join(ROOT, 'config.yml')

SRC_DIR = os.path.join(ROOT, 'src')
TEMPLATES_DIR = os.path.join(ROOT, 'templates')
BUILD_DIR = os.path.join(ROOT, 'build')
DIST_DIR = os.path.join(ROOT, 'dist')

def slugify(s):
    return s.lower().replace(' ', '-')

def read_config():
    with open(CONFIG, 'r') as f:
        return yaml.load(f, Loader=yaml.FullLoader)

def write_config(config):
    with open(CONFIG, 'w') as f:
        yaml.dump(config, f)

def get_template(name):
    template_file = os.path.join(TEMPLATES_DIR, f'{name}.tmpl')
    with open(template_file, 'r') as f:
        return f.read()

@task
def newproblem(c, name):
    problem_dir = os.path.join(SRC_DIR, name)
    c.run(f'mkdir {problem_dir}')
    assignment_file = os.path.join(problem_dir, 'assignment.tex')
    solution_file = os.path.join(problem_dir, 'solution.tex')
    template_file = os.path.join(TEMPLATES_DIR, 'standalone.tmpl')
    with open(template_file, 'r') as f:
        template = f.read()
    with open(assignment_file, 'w+') as f:
        content = render(template, {'name': f'{name} assignment'})
        f.write(content)
    with open(solution_file, 'w+') as f:
        content = render(template, {'name': f'{name} solution'})
        f.write(content)

@task
def newtarget(c, name, title='', author='', date=''):
    config = read_config()
    title = title or config['title']
    slug = slugify(title)
    slug += f'-{slugify(author)}' if author else ''
    slug += f'-{slugify(date)}' if date else ''
    targets = config['targets']
    targets[name] = {
        'title': title,
        'author': author,
        'date': date,
        'slug': slug,
        'problemset': []
    }
    write_config(config)


@task
def make(c, name, template='test'):
    config = read_config()
    targets = config['targets']
    target = targets[name]
    slug = target['slug']
    template = get_template(template)
    tex_file = os.path.join(BUILD_DIR, f'{slug}.tex')
    with open(tex_file, 'w+') as f:
        content = render(template, target)
        f.write(content)
    c.run(f'pdflatex -output-directory {DIST_DIR} -job-name {slug} {tex_file}')
