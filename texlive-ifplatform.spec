%global tl_name ifplatform
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.4a
Release:	%{tl_revision}.1
Summary:	Conditionals to test which platform is being used
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ifplatform
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ifplatform.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ifplatform.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ifplatform.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package uses the (La)TeX extension -shell-escape to establish
whether the document is being processed on a Windows or on a Unix-like
system (Mac OS X, Linux, etc.), or on Cygwin (Unix environment over a
windows system). Booleans provided are: \ifwindows, \iflinux, \ifmacosx
and \ifcygwin. The package also preserves the output of uname on a Unix-
like system, which may be used to distinguish between various classes of
Unix systems.

