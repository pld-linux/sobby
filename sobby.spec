Summary:	Sobby network editor server
Summary(pl):	Sobby - serwer edytora sieciowego
Name:		sobby
Version:	0.2.0
Release:	1
License:	BSD
Group:		Applications/Editors
Source0:	http://releases.0x539.de/sobby/%{name}-%{version}.tar.gz
# Source0-md5:	68e740d9ad051e7939de29fa2c28da56
URL:		http://sobby.0x539.de/
BuildRequires:	obby-devel >= 0.2.0
BuildRequires:	slang-devel
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
