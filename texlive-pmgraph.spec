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
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A set of extensions to LaTeX picture environment, including a
wider range of vectors, and a lot more box frame styles.

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
