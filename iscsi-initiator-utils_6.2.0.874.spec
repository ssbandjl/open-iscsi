%define open_iscsi_version	2.0
%define open_iscsi_build	874

Summary: iSCSI daemon and utility programs
Name: iscsi-initiator-utils
Version: 6.%{open_iscsi_version}.%{open_iscsi_build}
Release: 22%{?dist}
Group: System Environment/Daemons
License: GPLv2+
URL: http://www.open-iscsi.org

Source0: https://github.com/open-iscsi/open-iscsi/archive/%{open_iscsi_version}.%{open_iscsi_build}.tar.gz#/open-iscsi-%{open_iscsi_version}.%{open_iscsi_build}.tar.gz
Source4: 04-iscsi
Source5: iscsi-tmpfiles.conf

# upstream patches, post last tagged version
Patch1: open-iscsi-2.0.874-1-iBFT-origin-is-an-enum-not-a-string.patch
Patch2: open-iscsi-2.0.874-4-iscsid-treat-SIGTERM-like-iscsiadm-k-0.patch
Patch3: open-iscsi-2.0.874-5-Make-event_loop_stop-volatile-for-safer-access.patch
Patch4: open-iscsi-2.0.874-7-iscsid-Changes-to-support-the-new-qedi-transport.patch
Patch5: open-iscsi-2.0.874-8-iscsiuio-Add-support-for-the-new-qedi-transport.patch
Patch6: open-iscsi-2.0.874-9-iscsiuio-v0.7.8.3.patch
Patch7: open-iscsi-2.0.874-7-Allow-disabling-auto-LUN-scans.patch
Patch8: open-iscsi-2.0.874-23-Fix-manual-LUN-scans-feature.patch
Patch9: open-iscsi-2.0.874-27-iscsid-Add-qedi-ping-transport-hook.patch
Patch20: open-iscsi-2.0.874-30-isolate-iscsistart-socket-use.patch
# not (yet) upstream merged
Patch140: open-iscsi-2.0.874-iscsid-reset-head-on-wrap-when-buffer-empty.patch
Patch143: 0143-idmb_rec_write-check-for-tpgt-first.patch
Patch145: 0145-idbm_rec_write-seperate-old-and-new-style-writes.patch
Patch146: 0146-idbw_rec_write-pick-tpgt-from-existing-record.patch
Patch149: 0149-update-systemd-service-files-add-iscsi.service-for-s.patch
Patch150: 0150-iscsi-boot-related-service-file-updates.patch
Patch177: open-iscsi-2.0.874-30-iscsiuio-fix-dhcpv6-transaction-id-mismatch-error.patch
Patch178: open-iscsi-2.0.874-31-iscsiuio-serialize-xmit_mutex-lock-to-prevent-iscsiuio-seg-fault.patch
Patch179: open-iscsi-2.0.874-32-iscsiuio-allow-ARP-for-non-matching-src-and-dst-addresses.patch
Patch180: open-iscsi-2.0.874-33-iscsiuio-v0.7.8.4.patch
Patch181: open-iscsi-2.0.876-3-qedi.c-Removed-unused-linux-ethtool.h.patch
Patch182: open-iscsi-2.0.876-31-Fix-iscsiuio-segfault-when-shutting-down.patch
Patch183: open-iscsi-2.0.876-54-iscsiuio-Add-inter-host-mutex-while-doing-xmit.patch
Patch184: 0184-set-iscsid.safe_logout-to-Yes-by-default.patch

