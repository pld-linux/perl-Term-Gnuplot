#
# Conditional build:
%bcond_with	svga	# build with svgalib output support
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Term
%define	pnam	Gnuplot
Summary:	Term::Gnuplot - lowlevel graphics using gnuplot drawing routines
Summary(pl):	Term::Gnuplot - niskopoziomowa grafika przy u¿yciu funkcji rysuj±cych gnuplota
Name:		perl-Term-Gnuplot
Version:	0.5704
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ed096195e39e1a8ee3dd1fe36f1f6906
Patch0:		%{name}-vga.patch
BuildRequires:	XFree86-devel
BuildRequires:	gd-devel
BuildRequires:	perl-devel >= 5.8.0
%{?with_svga:BuildRequires:	svgalib-devel}
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is intended for low-resolution or high-resolution graphics
using gnuplot low-level functions.

%description -l pl
Ten modu³ jest przenaczony do tworzenia grafiki niskiej lub wysokiej
rozdzielczo¶ci przy u¿yciu niskopoziomowych funkcji gnuplota.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

%build
%{__perl} Makefile.PL \
	TRY_LIBS="-L/usr/X11R6/lib -lX11 -lm -lgd -lpng -lz %{?with_svga:-lvga}" \
	INSTALLDIRS=vendor

%{__make} \
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
%{perl_vendorarch}/auto/Term/Gnuplot/Gnuplot.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Term/Gnuplot/Gnuplot.so
%{_mandir}/man3/Term::Gnuplot*
