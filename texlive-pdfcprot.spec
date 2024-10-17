Name:		texlive-pdfcprot
Version:	18735
Release:	2
Summary:	Activating and setting of character protruding using pdflatex
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pdfcprot
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfcprot.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfcprot.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfcprot.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides an easy interface to adjust the character
protrusion for different fonts and choosing the right
adjustment automatically depending on the font.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
