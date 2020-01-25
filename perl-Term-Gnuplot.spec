#
# Conditional build:
%bcond_with	svga	# build with svgalib output support
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Term
%define		pnam	Gnuplot
Summary:	Term::Gnuplot - lowlevel graphics using gnuplot drawing routines
Summary(pl.UTF-8):	Term::Gnuplot - niskopoziomowa grafika przy użyciu funkcji rysujących gnuplota
Name:		perl-Term-Gnuplot
Version:	0.90380905
Release:	16
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ceccd4e30deb6291ebecce176e715208
Patch0:		%{name}-vga.patch
Patch1:		format-security.patch
URL:		http://search.cpan.org/dist/Term-Gnuplot/
BuildRequires:	gd-devel
BuildRequires:	perl-devel >= 1:5.8.0
%{?with_svga:BuildRequires:	svgalib-devel}
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is intended for low-resolution or high-resolution graphics
using gnuplot low-level functions.

%description -l pl.UTF-8
Ten moduł jest przeznaczony do tworzenia grafiki niskiej lub wysokiej
rozdzielczości przy użyciu niskopoziomowych funkcji gnuplota.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__perl} Makefile.PL \
	TRY_LIBS="-lX11 -lm -lgd -lpng -lz %{?with_svga:-lvga}" \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test </dev/null}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorarch}/Term/Gnuplot.pm
%dir %{perl_vendorarch}/auto/Term/Gnuplot
%attr(755,root,root) %{perl_vendorarch}/auto/Term/Gnuplot/Gnuplot.so
%{_mandir}/man3/Term::Gnuplot*
