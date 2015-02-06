%define upstream_name    Term-Prompt
%define upstream_version 1.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Perl extension for prompting a user for information
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Term/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Term::ReadKey)
BuildArch:	noarch

%description
A Perl module for prompting a user for information.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
chmod 644 Changes README lib/Term/Prompt.pm
perl -pi -e 's/\r\n$/\n/;'  Changes README lib/Term/Prompt.pm

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Term
%{_mandir}/*/*


%changelog
* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.40.0-1mdv2010.0
+ Revision: 405540
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.04-3mdv2009.0
+ Revision: 241961
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Jul 05 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.04-1mdv2008.0
+ Revision: 48613
- update to new version 1.04


* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.03-5mdv2007.0
- Rebuild

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.03-4mdk
- Fix SPEC according to Perl Policy
    - BuildRequires
    - Source URL

* Mon Mar 06 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.03-3mdk
- spec cleanup
- fix directory ownership

* Thu Sep 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.03-2mdk
- Fix url/Source
- mkrel
- Fix BuildRequires

* Wed Nov 24 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.03-1mdk
- 1.03
- new (terse) description

* Thu Jun 03 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.01-1mdk
- 1.01
- fix perms