Patch195: open-iscsi-2.0.874-35-iscsiuio-fix-long-options.patch
Patch196: open-iscsi-2.0.874-38-Update-bnx2.c.patch
Patch197: open-iscsi-2.0.874-39-Update-bnx2x.c.patch
Patch198: open-iscsi-2.0.875-7-Ignore-library-file-for-iscsiuio-src.patch
Patch199: open-iscsi-2.0.875-9-Remove-unused-variables.-No-functional-change.patch
Patch200: open-iscsi-2.0.875-10-Include-sys-sysmacros.h-to-properly-define-minor.patch
Patch201: open-iscsi-2.0.875-11-Declare-inline-best_match_bufcmp-as-static.patch
Patch202: open-iscsi-2.0.875-14-Check-for-root-peer-user-for-iscsiuio-IPC.patch
Patch203: open-iscsi-2.0.875-15-iscsiuio-should-ignore-bogus-iscsid-broadcast-packets.patch
Patch204: open-iscsi-2.0.875-16-Ensure-all-fields-in-iscsiuio-IPC-response-are-set.patch
Patch205: open-iscsi-2.0.875-17-Do-not-double-close-IPC-file-stream-to-iscsid.patch
Patch206: open-iscsi-2.0.875-18-Ensure-strings-from-peer-are-copied-correctly.patch
Patch207: open-iscsi-2.0.875-19-Skip-useless-strcopy-and-validate-CIDR-length.patch
Patch208: open-iscsi-2.0.875-20-Check-iscsiuio-ping-data-length-for-validity.patch
Patch209: open-iscsi-2.0.875-21-tell-git-to-ignore-the-iscsiuio-binary.patch
Patch210: open-iscsi-2.0.875-30-Cleanup-iscsiuio-master-Makefile-template.patch
Patch211: open-iscsi-2.0.876-5-bnx2x.c-Reorder-the-includes-to-avoid-duplicate-defines-with-musl.patch
Patch212: open-iscsi-2.0.876-6-Use-correct-size-when-copying-nic-name.patch
Patch213: 0001-Keep-iscsi_if-in-sync-with-kernel-version.patch
Patch214: 0001-Add-error-message-for-new-ISCSI_ERR_NOP_TIMEDOUT.patch
Patch215: open-iscsi-2.0.876-56-iscsiuio-Release-xmit_mutex-in-error-code-path.patch
Patch216: open-iscsi-2.0.876-57-iscsiuio-limit-retries-of-performing-dhcpv6-before-declaring-dhcp-failure.patch
Patch217: open-iscsi-2.0.876-58-iscsiuio-Do-not-flush-tx-queue-on-each-uio-interrupt.patch
Patch218: open-iscsi-2.0.876-59-qedi-Set-buf_size-in-case-of-ICMP-and-ARP-packet.patch
Patch219: open-iscsi-2.0.876-60-qedi-Use-uio-BD-index-instead-on-buffer-index.patch
Patch220: open-iscsi-2.0.876-61-iscsiuio-v0.7.8.5.patch
Patch221: open-iscsi-2.0.876-66-Close-file-handles-when-writing-pid-files.patch
Patch222: open-iscsi-2.0.876-66-iscsiuio-avoid-loosing-bad-rc-in-nic_nl_open.patch
Patch223: open-iscsi-2.0.876-67-iscsiuio-fail-on-nic_nl_open-failing.patch
Patch224: 0001-rec-update-disable-the-idbm_lock-in-read-write-when-.patch
Patch225: 0001-iscsiuio-allow-processing-of-iscsid-requests-in-DHCP.patch
Patch226: 0001-iscsiuio-update-version-to-0.7.8.6.patch
Patch227: 0001-iscsid-Update-boot-gateway-information-during-sync_s.patch

# distro specific modifications
Patch351: 0151-update-initscripts-and-docs.patch
Patch352: 0152-use-var-for-config.patch
Patch353: 0153-use-red-hat-for-name.patch
Patch354: 0154-add-libiscsi.patch
Patch356: 0156-remove-the-offload-boot-supported-ifdef.patch
Patch359: 0159-iscsiuio-systemd-unit-files.patch
Patch360: 0160-use-systemctl-to-start-iscsid.patch
Patch361: 0161-resolve-565245-multilib-issues-caused-by-doxygen.patch
Patch362: 0162-Don-t-check-for-autostart-sessions-if-iscsi-is-not-u.patch
Patch364: 0164-libiscsi-fix-incorrect-strncpy-use.patch
Patch366: 0166-start-socket-listeners-on-iscsiadm-command.patch
Patch367: 0167-Revert-iscsiadm-return-error-when-login-fails.patch
Patch368: 0168-update-handling-of-boot-sessions.patch
Patch369: 0169-update-iscsi.service-for-boot-session-recovery.patch
Patch370: 0170-fix-systemd-unit-wants.patch
Patch372: 0172-move-cleanup-to-seperate-service.patch
Patch375: open-iscsi-2.0.876-41-vlan-setting-sync-across-ipv4-ipv6-for-be2iscsi.patch
Patch376: 0001-enable-MaxOutstandingR2T-negotiation.patch

