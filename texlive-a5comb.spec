%global tl_name a5comb
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4
Release:	%{tl_revision}.1
Summary:	Support for a5 paper sizes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/a5comb
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/a5comb.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/a5comb.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Superseded by geometry.

