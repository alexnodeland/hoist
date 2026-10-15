# The LaTeX manuscript of ../hoist.md: `make` writes hoist.tex and figures/
# (build.py) and builds hoist.pdf; `make arxiv` packs the sources arXiv
# needs, the bibliography compiled (arXiv runs no BibTeX), into arxiv.tar.gz.
# Needs pandoc, rsvg-convert and a TeX distribution with latexmk.

# The PDF carries the date of the Markdown's last commit, so it rebuilds the same.
SOURCE_DATE_EPOCH ?= $(shell git log -1 --format=%ct -- ../hoist.md 2>/dev/null || date +%s)
export SOURCE_DATE_EPOCH
export FORCE_SOURCE_DATE = 1

SOURCES = hoist.tex refs.bib figure1.tex algorithm1.tex

all: hoist.pdf

hoist.tex: ../hoist.md build.py template.tex $(wildcard ../*.svg)
	python3 build.py

hoist.pdf: $(SOURCES)
	latexmk -pdf -interaction=nonstopmode -halt-on-error -silent hoist.tex

arxiv.tar.gz: hoist.pdf
	tar -czf $@ $(SOURCES) hoist.bbl figures/*.pdf

arxiv: arxiv.tar.gz

clean:
	latexmk -c hoist.tex
	rm -f arxiv.tar.gz

.PHONY: all arxiv clean
