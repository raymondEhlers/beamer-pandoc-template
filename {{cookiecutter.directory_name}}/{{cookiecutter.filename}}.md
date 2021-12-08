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

date: {{ cookiecutter.date|format_time('DD MMMM YYYY') }}

graphics: true
header-includes:
- \usepackage{amssymb}
- \usepackage{amsmath}
- \usepackage{siunitx}
- \usepackage{eulervm}  # Improve font in math mode to better match metropolis.
- \usepackage{changepage} # Used to move tikzpicture to the left.
- \usepackage{tikz}
- \usepackage[clock]{ifsym} # For work-in-progress symbol (clock)
- \usetikzlibrary{shapes,arrows}
- \usetikzlibrary{fit,calc} # For creating block diagrams.
- \usetikzlibrary{positioning}
- \input{$HOME/.local/share/pandoc/preamble/beamer.UCB.LBNL.tex}
- \input{../../shared/shared.tex}
# Customize beamer
# Customize the footer to include the short author followed by the date.
- \setbeamertemplate{frame footer}{\insertshortauthor~-~\insertdate}
# Font customization. Somehow the font sizes look smaller in the green, so we increase a number of them.
- \setbeamerfont{title}{size=\LARGE}
- \setbeamerfont{frametitle}{size=\Large}
- \setbeamerfont{author}{size=\normalsize}
# Customize metropolis colorscheme.
# Normally, we would just define normal text as UCBBlue and be done with it. However, the
# green text is hard to read on slides. So we need to make the normal text black, and then update
# the theme were needed.
{#- Main colors #}
- \definecolor{UCBBlue}{HTML}{003262} # UCB Blue (primary) - "Berkeley Blue"
- \definecolor{UCBLightBlue}{HTML}{3B7EA1} # UCB Light Blue (secondary) - "Founder's Rock"
- \definecolor{UCBOrange}{HTML}{D9661F} # UCB Orange (secondary) - "Wellman Tile"
- \setbeamercolor{normal text}{fg=black, bg=white}
{#- Tweaks any bars, including dividing #}
- \setbeamercolor{progress bar}{fg=UCBLightBlue, bg=UCBLightBlue!50!black!30} # Formula for bg is default in Metropolis.
{#- Title page #}
- \setbeamercolor{titlelike}{fg=UCBBlue, bg=white}
- \setbeamercolor{author}{fg=UCBBlue, bg=white}
- \setbeamercolor{date}{fg=UCBBlue, bg=white}
- \setbeamercolor{institute}{fg=UCBBlue, bg=white}
{#- Structure of the page (bullet point color, etc) #}
- \setbeamercolor{structure}{fg=UCBBlue, bg=white}
{#- Color of the frame title and background, so we invert it (this appears to be the standard approach) #}
- \setbeamercolor{palette primary}{fg=white, bg=UCBBlue}
{#- Footer color #}
- \setbeamercolor{footline}{fg=UCBBlue!90}
{#- Deal with the title logo. We have to use the int filter because bool isn't supported... #}
{%- if cookiecutter.include_UTK|int %}
- |
  \titlegraphic{
      \begin{tikzpicture}[remember picture,overlay]
          % Position logos relative to the corner.
          %\node [scale=0.14] (JetscapeTitleLogo) [above left= 2.9cm and 0.95cm of current page.south east] {\pgfuseimage{beamerTitleLogoJetscape}};
          \node [scale=0.05] (ORNLTitleLogo) [above left= 1.7cm and 0.5cm of current page.south east] {\pgfuseimage{beamerTitleLogoORNL}};
          \node [scale=0.48] (UTKTitleLogo) [above left= 0.5cm and 0.5cm of current page.south east] {\pgfuseimage{beamerTitleLogoUTK}};
          %\node [scale=0.1275] (JetscapeTitleLogo) [above left= 2.9cm and 0.9cm of current page.south east] {\pgfuseimage{beamerTitleLogoJetscape}};
          \node [scale=0.1275] (JetscapeTitleLogo) [above= 0.1 cm of ORNLTitleLogo] {\pgfuseimage{beamerTitleLogoJetscape}};
      \end{tikzpicture}
  }
{%- else %}
- |
  \titlegraphic{
      \begin{tikzpicture}[remember picture,overlay]
          % First, position the bottom right corner of the UCB logo relative to the corner of the page.
          \node [scale=0.35, anchor=south east] (UCBTitleLogo) [above left= 0.75cm and 0.75cm of current page.south east] {\pgfuseimage{beamerTitleLogoUCB}};
          % Position ALICE logo relative to the UCB logo, aligning the right edges
          \node [scale=0.14, above = 1.8cm of UCBTitleLogo.east, anchor=east] (aliceTitleLogo) {\pgfuseimage{beamerTitleLogoALICE}};
      \end{tikzpicture}
  }
{%- endif %}
theme: metropolis
# Invoke with: pandoc --standalone -t beamer pandocPresentation.md -o pandocPresentation.pdf
---

## A Slide


::: {.columns align=center}
::: {.column width="58%"}

- Some
- Content


:::
::: {.column width="58%"}

- For an image: `\insertImage{\textwidth}{pathInImagesDir.pdf}`


:::
:::

#

## {.plain .standout}

\LARGE Backup

