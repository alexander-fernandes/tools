#!/bin/bash
########################################
#
# simple bash script to automate
# server backups
#
# run a cronjob on this like:
#
# 0 0 2 */2 * * bashup.sh
#
# every 2 days at midnight every month
#
#######################################

# here is the list of directories to back up
# add or remove ones you need to back up at will
backup_dirs=("/etc" "/home" "/boot")
dest_dir="/backup"
dest_server="server1" # or whatever your server is
backup_date=$(date +%b-%d-%y)

echo "[+] Starting backup of: ${backup_dirs[@]}"

# for every dir in the list of backup dirs
for i in "${backup_dirs[@]}"; do
sudo tar -Pczf /tmp/$i-$backup_date.tar.gz $i
if [ $? -eq 0 ]; then
echo "[#] $i backup succeeded."
else
echo "[!] $i backup failed."
fi
scp /tmp/$i-$backup_date.tar.gz $dest_server:$dest_dir # copy the backup tarball to destination dir
if [ $? -eq 0 ]; then
echo "[#] $i transfer succeeded."
else
echo "[!] $i transfer failed."
fi
done

sudo rm /tmp/*.gzecho "[#] Backup is done."