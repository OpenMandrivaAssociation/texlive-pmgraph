%global tl_name pmgraph
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Poor mans graphics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pmgraph
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pmgraph.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pmgraph.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A set of extensions to LaTeX picture environment, including a wider
range of vectors, and a lot more box frame styles.

