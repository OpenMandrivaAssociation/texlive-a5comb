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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Superseded by geometry.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/a5comb
%dir %{_datadir}/texmf-dist/tex/latex/a5comb
%doc %{_datadir}/texmf-dist/doc/latex/a5comb/a5comb.pdf
%doc %{_datadir}/texmf-dist/doc/latex/a5comb/a5comb.tex
%{_datadir}/texmf-dist/tex/latex/a5comb/a5comb.sty
