#
# Conditional build:
%bcond_without	dist_kernel	# (don't add kernel related dependencies)
#
Summary:	802.1q vlan Linux implementation
Summary(pl):	Implementacja vlanów 802.1q dla Linuksa
Name:		vlan
Version:	1.8
Release:	2
License:	GPL
Group:		Networking/Utilities
Source0:	http://www.candelatech.com/~greear/vlan/%{name}.%{version}.tar.gz
# Source0-md5:	1edd81324b4ffc0702c9ff289a342d91
Source1:	http://www.candelatech.com/~greear/vlan/cisco_howto.html
# Source1-md5:	cf0422b58d1a83d088a65b0fb052ec8a
URL:		http://www.candelatech.com/~greear/vlan.html
%{?with_dist_kernel:Conflicts:	kernel < 2.4}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
This is vlan implementation 802.1q for Linux. There is vconfig inside,
which allows you to manage vlans.

%description -l pl
Implementacja vlanów 802.1q dla Linuksa. Pakiet zawiera program
vconfig, który pozwala na zarz±dzanie vlanami.

%prep
%setup -q -n %{name}

install %{SOURCE1} .

%build
%{__make} clean
%{__make} CC="%{__cc}" CCFLAGS="%{rpmcflags}" LDFLAGS="%{rpmldflags}" CCC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install vconfig $RPM_BUILD_ROOT%{_sbindir}/vconfig
install *.8	$RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGELOG vlan.html cisco_howto.html vlan_test.pl
%attr(755,root,root) %{_sbindir}/vconfig
%{_mandir}/man?/*
