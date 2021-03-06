#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	XML
%define		pnam	Filter-Namespace
Summary:	XML::Filter::Namespace - strip all but a single namespace
Summary(pl.UTF-8):	XML::Filter::Namespace - usunięcie wszystkich przestrzeni nazw oprócz jednej
Name:		perl-XML-Filter-Namespace
Version:	1.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	03ab0c24361eeb965243c8c262cbd7ea
URL:		http://search.cpan.org/dist/XML-Filter-Namespace/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-Accessor >= 0.17
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-XML-SAX
BuildRequires:	perl-XML-SAX-Writer >= 0.44
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The XML::Filter::Namespace Perl module strips out everything in an XML
document that does not belong in a specified namespace. This often
provides a view of the XML that is much clearer when multiple
namespaces are in use.

%description -l pl.UTF-8
Moduł Perla XML::Filter::Namespace usuwa z dokumentu XML wszystko to,
co nie należy do podanej przestrzeni nazw. Zwykle udostępnia to dużo
bardziej przejrzysty widok XML-a w przypadku, kiedy użyto wielu
przestrzeni nazw.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/XML/*/*.pm
%{_mandir}/man3/*
%{_mandir}/man1/*
