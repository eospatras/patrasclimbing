FROM texlive/texlive:latest-minimal

# Proxy to APT cacher: e.g. http://apt-cacher-ng.docker:3142
ARG APT_CACHER

# Set the env variables to non-interactive
ENV DEBIAN_FRONTEND noninteractive
ENV DEBIAN_PRIORITY critical
ENV DEBCONF_NOWARNINGS yes


# Debian
#
RUN set -x && \
    # Setup a cacher to speed up build
    if [ -n "${APT_CACHER}" ] ; then \
        echo "Acquire::http::Proxy \"${APT_CACHER}\";" | tee /etc/apt/apt.conf.d/01proxy ; \
    fi; \
    apt-get -qq update && \
    apt-get -qq upgrade && \
    apt-get -qy install --no-install-recommends \
        #
        texlive-lang-other \
        # fonts-noto \
        # fonts-noto-color-emoji \
        # fonts-noto-core \
        # fonts-noto-mono \
        fonts-linuxlibertine \
        texlive-bibtex-extra \
        biber \
        librsvg2-bin \
        gcc \
        python3-dev \
        pandoc \
        python3-pip \
        unzip \
        wget \
        texlive-fonts-recommended \
        # texlive-fonts-extra \
        texlive-xetex \
        xz-utils \
        lmodern

# 'scrbook.cls' 
# RUN tlmgr install koma-script
RUN tlmgr init-usertree
RUN tlmgr list
RUN tlmgr update --self && \
    tlmgr install \
    koma-script\
    merriweather \
    fontaxes \
    mweights \
    mdframed \
    needspace \
    sourcesanspro \
    sourcecodepro \
    titling \
    ly1 \
    pagecolor \
    adjustbox \
    collectbox \
    titlesec \
    fvextra \
    pdftexcmds \
    footnotebackref \
    zref \
    fontawesome5 \
    footmisc \
    sectsty \
    koma-script \
    lineno \
    awesomebox \
    background \
    everypage \
    xurl \
    epstopdf \
    hardwrap \
    catchfile \
    newfloat \
    libertine

# RUN apt-get -qy install --no-install-recommends lmodern
# # `scrartcl.cls’
# RUN apt -y install texlive-latex-recommended

# # 'scrbook.cls' 
# RUN tlmgr install koma-script

# JetBrains fonts
RUN wget -O /tmp/fonts-jetbrains-mono_2.242+ds-3_all.deb 'http://ftp.de.debian.org/debian/pool/main/f/fonts-jetbrains-mono/fonts-jetbrains-mono_2.242+ds-3_all.deb' \
    &&  dpkg -i /tmp/fonts-jetbrains-mono_2.242+ds-3_all.deb
RUN rm -f /tmp/fonts-jetbrains-mono_2.242+ds-3_all.deb

# Ubuntu fonts
RUN wget -O /tmp/fonts-ubuntu_0.83-6_all.deb 'http://ftp.br.debian.org/debian/pool/non-free/f/fonts-ubuntu/fonts-ubuntu_0.83-6_all.deb' \
    &&  dpkg -i /tmp/fonts-ubuntu_0.83-6_all.deb
RUN rm -f /tmp/fonts-ubuntu_0.83-6_all.deb
RUN wget -O /tmp/fonts-ubuntu-console_0.83-6_all.deb 'http://ftp.br.debian.org/debian/pool/non-free/f/fonts-ubuntu/fonts-ubuntu-console_0.83-6_all.deb' \
    &&  dpkg -i /tmp/fonts-ubuntu-console_0.83-6_all.deb
RUN rm -f /tmp/fonts-ubuntu-console_0.83-6_all.deb


# RUN tlmgr install adjustbox babel-german background bidi collectbox csquotes everypage filehook footmisc footnotebackref framed fvextra letltxmacro ly1 mdframed mweights needspace pagecolor sourcecodepro sourcesanspro titling ucharcat ulem unicode-math upquote xurl zref
# # xecjk

# RUN tlmgr install awesomebox fontawesome5

# RUN tlmgr update --self && \
#     tlmgr install \
#     merriweather \
#     fontaxes \
#     mweights \
#     mdframed \
#     needspace \
#     sourcesanspro \
#     sourcecodepro \
#     titling \
#     ly1 \
#     pagecolor \
#     adjustbox \
#     collectbox \
#     titlesec \
#     fvextra \
#     pdftexcmds \
#     footnotebackref \
#     zref \
#     fontawesome5 \
#     footmisc \
#     sectsty \
#     koma-script \
#     lineno \
#     awesomebox \
#     background \
#     everypage \
#     xurl \
#     epstopdf \
#     hardwrap \
#     catchfile \
#     newfloat

# RUN pip3 uninstall -y pandoc-xnos pandoc-fignos pandoc-secnos pandoc-tablenos
# RUN pip3 install pandoc-fignos

#     # clean up
#     # && apt-get clean && \
#     # rm -rf /var/lib/apt/lists/* /etc/apt/apt.conf.d/01proxy

# # ##
# # ## M I S C
# # ##

