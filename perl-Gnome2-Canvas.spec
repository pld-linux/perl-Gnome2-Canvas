#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires X server)
#
%include	/usr/lib/rpm/macros.perl
%define		pnam	Gnome2-Canvas
Summary:	Perl interface to the GNOME Canvas
Summary(pl.UTF-8):	Interfejs perlowy do GNOME Canvas
Name:		perl-Gnome2-Canvas
Version:	1.002
Release:	9
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://dl.sourceforge.net/gtk2-perl/%{pnam}-%{version}.tar.gz
# Source0-md5:	93405a987ba4bbd03c2f91592b88f5cb
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	gtk+2-devel
BuildRequires:	libgnomecanvas-devel >= 2.14.0
BuildRequires:	perl-ExtUtils-Depends >= 0.200
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.03
BuildRequires:	perl-Glib >= 1.120
BuildRequires:	perl-Gtk2 >= 1.121
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	libgnomecanvas >= 2.14.0
Requires:	perl-Glib >= 1.120
Requires:	perl-Gtk2 >= 1.121
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Gnome2 Perl module allows a perl developer to use the GnomeCanvas
widget.

%description -l pl.UTF-8
Moduł Perla Gnome2 umożliwia programistom perlowym korzystanie z
kontrolki GnomeCanvas.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
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
%dir %{perl_vendorarch}/Gnome2/Canvas
%dir %{perl_vendorarch}/Gnome2/Canvas/Install
%attr(755,root,root) %{perl_vendorarch}/auto/Gnome2/Canvas/*.so
%{perl_vendorarch}/auto/Gnome2/Canvas/*.bs
%{perl_vendorarch}/Gnome2/Canvas/Install/*
%{_mandir}/man3/*
