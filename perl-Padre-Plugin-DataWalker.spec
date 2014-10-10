%define upstream_name    Padre-Plugin-DataWalker
%define upstream_version 0.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Simple Perl data structure browser Padre
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Padre/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Module::Install)
BuildRequires:	perl(Padre)
BuildRequires:	perl(Wx::Perl::DataWalker)
BuildRequires:	perl(YAML::XS)
BuildArch:	noarch

%description
This plugin uses the the Wx::Perl::DataWalker manpage module to provide
facilities for interactively browsing Perl data structures.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.40.0-2mdv2011.0
+ Revision: 656950
- rebuild for updated spec-helper

* Sun Dec 19 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.40.0-1mdv2011.0
+ Revision: 622952
- new version

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.1 packages

* Wed Jan 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2010.1
+ Revision: 490488
- update to 0.02

* Sat May 30 2009 Jérôme Quelin <jquelin@mandriva.org> 0.10.0-1mdv2010.0
+ Revision: 381423
- fixing buildrequires:
- adding missing buildrequires:
- import perl-Padre-Plugin-DataWalker


* Sat May 30 2009 cpan2dist 0.01-1mdv
- initial mdv release, generated with cpan2dist

