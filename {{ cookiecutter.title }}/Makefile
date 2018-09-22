ENGINE = latest

TMPL_DIR = templates
TEX_DIR = tex
BUILD_DIR = build

MAIN_TMPL = $(TMPL_DIR)/{{ cookiecutter.template }}.tmpl
SOLUTIONS_TMPL = $(TMPL_DIR)/solutions.tmpl

DAT_FILE = {{ cookiecutter.template }}.yml
TEX_FILES = $(TEX_DIR)/*.tex
OUT_FILES = $(BUILD_DIR)/*.pdf
CLEAN_FILES = $(BUILD_DIR)/*.log $(BUILD_DIR)/*.aux
DISTCLEAN_FILES = $(BUILD_DIR)/*

MAIN = {{ cookiecutter.template }}
MAIN_TEX = $(TEX_DIR)/$(MAIN).tex
MAIN_PDF = $(BUILD_DIR)/{{ cookiecutter.slug }}-$(MAIN).pdf

SOLUTIONS = solutions
SOLUTIONS_TEX = $(TEX_DIR)/$(SOLUTIONS).tex
SOLUTIONS_PDF = $(BUILD_DIR)/{{ cookiecutter.slug }}-$(SOLUTIONS).tex

.PHONY: all main solutions clean distclean

all: main solutions

clean:
	rm -rf $(CLEAN_FILES)

distclean: clean
	rm -rf $(DISTCLEAN_FILES)

main: $(MAIN_TEX) $(MAIN_PDF)

$(MAIN_TEX): $(MAIN_TMPL) $(DAT_FILE)
	$(ENGINE) $(MAIN_TMPL) $(DAT_FILE) -o $(MAIN_TEX)

$(MAIN_PDF): $(MAIN_TEX) $(TEX_FILES)
	pdflatex -output-directory $(BUILD_DIR) $(MAIN_TEX)

solutions: $(SOLUTIONS_TEX) $(SOLUTIONS_PDF)

$(SOLUTIONS_TEX): $(SOLUTIONS_TMPL) $(DAT_FILE)
	$(ENGINE) $(SOLUTIONS_TMPL) $(DAT_FILE) -o $(SOLUTIONS_TEX)

$(SOLUTIONS_PDF): $(SOLUTIONS_TEX) $(TEX_FILES)
	pdflatex -output-directory $(BUILD_DIR) $(SOLUTIONS_TEX)
