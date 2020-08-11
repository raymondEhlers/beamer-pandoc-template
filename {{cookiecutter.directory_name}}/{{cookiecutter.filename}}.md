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
- \usepackage{eulervm}  # Improve font in math mode to better match metropolis.
- \usepackage{changepage} # Used to move tikzpicture to the left.
- \usepackage{tikz}
- \usepackage[clock]{ifsym} # For work-in-progress symbol (clock)
- \usetikzlibrary{shapes,arrows}
- \usetikzlibrary{fit,calc} # For creating block diagrams.
- \usetikzlibrary{positioning}
- \input{$HOME/.local/share/pandoc/preamble/beamer.oakRidge.tex}
- \input{../../shared/shared.tex}
# Customize beamer
# Customize the footer to include the short author followed by the date.
- \setbeamertemplate{frame footer}{\insertshortauthor~-~\insertdate}
# Font customization. Somehow the font sizes look smaller in the green, so we increase a number of them.
- \setbeamerfont{title}{size=\LARGE}
- \setbeamerfont{frametitle}{size=\Large}
- \setbeamerfont{author}{size=\normalsize}
# Customize metropolis colorscheme.
# Normally, we would just define normal text as ORNLGreen and be done with it. However, the
# green text is hard to read on slides. So we need to make the normal text black, and then update
# the theme were needed.
{#- Main colors #}
- \definecolor{ORNLGreen}{rgb}{0.0, 0.4745, 0.2} # ORNL Green (primary)
- \definecolor{ORNLGray}{rgb}{0.9, 0.91, 0.9} # ORNL Grey (secondary)
- \setbeamercolor{normal text}{fg=black, bg=white}
{#- Tweaks any bars, including dividing #}
- \setbeamercolor{progress bar}{fg=ORNLGray, bg=ORNLGray!50!black!30} # Formula for bg is default in Metropolis.
{#- Title page #}
- \setbeamercolor{titlelike}{fg=ORNLGreen, bg=white}
- \setbeamercolor{author}{fg=ORNLGreen, bg=white}
- \setbeamercolor{date}{fg=ORNLGreen, bg=white}
- \setbeamercolor{institute}{fg=ORNLGreen, bg=white}
{#- Structure of the page (bullet point color, etc) #}
- \setbeamercolor{structure}{fg=ORNLGreen, bg=white}
{#- Color of the frame title and background, so we invert it (this appears to be the standard approach) #}
- \setbeamercolor{palette primary}{fg=white, bg=ORNLGreen}
{#- Footer color #}
- \setbeamercolor{footline}{fg=ORNLGreen!90}
{#- Deal with the title logo. We have to use the int filter because bool isn't supported... #}
{%- if cookiecutter.include_UTK|int %}
- |
  \titlegraphic{
      \begin{tikzpicture}[remember picture,overlay]
          % Position other logo relative to the ALICE logo.
          \node [scale=0.14] (aliceTitleLogo) [above left= 1.25cm and 1.25cm of current page.south east] {\pgfuseimage{beamerTitleLogoALICE}};
          \node [scale=0.05] (ORNLTitleLogo) [above left= -1.1cm and 0.08cm of aliceTitleLogo] {\pgfuseimage{beamerTitleLogoORNL}};
          \node [scale=0.48] (UTKTitleLogo) [below left= -1.3cm and 0.08cm of aliceTitleLogo] {\pgfuseimage{beamerTitleLogoUTK}};
      \end{tikzpicture}
  }
{%- else %}
- |
  \titlegraphic{
      \begin{tikzpicture}[remember picture,overlay]
          % Position other logo relative to the ALICE logo.
          \node [scale=0.14] (aliceTitleLogo) [above left= 1.25cm and 1.5cm of current page.south east] {\pgfuseimage{beamerTitleLogoALICE}};
          % NOTE: The y shift is much smaller than the 1cm value implies...
          \node [scale=0.06, yshift=1cm] (ORNLTitleLogo) [left=0.15cm of aliceTitleLogo] {\pgfuseimage{beamerTitleLogoORNL}};
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

