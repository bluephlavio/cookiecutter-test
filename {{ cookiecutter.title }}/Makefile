LATEST = latest

TEMPLATES_DIR = templates
TEST_TEMPLATE = $(TEMPLATES_DIR)/test.tmpl

TEX_DIR = tex
TEX_FILES = $(TEX_DIR)/*.tex

MAIN = test
MAIN_DAT = $(MAIN).yml
MAIN_TEX = $(MAIN).tex
MAIN_PDF = $(MAIN).pdf

CLEAN_FILES = *.log *.aux
DISTCLEAN_FILES = *.tex *.pdf *.dvi

.PHONY: all main clean distclean

all: $(MAIN_TEX) $(MAIN_PDF)

$(MAIN_TEX): $(TEMPLATE) $(MAIN_DAT)
	$(LATEST) $(TEST_TEMPLATE) $(MAIN_DAT) -o $(MAIN_TEX)

$(MAIN_PDF): $(MAIN_TEX)
	pdflatex $(MAIN_TEX)
	pdflatex $(MAIN_TEX)

clean:
	rm -rf $(CLEAN_FILES)
	find . -name *~ | xargs rm -rf

distclean: clean
	rm -rf $(DISTCLEAN_FILES)
