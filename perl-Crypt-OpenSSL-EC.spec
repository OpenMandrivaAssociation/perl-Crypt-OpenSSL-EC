%define upstream_name    Crypt-OpenSSL-EC
%define upstream_version 1.01

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:    Perl extension for OpenSSL EC (Elliptic Curves) library
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Crypt/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Crypt::OpenSSL::Bignum)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl-devel
BuildRequires: pkgconfig(libssl)

%description
This module provides a standard (non-OO) interface to the OpenSSL EC
(Elliptic Curve) library. Some OO Calls are supported.

Most of the functions described in openssl/ec.h are supported.

It provides the Crypt::OpenSSL::EC class which defines some high level
functions and constants. At also provides 4 other classes for managing EC
objects:

%prep
%setup -qn %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes META.yml META.json
%{_mandir}/man3/*
%{perl_vendorlib}/*