# upstream removed internal open-isns, but not taking that here just yet
# it requires repackaging isns-utils to provide a debug package
Patch380: keep-open-isns.patch
# version string, needs to be updated with each build
Patch400: 0199-use-Red-Hat-version-string-to-match-RPM-package-vers.patch
Patch401: 0001-Update-service-files-and-add-sd_notify-support-to-is.patch
Patch402: 0001-restore-some-service-file-differences.patch
Patch403: 0001-fix-upstream-build-breakage-of-iscsiuio-LDFLAGS.patch
Patch404: 0001-improve-systemd-service-files-for-boot-session-handl.patch

Patch500: 0500-CHAP-SHA-1-SHA-256-SHA3-256-via-OpenSSL-s-libcrypto.patch
Patch501: 0501-configuration-support-for-CHAP-algorithms.patch
Patch502: 0502-CHAP-FIPS-backport-fixups.patch
Patch503: 0503-fix-libiscsi-after-adding-libcrypto-requirement.patch
Patch504: 0504-iscsiadm-buffer-overflow-regression-when-discovering.patch
Patch505: 0001-missing-break-causing-segfault-with-case-sensitive-c.patch

BuildRequires: flex bison python-devel doxygen kmod-devel systemd-devel libmount-devel autoconf automake libtool openssl-devel
# For dir ownership
Requires: %{name}-iscsiuio >= %{version}-%{release}
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%global _hardened_build 1
%global __provides_exclude_from ^(%{python_sitearch}/.*\\.so)$

%description
The iscsi package provides the server daemon for the iSCSI protocol,
as well as the utility programs used to manage it. iSCSI is a protocol
for distributed disk access using SCSI commands sent over Internet
Protocol networks.

%package iscsiuio
Summary: Userspace configuration daemon required for some iSCSI hardware
Group: System Environment/Daemons
License: BSD
Requires: %{name} = %{version}-%{release}

%description iscsiuio
The iscsiuio configuration daemon provides network configuration help
for some iSCSI offload hardware.

%package devel
Summary: Development files for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n open-iscsi-%{open_iscsi_version}.%{open_iscsi_build}

# change exec_prefix, there's no easy way to override
%{__sed} -i -e 's|^exec_prefix = /$|exec_prefix = %{_exec_prefix}|' Makefile

%build

# configure sub-packages from here
# letting the top level Makefile do it will lose setting from rpm
cd iscsiuio
autoreconf --install
%{configure}
cd ..

cd utils/open-isns
chmod +x ./configure
%{configure} --with-security=no --with-slp=no
cd ../..

