Summary:	Sobby network editor server
Summary(pl.UTF-8):	Sobby - serwer edytora sieciowego
Name:		sobby
Version:	0.4.8
Release:	3
License:	GPL v2+
Group:		Applications/Editors
Source0:	http://releases.0x539.de/sobby/%{name}-%{version}.tar.gz
# Source0-md5:	1f7cf8c09cdeddbf2152843b28f73ce1
Source1:	%{name}.init
URL:		http://gobby.0x539.de/
BuildRequires:	avahi-glib-devel
BuildRequires:	glibmm-devel >= 2.6.0
BuildRequires:	libxml++2-devel >= 2.6
BuildRequires:	net6-devel >= 1.3.12
BuildRequires:	obby-devel >= 0.4.3
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	slang-devel
Requires(post,preun):	/sbin/chkconfig
Requires:	glibmm >= 2.6.0
Requires:	libxml++2 >= 2.6
Requires:	net6 >= 1.3.12
Requires:	obby >= 0.4.3
Requires:	rc-scripts
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sobby network editor server.

%description -l pl.UTF-8
Sobby - serwer edytora sieciowego.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add sobby
%service sobby restart

%preun
if [ "$1" = "0" ]; then
	%service sobby stop
	/sbin/chkconfig --del sobby
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/sobby
%attr(754,root,root) /etc/rc.d/init.d/sobby
%{_mandir}/man1/sobby.1*
