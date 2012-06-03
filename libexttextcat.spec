#
# Conditional build:
%bcond_without	tests		# do not perform "make check"
%bcond_without	static_libs	# static libraries
#
Summary:	Text categorization library
Summary(pl.UTF-8):	Biblioteka kategoryzacji tekstu
Name:		libexttextcat
Version:	3.3.1
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://dev-www.libreoffice.org/src/libexttextcat/%{name}-%{version}.tar.xz
# Source0-md5:	96de83da47db47c15784d9c21770819f
URL:		http://www.freedesktop.org/wiki/Software/libexttextcat
Provides:	libtextcat = %{version}-%{release}
Obsoletes:	libtextcat < 3.2.0-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libexttextcat is an N-Gram-Based Text Categorization library primarily
intended for language guessing.

%description -l pl.UTF-8
libexttextcat jest bazowaną na N-GRAM biblioteką kategoryzacji tekstu
przeznaczona głównie do odgadywania języka.

%package devel
Summary:	Development files for %{name}
Summary(pl.UTF-8):	Pliki nagłówkowe dla %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	libtextcat-devel = %{version}-%{release}
Obsoletes:	libtextcat-devel < 3.2.0-1

%description devel
This package contains the header files for developing applications
that use %{name}.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do tworzenia aplikacji opartych na
%{name}.

%package static
Summary:	Static libexttextcat library
Summary(pl.UTF-8):	Statyczna biblioteka libexttextcat
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libexttextcat library.

%description static -l pl.UTF-8
Statyczna biblioteka libexttextcat.

%package -n vala-libexttextcat
Summary:	libexttextcat API for Vala language
Summary(pl.UTF-8):	API libexttextcat dla języka Vala
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description -n vala-libexttextcat
libexttextcat API for Vala language.

%description -n vala-libexttextcat -l pl.UTF-8
API libexttextcat dla języka Vala.

%package tools
Summary:	Tool for creating custom document fingerprints
Summary(pl.UTF-8):	Narzędzia do tworzenia własnych odcisków dokumentów
Group:		Applications/Publishing
Requires:	%{name} = %{version}-%{release}

%description tools
This package contains the createfp program that allows you to easily
create your own document fingerprints.

%description tools -l pl.UTF-8
Ten pakiet zawiera program createfp pozwalający łatwo tworzyć odciski
(fingerprints) dokumentów.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static} \
	--disable-werror

%{__make}
%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p/sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README*
%attr(755,root,root) %{_libdir}/libexttextcat-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libexttextcat-1.0.so.0
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libexttextcat-1.0.so
%{_includedir}/%{name}
%{_pkgconfigdir}/%{name}.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libexttextcat-1.0.a
%endif

%files -n vala-libexttextcat
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/libexttextcat.vapi

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/createfp
