---
title: Πάτρα - Αναρριχητικός οδηγός
author: ΕΟΣ Πατρών και φίλοι

keywords:
    - Climbing
    - Patras
    - Greece
    - Climbing guide
lang: el-GR
subject: Climbing guide
book: true
toc-own-page: true
toc: true
classoption:
    - twoside

titlepage: true
titlepage-color: f2f2f2
titlepage-text-color: 435488
titlepage-rule-height: 10
titlepage-rule-color: 435488
# titlepage-background: images/cover-6.png
# logo: images/logos-combined.png

number_sections: true
toc_depth: 2

colorlinks: true
header-includes:
    - |
        ```{=latex}
        \usepackage{cleveref}
        \usepackage{caption}
        % pandoc-fignos: change the caption name
        \renewcommand{\figurename}{Εικόνα}
        ```

plot-configuration: conf/pandoc-plot.yml

# pandoc-latex-environment:
#     noteblock: [note]
#     tipblock: [tip]
#     warningblock: [warning]
#     cautionblock: [caution]
#     importantblock: [important]

# xnos-warning-level: 1
# fignos-cleveref: False
# fignos-plus-name: Εικόνα
# fignos-star-name: Εικόνα
# fignos-caption-name: Εικόνα
# fignos-caption-separator: period
# fignos-number-by-section: False
caption-justification: centering # see caption package docs
caption-labelformat: original # see caption package docs
geometry: [a4paper, bindingoffset=10mm, inner=20mm, outer=20mm, top=20mm, bottom=20mm] # See https://ctan.org/pkg/geometry for more options

pandoc-latex-environment:
    noteblock: [note]
    tipblock: [tip]
    warningblock: [warning]
    cautionblock: [caution]
    importantblock: [important]
listings-disable-line-numbers: false
disable-header-and-footer: false
header-left: "\\leftmark"
header-right: "\\hspace{1cm}"
# header-center: header-center
# number-offset: 4,3

mainfont: "Linux Libertine O"
# CJKmainfont: Noto Serif CJK SC
sansfont: "Linux Biolinum O"
monofont: "Ubuntu Mono"

# float-placement-figure: t

lof: false # List of figures
lot: false # List of tables

table-use-row-colors: true


---

