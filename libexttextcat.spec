%bcond_without	tests
Summary:	Text categorization library
Name:		libexttextcat
Version:	3.2.0
Release:	1
License:	BSD
Group:		Libraries
URL:		http://www.freedesktop.org/wiki/Software/libexttextcat
Source0:	http://dev-www.libreoffice.org/src/libexttextcat/%{name}-%{version}.tar.xz
# Source0-md5:	941ec532832ffea01e121373a2733a96
Provides:	libtextcat = %{version}
Obsoletes:	libtextcat < 3.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{name} is an N-Gram-Based Text Categorization library primarily
intended for language guessing.

%package devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig
Provides:	libtextcat-devel = %{version}
Obsoletes:	libtextcat-devel < 3.2.0

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package tools
Summary:	Tool for creating custom document fingerprints
Group:		Applications/Publishing
Requires:	%{name} = %{version}-%{release}

%description tools
The %{name}-tools package contains the createfp program that allows
you to easily create your own document fingerprints.

%prep
%setup -q

%build
%configure \
	--disable-static \
	--disable-werror \

%{__make}
%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README*
%attr(755,root,root) %{_libdir}/%{name}.so.*
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}.so
%{_pkgconfigdir}/%{name}.pc


%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/createfp
