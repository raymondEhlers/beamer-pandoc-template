---
title: {{cookiecutter.title}}
subtitle: {%- if cookiecutter.subtitle|length %} {{cookiecutter.subtitle}}{%- else -%}{%- endif %}
aspectratio: 169
author:
- {{cookiecutter.author}}\inst{1}
shortAuthor: {{cookiecutter.short_author}}
institute: |
 \inst{1}{{cookiecutter.institute}}

date: {{ cookiecutter.date|format_time('DD MMMM YYYY') }}

graphics: true
{#- mathspec seems to be required to get an output with Noto Sans. See: https://tex.stackexchange.com/a/118254 #}
mathspec: true
{#- NOTE: We could reduce the size of the font (to an extent), but I think scaling looks better, so keep it this way #}
mainfont: Noto Sans
mainfontoptions:
- Scale=0.81
- ItalicFont=Noto Sans Italic
- BoldFont=Noto Sans Bold
- BoldItalicFont=Noto Sans Bold Italic
mathfont: Noto Sans Math
mathfontoptions:
- Scale=0.81
- ItalicFont=Noto Sans Italic
- BoldFont=Noto Sans Bold
- BoldItalicFont=Noto Sans Bold Italic

header-includes:
- \input{$HOME/.local/share/pandoc/preamble/beamer.UCB.LBNL.tex}
- \input{../../shared/shared.tex}
{#- Deal with the title logo. We have to use the int filter because bool isn't supported... #}
{%- if cookiecutter.jetscape_talk|int %}
- |
  \titlegraphic{
      \begin{tikzpicture}[remember picture,overlay]
          % First, position the bottom right corner of the LBL logo relative to the corner of the page.
          \node [scale=0.50, anchor=south east] (LBLTitleLogo) [above left= 0.5cm and 0.5cm of current page.south east] {\pgfuseimage{beamerTitleLogoLBL}};
          % Position UCB logo relative to the LBL logo, aligning the right edges
          \node [scale=0.34, above=-0.3cm of LBLTitleLogo.north east, anchor=south east] (UCBTitleLogo) {\pgfuseimage{beamerTitleLogoUCB}};
          % Position JETSCAPE logo relative to the upper right corner, aligning the right edges
          \node [scale=0.1275, anchor=north east] (JetscapeTitleLogo) [below left= 0.5cm and 0.5cm of current page.north east] {\pgfuseimage{beamerTitleLogoJetscape}};
      \end{tikzpicture}
  }
{%- else %}
- |
  \titlegraphic{
      \begin{tikzpicture}[remember picture,overlay]
          % First, position the bottom right corner of the LBL logo relative to the corner of the page.
          \node [scale=0.50, anchor=south east] (LBLTitleLogo) [above left= 0.5cm and 0.5cm of current page.south east] {\pgfuseimage{beamerTitleLogoLBL}};
          % Position UCB logo relative to the LBL logo, aligning the right edges
          \node [scale=0.34, above=-0.3cm of LBLTitleLogo.north east, anchor=south east] (UCBTitleLogo) {\pgfuseimage{beamerTitleLogoUCB}};
          % Position ALICE logo relative to the upper right corner, aligning the right edges
          \node [scale=0.3, anchor=north east] (aliceTitleLogo) [below left= 0.5cm and 0.5cm of current page.north east] {\pgfuseimage{beamerTitleLogoALICE}};
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

