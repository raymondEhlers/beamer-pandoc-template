# Determine the next draft number
DRAFTS:= $(wildcard drafts/*.pdf)
N_DRAFTS:= $(words $(DRAFTS))
# NOTE: Need to do these gymnastics to get the version number here because the more
# 		standard approach will wait to evaluate until we actually use it. Which means
# 		that the user then has to do the addition themselves. This isn't so hard, but is
# 		less than ideal. So we evaluate it here using the shell instead.
NEXT_VERSION:= $(shell echo $$(( $(N_DRAFTS) + 1 )))

.PHONY: all draft

all: {{cookiecutter.filename}}.md
	 pandoc --to beamer --verbose --standalone --pdf-engine-opt=-shell-escape {{cookiecutter.filename}}.md -o {{cookiecutter.filename}}.pdf

draft: all
	# The next version of the draft will be the number of pdf files + 1
	cp {{cookiecutter.filename}}.pdf drafts/$(shell date '+%Y-%m-%d').{{cookiecutter.author_identifier}}.{{cookiecutter.filename}}.v$(NEXT_VERSION).pdf

