Summary:	802.1q vlan Linux implementation
Summary(pl):	Implementacja vlan'ów 802.1q dla Linux'a
Name:		vlan
Version:	1.4
Release:	1
License:	GPL
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(pl):	Sieciowe/Narzêdzia
Source0:	http://scry.wanfear.com/~greear/vlan/%{name}.%{version}.tar.gz
Source1:	http://scry.wanfear.com/~greear/vlan/cisco_howto.html
URL:		http://scry.wanfear.com/~greear/vlan.html
BuildRequires:	gcc-c++
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
This is vlan implementation 802.1q for Linux. There is vconfig inside,
which allows you to manage vlans. 

%description -l pl
Implementacja vlan'ów 802.1q dla Linux'a. Pakiet zawiera program
vconfig, który pozwala na zarz±dzanie vlan'ami.

%prep
%setup -q -n %{name}

%{__install} %{SOURCE1} .

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_sbindir}

gzip -9nf README CHANGELOG 

install vconfig $RPM_BUILD_ROOT/%{_sbindir}/vconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz *.html vlan_test.pl
%attr(755,root,root) %{_sbindir}/vconfig
