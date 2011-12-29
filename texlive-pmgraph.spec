# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/pmgraph
# catalog-date 2008-11-04 08:05:43 +0100
# catalog-license gpl
# catalog-version 1.0
Name:		texlive-pmgraph
Version:	1.0
Release:	1
Summary:	"Poor man's" graphics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pmgraph
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pmgraph.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pmgraph.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A set of extensions to LaTeX picture environment, including a
wider range of vectors, and a lot more box frame styles.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pmgraph/pmgraph.sty
%doc %{_texmfdistdir}/doc/latex/pmgraph/COPYING
%doc %{_texmfdistdir}/doc/latex/pmgraph/README
%doc %{_texmfdistdir}/doc/latex/pmgraph/pmgraph.pdf
%doc %{_texmfdistdir}/doc/latex/pmgraph/pmgraph.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
