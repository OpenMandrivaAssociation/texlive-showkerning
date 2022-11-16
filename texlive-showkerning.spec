Name:		texlive-showkerning
Version:	63708
Release:	1
Summary:	Showing kerns in a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/showkerning
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/showkerning.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/showkerning.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package displays all kerning values in the form of colored
bars directly at the respective position in the document.
Positive values are displayed in green, negative values in red.
The width of the bars corresponds exactly to the respective
kerning value. By option the bars can be placed behind or in
front of the glyphs. The package requires LuaLaTeX.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/lualatex/showkerning
%doc %{_texmfdistdir}/doc/lualatex/showkerning

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
