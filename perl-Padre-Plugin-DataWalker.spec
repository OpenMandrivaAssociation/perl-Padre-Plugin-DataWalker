%define upstream_name    Padre-Plugin-DataWalker
%define upstream_version 0.01

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Simple Perl data structure browser Padre
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Padre/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Padre)
BuildRequires: perl(Wx::Perl::DataWalker)
BuildRequires: perl(YAML::XS)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
This plugin uses the the Wx::Perl::DataWalker manpage module to provide
facilities for interactively browsing Perl data structures.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/man3/*
%perl_vendorlib/*