# # #
# # # emojis support for latex
# # # https://github.com/mreq/xelatex-emoji
# # #
# # ARG TEXMF=/usr/share/texmf/tex/latex/
# # ARG EMOJI_DIR=/tmp/twemoji2
# # RUN git clone --single-branch --depth=1 --branch gh-pages https://github.com/twitter/twemoji.git $EMOJI_DIR && \
# #     # fetch xelatex-emoji
# #     mkdir -p ${TEXMF} && \
# #     cd ${TEXMF} && \
# #     rm -rf xelatex-emoji2 && \
# #     git clone --single-branch --branch images https://github.com/daamien/xelatex-emoji.git xelatex-emoji2 && \
# #     # convert twemoji SVG files into PDF files
# #     cp -r $EMOJI_DIR/2/svg xelatex-emoji2/images && \
# #     cd xelatex-emoji2/images && \
# #     ../bin/convert_svgs_to_pdfs ./*.svg && \
# #     # clean up
# #     rm -f *.svg && \
# #     rm -fr ${EMOJI_DIR} && \
# #     rm -rf xelatex-emoji2 && \
# #     # update texlive
# #     cd ${TEXMF} && \
# #     texhash

# # RUN pip3 install pandoc-fignos
# # RUN pip3 install pandoc-secnos
# # RUN pip3 install pandoc-tablenos
# # RUN pip3 install pandoc-xnos
# # RUN apt remove -y gcc python3-dev
# # RUN apt autoremove -y
# # RUN apt autoclean -y
# # # RUN rm -rf /usr/share/texmf/tex/latex/twemoji*
# # # RUN rm -rf /usr/share/texmf/fonts/truetype/OpenMoji-Color.ttf
# # RUN kpsewhich -var-value TEXMFLOCAL 
# # RUN mkdir -p /usr/local/share/texmf/tex/latex
# # RUN wget -O  /usr/local/share/texmf/tex/latex/twemojis.zip https://mirrors.ctan.org/macros/latex/contrib/twemojis.zip
# # RUN unzip    /usr/local/share/texmf/tex/latex/twemojis.zip -d /usr/local/share/texmf/tex/latex/
# # RUN rm       /usr/local/share/texmf/tex/latex/twemojis.zip
# # # RUN cd /usr/local/share/texmf/tex/latex/twemojis/ && pdflatex twemojis.ins
# # RUN wget -O  /usr/local/share/texmf/tex/latex/twemojis/twemojis.sty http://hci.ece.upatras.gr/twemojis.sty

# RUN mktexlsrf

# # # RUN wget -O /usr/share/texmf/fonts/truetype/OpenMoji-Color.ttf 'https://raw.githubusercontent.com/hfg-gmuend/openmoji/master/font/OpenMoji-Color.ttf'
# # # RUN mktexlsr

# RUN source .venv/bin/activate
RUN pip install pandoc-fignos --break-system-packages
RUN pip install pandoc-secnos --break-system-packages
RUN pip install pandoc-tablenos --break-system-packages
RUN pip install pandoc-xnos --break-system-packages
# patch xnos
RUN patch -p1 /usr/local/lib/python3.11/dist-packages/pandocxnos/core.py <<'EOF'
174c174
<     pattern = re.compile(r'^[1-2]\.[0-9]+(?:\.[0-9]+)?(?:\.[0-9]+)?$')
---
>     pattern = re.compile(r'^[1-3]\.[0-9]+(?:\.[0-9]+)?(?:\.[0-9]+)?$')
EOF


RUN pip install matplotlib --break-system-packages
RUN pip install pandoc-latex-environment --break-system-packages

RUN mv /usr/share/texlive/texmf-dist/tex/latex/caption /usr/share/texlive/texmf-dist/tex/latex/caption-latest
RUN wget -O /tmp/caption-CTAN_2020-10-26.zip 'https://gitlab.com/axelsommerfeldt/caption/-/archive/CTAN_2020-10-26/caption-CTAN_2020-10-26.zip'
RUN unzip -j /tmp/caption-CTAN_2020-10-26.zip "caption-CTAN_2020-10-26/tex/*" -d /usr/share/texlive/texmf-dist/tex/latex/caption


# # pandoc-plot
RUN wget -O  /tmp/pandoc-plot-Linux-x86_64-static.zip https://github.com/LaurentRDC/pandoc-plot/releases/download/1.7.0/pandoc-plot-Linux-x86_64-static.zip
RUN unzip    /tmp/pandoc-plot-Linux-x86_64-static.zip -d /usr/local/bin/
RUN chmod +x /usr/local/bin/pandoc-plot
RUN rm       /tmp/pandoc-plot-Linux-x86_64-static.zip
# RUN mktextfm /OT

RUN cd /tmp
RUN apt-get -qy download --no-install-recommends texlive-fonts-extra

# dpkg -x texlive-fonts-extra_2019.202000218-1_all.deb ./

# sudo mkdir -p /usr/share/texlive/texmf-dist/tex/latex/fontawesome/
# sudo cp -v ./usr/share/texlive/texmf-dist/tex/latex/fontawesome/fontawesome.sty /usr/share/texlive/texmf-dist/tex/latex/fontawesome/fontawesome.sty

# cd ..
# rm -rf fontdownload

## HOW TO INSTALL ONLY fontwesome.sty
# mkdir fontdownload
# cd fontdownload

# sudo apt-get download texlive-fonts-extra

# dpkg -x texlive-fonts-extra_2019.202000218-1_all.deb ./

# sudo mkdir -p /usr/share/texlive/texmf-dist/tex/latex/fontawesome/
# sudo cp -v ./usr/share/texlive/texmf-dist/tex/latex/fontawesome/fontawesome.sty /usr/share/texlive/texmf-dist/tex/latex/fontawesome/fontawesome.sty

# cd ..
# rm -rf fontdownload

RUN mkdir /pandoc
VOLUME /pandoc
WORKDIR /pandoc

ENTRYPOINT ["pandoc"]