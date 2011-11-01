Name:		texlive-a5comb
Version:	4
Release:	1
Summary:	Support for a5 paper sizes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive//macros/latex/contrib/a5comb
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/a5comb.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/a5comb.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Superceded by geometry.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/a5comb/a5comb.sty
%doc %{_texmfdistdir}/doc/latex/a5comb/a5comb.pdf
%doc %{_texmfdistdir}/doc/latex/a5comb/a5comb.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
