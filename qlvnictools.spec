Summary:	QLogic VNIC driver
Summary(pl.UTF-8):	Sterownik QLogic VNIC
Name:		qlvnictools
Version:	0.0.1
%define	snap	2
%define	gitref	ge27eef7
Release:	0.%{snap}.1
License:	BSD or GPL v2
Group:		Networking/Utilities
Source0:	http://www.openfabrics.org/downloads/qlvnictools/%{name}-%{version}-0.1.%{gitref}.tar.gz
# Source0-md5:	cb18ed6959f63c0fb68e400ac18c2891
URL:		http://www.openfabrics.org/
BuildRequires:	libibumad-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Measure socket and RDMA performance.

%description -l pl.UTF-8
Pomiar wydajności gniazd i RDMA.

%prep
%setup -q

cp -p qlgc_vnic_daemon/README README.qlgc_vnic_daemon

%build

cd ibvexdmtools
%configure
%{__make}
cd ..

cd qlgc_vnic_daemon
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C ibvexdmtools install \
	DESTDIR=$RPM_BUILD_ROOT 

%{__make} -C qlgc_vnic_daemon install \
	DESTDIR=$RPM_BUILD_ROOT 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README README.qlgc_vnic_daemon qlgc_vnic.cfg.sample
%attr(755,root,root) %{_sbindir}/ib_qlgc_vnic_query
%attr(755,root,root) %{_sbindir}/ib_qlgc_vnic_update
