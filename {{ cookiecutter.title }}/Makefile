ENGINE = latest

TMPL_DIR = templates
TEX_DIR = tex
BUILD_DIR = build

MAIN_TMPL = $(TMPL_DIR)/{{ cookiecutter.template }}.tmpl
SOLUTIONS_TMPL = $(TMPL_DIR)/solutions.tmpl

DAT_FILES = *.yml *.yaml
TEX_FILES = $(TEX_DIR)/*.tex
OUT_FILES = $(BUILD_DIR)/*.pdf
CLEAN_FILES = $(BUILD_DIR)/*.log $(BUILD_DIR)/*.aux
DISTCLEAN_FILES = $(BUILD_DIR)/*

MAIN = {{ cookiecutter.template }}
MAIN_DAT = $(MAIN).yml
MAIN_TEX = $(TEX_DIR)/$(MAIN).tex
MAIN_PDF = $(BUILD_DIR)/$(MAIN).pdf

{% if cookiecutter.template == 'test' %}
REC = {{ cookiecutter.template }}-rec
REC_DAT = $(REC).yml
REC_TEX = $(TEX_DIR)/$(REC).tex
REC_PDF = $(BUILD_DIR)/$(REC).pdf
{% endif %}

EDITOR = {{ cookiecutter.editor }}
VIEWER = {{ cookiecutter.viewer }}

.PHONY: all main solutions rec clean distclean edit view

all: main

clean:
	rm -rf $(CLEAN_FILES)

distclean: clean
	rm -rf $(DISTCLEAN_FILES)

main: $(MAIN_TEX) $(MAIN_PDF)

$(MAIN_TEX): $(MAIN_TMPL) $(MAIN_DAT)
	$(ENGINE) $(MAIN_TMPL) $(MAIN_DAT) -o $(MAIN_TEX)

$(MAIN_PDF): $(MAIN_TEX) $(TEX_FILES)
	pdflatex -output-directory $(BUILD_DIR) $(MAIN_TEX)
	pdflatex -output-directory $(BUILD_DIR) $(MAIN_TEX)

solutions: $(SOLUTIONS_TEX) $(MAIN_DAT)

$(SOLUTIONS_TEX): $(SOLUTIONS_TMPL) $(MAIN_DAT)
	$(ENGINE) $(SOLUTONS_TMPL) $(MAIN_DAT) -o $(SOLUTIONS_TEX)

$(SOLUTIONS_PDF): $(SOLUTIONS_TEX) $(TEX_FILES)
	pdflatex -output-directory $(BUILD_DIR) $(SOLUTIONS_TEX)
	pdflatex -output-directory $(BUILD_DIR) $(SOLUTIONS_TEX)

{% if cookiecutter.template == 'test' %}
rec: $(REC_TEX) $(REC_PDF)

$(REC_TEX): $(TEMPLATE) $(REC_DAT)
	$(LATEST) $(TEMPLATE) $(REC_DAT) -o $(REC_TEX)

$(REC_PDF): $(REC_TEX) $(TEX_FILES)
	pdflatex -output-directory $(BUILD_DIR) $(REC_TEX)
	pdflatex -output-directory $(BUILD_DIR) $(REC_TEX)
{% endif %}

edit:
	$(EDITOR) $(DAT_FILES) $(TEX_FILES)

view:
	$(VIEWER) $(OUT_FILES)
