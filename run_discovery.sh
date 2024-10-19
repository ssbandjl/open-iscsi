iscsiadm -m discovery -t sendtargets -p 172.17.136.132 -d 8
iscsiadm -m discovery -t sendtargets -p 10.13.4.15:3261 -d 8
iscsiadm -m node -T iqn.2016-06.io.spdk:disk1 -p 10.13.4.15:3261 --login -d 8
./usr/iscsiadm -m discovery -t sendtargets -p 10.13.4.15:3261 -d 8

