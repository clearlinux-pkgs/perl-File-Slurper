#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-File-Slurper
Version  : 0.012
Release  : 1
URL      : https://cpan.metacpan.org/authors/id/L/LE/LEONT/File-Slurper-0.012.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/L/LE/LEONT/File-Slurper-0.012.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libf/libfile-slurper-perl/libfile-slurper-perl_0.012-1.debian.tar.xz
Summary  : 'A simple, sane and efficient module to slurp a file'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-File-Slurper-license
Requires: perl-File-Slurper-man
BuildRequires : perl(Test::Warnings)

%description
This archive contains the distribution File-Slurper,
version 0.012:
A simple, sane and efficient module to slurp a file

%package license
Summary: license components for the perl-File-Slurper package.
Group: Default

%description license
license components for the perl-File-Slurper package.


%package man
Summary: man components for the perl-File-Slurper package.
Group: Default

%description man
man components for the perl-File-Slurper package.


%prep
tar -xf %{SOURCE1}
cd ..
%setup -q -n File-Slurper-0.012
mkdir -p %{_topdir}/BUILD/File-Slurper-0.012/deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/File-Slurper-0.012/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/perl-File-Slurper
cp LICENSE %{buildroot}/usr/share/doc/perl-File-Slurper/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/File/Slurper.pm

%files license
%defattr(-,root,root,-)
/usr/share/doc/perl-File-Slurper/LICENSE

%files man
%defattr(-,root,root,-)
/usr/share/man/man3/File::Slurper.3
