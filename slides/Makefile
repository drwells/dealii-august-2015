LFLAGS=-halt-on-error -file-line-error
LDRAFTFLAGS=-draftmode $(LFLAGS)
UNAME = $(shell uname)
CWD = $(shell pwd)
# the command to create a temporary folder varies by platform.
ifeq ($(UNAME), Darwin)
	PYGMENTIZE = "/Users/drwells/Applications/sage.d/local/bin/pygmentize"
	PDFLATEX = "/usr/local/texlive/2012/bin/x86_64-darwin/pdflatex"
	BIBTEX = "/usr/local/texlive/2012/bin/x86_64-darwin/bibtex"
	TMPCMD = $(shell TMPDIR=$(CWD) && mktemp -t TMPMAIN)
else
	PYGMENTIZE = $(shell which pygmentize)
	PDFLATEX = $(shell which pdflatex)
	BIBTEX = $(shell which bibtex)
	TMPCMD = $(shell mktemp --tmpdir=$(CWD) -t XXXXXXXX)
endif

CPP_SRC_FILES := $(shell ls c++/*.cc)
CODE_TEX_FILES := $(patsubst %.cc, %.tex, $(CPP_SRC_FILES))
PYGMENTIZE_FLAGS :=-f latex -O style=colorful,linenos=1

main: *tex $(CODE_TEX_FILES)
	rm -f *aux
	$(PDFLATEX) $(LDRAFTFLAGS) main.tex | python ../filter.py
	$(BIBTEX) main
	$(PDFLATEX) $(LDRAFTFLAGS) main.tex 1>/dev/null
	$(PDFLATEX) $(LFLAGS) main.tex 1>/dev/null
	@printf "number of pages: %d\n" `pdfinfo main.pdf | grep 'Pages' | awk '{print $$2}'`
	cp main.pdf slides.pdf

# create temporary files; these must be deleted later.
setuptemp: quickcheck
	@$(eval TMPMAINROOT = $(TMPCMD))
	@$(eval TMPMAINTEX = $(TMPMAINROOT).tex)
	@$(eval TMPMAINBASE = $(shell basename $(TMPMAINROOT)))

# Compile with the nag package.
nag: *.tex setuptemp
	@printf "\\RequirePackage[l2tabu, orthodox]{nag}\n" >> $(TMPMAINTEX)
	@cat main.tex >> $(TMPMAINTEX)
	@$(PDFLATEX) $(LDRAFTFLAGS) $(TMPMAINTEX) 1>/dev/null
	@$(BIBTEX)   $(TMPMAINBASE) 1>/dev/null
	@$(PDFLATEX) $(LDRAFTFLAGS) $(TMPMAINTEX) 1>/dev/null
	@$(PDFLATEX) $(LFLAGS)    $(TMPMAINTEX) | python ../filterwarn.py
	@rm $(TMPMAINROOT)*

# Compile and show LaTeX warnings.
warn: main
	@$(PDFLATEX) $(LFLAGS) main.tex | python ../filterwarn.py

clean:
	rm -f *aux *lof *log *out *bbl *blg

c++/%.tex: c++/%.cc
	$(PYGMENTIZE) $(PYGMENTIZE_FLAGS) $< > $@
