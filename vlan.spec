Summary:	802.1q vlan Linux implementation
Summary(pl):	Implementacja vlan'�w 802.1q dla Linux'a
Name:		vlan
Version:	1.0.1
Release:	2
License:	GPL
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(pl):	Sieciowe/Narz�dzia
Source0:	http://scry.wanfear.com/~greear/vlan/%{name}.%{version}.tar.gz
Source1:	http://scry.wanfear.com/~greear/vlan/cisco_howto.html
BuildRequires:	gcc-c++
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is vlan implementation 802.1q for Linux. There is vconfig inside,
which allows you to manage vlans.

%description -l pl
Implementacja vlan'�w 802.1q dla Linux'a. Pakiet zawiera program
vconfig, kt�ry pozwala na zarz�dzanie vlan'ami.

%prep
%setup -q -n %{name}.%{version}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_sbindir}
install -d $RPM_BUILD_ROOT/%{_datadir}/doc/%{name}-%{version}

gzip -9nf README CHANGELOG 

install vconfig $RPM_BUILD_ROOT/%{_sbindir}/vconfig
install %{SOURCE1} $RPM_BUILD_ROOT/%{_datadir}/doc/%{name}-%{version}
install {vlan.html,vlan_test.pl,README.gz,CHANGELOG.gz}	$RPM_BUILD_ROOT/%{_datadir}/doc/%{name}-%{version}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/vconfig
%{_datadir}/doc/%{name}-%{version}/*