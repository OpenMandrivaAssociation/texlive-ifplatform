Name:		texlive-ifplatform
Version:	45533
Release:	2
Summary:	Conditionals to test which platform is being used
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ifplatform
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifplatform.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifplatform.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifplatform.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package uses the (La)TeX extension -shell-escape to
establish whether the document is being processed on a Windows
or on a Unix-like system (Mac OS X, Linux, etc.), or on Cygwin
(Unix environment over a windows system). Booleans provided
are: - \ifwindows, - \iflinux, - \ifmacosx and - \ifcygwin. The
package also preserves the output of uname on a Unix-like
system, which may be used to distinguish between various
classes of Unix systems.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ifplatform/ifplatform.sty
%doc %{_texmfdistdir}/doc/latex/ifplatform/README
%doc %{_texmfdistdir}/doc/latex/ifplatform/ifplatform.pdf
#- source
%doc %{_texmfdistdir}/source/latex/ifplatform/ifplatform.dtx
%doc %{_texmfdistdir}/source/latex/ifplatform/ifplatform.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
