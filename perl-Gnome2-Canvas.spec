#
# Conditional build:
%bcond_with tests	# perform "make test" (requires X server)
#
%include	/usr/lib/rpm/macros.perl
%define	pnam	Gnome2-Canvas
Summary:	Perl interface to the Gnome Canvas
Summary(pl):	Interfejs perlowy do Gnome Canvas
Name:		perl-%{pnam}
Version:	0.32
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://dl.sourceforge.net/gtk2-perl/%{pnam}-%{version}.tar.gz
# Source0-md5:	077fa5d2a2e348a02ed6b191b79666c2
URL:		http://gtk2-perl.sf.net/
BuildRequires:	gtk+2-devel
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	perl-Glib >= 0.95
BuildRequires:	perl-Gtk2 >= 0.95
BuildRequires:	perl-Gnome2 >= 0.30
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Gnome2-common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Gnome2 Perl module allows a perl developer to use the GnomeCanvas
widget.

%description -l pl
Modu³ Perla Gnome2 umo¿liwia programistom perlowym korzystanie z
kontrolki GnomeCanvas.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS TODO README
%{perl_vendorarch}/Gnome2/Canvas.pm
%dir %{perl_vendorarch}/auto/Gnome2/Canvas
%attr(755,root,root) %{perl_vendorarch}/auto/Gnome2/Canvas/*.so
%{perl_vendorarch}/auto/Gnome2/Canvas/*.bs
%{_mandir}/man3/*
