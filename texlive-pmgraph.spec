Name:		texlive-pmgraph
Version:	15878
Release:	2
Summary:	"Poor man's" graphics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pmgraph
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pmgraph.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pmgraph.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