%{__make} OPTFLAGS="%{optflags} %{?__global_ldflags} -DUSE_KMOD -lkmod"
pushd libiscsi
python setup.py build
touch -r libiscsi.doxy html/*
popd


%install
%{__make} DESTDIR=%{?buildroot} install_programs install_doc install_etc
# upstream makefile doesn't get everything the way we like it
rm $RPM_BUILD_ROOT%{_sbindir}/iscsi_discovery
rm $RPM_BUILD_ROOT%{_mandir}/man8/iscsi_discovery.8
%{__install} -pm 755 usr/iscsistart $RPM_BUILD_ROOT%{_sbindir}
%{__install} -pm 644 doc/iscsistart.8 $RPM_BUILD_ROOT%{_mandir}/man8
%{__install} -pm 644 doc/iscsi-iname.8 $RPM_BUILD_ROOT%{_mandir}/man8
%{__install} -d $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
%{__install} -pm 644 iscsiuio/iscsiuiolog $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d

%{__install} -d $RPM_BUILD_ROOT%{_sharedstatedir}/iscsi
%{__install} -d $RPM_BUILD_ROOT%{_sharedstatedir}/iscsi/nodes
%{__install} -d $RPM_BUILD_ROOT%{_sharedstatedir}/iscsi/send_targets
%{__install} -d $RPM_BUILD_ROOT%{_sharedstatedir}/iscsi/static
%{__install} -d $RPM_BUILD_ROOT%{_sharedstatedir}/iscsi/isns
%{__install} -d $RPM_BUILD_ROOT%{_sharedstatedir}/iscsi/slp
%{__install} -d $RPM_BUILD_ROOT%{_sharedstatedir}/iscsi/ifaces

# for %%ghost
%{__install} -d $RPM_BUILD_ROOT/var/lock/iscsi
touch $RPM_BUILD_ROOT/var/lock/iscsi/lock


%{__install} -d $RPM_BUILD_ROOT%{_unitdir}
%{__install} -pm 644 etc/systemd/iscsi.service $RPM_BUILD_ROOT%{_unitdir}
%{__install} -pm 644 etc/systemd/iscsi-onboot.service $RPM_BUILD_ROOT%{_unitdir}
%{__install} -pm 644 etc/systemd/iscsi-shutdown.service $RPM_BUILD_ROOT%{_unitdir}
%{__install} -pm 644 etc/systemd/iscsid.service $RPM_BUILD_ROOT%{_unitdir}
%{__install} -pm 644 etc/systemd/iscsid.socket $RPM_BUILD_ROOT%{_unitdir}
%{__install} -pm 644 etc/systemd/iscsiuio.service $RPM_BUILD_ROOT%{_unitdir}
%{__install} -pm 644 etc/systemd/iscsiuio.socket $RPM_BUILD_ROOT%{_unitdir}

%{__install} -d $RPM_BUILD_ROOT%{_libexecdir}
%{__install} -pm 755 etc/systemd/iscsi-mark-root-nodes $RPM_BUILD_ROOT%{_libexecdir}

%{__install} -d $RPM_BUILD_ROOT%{_sysconfdir}/NetworkManager/dispatcher.d
%{__install} -pm 755 %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/NetworkManager/dispatcher.d

%{__install} -d $RPM_BUILD_ROOT%{_tmpfilesdir}
%{__install} -pm 644 %{SOURCE5} $RPM_BUILD_ROOT%{_tmpfilesdir}/iscsi.conf

%{__install} -d $RPM_BUILD_ROOT%{_libdir}
%{__install} -pm 755 libiscsi/libiscsi.so.0 $RPM_BUILD_ROOT%{_libdir}
%{__ln_s}    libiscsi.so.0 $RPM_BUILD_ROOT%{_libdir}/libiscsi.so
%{__install} -d $RPM_BUILD_ROOT%{_includedir}
%{__install} -pm 644 libiscsi/libiscsi.h $RPM_BUILD_ROOT%{_includedir}

%{__install} -d $RPM_BUILD_ROOT%{python_sitearch}
%{__install} -pm 755 libiscsi/build/lib.linux-*/libiscsimodule.so \
	$RPM_BUILD_ROOT%{python_sitearch}


%post
/sbin/ldconfig

%systemd_post iscsi.service iscsi-onboot.service iscsi-shutdown.service iscsid.service iscsid.socket

if [ $1 -eq 1 ]; then
	if [ ! -f %{_sysconfdir}/iscsi/initiatorname.iscsi ]; then
		echo "InitiatorName=`/usr/sbin/iscsi-iname`" > %{_sysconfdir}/iscsi/initiatorname.iscsi
	fi
	# enable socket activation and persistant session startup by default
	/bin/systemctl enable iscsi.service >/dev/null 2>&1 || :
	/bin/systemctl enable iscsi-onboot.service >/dev/null 2>&1 || :
	/bin/systemctl enable iscsid.socket >/dev/null 2>&1 || :
	/bin/systemctl start iscsid.socket >/dev/null 2>&1 || :
fi

%post iscsiuio
%systemd_post iscsiuio.service iscsiuio.socket

if [ $1 -eq 1 ]; then
	/bin/systemctl enable iscsiuio.socket >/dev/null 2>&1 || :
	/bin/systemctl start iscsiuio.socket >/dev/null 2>&1 || :
fi

%preun
%systemd_preun iscsi.service iscsi-onboot.service iscsi-shutdown.service iscsid.service iscsid.socket

%preun iscsiuio
%systemd_preun iscsiuio.service iscsiuio.socket

%postun
/sbin/ldconfig
%systemd_postun iscsi.service iscsi-onboot.service iscsi-shutdown.service iscsid.service iscsid.socket

