Summary:	utilities for block layer IO tracing
Name:		blktrace
Version:	1.0.0
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://brick.kernel.dk/snaps/%{name}-%{version}.tar.bz2
# Source0-md5:	e58f359f6c27efe7043be19abb8b95ba
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
blktrace is a block layer IO tracing mechanism which provides detailed
information about request queue operations up to user space. There are
three major components that are provided:

blktrace: A utility which transfers event traces from the kernel into
either long-term on-disk storage, or provides direct formatted output
(via blkparse).

blkparse: A utility which formats events stored in files, or when run
in live mode directly outputs data collected by blktrace.

%prep
%setup -q -n %{name}

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{makeinstall}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
