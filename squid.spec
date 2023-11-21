#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v2
# autospec commit: e661f3a625d7
#
# Source0 file verified with key 0xCD6DBF8EF3B17D3E (squid3@treenet.co.nz)
#
Name     : squid
Version  : 6.5
Release  : 25
URL      : https://squid.mirror.globo.tech/archive/6/squid-6.5.tar.xz
Source0  : https://squid.mirror.globo.tech/archive/6/squid-6.5.tar.xz
Source1  : squid.service
Source2  : squid.tmpfiles
Source3  : https://squid.mirror.globo.tech/archive/6/squid-6.5.tar.xz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 LGPL-2.1
Requires: squid-bin = %{version}-%{release}
Requires: squid-config = %{version}-%{release}
Requires: squid-data = %{version}-%{release}
Requires: squid-libexec = %{version}-%{release}
Requires: squid-license = %{version}-%{release}
Requires: squid-man = %{version}-%{release}
Requires: squid-services = %{version}-%{release}
BuildRequires : Linux-PAM-dev
BuildRequires : buildreq-configure
BuildRequires : cyrus-sasl-dev
BuildRequires : glib-dev
BuildRequires : krb5-dev
BuildRequires : openldap-dev
BuildRequires : pkgconfig(cppunit)
BuildRequires : pkgconfig(expat)
BuildRequires : pkgconfig(gnutls)
BuildRequires : pkgconfig(ldap)
BuildRequires : pkgconfig(libcap)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(mit-krb5)
BuildRequires : pkgconfig(mit-krb5-gssapi)
BuildRequires : pkgconfig(nettle)
BuildRequires : pkgconfig(openssl)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Add-template-squid.conf.patch

%description
SQUID Web Proxy Cache                        http://www.squid-cache.org/
------------------------------------------------------------------------

%package bin
Summary: bin components for the squid package.
Group: Binaries
Requires: squid-data = %{version}-%{release}
Requires: squid-libexec = %{version}-%{release}
Requires: squid-config = %{version}-%{release}
Requires: squid-license = %{version}-%{release}
Requires: squid-services = %{version}-%{release}

%description bin
bin components for the squid package.


%package config
Summary: config components for the squid package.
Group: Default

%description config
config components for the squid package.


%package data
Summary: data components for the squid package.
Group: Data

%description data
data components for the squid package.


%package doc
Summary: doc components for the squid package.
Group: Documentation
Requires: squid-man = %{version}-%{release}

%description doc
doc components for the squid package.


%package libexec
Summary: libexec components for the squid package.
Group: Default
Requires: squid-config = %{version}-%{release}
Requires: squid-license = %{version}-%{release}

%description libexec
libexec components for the squid package.


%package license
Summary: license components for the squid package.
Group: Default

%description license
license components for the squid package.


%package man
Summary: man components for the squid package.
Group: Default

%description man
man components for the squid package.


%package services
Summary: services components for the squid package.
Group: Systemd services
Requires: systemd

%description services
services components for the squid package.


%prep
%setup -q -n squid-6.5
cd %{_builddir}/squid-6.5
%patch -P 1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1700526381
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%configure --disable-static --disable-arch-native \
--datadir=/usr/share/squid \
--sysconfdir=/etc/squid \
--with-logdir=/var/log/squid \
--enable-linux-netfilter \
--with-default-user=squid
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1700526381
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/squid
cp %{_builddir}/squid-%{version}/COPYING %{buildroot}/usr/share/package-licenses/squid/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/squid-%{version}/errors/COPYRIGHT %{buildroot}/usr/share/package-licenses/squid/bd8ef79f284c33d1a5c89e20f84db61dff649860 || :
cp %{_builddir}/squid-%{version}/libltdl/COPYING.LIB %{buildroot}/usr/share/package-licenses/squid/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/squid.service
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/tmpfiles.d/squid.conf
## install_append content
mkdir -p %{buildroot}/usr/share/doc/squid
install squid.conf.default %{buildroot}/usr/share/doc/squid/
install src/mime.conf.default %{buildroot}/usr/share/doc/squid/
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/purge
/usr/bin/squid
/usr/bin/squidclient

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/squid.conf