%postun iscsiuio
%systemd_postun iscsiuio.service iscsiuio.socket

%triggerun -- iscsi-initiator-utils < 6.2.0.873-22
# prior to 6.2.0.873-22 iscsi.service was missing a Wants=remote-fs-pre.target
# this forces remote-fs-pre.target active if needed for a clean shutdown/reboot
# after upgrading this package
if [ $1 -gt 0 ]; then
    /usr/bin/systemctl -q is-active iscsi.service
    if [ $? -eq 0 ]; then
        /usr/bin/systemctl -q is-active remote-fs-pre.target
        if [ $? -ne 0 ]; then
            SRC=`/usr/bin/systemctl show --property FragmentPath remote-fs-pre.target | cut -d= -f2`
            DST=/run/systemd/system/remote-fs-pre.target
            if [ $SRC != $DST ]; then
                cp $SRC $DST
            fi
            sed -i 's/RefuseManualStart=yes/RefuseManualStart=no/' $DST
            /usr/bin/systemctl daemon-reload >/dev/null 2>&1 || :
            /usr/bin/systemctl start remote-fs-pre.target >/dev/null 2>&1 || :
        fi
    fi
fi
# added in 6.2.0.873-26
if [ $1 -gt 0 ]; then
    systemctl start iscsi-shutdown.service >/dev/null 2>&1 || :
fi

%files
%doc README
%dir %{_sharedstatedir}/iscsi
%dir %{_sharedstatedir}/iscsi/nodes
%dir %{_sharedstatedir}/iscsi/isns
%dir %{_sharedstatedir}/iscsi/static
%dir %{_sharedstatedir}/iscsi/slp
%dir %{_sharedstatedir}/iscsi/ifaces
%dir %{_sharedstatedir}/iscsi/send_targets
%ghost %attr(0700, -, -) %{_var}/lock/iscsi
%ghost %attr(0600, -, -) %{_var}/lock/iscsi/lock
%{_unitdir}/iscsi.service
%{_unitdir}/iscsi-onboot.service
%{_unitdir}/iscsi-shutdown.service
%{_unitdir}/iscsid.service
%{_unitdir}/iscsid.socket
%{_libexecdir}/iscsi-mark-root-nodes
%{_sysconfdir}/NetworkManager/dispatcher.d/04-iscsi
%{_tmpfilesdir}/iscsi.conf
%dir %{_sysconfdir}/iscsi
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/iscsi/iscsid.conf
%{_sbindir}/iscsi-iname
%{_sbindir}/iscsiadm
%{_sbindir}/iscsid
%{_sbindir}/iscsistart
%{_libdir}/libiscsi.so.0
%{python_sitearch}/libiscsimodule.so
%{_mandir}/man8/iscsi-iname.8.gz
%{_mandir}/man8/iscsiadm.8.gz
%{_mandir}/man8/iscsid.8.gz
%{_mandir}/man8/iscsistart.8.gz

%files iscsiuio
%{_sbindir}/iscsiuio
%{_unitdir}/iscsiuio.service
%{_unitdir}/iscsiuio.socket
%config(noreplace) %{_sysconfdir}/logrotate.d/iscsiuiolog
%{_mandir}/man8/iscsiuio.8.gz

%files devel
%doc libiscsi/html
%{_libdir}/libiscsi.so
%{_includedir}/libiscsi.h

%changelog
* Thu Oct 07 2021 Chris Leech <cleech@redhat.com> - 6.2.0.874-22
- 1946578 fix segfault on case mismatch in config/record file

* Mon Aug 09 2021 Chris Leech <cleech@redhat.com> - 6.2.0.874-21
- 1989972 set proper attr in rpm db for lockfiles, fixes rpm verificiation warning

* Wed Sep 30 2020 Chris Leech <cleech@redhat.com> - 6.2.0.874-20
- 1881245 iscsiadm regression when discovering many targets at once

* Thu Jul 02 2020 Chris Leech <cleech@redhat.com> - 6.2.0.874-19
- 1851250 fix libiscsi for libcrypto requirement

* Tue May 12 2020 Chris Leech <cleech@redhat.com> - 6.2.0.874-18
- 1809945 backport new CHAP modes for FIPS environments (SHA1 and SHA256 only, no SHA3 in OpenSSL-1.0.2)

