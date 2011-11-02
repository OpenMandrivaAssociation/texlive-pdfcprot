Name:		texlive-pdfcprot
Version:	1.7a
Release:	1
Summary:	Activating and setting of character protruding using pdflatex
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pdfcprot
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfcprot.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfcprot.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfcprot.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package provides an easy interface to adjust the character
protrusion for different fonts and choosing the right
adjustment automatically depending on the font.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pdfcprot/pdfcprot.sty
%{_texmfdistdir}/tex/latex/pdfcprot/pplmnOT1.cpa
%{_texmfdistdir}/tex/latex/pdfcprot/pplmnOT2.cpa
%{_texmfdistdir}/tex/latex/pdfcprot/pplmnT1.cpa
%{_texmfdistdir}/tex/latex/pdfcprot/pplmnT2A.cpa
%{_texmfdistdir}/tex/latex/pdfcprot/pplmnTS1.cpa
%doc %{_texmfdistdir}/doc/latex/pdfcprot/00CONTEN
%doc %{_texmfdistdir}/doc/latex/pdfcprot/00README
%doc %{_texmfdistdir}/doc/latex/pdfcprot/INSTALL.txt
%doc %{_texmfdistdir}/doc/latex/pdfcprot/LEGAL.txt
%doc %{_texmfdistdir}/doc/latex/pdfcprot/Makefile.unx
%doc %{_texmfdistdir}/doc/latex/pdfcprot/README.txt
%doc %{_texmfdistdir}/doc/latex/pdfcprot/TODO
%doc %{_texmfdistdir}/doc/latex/pdfcprot/pdfcprot.pdf
#- source
%doc %{_texmfdistdir}/source/latex/pdfcprot/pdfcprot.dtx
%doc %{_texmfdistdir}/source/latex/pdfcprot/pdfcprot.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
