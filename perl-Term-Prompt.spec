%define module  Term-Prompt
%define name    perl-%{module}
%define version 1.04
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Perl extension for prompting a user for information
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Term/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
Buildrequires:  perl(Term::ReadKey)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
A Perl module for prompting a user for information.

%prep
%setup -q -n %{module}-%{version} 
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