* Mon Oct 28 2019 Chris Leech <cleech@redhat.com> - 6.2.0.874-17
- 1518367 boot from iSCSI not establishing all sessions persistently
- 1667965 A manual restart of iscsi.service modifies records node.startup value

* Thu Oct 17 2019 Chris Leech <cleech@redhat.com> - 6.2.0.874-16
- upstream iscsiuio/configure.ac changes were breaking build hardening

* Wed Oct 16 2019 Chris Leech <cleech@redhat.com> - 6.2.0.874-15
- 1396651 Update service files, support sd_notify instead of pid files, stop forking

* Wed Sep 11 2019 Chris Leech <cleech@redhat.com> - 6.2.0.874-14
- 1598647 update boot gateway information during sync_session

* Fri Aug 23 2019 Chris Leech <cleech@redhat.com> - 6.2.0.874-13
- 1724579 iscsiuio update, allow processing requests in DHCP failure condition

* Tue Aug 20 2019 Chris Leech <cleech@redhat.com> - 6.2.0.874-12
- 1389071 handle newer ISCSI_ERR_NOP_TIMEDOUT code from the kernel
- 1624670 Login negotiation failed due to CHAP_N values do not match
          (rec update race condition)

* Wed Mar 06 2019 Chris Leech <cleech@redhat.com> - 6.2.0.874-11
- 1649401, 1649413 iscsiuio updates

* Wed Aug 29 2018 Chris Leech <cleech@redhat.com> - 6.2.0.874-10
- 1185734 set iscsid.safe_logout to Yes by default

* Fri Jun 22 2018 Chris Leech <cleech@redhat.com> - 6.2.0.874-9
- 1578984 update iscsiuio to v0.7.8.4

* Fri Jun 22 2018 Chris Leech <cleech@redhat.com> - 6.2.0.874-8
- 1278438 enable MaxOutstandingR2T negotiation during login

* Thu Nov 30 2017 Chris Leech <cleech@redhat.com> - 6.2.0.874-7
- 1328694 keep vlan settings in sync for ipv4/ipv6 iface records with be2iscsi

* Wed Nov 01 2017 Chris Leech <cleech@redhat.com> - 6.2.0.874-6
- 1507945 force start iscsiuio for boot session recovery with qedi
- 1457359 start systemd socket listeners, otherwise if iscsid is started
  directly iscsiuio doesn't activate as expected

* Tue Aug 15 2017 Chris Leech <cleech@redhat.com> - 6.2.0.874-5
- 1431622 fix default in iscsi-iname manpage to match Red Hat customization

* Tue Jun 27 2017 Chris Leech <cleech@redhat.com> - 6.2.0.874-4
- 1450756 isolate iscsistart sockets

* Fri Apr 28 2017 Chris Leech <cleech@redhat.com> - 6.2.0.874-3
- 1445686 add missing ping hook for the qedi transport driver

* Tue Apr 11 2017 Chris Leech <cleech@redhat.com> - 6.2.0.874-2
- 1422941 allow disabling of auto scanning sessions, requested for OpenStack

* Tue Feb 28 2017 Chris Leech <cleech@redhat.com> - 6.2.0.874-1
- 1384090 upstream 2.0.874+ with qedi support
- 1414819 iscsid reporting blank emerg messages

* Thu Aug 18 2016 Chris Leech <cleech@redhat.com> - 6.2.0.873-35
- 1362590 Revert iscsiuio pthread changes that result in a race condition on shutdown

* Tue Jun 14 2016 Chris Leech <cleech@redhat.com> - 6.2.0.873-34
- 1322000 ensure TCP abort on session failure to prevent data corruption with link flap
- 1294964, 1265073, 1213569 iscsiuio update, fix small ARP table issue
- 1309488 remove broken sysfs cache code to speed up login of many sessions
- 1330348 sync with upstream Open-iSCSI for minor fixes

* Tue Apr 26 2016 Chris Leech <cleech@redhat.com> - 6.2.0.873-33
- 1275139 iscsiuio support for multi-function mode NetXtreme2 HBAs

