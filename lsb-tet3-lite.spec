# LSB Compliant packages require the following in ~/.rpmmacros
#%_binary_payload	w9.gzdio

# LSB release version
%define LSBRelease 3

Summary: Test Environment Toolkit
Name: lsb-tet3-lite
Vendor: The Open Group
URL: http://tetworks.opengroup.org/tet
Version: 3.6b
Release: 9.lsb%{LSBRelease}
Source0: tet3.6b-lite.unsup.src.tgz
Source1: tet3-lite-manpages-v1.1.tgz
Source2: support.tgz
Patch0: tet3.6b-lite-lsb.patch
License: Artistic
Group: Development/Tools
Buildroot: %{_builddir}/%{name}-root
AutoReqProv: no


# comment this out, since it often means that the
# package cannot be installed , the value 3.0 is for LSB 3.0
%ifarch i386 i486 i585 i686 athlon
PreReq: lsb-core-ia32 >= 3.0
%endif
%ifarch ia64
PreReq: lsb-core-ia64 >= 3.0
%endif
%ifarch ppc
PreReq: lsb-core-ppc32 >= 3.0
%endif
%ifarch ppc64
PreReq: lsb-core-ppc64 >= 3.0
%endif
%ifarch s390
PreReq: lsb-core-s390 >= 3.0
%endif
%ifarch s390x
PreReq: lsb-core-s390x >= 3.0
%endif
%ifarch x86_64
PreReq: lsb-core-amd64 >= 3.0
%endif

%description
This is an LSB conforming package of the Test Environment Toolkit.
This base package contains the tcc binary, shared objects for
the C API, and tcm modules for the ksh, posix_sh, perl and xpg3sh
APIs, and supporting documentation.
The Test Environment Toolkit is a standard framework for
developing and running test cases.
This version for LSB 3.0.

%prep

if [ ! -x /opt/lsb/bin/lsbcc ] ; then
    printf "lsbcc not found, required for compilation, aborting\n"
    exit 1
fi

if [ ! -x /opt/lsb/bin/lsbc++ ] ; then
    printf "lsbc++ not found, required for compilation, aborting\n"
    exit 1
fi

%setup -n tet3-lite-3.6b -q -a1
%patch -p1


%build

sh ./configure -t lite
cd src && make

%install

rm -rf $RPM_BUILD_ROOT
cd src && make  install
cd ..
mkdir -p $RPM_BUILD_ROOT/opt/lsb-tet3-lite
find inc lib bin man -print|grep -v .keep_me|cpio -pdv $RPM_BUILD_ROOT/opt/lsb-tet3-lite/
mkdir -p $RPM_BUILD_ROOT/opt/lsb-tet3-lite/doc
cp  README.FIRST Artistic Licence $RPM_BUILD_ROOT/opt/lsb-tet3-lite/doc/
install -m 555 contrib/scripts/vres $RPM_BUILD_ROOT/opt/lsb-tet3-lite/bin/vres
install -m 555 contrib/scripts/dres $RPM_BUILD_ROOT/opt/lsb-tet3-lite/bin/dres

sed -e "/^HOME=/d" -e "s@^echo Unconfigured@TET_ROOT=/opt/lsb-tet3-lite@" profile.skeleton > $RPM_BUILD_ROOT/opt/lsb-tet3-lite/profile 

tar zxvf $RPM_SOURCE_DIR/support.tgz
install -m 555 support/tjreport $RPM_BUILD_ROOT/opt/lsb-tet3-lite/bin/tjreport
cp support/tjreport.1 $RPM_BUILD_ROOT/opt/lsb-tet3-lite/man/man1/
 
