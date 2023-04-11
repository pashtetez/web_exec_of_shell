journalctl _SYSTEMD_INVOCATION_ID=`systemctl show -p InvocationID --value zomboid.service` |grep STARTED
