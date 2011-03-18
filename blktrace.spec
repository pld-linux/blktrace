Summary:	Utilities for block layer I/O tracing
Summary(pl.UTF-8):	Narzędzia do śledzenia we/wy warstwy blokowej
Name:		blktrace
Version:	1.0.2
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://brick.kernel.dk/snaps/%{name}-%{version}.tar.bz2
# Source0-md5:	088e30d28d0be8e32d1d3a839bde6946
BuildRequires:	libaio-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
blktrace is a block layer I/O tracing mechanism which provides
detailed information about request queue operations up to user space.
This is valuable for diagnosing and fixing performance or application
problems relating to block layer I/O.

%description -l pl.UTF-8
blktrace to mechanizm do śledzenia we/wy warstwy blokowej,
zapewniający szczegółowe informacje o operacjach kolejki żądań dla
przestrzeni użytkownika. Jest to bardzo przydatne przy diagnostyce i
naprawianiu problemów z wydajnością lub aplikacjami związanych z we/wy
warstwy blokowej.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix} \
	mandir=%{_mandir}

mv $RPM_BUILD_ROOT%{_bindir}/{bno_plot.py,bno_plot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/blkiomon
%attr(755,root,root) %{_bindir}/blkparse
%attr(755,root,root) %{_bindir}/blkrawverify
%attr(755,root,root) %{_bindir}/blktrace
%attr(755,root,root) %{_bindir}/bno_plot
%attr(755,root,root) %{_bindir}/btrace
%attr(755,root,root) %{_bindir}/btrecord
%attr(755,root,root) %{_bindir}/btreplay
%attr(755,root,root) %{_bindir}/btt
%attr(755,root,root) %{_bindir}/verify_blkparse
%{_mandir}/man1/blkparse.1*
%{_mandir}/man1/blkrawverify.1*
%{_mandir}/man1/bno_plot.1*
%{_mandir}/man1/btt.1*
%{_mandir}/man1/verify_blkparse.1*
%{_mandir}/man8/blkiomon.8*
%{_mandir}/man8/blktrace.8*
%{_mandir}/man8/btrace.8*
%{_mandir}/man8/btrecord.8*
%{_mandir}/man8/btreplay.8*
