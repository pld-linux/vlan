Summary:	802.1q vlan Linux implementation
Summary(pl):	Implementacja vlan'ów 802.1q dla Linux'a
Name:		vlan
Version:	1.0.1
Release:	1
License:	GPL (?)
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(pl):	Sieciowe/Narzêdzia
Source0:	http://scry.wanfear.com/~greear/vlan/%{name}.%{version}.tar.gz
BuildRequires:	gcc-c++
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is vlan implementation 802.1q for Linux. There is vconfig inside,
which allows you to manage vlans.

%description -l pl
Implementacja vlan'ów 802.1q dla Linux'a. Pakiet zawiera program
vconfig, który pozwala na zarz±dzanie vlan'ami.

%prep
%setup -q -n %{name}.%{version}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_sbindir}

install vconfig $RPM_BUILD_ROOT/%{_sbindir}/vconfig

gzip -9nf README CHANGELOG 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz vlan.html vlan_test.pl
%attr(755,root,root) %{_sbindir}/vconfig
