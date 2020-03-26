---
title: {{cookiecutter.title}}
subtitle: {%- if cookiecutter.subtitle|length %} {{cookiecutter.subtitle}}{%- else -%}{%- endif %}
# 16x9 aspect ratio
aspectratio: 169
author:
- {{cookiecutter.author}}\inst{1}
shortAuthor: {{cookiecutter.short_author}}
institute: |
 \inst{1}{{cookiecutter.institute}}

date: {{ cookiecutter.date|format_time('YYYY MMMM DD') }}

graphics: true
header-includes:
- \usepackage{amssymb}
- \usepackage{amsmath}
- \usepackage{siunitx}
- \usepackage{changepage} # Used to move tikzpicture to the left.
- \usepackage{tikz}
- \usepackage[clock]{ifsym} # For work-in-progress symbol (clock)
- \usetikzlibrary{shapes,arrows}
- \usetikzlibrary{fit,calc} # For creating block diagrams.
- \usetikzlibrary{positioning}
- \usetikzlibrary{decorations.pathreplacing} # For the bracket labeling Overwatch
- \input{$HOME/.local/share/pandoc/preamble/beamer.oakRidge.tex}
- \input{../../shared/shared.tex}
- \definecolor{YaleDarkBlue}{RGB}{0,62,114}
- \setbeamercolor{normal text}{fg=YaleDarkBlue, bg=black!2} # I don't think we have to specify the bg color, but it's done for safety. (It's black!2)
- \setbeamercolor{background canvas}{bg=white}
- \setbeamertemplate{frame footer}{\insertshortauthor~-~\insertdate}
- \usepackage{eulervm}  # Improve font in math mode to better match metropolis.
theme: metropolis
# Invoke with: pandoc --standalone -t beamer pandocPresentation.md -o pandocPresentation.pdf
---

## A Slide

::: {.columns}
::: {.column width="58%"}

- Some
- Content

:::
::: {.column width="58%"}

- For an image: `\insertImage{\textwidth}{pathInImagesDir.pdf}`

:::
:::

#

## {.standout}

Backup

