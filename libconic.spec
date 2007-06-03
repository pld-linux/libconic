Summary:	Maemo Internet Connectivity library
Summary(pl.UTF-8):	Biblioteka łączności z Internetem dla Maemo
Name:		libconic
Version:	0.13
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://repository.maemo.org/pool/bora/free/source/%{name}_%{version}.tar.gz
# Source0-md5:	f852e61c2700b5bc571a730c6516e4ce
Patch0:		%{name}-version.patch
Patch1:		%{name}-dbus.patch
Patch2:		%{name}-noWerror.patch
URL:		http://maemo.org/
BuildRequires:	GConf2-devel >= 2.0
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.60
BuildRequires:	glib2-devel >= 1:2.0
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	osso-ic-oss-devel >= 1.0.1
BuildRequires:	pkgconfig
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

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libconic.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libconic.so
%{_libdir}/libconic.la
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
