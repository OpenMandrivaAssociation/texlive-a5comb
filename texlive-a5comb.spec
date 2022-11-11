Name:		texlive-a5comb
Version:	17020
Release:	1
Summary:	Support for a5 paper sizes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/a5comb
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/a5comb.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/a5comb.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Superceded by geometry.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/a5comb/a5comb.sty
%doc %{_texmfdistdir}/doc/latex/a5comb/a5comb.pdf
%doc %{_texmfdistdir}/doc/latex/a5comb/a5comb.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
