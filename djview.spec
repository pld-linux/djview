Summary:	DjVu Viewer
Summary(pl):	Przegl±darka plików DjVu
Name:		djview
Version:	3.2.5.3
Release:	1
Group:		X11/Applications/Graphics
Group(de):	X11/Applikationen/Grafik
Group(pl):	X11/Aplikacje/Grafika
License:	non-distributable, no source
Source0:	djvu_lin.tar.gz
NoSource:	0
URL:		http://www.djvu.att.com/
ExclusiveArch:	%{ix86}
Requires:	XFree86-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
DjVu Viewer.

%description -l pl
Przegl±dardka plików DjVu.

%package netscape
Summary:	DjVu plugin for Netscape 4.x
Summary(pl):	Wtyczka DjVu do Netscape 4.x
Group:		X11/Applications/Graphics
Group(de):	X11/Applikationen/Grafik
Group(pl):	X11/Aplikacje/Grafika
Requires:	%{name} = %{version}
Requires:	netscape-common >= 4.0

%description netscape
DjVu plugin for Netscape 4.x.

%description netscape -l pl
Wtyczka DjVu do Netscape 4.x.

%prep
%setup -q -n npdjvu-%{version}

%build
./install --extract

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/netscape/plugins}

install TRUE/djview $RPM_BUILD_ROOT%{_bindir}
install TRUE/nsdejavu_libc6.so $RPM_BUILD_ROOT%{_libdir}/netscape/plugins

gzip -9nf README.txt TRUE/license.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz TRUE/{*.gz,*.html,*.jpg,*.djvu}
%attr(755,root,root) %{_bindir}/*

%files netscape
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/netscape/plugins/*.so
