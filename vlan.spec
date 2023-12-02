#
# Conditional build:
%bcond_without	dist_kernel	# (don't add kernel related dependencies)
#
Summary:	802.1q vlan Linux implementation
Summary(pl.UTF-8):	Implementacja vlanów 802.1q dla Linuksa
Name:		vlan
Version:	1.9
Release:	1
License:	GPL
Group:		Networking/Admin
Source0:	http://www.candelatech.com/~greear/vlan/%{name}.%{version}.tar.gz
# Source0-md5:	5f0c6060b33956fb16e11a15467dd394
Source1:	http://www.candelatech.com/~greear/vlan/cisco_howto.html
# Source1-md5:	cf0422b58d1a83d088a65b0fb052ec8a
URL:		http://www.candelatech.com/~greear/vlan.html
Patch0:		%{name}-format-security.patch
%{?with_dist_kernel:Conflicts:	kernel < 2.4}
Obsoletes:	vconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_debugsource_packages	0

%define		_sbindir	/sbin

%description
This is vlan implementation 802.1q for Linux. There is vconfig inside,
which allows you to manage vlans.

%description -l pl.UTF-8
Implementacja vlanów 802.1q dla Linuksa. Pakiet zawiera program
vconfig, który pozwala na zarządzanie vlanami.

%prep
%setup -q -n %{name}
%patch0 -p1

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
