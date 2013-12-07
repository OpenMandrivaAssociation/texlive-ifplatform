# revision 21156
# category Package
# catalog-ctan /macros/latex/contrib/ifplatform
# catalog-date 2009-09-10 17:35:10 +0200
# catalog-license lppl
# catalog-version 0.3a
Name:		texlive-ifplatform
Version:	0.3a
Release:	6
Summary:	Conditionals to test which platform is being used
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ifplatform
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifplatform.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifplatform.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifplatform.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.3a-2
+ Revision: 752724
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.3a-1
+ Revision: 718702
- texlive-ifplatform
- texlive-ifplatform
- texlive-ifplatform
- texlive-ifplatform

