#
# Conditional build:
%bcond_with tests	# perform "make test" (requires X server)
#
%include	/usr/lib/rpm/macros.perl
%define	pnam	Gnome2-Canvas
Summary:	Perl interface to the Gnome Canvas
Summary(pl):	Interfejs perlowy do Gnome Canvas
Name:		perl-%{pnam}
Version:	0.34
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://dl.sourceforge.net/gtk2-perl/%{pnam}-%{version}.tar.gz
# Source0-md5:	d63942ddc8a221c64190d014998da7a3
URL:		http://gtk2-perl.sf.net/
BuildRequires:	gtk+2-devel
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	perl-Glib >= 1.012
BuildRequires:	perl-Gtk2 >= 1.012
BuildRequires:	perl-Gnome2 >= 0.30
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov >= 4.1-13
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

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/Gnome2/Canvas/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS TODO README
%{perl_vendorarch}/Gnome2/Canvas.pm
%dir %{perl_vendorarch}/auto/Gnome2/Canvas
%dir %{perl_vendorarch}/Gnome2/Canvas/Install
%attr(755,root,root) %{perl_vendorarch}/auto/Gnome2/Canvas/*.so
%{perl_vendorarch}/auto/Gnome2/Canvas/*.bs
%{perl_vendorarch}/Gnome2/Canvas/Install/*
%{_mandir}/man3/*