* Fri Jul 24 2015 Chris Leech <cleech@redhat.com> - 6.2.0.873-32
- 1235684 apply safe_logout setting to flashnode sessions as well
  but only when logging out by session id, not by flashnode index

* Tue Jul 21 2015 Chris Leech <cleech@redhat.com> - 6.2.0.873-31
- 1235684 fix safe logout DM name canonicalization, use libmount cache

* Mon Jul 06 2015 Chris Leech <cleech@redhat.com> - 6.2.0.873-30
- 1235684 add iscsid safe logout option

* Fri Jan 30 2015 Chris Leech <cleech@redhat.com> - 6.2.0.873-29
- 1166713 1187792 add missing ExecStart, only newer systemd lets that be optional for oneshot services

* Thu Jan 15 2015 Chris Leech <cleech@redhat.com> - 6.2.0.873-28
- 1180100 scriptlets were never split out properly for the iscsiuio subpackage

* Thu Jan 15 2015 Chris Leech <cleech@redhat.com> - 6.2.0.873-27
- 1168556 fix regression in network interface binding

* Mon Jan 12 2015 Chris Leech <cleech@redhat.com> - 6.2.0.873-26
- 1166713 created iscsi-shutdown.service to ensure that session cleanup happens

* Thu Dec 11 2014 Andy Grover <agrover@redhat.com> - 6.2.0.873-25
- Add --with-slp=no for #1088020

* Tue Nov 18 2014 Chris Leech <cleech@redhat.com> - 6.2.0.873-24
- 1040343 segfault from unexpected netlink event during discovery
- inhibit strict aliasing optimizations in iscsiuio, rpmdiff error

