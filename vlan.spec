# --without	dist_kernel	(don't add kernel related dependencies)

Summary:	802.1q vlan Linux implementation
Summary(pl.UTF-8):   Implementacja vlanów 802.1q dla Linuksa
Name:		vlan
Version:	1.6
Release:	2
License:	GPL
Group:		Networking/Utilities
Source0:	http://www.candelatech.com/~greear/vlan/%{name}.%{version}.tar.gz
Source1:	http://www.candelatech.com/~greear/vlan/cisco_howto.html
URL:		http://www.candelatech.com/~greear/vlan.html
%{!?_without_dist_kernel:Conflicts:	kernel < 2.4}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
This is vlan implementation 802.1q for Linux. There is vconfig inside,
which allows you to manage vlans.

%description -l pl.UTF-8
Implementacja vlanów 802.1q dla Linuksa. Pakiet zawiera program
vconfig, który pozwala na zarządzanie vlanami.

%prep
%setup -q -n %{name}

install %{SOURCE1} .

%build
%{__make} CC="%{__cc}" CCFLAGS="%{rpmcflags}" LDFLAGS="%{rpmldflags}" CCC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{%{_sbindir},%{_mandir}/man8}

gzip -9nf README CHANGELOG

install vconfig $RPM_BUILD_ROOT%{_sbindir}/vconfig
install *.8     $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz *.html vlan_test.pl
%attr(755,root,root) %{_sbindir}/vconfig
%{_mandir}/man?/*