%files data
%defattr(-,root,root,-)
/usr/share/squid/errors/COPYRIGHT
/usr/share/squid/errors/TRANSLATORS
/usr/share/squid/errors/templates/ERR_ACCESS_DENIED
/usr/share/squid/errors/templates/ERR_ACL_TIME_QUOTA_EXCEEDED
/usr/share/squid/errors/templates/ERR_AGENT_CONFIGURE
/usr/share/squid/errors/templates/ERR_AGENT_WPAD
/usr/share/squid/errors/templates/ERR_CACHE_ACCESS_DENIED
/usr/share/squid/errors/templates/ERR_CACHE_MGR_ACCESS_DENIED
/usr/share/squid/errors/templates/ERR_CANNOT_FORWARD
/usr/share/squid/errors/templates/ERR_CONFLICT_HOST
/usr/share/squid/errors/templates/ERR_CONNECT_FAIL
/usr/share/squid/errors/templates/ERR_DIR_LISTING
/usr/share/squid/errors/templates/ERR_DNS_FAIL
/usr/share/squid/errors/templates/ERR_ESI
/usr/share/squid/errors/templates/ERR_FORWARDING_DENIED
/usr/share/squid/errors/templates/ERR_FTP_DISABLED
/usr/share/squid/errors/templates/ERR_FTP_FAILURE
/usr/share/squid/errors/templates/ERR_FTP_FORBIDDEN
/usr/share/squid/errors/templates/ERR_FTP_NOT_FOUND
/usr/share/squid/errors/templates/ERR_FTP_PUT_CREATED
/usr/share/squid/errors/templates/ERR_FTP_PUT_ERROR
/usr/share/squid/errors/templates/ERR_FTP_PUT_MODIFIED
/usr/share/squid/errors/templates/ERR_FTP_UNAVAILABLE
/usr/share/squid/errors/templates/ERR_GATEWAY_FAILURE
/usr/share/squid/errors/templates/ERR_ICAP_FAILURE
/usr/share/squid/errors/templates/ERR_INVALID_REQ
/usr/share/squid/errors/templates/ERR_INVALID_RESP
/usr/share/squid/errors/templates/ERR_INVALID_URL
/usr/share/squid/errors/templates/ERR_LIFETIME_EXP
/usr/share/squid/errors/templates/ERR_NO_RELAY
/usr/share/squid/errors/templates/ERR_ONLY_IF_CACHED_MISS
/usr/share/squid/errors/templates/ERR_PRECONDITION_FAILED
/usr/share/squid/errors/templates/ERR_PROTOCOL_UNKNOWN
/usr/share/squid/errors/templates/ERR_READ_ERROR
/usr/share/squid/errors/templates/ERR_READ_TIMEOUT
/usr/share/squid/errors/templates/ERR_SECURE_CONNECT_FAIL
/usr/share/squid/errors/templates/ERR_SHUTTING_DOWN
/usr/share/squid/errors/templates/ERR_SOCKET_FAILURE
/usr/share/squid/errors/templates/ERR_TOO_BIG
/usr/share/squid/errors/templates/ERR_UNSUP_HTTPVERSION
/usr/share/squid/errors/templates/ERR_UNSUP_REQ
/usr/share/squid/errors/templates/ERR_URN_RESOLVE
/usr/share/squid/errors/templates/ERR_WRITE_ERROR
/usr/share/squid/errors/templates/ERR_ZERO_SIZE_OBJECT
/usr/share/squid/errors/templates/error-details.txt
/usr/share/squid/icons/SN.png
/usr/share/squid/icons/silk/application.png
/usr/share/squid/icons/silk/arrow_up.png
/usr/share/squid/icons/silk/bomb.png
/usr/share/squid/icons/silk/box.png
/usr/share/squid/icons/silk/bricks.png
/usr/share/squid/icons/silk/bullet_red.png
/usr/share/squid/icons/silk/cd.png
/usr/share/squid/icons/silk/chart_line.png
/usr/share/squid/icons/silk/compress.png
/usr/share/squid/icons/silk/computer_link.png
/usr/share/squid/icons/silk/css.png
/usr/share/squid/icons/silk/cup.png
/usr/share/squid/icons/silk/database.png
/usr/share/squid/icons/silk/database_table.png
/usr/share/squid/icons/silk/drive_disk.png
/usr/share/squid/icons/silk/film.png
/usr/share/squid/icons/silk/film_key.png
/usr/share/squid/icons/silk/folder.png
/usr/share/squid/icons/silk/folder_table.png
/usr/share/squid/icons/silk/image.png
/usr/share/squid/icons/silk/information.png
/usr/share/squid/icons/silk/layers.png
/usr/share/squid/icons/silk/layout.png
/usr/share/squid/icons/silk/link.png
/usr/share/squid/icons/silk/music.png
/usr/share/squid/icons/silk/package.png
/usr/share/squid/icons/silk/package_go.png
/usr/share/squid/icons/silk/page_code.png
/usr/share/squid/icons/silk/page_excel.png
/usr/share/squid/icons/silk/page_green.png
/usr/share/squid/icons/silk/page_white.png
/usr/share/squid/icons/silk/page_white_acrobat.png
/usr/share/squid/icons/silk/page_white_c.png
/usr/share/squid/icons/silk/page_white_cplusplus.png
/usr/share/squid/icons/silk/page_white_flash.png
/usr/share/squid/icons/silk/page_white_magnify.png
/usr/share/squid/icons/silk/page_white_picture.png
/usr/share/squid/icons/silk/page_white_powerpoint.png
/usr/share/squid/icons/silk/page_white_stack.png
/usr/share/squid/icons/silk/page_white_text.png
/usr/share/squid/icons/silk/page_white_word.png
/usr/share/squid/icons/silk/page_white_zip.png
/usr/share/squid/icons/silk/page_world.png
/usr/share/squid/icons/silk/photo.png
/usr/share/squid/icons/silk/picture.png
/usr/share/squid/icons/silk/plugin.png
/usr/share/squid/icons/silk/plugin_add.png
/usr/share/squid/icons/silk/script.png
/usr/share/squid/icons/silk/script_gear.png
/usr/share/squid/icons/silk/script_palette.png
/usr/share/squid/mib.txt

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/squid/*

%files libexec
%defattr(-,root,root,-)
/usr/libexec/basic_db_auth
/usr/libexec/basic_fake_auth
/usr/libexec/basic_getpwnam_auth
/usr/libexec/basic_ldap_auth
/usr/libexec/basic_ncsa_auth
/usr/libexec/basic_pam_auth
/usr/libexec/basic_pop3_auth
/usr/libexec/basic_radius_auth
/usr/libexec/basic_sasl_auth
/usr/libexec/basic_smb_auth
/usr/libexec/basic_smb_auth.sh
/usr/libexec/cachemgr.cgi
/usr/libexec/cert_tool
/usr/libexec/digest_edirectory_auth
/usr/libexec/digest_file_auth
/usr/libexec/digest_ldap_auth
/usr/libexec/diskd
/usr/libexec/ext_delayer_acl
/usr/libexec/ext_edirectory_userip_acl
/usr/libexec/ext_file_userip_acl
/usr/libexec/ext_kerberos_ldap_group_acl
/usr/libexec/ext_kerberos_sid_group_acl
/usr/libexec/ext_ldap_group_acl
/usr/libexec/ext_sql_session_acl
/usr/libexec/ext_unix_group_acl
/usr/libexec/ext_wbinfo_group_acl
/usr/libexec/helper-mux
/usr/libexec/log_db_daemon
/usr/libexec/log_file_daemon
/usr/libexec/negotiate_kerberos_auth
/usr/libexec/negotiate_kerberos_auth_test
/usr/libexec/negotiate_wrapper_auth
/usr/libexec/ntlm_fake_auth
/usr/libexec/security_fake_certverify
/usr/libexec/storeid_file_rewrite
/usr/libexec/unlinkd
/usr/libexec/url_fake_rewrite
/usr/libexec/url_fake_rewrite.sh
/usr/libexec/url_lfs_rewrite

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/squid/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/squid/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/squid/bd8ef79f284c33d1a5c89e20f84db61dff649860

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/purge.1
/usr/share/man/man1/squidclient.1
/usr/share/man/man8/basic_db_auth.8
/usr/share/man/man8/basic_getpwnam_auth.8
/usr/share/man/man8/basic_ldap_auth.8
/usr/share/man/man8/basic_ncsa_auth.8
/usr/share/man/man8/basic_pam_auth.8
/usr/share/man/man8/basic_pop3_auth.8
/usr/share/man/man8/basic_radius_auth.8
/usr/share/man/man8/basic_sasl_auth.8
/usr/share/man/man8/cachemgr.cgi.8
/usr/share/man/man8/digest_file_auth.8
/usr/share/man/man8/ext_delayer_acl.8
/usr/share/man/man8/ext_edirectory_userip_acl.8
/usr/share/man/man8/ext_file_userip_acl.8
/usr/share/man/man8/ext_kerberos_sid_group_acl.8
/usr/share/man/man8/ext_ldap_group_acl.8
/usr/share/man/man8/ext_sql_session_acl.8
/usr/share/man/man8/ext_unix_group_acl.8
/usr/share/man/man8/ext_wbinfo_group_acl.8
/usr/share/man/man8/helper-mux.8
/usr/share/man/man8/log_db_daemon.8
/usr/share/man/man8/negotiate_kerberos_auth.8
/usr/share/man/man8/security_fake_certverify.8
/usr/share/man/man8/squid.8
/usr/share/man/man8/storeid_file_rewrite.8
/usr/share/man/man8/url_lfs_rewrite.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/squid.service
