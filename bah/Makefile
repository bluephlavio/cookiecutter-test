LATEST = latest

TEMPLATES_DIR = templates
TEX_DIR = tex
BUILD_DIR = build

TEST_TEMPLATE = $(TEMPLATES_DIR)/test.tmpl
TEX_FILES = $(TEX_DIR)/*.tex

MAIN = test
MAIN_DAT = $(MAIN).yml
MAIN_TEX = $(TEX_DIR)/$(MAIN).tex
MAIN_PDF = $(BUILD_DIR)/$(MAIN).pdf

REC = test-rec
REC_DAT = $(REC).yml
REC_TEX = $(TEX_DIR)/$(REC).tex
REC_PDF = $(BUILD_DIR)/$(REC).pdf

CLEAN_FILES = $(BUILD_DIR)/*.log $(BUILD_DIR)/*.aux
DISTCLEAN_FILES = $(BUILD_DIR)/*


.PHONY: all main rec clean distclean

all: main clean

clean:
	rm -rf $(CLEAN_FILES)
	find . -name *~ | xargs rm -rf

distclean: clean
	rm -rf $(DISTCLEAN_FILES)

main: $(MAIN_TEX) $(MAIN_PDF)

$(MAIN_TEX): $(TEST_TEMPLATE) $(MAIN_DAT)
	$(LATEST) $(TEST_TEMPLATE) $(MAIN_DAT) -o $(MAIN_TEX)

$(MAIN_PDF): $(MAIN_TEX) $(TEX_FILES)
	pdflatex -output-directory $(BUILD_DIR) $(MAIN_TEX)
	pdflatex -output-directory $(BUILD_DIR) $(MAIN_TEX)

rec: $(REC_TEX) $(REC_PDF)

$(REC_TEX): $(TEST_TEMPLATE) $(REC_DAT)
	$(LATEST) $(TEST_TEMPLATE) $(REC_DAT) -o $(REC_TEX)

$(REC_PDF): $(REC_TEX) $(TEX_FILES)
	pdflatex -output-directory $(BUILD_DIR) $(REC_TEX)
	pdflatex -output-directory $(BUILD_DIR) $(REC_TEX)

