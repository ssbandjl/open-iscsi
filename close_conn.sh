iscsiadm -m node --logoutall=all;iscsiadm -m node -o delete -T iqn.2018-01.com.h3c.onestor:f2a23531433249f7bf2a6d01760fe755 -p 172.17.136.132:3260;rm -rf /var/lib/iscsi/send_targets/
