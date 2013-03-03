Summary:	XTS - X Test Suite
Summary(pl.UTF-8):	XTS - zestaw testów X
Name:		xorg-xts
Version:	0.99.1
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/test/xts-%{version}.tar.bz2
# Source0-md5:	918423bc9e03f5db192f9bb0c11dcc84
URL:		http://xorg.freedesktop.org/
BuildRequires:	asciidoc
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	perl-base
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	sed >= 4.0
BuildRequires:	xmlto
BuildRequires:	xorg-app-xdpyinfo
BuildRequires:	xorg-app-xset
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXau-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xorg-lib-xtrans-devel
BuildRequires:	xorg-util-util-macros >= 1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a revamped version of X Test Suite (XTS) which removes some of
the ugliness of building and running the tests.

%description -l pl.UTF-8
Ten pakiet zawiera przekształconą wersję XTS (X Test Suite, czyli
zestawu testów X), usuwającą część brzydoty z procesu budowania i
uruchamiania testów.

%prep
%setup -q -n xts-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# conflict with tcc package
%{__mv} $RPM_BUILD_ROOT%{_bindir}/{tcc,xts-tcc}
%{__sed} -i -e 's,/tcc,/xts-tcc,' $RPM_BUILD_ROOT%{_bindir}/xts-run

# useless
%{__rm} $RPM_BUILD_ROOT%{_libdir}/xts5/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/xts-blowup
%attr(755,root,root) %{_bindir}/xts-config
%attr(755,root,root) %{_bindir}/xts-report
%attr(755,root,root) %{_bindir}/xts-run
%attr(755,root,root) %{_bindir}/xts-tcc
%dir %{_libdir}/xts5
%attr(755,root,root) %{_libdir}/xts5/libapi_s.so
%attr(755,root,root) %{_libdir}/xts5/libxts5.so
%attr(755,root,root) %{_libdir}/xts5/libxts5proto.so
%attr(755,root,root) %{_libdir}/xts5/SHAPE
%attr(755,root,root) %{_libdir}/xts5/XI
%attr(755,root,root) %{_libdir}/xts5/XIproto
%attr(755,root,root) %{_libdir}/xts5/Xlib3
%attr(755,root,root) %{_libdir}/xts5/Xlib4
%attr(755,root,root) %{_libdir}/xts5/Xlib5
%attr(755,root,root) %{_libdir}/xts5/Xlib6
%attr(755,root,root) %{_libdir}/xts5/Xlib7
%attr(755,root,root) %{_libdir}/xts5/Xlib8
%attr(755,root,root) %{_libdir}/xts5/Xlib9
%attr(755,root,root) %{_libdir}/xts5/Xlib10
%attr(755,root,root) %{_libdir}/xts5/Xlib11
%attr(755,root,root) %{_libdir}/xts5/Xlib12
%attr(755,root,root) %{_libdir}/xts5/Xlib13
%attr(755,root,root) %{_libdir}/xts5/Xlib14
%attr(755,root,root) %{_libdir}/xts5/Xlib15
%attr(755,root,root) %{_libdir}/xts5/Xlib16
%attr(755,root,root) %{_libdir}/xts5/Xlib17
%attr(755,root,root) %{_libdir}/xts5/Xopen
%attr(755,root,root) %{_libdir}/xts5/Xproto
%attr(755,root,root) %{_libdir}/xts5/Xt3
%attr(755,root,root) %{_libdir}/xts5/Xt4
%attr(755,root,root) %{_libdir}/xts5/Xt5
%attr(755,root,root) %{_libdir}/xts5/Xt6
%attr(755,root,root) %{_libdir}/xts5/Xt7
%attr(755,root,root) %{_libdir}/xts5/Xt8
%attr(755,root,root) %{_libdir}/xts5/Xt9
%attr(755,root,root) %{_libdir}/xts5/Xt10
%attr(755,root,root) %{_libdir}/xts5/Xt11
%attr(755,root,root) %{_libdir}/xts5/Xt12
%attr(755,root,root) %{_libdir}/xts5/Xt13
%attr(755,root,root) %{_libdir}/xts5/Xt14
%attr(755,root,root) %{_libdir}/xts5/Xt15
%attr(755,root,root) %{_libdir}/xts5/XtC
%attr(755,root,root) %{_libdir}/xts5/XtE
%{_datadir}/xts5
%{_mandir}/man7/XTS.7*
