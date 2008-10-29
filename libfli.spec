%define svn   190

Name:          libfli
Summary:       Finger Lakes Instrument Library
Version:       1.7
Release:       %mkrel 0.%svn.2
Url:           http://indi.sourceforge.net/index.php/Main_Page
License:       GPLv2+
Group:         Development/KDE and Qt
BuildRoot:     %{_tmppath}/%{name}-%{version}-build
Source0:       %{name}-%{version}.%svn.tar.bz2
Patch0:        libfli-1.7.190-fix-link.patch
Patch1:        libfli-1.7.190-fix-lib.patch
BuildRequires: kde4-macros

%description
Finger Lakes Instrument Library

#---------------------------------------------

%define fli_major 1
%define libfli %mklibname fli %{fli_major}

%package -n %libfli
Summary: KDE 4 library
Group: System/Libraries

%description -n %libfli
%name library

%files -n %libfli
%defattr(-,root,root)
%_kde_libdir/libfli.so.%{fli_major}*

#-----------------------------------------------------------------------------

%package devel
Summary: Devel stuff for %{name}
Group: Development/KDE and Qt
Requires: %libfli = %version

%description  devel
Files needed to build applications based on %{name}.

%files devel
%defattr(-,root,root)
%_kde_includedir/libfli.h
%_kde_libdir/libfli.so

#---------------------------------------------

%prep
%setup -q  -n %name
%patch0 -p0
%patch1 -p0

%build
%cmake_kde4
%make

%install
cd build
make DESTDIR=%buildroot install

%clean
rm -rf "%{buildroot}"
