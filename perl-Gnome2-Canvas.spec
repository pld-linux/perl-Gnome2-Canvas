#
# Conditional build:
# _with_tests - perform "make test" (requires X server)
#
%include	/usr/lib/rpm/macros.perl
%define	pnam	Gnome2-Canvas
Summary:	Perl interface to the Gnome Canvas
Name:		perl-%{pnam}
Version:	0.28
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/M/ML/MLEHMANN/%{pnam}-%{version}.tar.gz
# Source0-md5:	5ea51c2d9302ca089a2debd035cac50c
BuildRequires:	gtk+2-devel
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	perl-ExtUtils-Depends
BuildRequires:	perl-Glib >= 0.95
BuildRequires:	perl-Gtk2 >= 0.95
BuildRequires:	perl-Gnome2 >= 0.30
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Gnome2 Perl module allows a perl developer to use the GnomeCanvas
widget.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?_with_tests:%{__make} test}

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
%attr(755,root,root) %{perl_vendorarch}/auto/Gnome2/Canvas/*.so
%{perl_vendorarch}/auto/Gnome2/Canvas/*.bs
%{_mandir}/man3/*
