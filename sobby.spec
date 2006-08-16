Summary:	Sobby network editor server
Summary(pl):	Sobby - serwer edytora sieciowego
Name:		sobby
Version:	0.3.0
Release:	1
License:	BSD
Group:		Applications/Editors
Source0:	http://releases.0x539.de/sobby/%{name}-%{version}.tar.gz
# Source0-md5:	5408fc08d610be5aac4476c6ea6277f9
Source1:	%{name}.init
URL:		http://sobby.0x539.de/
BuildRequires:	obby-devel >= 0.3.0
BuildRequires:	slang-devel
Requires(post,preun):	/sbin/chkconfig
Requires:	rc-scripts
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sobby network editor server.

%description -l pl
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

%post
/sbin/chkconfig --add sobby
%service sobby restart

%preun
if [ "$1" = "0" ]; then
	%service sobby stop
	/sbin/chkconfig --del sobby
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(754,root,root) /etc/rc.d/init.d/%{name}
