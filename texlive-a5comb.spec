# revision 17020
# category Package
# catalog-ctan /macros/latex/contrib/a5comb
# catalog-date 2010-02-23 16:03:07 +0100
# catalog-license pd
# catalog-version 4
Name:		texlive-a5comb
Version:	4
Release:	4
Summary:	Support for a5 paper sizes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/a5comb
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/a5comb.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/a5comb.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 4-2
+ Revision: 749039
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 4-1
+ Revision: 717780
- texlive-a5comb
- texlive-a5comb
- texlive-a5comb
- texlive-a5comb
- texlive-a5comb

