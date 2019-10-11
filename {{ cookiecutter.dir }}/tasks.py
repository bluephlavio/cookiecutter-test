import os
import glob
import oyaml as yaml
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
def newproblem(c, name, version):
    problem_dir = os.path.join(SRC_DIR, name)
    version_dir = os.path.join(problem_dir, version)
    assignment_dir = os.path.join(version_dir, 'assignment')
    solution_dir = os.path.join(version_dir, 'solution')
    if not os.path.isdir(problem_dir):
        os.mkdir(problem_dir)
    os.mkdir(version_dir)
    os.mkdir(assignment_dir)
    os.mkdir(solution_dir)
    assignment_file = os.path.join(assignment_dir, 'assignment.tex')
    solution_file = os.path.join(solution_dir, 'solution.tex')
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
def newtarget(c, name):
    config = read_config()
    default_title = config['title']
    title_prompt = input(f'Title [{default_title}]:')
    title = title_prompt if title_prompt else config['title']
    author = input('Author:')
    date = input('Date:')
    template_prompt = input('Template [test]:')
    template = template_prompt if template_prompt else 'test'
    slug = slugify(title)
    slug += f'-{slugify(name)}'
    targets = config.get('targets', {})
    targets[name] = {
        'title': title,
        'author': author,
        'date': date,
        'slug': slug,
        'template': template
    }
    config['targets'] = targets
    write_config(config)


@task
def make(c, name, twice=False, doc=None):
    config = read_config()
    targets = config['targets']
    target = targets[name]
    slug = target['slug']
    template_name = doc or target['template']
    template = get_template(template_name)
    tex_file = os.path.join(BUILD_DIR, f'{slug}-{template_name}.tex')
    with open(tex_file, 'w+') as f:
        content = render(template, target)
        f.write(content)
    out_filename = f'{slug}-{template_name}'
    c.run(f'pdflatex -output-directory {DIST_DIR} -job-name {out_filename} {tex_file}')
    if twice:
        c.run(f'pdflatex -output-directory {DIST_DIR} -job-name {out_filename} {tex_file}')


@task
def view(c, target, doc=None):
    config = read_config()
    targets = config['targets']
    target = targets[target]
    slug = target['slug']
    pdf_filename = f'{slug}-{doc}' if doc else slug
    pdf_file = os.path.join(DIST_DIR, f'{pdf_filename}.pdf')
    os.system(f'sumatrapdf {pdf_file} &')


@task
def clean(c, dist=False, targets=False):
    for f in glob.iglob('build/*'):
        os.remove(f)
    for f in glob.iglob('dist/*'):
        if not f.endswith('.pdf') or dist:
            os.remove(f)
    for f in glob.iglob('src/**/*', recursive=True):
        if not f.endswith('.tex') and os.path.isfile(f):
            os.remove(f)
    if targets:
        config = read_config()
        del config['targets']
        write_config(config)