chmod 755 $RPM_BUILD_ROOT/opt/lsb-tet3-lite/man/man1 $RPM_BUILD_ROOT/opt/lsb-tet3-lite/man/man3 $RPM_BUILD_ROOT/opt/lsb-tet3-lite/man/man4
chmod 644 $RPM_BUILD_ROOT/opt/lsb-tet3-lite/man/man1/* $RPM_BUILD_ROOT/opt/lsb-tet3-lite/man/man3/* $RPM_BUILD_ROOT/opt/lsb-tet3-lite/man/man4/*


%files

%defattr(-,bin,bin)

/opt/lsb-tet3-lite/bin
#/opt/lsb-tet3-lite/inc
#/opt/lsb-tet3-lite/lib
/opt/lsb-tet3-lite/lib/ksh/tcm.ksh
/opt/lsb-tet3-lite/lib/ksh/tetapi.ksh
/opt/lsb-tet3-lite/lib/perl/api.pl
/opt/lsb-tet3-lite/lib/perl/tcm.pl
/opt/lsb-tet3-lite/lib/perl/README
/opt/lsb-tet3-lite/lib/posix_sh/tcm.sh
/opt/lsb-tet3-lite/lib/posix_sh/tetapi.sh
/opt/lsb-tet3-lite/lib/tet3/libapi_s.so
/opt/lsb-tet3-lite/lib/tet3/libthrapi_s.so
/opt/lsb-tet3-lite/lib/xpg3sh/tcm.sh
/opt/lsb-tet3-lite/lib/xpg3sh/tetapi.sh
/opt/lsb-tet3-lite/profile
%dir /opt/lsb-tet3-lite
%dir /opt/lsb-tet3-lite/man

%doc /opt/lsb-tet3-lite/doc
%doc /opt/lsb-tet3-lite/man/man1
%doc /opt/lsb-tet3-lite/man/man4

%package devel
Summary: Development option for the TET
Group: Development/Tools
Requires: lsb-tet3-lite


%description devel
This is an LSB conforming package of the TET development environment for
building tests from source.  The Test Environment Toolkit is a standard
framework for developing and running test cases.


%files devel

%defattr(-,bin,bin)

/opt/lsb-tet3-lite/inc
#/opt/lsb-tet3-lite/lib
/opt/lsb-tet3-lite/lib/tet3/libapi.a
/opt/lsb-tet3-lite/lib/tet3/libthrapi.a
/opt/lsb-tet3-lite/lib/tet3/tcm.o
/opt/lsb-tet3-lite/lib/tet3/tcmchild.o
/opt/lsb-tet3-lite/lib/tet3/tcm_m.o
/opt/lsb-tet3-lite/lib/tet3/tcmc_m.o
/opt/lsb-tet3-lite/lib/tet3/thrtcm.o
/opt/lsb-tet3-lite/lib/tet3/thrtcmchild.o
/opt/lsb-tet3-lite/lib/tet3/thrtcm_m.o
/opt/lsb-tet3-lite/lib/tet3/thrtcmc_m.o
/opt/lsb-tet3-lite/lib/tet3/libtcm_s.a
/opt/lsb-tet3-lite/lib/tet3/tcm_s.o
/opt/lsb-tet3-lite/lib/tet3/tcmchild_s.o
/opt/lsb-tet3-lite/lib/tet3/tcm_ms.o
/opt/lsb-tet3-lite/lib/tet3/tcmc_ms.o
/opt/lsb-tet3-lite/lib/tet3/libthrtcm_s.a
/opt/lsb-tet3-lite/lib/tet3/thrtcm_s.o
/opt/lsb-tet3-lite/lib/tet3/thrtcmchild_s.o
/opt/lsb-tet3-lite/lib/tet3/thrtcm_ms.o
/opt/lsb-tet3-lite/lib/tet3/thrtcmc_ms.o
/opt/lsb-tet3-lite/lib/tet3/Ctcm.o
/opt/lsb-tet3-lite/lib/tet3/Ctcmchild.o
/opt/lsb-tet3-lite/lib/tet3/Cthrtcm.o
/opt/lsb-tet3-lite/lib/tet3/Cthrtcmchild.o
/opt/lsb-tet3-lite/lib/tet3/Ctcm_s.o
/opt/lsb-tet3-lite/lib/tet3/Ctcmchild_s.o
/opt/lsb-tet3-lite/lib/tet3/Cthrtcm_s.o
/opt/lsb-tet3-lite/lib/tet3/Cthrtcmchild_s.o
%doc /opt/lsb-tet3-lite/man/man3


%post

# put out a message 

echo 
echo "To use the TET-lite package set your TET_ROOT, PATH and MANPATH environment"
echo "variables, for example:"
echo "   export TET_ROOT=/opt/lsb-tet3-lite"
echo "   export PATH=\$PATH:\$TET_ROOT/bin"
echo "   export MANPATH=\$MANPATH:\$TET_ROOT/man"
echo "See /opt/lsb-tet3-lite/profile for sample profile additions"
echo


%changelog

* Tue Jun 07 2005  Andrew Josey

Ensure devel tree does not overlap with base in lib/tet3/

* Mon Apr 18 2005  Andrew Josey

The runtime package should include tcm runtime parts of the lib tree


* Mon Apr 18 2005  Andrew Josey

Rebuild for LSB3.0

* Wed Mar  9 2005  Andrew Josey

Change payload to be gzip'd rather than bzip'd

* Thu Mar  3 2005  Andrew Josey

Add supplementary binaries

* Wed Mar  2 2005  Andrew Josey

Add a development package

* Tue Mar  1 2005  Andrew Josey

Initial spec file for an LSB tet package


