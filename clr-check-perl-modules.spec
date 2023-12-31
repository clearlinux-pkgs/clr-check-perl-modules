#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
#
Name     : clr-check-perl-modules
Version  : 10
Release  : 2
URL      : https://github.com/clearlinux/clr-check-perl-modules/archive/v10/clr-check-perl-modules-10.tar.gz
Source0  : https://github.com/clearlinux/clr-check-perl-modules/archive/v10/clr-check-perl-modules-10.tar.gz
Source1  : clr-check-perl-modules-motd.service
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: clr-check-perl-modules-bin = %{version}-%{release}
Requires: clr-check-perl-modules-license = %{version}-%{release}
Requires: clr-check-perl-modules-services = %{version}-%{release}
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# clr-check-perl-modules
This tool checks paths where Perl modules may have been installed, reporting
any that are left from a previous version. It reports separately those legacy
paths that are still supported by the current Perl configuration and those
legacy paths that *are not* supported.

%package bin
Summary: bin components for the clr-check-perl-modules package.
Group: Binaries
Requires: clr-check-perl-modules-license = %{version}-%{release}
Requires: clr-check-perl-modules-services = %{version}-%{release}

%description bin
bin components for the clr-check-perl-modules package.


%package license
Summary: license components for the clr-check-perl-modules package.
Group: Default

%description license
license components for the clr-check-perl-modules package.


%package services
Summary: services components for the clr-check-perl-modules package.
Group: Systemd services
Requires: systemd

%description services
services components for the clr-check-perl-modules package.


%prep
%setup -q -n clr-check-perl-modules-10
cd %{_builddir}/clr-check-perl-modules-10

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1691767124
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1691767124
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/clr-check-perl-modules
cp %{_builddir}/clr-check-perl-modules-%{version}/COPYING %{buildroot}/usr/share/package-licenses/clr-check-perl-modules/4cc77b90af91e615a64ae04893fdffa7939db84c || :
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/clr-check-perl-modules-motd.service

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/clr-check-perl-modules
/usr/bin/clr-check-perl-modules-motd

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/clr-check-perl-modules/4cc77b90af91e615a64ae04893fdffa7939db84c

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/clr-check-perl-modules-motd.service