* Tue Oct 21 2014 Chris Leech <cleech@redhat.com> - 6.2.0.873-23
- make sure to pass --with-security=no to isns configure (#1088020)

* Wed Sep 24 2014 Chris Leech <cleech@redhat.com> - 6.2.0.873-22
- 1081798 retry login on host not found error
- 1111925 ignore iscsiadm return in iscsi.service
- 1126524 make sure systemd order against remote mounts is correct
- 963039 add discovery as a valid mode in iscsiadm.8
- sync with upstream

* Tue Mar 18 2014 Chris Leech <cleech@redhat.com> - 6.2.0.873-21
- 1069825
- boot session handling improvements
- Fix iscsi-mark-root for changed iscsiadm output
- Make sure iscsiuio is running for boot session recovery when using the
  bnx2i transport by forcing iscsiuio.service start
- Make NM dispatch triggered re-check for autostart sessions async
- Accept exit code 21, no records, from iscsiadm as success in
  iscsi.service

* Tue Feb 25 2014 Chris Leech <cleech@redhat.com> - 6.2.0.873-20
- 1049710 host0 being treated as an invalid in the host stats command
- 1015563 revert change to return code when calling login_portal for sessions
  that already exist, as it impacts users scripting around iscsiadm

* Mon Feb 17 2014 Chris Leech <cleech@redhat.com> - 6.2.0.873-19
- 1007388 fixes for iscsiadm to support qla4xxx
- refresh boot session info patches to final version from upstream,
  fixes context issues with later patches
- 1006156, 1006161 Add/Update entries in chap table through Open-iSCSI
- 948134 extend support to set additional parameters for network configuration
- 1049710 update open-iscsi to support host statistics
- 1043019 iscsiuio fix for arp cache flush issue
- 1059332 Fix broken discovery sessions over iser
- 1017393 split out iscsiuio into a seperate sub-package

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 6.2.0.873-18
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 6.2.0.873-17
- Mass rebuild 2013-12-27

* Mon Nov 25 2013 Chris Leech <cleech@redhat.com> - 6.2.0.873-16
- fix iscsiuio socket activation
- have systemd start socket units on iscsiadm use, if not already listening

* Sun Sep 15 2013 Chris Leech <cleech@redhat.com> - 6.2.0.873-15
- move /sbin to /usr/sbin
- use rpm macros in install rules

* Fri Sep 13 2013 Chris Leech <cleech@redhat.com> - 6.2.0.873-14
- fix iscsiuio hardened build and other compiler flags

* Fri Aug 23 2013 Andy Grover <agrover@redhat.com> - 6.2.0.873-13
- Fix patch 0041 to check session != NULL before calling iscsi_sysfs_read_boot()

* Tue Aug 20 2013 Chris Leech <cleech@redhat.com> - 6.2.0.873-12
- fix regression in last build, database records can't be accessed

* Mon Aug 19 2013 Chris Leech <cleech@redhat.com> - 6.2.0.873-11
- iscsi boot related fixes
  make sure iscsid gets started if there are any boot sessions running
  add reload target to fix double session problem when restarting from NM
  don't rely on session list passed from initrd, never got fully implemented
  remove patches related to running iscsid from initrd, possible to revisit later

* Sun Aug 18 2013 Chris Leech <cleech@redhat.com> - 6.2.0.873-10
- sync with upstream git, minor context fixes after rebase of out-of-tree patches
- iscsiuio is merged upstream, remove old source archive and patches
- spec cleanups to fix rpmlint issues

* Sun Aug  4 2013 Peter Robinson <pbrobinson@fedoraproject.org> 6.2.0.873-9
- Fix FTBFS, cleanup spec

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2.0.873-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 11 2013 Chris Leech <cleech@redhat.com> - 6.2.0.873-7
- Use the systemd tmpfiles service to recreate lockfiles in /var/lock
- 955167 build as a position independent executable
- 894576 fix order of setuid/setgid and drop additional groups

* Tue May 28 2013 Chris Leech <cleech@redhat.com> - 6.2.0.873-6
- Don't have iscsiadm scan for autostart record if node db is empty (bug #951951)

* Tue Apr 30 2013 Orion Poplawski <orion@cora.nwra.com> - 6.2.0.873-5
- Fix typo in NM dispatcher script (bug #917058)

* Thu Feb 21 2013 Chris Leech <cleech@redhat.com> - 6.2.0.873-4
- build with libkmod support, instead of calling out to modprobe
- enable socket activation by default

* Thu Jan 24 2013 Kalev Lember <kalevlember@gmail.com> - 6.2.0.873-3
- Fix the postun script to not use ldconfig as the interpreter

* Wed Jan 23 2013 Chris Leech <cleech@redhat.com> - 6.2.0.873-2
- package iscsi_mark_root_nodes script, it's being referenced by the unit files

* Tue Jan 22 2013 Chris Leech <cleech@redhat.com> - 6.2.0.873-1
- rebase to new upstream code
- systemd conversion
- 565245 Fix multilib issues caused by timestamp in doxygen footers

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2.0.872-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 14 2012 Mike Christie <mchristi@redhat.com> 6.2.0.872.18
- 789683 Fix boot slow down when the iscsi service is started
  (regression added in 6.2.0.872.16 when the nm wait was added).

* Mon Feb 6 2012 Mike Christie <mchristi@redhat.com> 6.2.0.872.17
- 786174 Change iscsid/iscsi service startup, so it always starts
  when called.

* Sat Feb 4 2012 Mike Christie <mchristi@redhat.com> 6.2.0.872.16
- 747479 Fix iscsidevs handling of network requirement

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2.0.872-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 30 2011 Mike Christie <mcrhsit@redhat.com> 6.2.0.872.14
- Fix version string to reflect fedora and not rhel.

* Tue Oct 18 2011 Mike Christie <mcrhsit@redhat.com> 6.2.0.872.13
- Update iscsi tools.

* Sat Apr 30 2011 Hans de Goede <hdegoede@redhat.com> - 6.2.0.872-12
- Change iscsi init scripts to check for networking being actually up, rather
  then for NetworkManager being started (#692230)

* Tue Apr 26 2011 Hans de Goede <hdegoede@redhat.com> - 6.2.0.872-11
- Fix iscsid autostarting when upgrading from an older version
  (add iscsid.startup key to iscsid.conf on upgrade)
- Fix printing of [ OK ] when successfully stopping iscsid
- systemd related fixes:
 - Add Should-Start/Stop tgtd to iscsi init script to fix (re)boot from
   hanging when using locally hosted targets
 - %%ghost /var/lock/iscsi and contents (#656605)

* Mon Apr 25 2011 Mike Christie <mchristi@redhat.com> 6.2.0.872-10
- Fix iscsi init scripts check for networking being up (#692230)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2.0.872-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
