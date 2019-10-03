#
# Conditional build:
%bcond_without	apidocs	# Doxygen documentation

Summary:	Maemo Internet Connectivity library
Summary(pl.UTF-8):	Biblioteka łączności z Internetem dla Maemo
Name:		libconic
Version:	0.24.1
Release:	1
License:	LGPL v2.1
Group:		Libraries
#Source0Download: https://github.com/maemo-leste/libconic/releases
Source0:	https://github.com/maemo-leste/libconic/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	fc387d4fb49631c5298bd734cc6b7231
Patch0:		%{name}-version.patch
Patch1:		%{name}-format.patch
Patch2:		%{name}-noWerror.patch
URL:		http://maemo.org/
BuildRequires:	GConf2-devel >= 2.0
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.60
%{?with_apidocs:BuildRequires:	doxygen}
BuildRequires:	glib2-devel >= 1:2.0
BuildRequires:	libtool
BuildRequires:	icd2-osso-ic-devel >= 1.0.1
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Internet Connectivity library for Maemo platform.

%description -l pl.UTF-8
Biblioteka łączności z Internetem dla platformy Maemo.

%package devel
Summary:	Header files for libconic
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libconic
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	GConf2-devel >= 2.0
Requires:	dbus-glib-devel >= 0.60
Requires:	glib2-devel >= 1:2.0

%description devel
Header files for libconic.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libconic.

%package static
Summary:	Static libconic library
Summary(pl.UTF-8):	Statyczna biblioteka libconic
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static liboss library.

%description static -l pl.UTF-8
Statyczna biblioteka libconic.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%{__sed} -i -e 's/@VERSION@/%{version}/' configure.ac

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-docs%{!?with_apidocs:=no}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_bindir}/test-*
# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libconic.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libconic.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libconic.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libconic.so
%dir %{_includedir}/conic
%{_includedir}/conic/conic.h
%{_includedir}/conic/conicconnection.h
%{_includedir}/conic/conicconnectionevent.h
%{_includedir}/conic/conicevent.h
%{_includedir}/conic/coniciap.h
%{_includedir}/conic/conicstatisticsevent.h
%{_pkgconfigdir}/conic.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libconic.a
