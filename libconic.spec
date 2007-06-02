#
Summary:	Maemo conic library
Name:		libconic
Version:	0.10
Release:	1
License:	LGPL
Group:		Development/Libraries
Source0:	http://repository.maemo.org/pool/bora/free/source/%{name}_%{version}.tar.gz
# Source0-md5:	51ddafe361d4cccdb7186f50f637afcc
Patch0:		%{name}-version.patch
Patch1:		%{name}-dbus.patch
Patch2:		%{name}-noWerror.patch
URL:		http://maemo.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	osso-ic-oss-devel
#BuildRequires:	python-devel
#BuildRequires:	xulrunner-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%package devel
Summary:	Header files for libconic
Group:		Development/Libraries

%description devel
Header files for libconic.

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
%{__glib_gettextize}
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
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root)    %{_libdir}/libconic.so.0.0.0

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/conic
%{_includedir}/conic/conic.h
%{_includedir}/conic/conicconnection.h
%{_includedir}/conic/conicconnectionevent.h
%{_includedir}/conic/conicevent.h
%{_includedir}/conic/coniciap.h
%{_includedir}/conic/conicstatisticsevent.h
%{_libdir}/libconic.la
%{_libdir}/libconic.so
%{_pkgconfigdir}/conic.pc


%files static
%defattr(644,root,root,755)
%{_libdir}/libconic.a
