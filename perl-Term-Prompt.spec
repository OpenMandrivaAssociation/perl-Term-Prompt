%define upstream_name    Term-Prompt
%define upstream_version 1.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Perl extension for prompting a user for information
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Term/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
Buildrequires:  perl(Term::ReadKey)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
A Perl module for prompting a user for information.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
chmod 644 Changes README lib/Term/Prompt.pm
perl -pi -e 's/\r\n$/\n/;'  Changes README lib/Term/Prompt.pm

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot} 
%makeinstall_std

%clean 
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Term
%{_mandir}/*/*
