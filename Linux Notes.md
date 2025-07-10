### My Linux###
Focuses on: RedHat Enterprise v5x
Successor to LinuxCBT EL-4 Edition, which succeeds LinuxCBT Classic Edition

Features:
 1. 2.6x kernel (2.6.18)
  a. 'uname -a' returns OS/Kernel information
Note: 'uname -a' returns the following useful info:
 1. OS - Linux
 2. Fully Qualified Domain Name (FQDN)
 3. Kernel version - 2.6.18...
  a. 2.6 = major version
  b. .18 = minor version
  c. anything else after the minor version indicates that the kernel was patched by the distributor
 4. Date and time that the kernel was compiled

 2. Supports multiple versions:
  a. Basic - Red Hat Enterprise Linux Server
   a1. supports 2 physical (Socket) CPUs
   a2. Up to 4 virtual guests

  b. Advanced Platform 
   b1. supports unlimited physical CPUs
   b2. supports unlimited virtual guests

Note: Virtualization limits pertain to the virtualization technology included with Red Hat Enterprise Linux. NOT third-party software (VMWare)


 3. Supports the following platforms:
  a. Intel 32/64-bits
  b. AMD 32/64-bits
  c. IBM - POWER and z-series, S/390

Note: Memory limitation is based on hardware


Note: Common uses of the various versions of RHEL
 1. RHEL Basic Version
  a. File & Print
  b. Web server
  c. Infrastructure server (DHCP, DNS, Proxy, etc.)

 2. RHEL Advanced Version
  a. Application server (Apache Tomcat, JBOSS, Weblogic, WebSphere, etc.)
  b. Database server (MySQL, PostgreSQL, Oracle, Ingres, etc.)
  c. Clustering


###Kickstart Configurator###

Features:
 1. Hands-free, automated installation
 2. Scripted installation
 3. Script can be used on multiple systems

Note: 'system-config-kickstart' is NOT installed by default

Steps:
 1. Open previously created 'anaconda-ks.cfg' file and modify
 2. Define partitions accordingly
 3. Confirm settings
 4. Publish the 'ks.cfg' file to HTTP server
 5. Install server using the following at the main menu:
  'linux ks=http://192.168.75.100/ks.cfg'

Note: The following can be used to boot a kickstart installation:
 1. boot.iso CD-ROM
 2. First CD-ROM of the RH5 installation set
 3. The DVD-ROM of the RH5 installation set
 4. USB Pen/Stick - diskboot.img (use dd)



###FTP INSTALLATION###

Steps:
 1. Create FTP user account on FTP server
  a. 'useradd -s /bin/false -d /srv/wwwlinuxcbt.com linuxinstall'
  b. 'passwd linuxinstall'
 2. Confirm FTP connectivity as the user 'linuxinstall'

 3. Reboot server with 'boot.iso' CD and type 'linux askmethod'

###BASIC LINUX COMMANDS###

1. tty - reveals the current terminal
2. whoami - reveals the currently logged-in user
3. which - reveals where in the search path a program is located
4. echo - prints to the screen
 a. echo $PATH - dumps the current path to STDOUT
 b. echo $PWD - dumps ths contents of the $PWD variable
 c. echo $OLDPWD - dumps the most recently visited directory

5. set - prints and optionally sets shell variables
6. clear - clears the screen or terminal
7. reset - resets the screen buffer
8. history - reveals your command history
 a. !690 - executes the 690th command in our history
 b. command history is maintained on a per-user basis via: 
  ~/.bash_history
~ = users's $HOME directory in the BASH shell
9. pwd - prints the working directory
10. cd - changes directory to desired directory
 a. 'cd ' with no options changes to the $HOME directory
 b. 'cd ~' changes to the $HOME directory
 c. 'cd /' changes to the root of the file system
 d. 'cd Desktop/' changes us to the relative directory 'Desktop'
 e. 'cd ..' changes us one-level up in the directory tree
 f. 'cd ../..' changes us two-levels up in the directory tree

11. Arrow keys (up and down) navigates through your command history
12. BASH supports tab completion: 
 a. type unique characters in the command and press 'Tab' key
13. You can copy and paste in GNOME terminal windows using:
  a. left button to block
  b. right button to paste OR Ctrl-Shift-v to paste

14. ls - lists files and directories
 a. ls / - lists the contents of the '/' mount point
 b. ls -l - lists the contents of a directory in long format:
 Includes: permissions, links, ownership, size, date, name
 c. ls -ld /etc - lists properties of the directory '/etc', NOT the contents of '/etc'
 d. ls -ltr - sorts chronologically from older to newer (bottom)
 e. ls --help - returns possible usage information
 f. ls -a - reveals hidden files. e.g. '.bash_history'
Note: files/directories prefixed with '.' are hidden. e.g. '.bash_history'

15. cat - catenates files
 a. cat 123.txt - dumps the contents of '123.txt' to STDOUT
 b. cat 123.txt 456.txt dumps both files to STDOUT
 c. cat 123.txt 456.txt > 123456.txt - creates new catenated file

16. mkdir - creates a new directory
 a. mkdir testRH5 - creates a 'testRH5' directory

17. cp - copies files
 a. cp 123.txt testRH5/
By default, 'cp' does NOT preserve the original modification time

 b. cp -v 456.txt testRH5/

18. mv - moves files
 a. mv 123456.txt testRH5/ - moves the file, preserving timestamp

19. rm - removes files/directories
 a. rm 123.txt
 b. rm -rf 456.txt - removes recursively and enforces

20. touch - creates blank file/updates timestamp
 a. touch test.txt - will create a zero-byte file, if it doesn't exist
 b. touch 123456.txt - will update the timestamp
 c. touch -t 200801091530 123456.txt - changes timestamp

21. stat - reveals statistics of files
 a. stat 123456.txt - reveals full attributes of the file

22. find - finds files using search patterns
 a. find / -name 'fstab'
Note: 'find' can search for fields returned by the 'stat' command

23. alias - returns/sets aliases for commands
 a. alias - dumps current aliases
 b. alias copy='cp -v'


###Linux Redirection & Pipes###
Features:
 1. Ability to control input and output

Input redirection '<':
 1. cat < 123.txt
Note: Use input redirection when program does NOT default to file as input

Output redirection '>':
 1. cat 123.txt > onetwothree.txt
Note: Default nature is to:
 1. Clobber the target file
 2. Populate with information from input stream


Append redirection '>>':
 1. cat 123.txt >> numbers.txt - creates 'numbers.txt' if it doesn't exist, or appends if it does

 2. cat 456.txt >> numbers.txt


Pipes '|':
Features: Connects the output stream of one command to the input stream of a subsequent command

 1. cat 123.txt | sort
 2. cat 456.txt 123.txt | sort
 3. cat 456.txt 123.txt | sort | grep 3


###Command Chaining###
Features:
 1. Permits the execution of multiple commands in sequence
 2. Also permits execution based on the success or failure of a previous command

 1. cat 123.txt ; ls -l - this runs first command, then second command without regards for exit status of the first command

 2. cat 123.txt && ls -l - this runs second command, if first command is successful
 3. cat 1234.txt && ls -l

 4. cat 123.txt || ls -l - this runs second command, if first command fails


24. more|less - paginators, which display text one-page @ a time
 1. more /etc/fstab
 2. less 1thousand.txt

25. seq - echoes a sequence of numbers
 a. seq 1000 > 1thousand.txt - creates a file with numbers 1-1000

26. su - switches users
 a. su - with no options attempts to log in as 'root'

27. head - displays opening lines of text files
 a. head /var/log/messages

28. tail - displays the closing lines of text files
 a. tail /var/log/messages

29. wc - counts words and optionally lines of text files
 a. wc -l /var/log/messages
 b. wc -l 123.txt

30. file - determines file type
 a. file /var/log/messages


###Tar, Gzip, Bzip2, Zip###
Features:
 1. Compression utilities (gzip, bzip2, zip)
 2. File rollers (the ability to represent many files as one)


Gzip:
Includes:
 1. gzip - compresses/decompresses files
 2. gunzip - decompresses gzip files

Tasks:
 1. compress '1million.txt' file using gzip
  a. gzip -c 1million.txt > 1million.txt.gz

Note: gzip auto-dumps to STDOUT, by default

  b. gzip -l 1million.txt.gz - returns status information
  c. gunzip 1million.txt.gz - dumps to file, and removes compressed version
  d. gzip -d 1million.txt.gz
  e. zcat 1million.txt.gz - dumps the contents to STDOUT
  f. less 1million.txt.gzip - dumps the contents of gzip files to STDOUT


Bzip2:

 1. bzip2 -c 1million.txt > 1million.txt.bz2

Note: Bzip2 tends to outperform gzip on larger files
 2. bunzip2 1million.txt.bz2
 3. bzip2 -d 1million.txt.bz2
 4. bzcat 1million.txt.bz2 - dumps contents to STDOUT
 5. less 1million.txt.bz2 - also dumps the contents to STDOUT


Zip & unzip:
 1. zip filename.zip path/ - general usage
 2. zip 1million.txt.zip 1million.txt
Note: zip differs slight from gzip and bzip2 in that the destination file (resultant zip file) is specified before the source
 3. unzip 1million.txt.zip


Tar & Gzip/Bzip2:

 1. tar -cvf filename.tar path/ - creates a non-compressed archive
 2. tar -cvf 1million.txt.tar 1million.txt
Note: tar, requires a small overhead for itself in each file

 3. tar -czvf 1million.txt.tar.gz 1million.txt - creates, tar/gzip document
 4. tar -cjvf 1million.txt.tar.bz2 1million.txt - creates, tar/bzip2 document
 5. tar -tzvf

 6. tar -cjvf 1million.txt.tar.bz2 1million.txt testRH5/- creates, tar/bzip2 document for the text file and 'testRH5' directory tree



###GREP###
Features:
 1. The ability to parse lines based on text and/or RegExes
 2. Post-processor
 3. Searches case-sensitively, by default
 4. Searches for the text anywhere on the line


1. grep 'linux' grep1.txt
2. grep -i 'linux' grep1.txt - case-insensitive search
3. grep '^linux' grep1.txt - uses '^' anchor to anchor searches at the beginning of lines
4. grep -i '^linux' grep1.txt
5. grep -i 'linux$' grep1.txt - uses '$' anchor to anchor searches at the end of lines

Note: Anchors are RegEx characters (meta-characters). They're used to match at the beginning and end of lines

6. grep '[0-9]' grep1.txt - returns lines containing at least 1 number
7. grep '[a-z]' grep1.txt


8. rpm -qa | grep grep - searches the package database for programs named 'grep'

9. rpm -qa | grep -i xorg | wc -l - returns the number of pacakges with 'xorg' in their names

10. grep sshd messages
11. grep -v sshd messages - performs and inverted search (all but 'sshd' entries will be returned)
12. grep -v sshd messages | grep -v gconfd
13. grep -C 2 sshd messages - returns 2 lines, above and below matching line

Note: Most, if not all, Linux programs log linearly, which means one line after another, from the earliest to the current

Note: Use single or double quotes to specify RegExes
Also, execute 'grep' using 'egrep' when RegExes are being used


###Awk###
Features:
 1. Field/Column processor
 2. Supports egrep-compatible (POSIX) RegExes
 3. Can return full lines like grep
 4. Awk runs 3 steps:
  a. BEGIN - optional 
  b. Body, where the main action(s) take place
  c. END - optional
 5. Multiple body actions can be executed by separating them using semicolons. e.g. '{ print $1; print $2 }'
 6. Awk, auto-loops through input stream, regardless of the source of the stream. e.g. STDIN, Pipe, File


Usage:
 1. awk '/optional_match/ { action }' file_name | Pipe
 2. awk '{ print $1 }' grep1.txt

Note: Use single quotes with awk, to avoid shell interpolation of awk's variables

 3. awk '{ print $1,$2 }' grep1.txt

Note: Default input and output field separators is whitespace

 4. awk '/linux/ { print } ' grep1.txt - this will print ALL lines containing 'linux'

 5. awk '{ if ($2 ~ /Linux/) print}' grep1.txt

 6. awk '{ if ($2 ~ /8/) print }' /var/log/messages - this will print the entire line for log items for the 8th

 7. awk '{ print $3 }' /var/log/messages | awk -F: '{ print $1}'


###Sed - Stream Editor###
Features:
 1. Faciliates automated text editing
 2. Supports RegExes (POSIX)
 3. Like Awk, supports scripting using '-F' option
 4. Supports input via: STDIN, pipe, file

Usage:
 1. sed [options] 'instruction[s]' file[s]
 2. sed -n '1p' grep1.txt - prints the first line of the file
 3. sed -n '1,5p' grep1.txt - prints the first 5 lines of the file
 4. sed -n '$p' grep1.txt - prints the last line of the file
 5. sed -n '1,3!p' grep1.txt - prints ALL but lines 1-3
 6. sed -n '/linux/p' grep1.txt - prints lines with 'linux'
 7. sed -e '/^$/d' grep1.txt - deletes blank lines from the document
 8. sed -e '/^$/d' grep1.txt > sed1.txt - deletes blank lines from the document 'grep1.txt' and creates 'sed1.txt'

 9. sed -ne 's/search/replace/p' sed1.txt
10. sed -ne 's/linux/unix/p' sed1.txt
11. sed -i.bak -e 's/3/4' sed1.txt - this backs up the original file and creates a new 'sed1.txt' with the modifications indicated in the command

Note: Generally, to create new files, use output redirection, instead of allowing sed to write to STDOUT

Note: Sed applies each instruction to each line


###Perl###
Features:
 1. Parses text
 2. Executes programs
 3. CGI - Web forms, etc.
 4. Supports RegExes (Perl and POSIX)
 5. etc.


Task:
 1. Print 'Hello World' to STDOUT
  a. perl -c helloworld.pl - checks the syntax of the script
  b. perl helloworld.pl - executes the script
  c. chmod +x helloworld.pl && ./helloworld.pl

 2. Parse RegExes from the command line



###System Utilities###
Features:
 1. Process listing
 2. Free/available memory
 3. Disk utilization


1. ps - process status/listing
 a. ps -ef or ps -aux

2. top - combines, ps, uptime, free and updates regulary

3. uptime - returns useful system utilization information:
 a. current time
 b. uptime - days, hours and minutes
 c. connected users
 d. load averaged - 1,5,15 minute values

4. free - returns memory utilization
 a. RAM
 b. SWAP
 free -m - for human readable format

5. df - returns disk partition/mount point information
 a. df - returns info. using kilobytes
 b. df -h - returns info. using megabytes/human readable (gigs/teray/etc.)

6. vmstat - reports on: processes, memory, paging, block I/O, traps, CPU activity

 a. vmstat
 b. vmstat -p /dev/hda1 - returns partitions stats for /dev/hda1 (/boot)

7. gnome-system-monitor - GUI, combining most system utilities
8. ls -ltr /proc
 a. cat /proc/cpuinfo

9. kill PID - kills the process with a given PID
10. runlevel - returns runlevel information using 2 fields:
 a. represents previous runlevel
 b. represents current runlevel


###User/Group Management###
Features:
 1. The ability to control users and groups

Primary tools:
 1. useradd - used to add users and modify group membership
 2. system-config-users

Task:
 1. Create a user named 'student1' using 'useradd'

Note: Default user settings derive from: /etc/login.defs
 a. useradd student1
 b. set password for user 'student1': passwd student1


Default User Accounts DB: /etc/passwd
student1:x:501:501::/home/student1:/bin/bash

username:shadow_reference:uid:gid:Description(GECOS):$HOME:$SHELL
Note: /etc/passwd is a world-readable file
Note: /etc/shadow now stores passwords in encrypted form
Note: /etc/shadow is NOT world-readable

Fields in /etc/shadow:
student1:$1$XSFMv2ru$lfTACjN.XxaxbHA0EkB4U0:13891:0:99999:7:::

1. username:
2. encrypted_password:
3. Days_since_Unix_epoch_password_was_changed (01/01/1970)
4. Days before password may be changed
5. Days after which the password MUST be changed
6. Days before password is to expire that user is warned
7. Days after password expires, that account is disabled
8. Days since Unix epoch, that account is disabled
9. Reserved field (currently unused)


 2. Modify user 'student1' to have password expire after 45 days
  a. usermod


Groups:
 1. groupadd - adds new group
 2. groups - lists groups on the system: /etc/group
/etc/group - maintains group membership information

Task: Create a 'sales' group and add 'linuxcbt' and 'student1' as members
 1. groupadd sales
 2. usermod -G sales linuxcbt
 3. usermod -G sales student1

Note: 2 types of groups exist:
 1. Primary - used by default for a user's permissions
 2. Supplemental - used to determine effective permissions

Note: use 'id' to determine the group information of user
Note: Create a new shell session to realize new group membership information

userdel/groupdel are used to delete users and groups, respectively


###File Types - Permissions - Symlinks###
Features:
 1. The ability to restrict/control access to files

Note: 10 bits represent permissions for files (including directories)

Note: use 'ls -l' to examine permissions or GUI application like 'Nautilus'

-rwxrwxr-x 1 linuxcbt linuxcbt  681 Jan 13 11:31 regextest.pl

1st bit = file type. '-' = file, 'd' = directory
2nd - 4th bits = owner's permissions
r = read = 4
w = write = 2
x = execute = 1
- = none = 0

5th - 7th bits = group owner's permissions
r = read = 4
w = write = 2
x = execute = 1
- = none = 0

8th - 10th bits = everyone (world)
r = read = 4
w = write = 2
x = execute = 1
- = none = 0

Task:
 1. Manipulate file permissions using 'chmod'
  a. chmod -x regextest.pl

-rw-rw-r-- 1 linuxcbt linuxcbt 681 Jan 13 11:31 regextest.pl
rw = 6 or 4+2 for owner
rw = 6 or 4+2 for group owner
r = 4 for everyone else (world)

Octal notation: 664 for file 'regexetest.pl'

chmod 664 regextest.pl - removes execution for ALL users
chmod 775 regextest.pl - enables execution for ALL users


 2. Ensure that 'regextest.pl' is rw by owner and noone else
 a. chmod 600 regextest.pl

Note: File will now be rw by owner (linuxcbt) and 'root'

 3. Ensure that 'regextest.pl' is r by owner and noone else
 a. chmod 400 regextest.pl && ls -l regextest.pl

Note: chmod supports string values, which represent octal values
chmod +/- x file
chmod +/- w file
chmod +/- r file

chmod +/- u+x file - updates owner's execute permissions on the file
chmod +/- o+x file - updates other's execute permissions on the file
chmod +/- g+x file - updates group's execute permissions on the file

chmod a+rwx = chmod 777


chown - permits changing of ownership of files
 a. chown root regextest.pl - changes ownership to 'root'
 b. chown linuxcbt:sales regextest.pl - changes owner and group to 'linuxcbt:sales'

Task:
 Update 'regextest.pl' so that owner and group owner may modify the file

 a. chmod 660 regextest.pl


SETUID:
 Features:
  1. ability to execute file as owner

chmod 4760 regextest.pl - this will ensure that the perl script always executes as the user 'linuxcbt'
-rwsrw---- 1 linuxcbt sales 787 Jan 13 16:08 regextest.pl

's' in the execute position means that the program will execute as that user


SETGID:
 Features:
  1. Ability to enforce permissions to a directory structure

mkdir /sales
chmod 2775 /sales

Create a file in the '/sales' directory as 'linuxcbt'
seq 1000000 > linuxcbt.1million.txt


chgrp:
 Permits updating of group permissions


Sticky Bit:
 Features:
  1. Ability to ensure that users cannot delete others' files in a directory

drwxrwxrwt 23 root root 4096 Jan 13 15:05 /tmp/


/tmp - users cannot delete other user's files in '/tmp'

chmod 3777 /sales - ensures that /sales will not lose files from incorrect users

Task:
 1. Set '/sales' using sticky bit and test
  a. chmod 3777 /sales && ls -ld /sales OR chmod 777 /sales && chmod +t /sales


###Symlinks###
Features:
 1. Provides shortcuts to files (including directories)
 2. Provides hard links to inode (file system) locations

Soft Links:
 1. ln -s source_file target
  a. ln -s ./regextest.pl lastscript.pl

Note: Soft links may span multiple file systems/hard drives
Note: Symlink count is NOT increased when using soft links

 2.  ln -s /home/linuxcbt/testRH5/regextest.pl . - this will symlink (soft) to the /boot file system

Note: With soft links, if you change the name or location of the source file, you will break ALL of the symlinks (soft)


Hard Links:
 Features:
  1. The ability to reference the same inode/hard drive location from multiple places within the same file system
   a. ln source target
      ln regextest.pl ./testhardregextest.pl - creates a hard link



###Quotas###
 Features:
  1. Limits disk usage (blocks or inodes)
  2. Tied to file systems (set on a per file system basis)
  3. Can be configured for users and groups

Steps to enable quota support:
 1. Enable quota support per file system in: /etc/fstab
  a. defaults,usrquota,grpquota
 2. Remount the file system(s)
  a. mount -o remount /
  b. use 'mount' to confirm that 'usrquota,grpquota' support are enabled
 3. Create quota database files and generate disk usage table
  a. quotacheck -mcug / - this creates /aquota.user & /aquota.group
  b. quotacheck -mavug
 4. Assign quota policies
  a. edquota username - set blocks/inodes soft_limits hard_limit
     edquota student1 - sets quotas for user 'student1'
     export EDITOR=nano - to have edquota default to 'nano' editor 
5. Check quotas
  a. quota username
     quota student1

Note: place 'quotacheck -avug' in /etc/cron.*(hourly,daily)

6. Report on usage
  a. repquota -a - this reports on usage

Note: The blocks are measured in 1K increments. i.e. 20000 blocks is roughly 20MB


###Basic Provisioning of Partitions and File Systems###
 Features:
  1. Ability to provision extra storage on-the-fly

Steps:
 1. Identify available storage
  a. 'fdisk -l' - returns connected storage

 2. Create partitions on desired hard drive:
  a. 'fdisk /dev/sdb' - interacts with /dev/sdb drive
  b. 'n' - to add a new partition
  c. 'p' - primary
  d. '1' - start cylinder
  e. '+4096M' - to indicate 4 Gigabytes
  f. 'w' - to write the changes to the disk

Note: use 'partprobe partition (/dev/sdb1)' to force a write to a hard drive's partition table on a running system

Note: 'fdisk' creates raw partitions

 3. Overlay (format) the raw partition with a file system
  a. mke2fs -j /dev/sdb1 - this will write inodes to partition

 4. Mount the file system in the Linux file system hierarchy:
  a. mkdir /home1 && mount /dev/sdb1 /home1
  b. mount OR df -h - either will reveal that /dev/sdb1 is mounted

Note: lost+found directory is created for each distinct file system

 5. Configure '/home1' to auto-mount when the system boots
  a. nano /etc/fstab and copy and modify the '/home' entry

###Swap Partitions & Files###
 Features:
  1. Extra, virtual RAM for the OS


Steps:
 1. Identify current swap space
  a. swapon -s - enumerates partitions and/or files, which constitute swap storage

  b. free -m

 2. Select target drive and provision swap partition
  a. fdisk /dev/sdb
  b. n
  c. 2
  d. 500
  e. +512 (cylinder 562) - 63 cylinders are required for 512MB
  f. t - change type
  g. 82 - Linux Swap/Solaris
  h. w - committ changes to disk

 3. Create the swap file system on the raw partition: /dev/sdb2
  a. mkswap /dev/sdb2

 4. Enable swapping - publish the swap space to the kernel
  a. swapon /dev/sdb2 - this enables swapping on /dev/sdb2

 5. update /etc/fstab
  a. /dev/sdb2 swap swap defaults 0 0

swapoff /dev/sdb2 - disables swapping on /dev/sdb2

Task:
 1. Improve system performance by distributing swapping to /dev/sdb2
  a. swapon /dev/sdb2
  b. swapoff /dev/sda6
  c. disable /dev/sda6 via /etc/fstab


###Create Swap based on File###
 Features:
  1. The ability to provision swap space based on a file, similar to pagefile.sys in Windows NT, etc., if you have no available disk space to partition.

  2. Doesn't waste partitions


Task:
 1. Create 512MB swap file
  a. dd if=/dev/zero of=/home1/swapfile1 bs=1024 count=524288
  b. mkswap /home1/swapfile1 - overlays swap file system
  c. swapon /home1/swapfile1 - makes swap space avaialable to the kernel

 2. Ensure that when the system reboots, the swapfile is made avialable to the kernel
  a. nano /etc/fstab - /home1/swapfile1 swap swap defaults 0 0


 3. Create 2GB swap file
  a. dd if=/dev/zero of=/home1/swapfile2 count=2G


###Logical Volume Management (LVM)###
 Features:
  1. Ability to create volume sets and stripe sets
  2. LVM masks the underlying physical technology (ATA,ATAPI,IDE,SCSI,SATA,PATA,etc.)
  3. LVM represents storage using a hierarchy:
   a. Volume groups
    a1. Physical volumes (/dev/sda2, /dev/sdb2, etc.)
   b. Logical Volumes
    b1. File systems
  3. LVM physical volumes can be of various sizes
  4. Ability to resize volumes on the fly

Note: Volume groups join: physical volumes (PVs) and Logical Volumes (LVs)


6 Steps to setup LVM:
 1. Create LVM partitions via fdisk or parted
  a. fdisk /dev/sda, /dev/sdb, /dev/sdc
  b. n
  c. p
  d. +10G
  e. t - change to type '8e' (LVM)
  f. w
  g. partprobe /dev/sda

 2. Create Physical Volumes using 'pvcreate'
  a. pvcreate /dev/sda3 /dev/sdb3 /dev/sdc3

 3. Create Volume Groups using 'vgcreate'
  a. vgcreate volgroup001 /dev/sda3 /dev/sdb3 /dev/sdc3
Note: Volume groups can be segmented into multiple logical volumes

 4. Create one or more Logical Volumes
  a. lvcreate -L 10GB -n logvolvar1 volgroup001
  b. lvcreate -L 10GB -n logvolusr1 volgroup001

 5. Create File system on logical volume(s)
  a. mke2fs -j /dev/volgroup001/logvolvar1
  b. mke2fs -j /dev/volgroup001/logvolusr1

 6. Mount logical volume
  a. mkdir /var1
  b. mount /dev/volgroup001/logvolvar1 /var1
  c. mkdir /usr1
  d. mount /dev/volgroup001/logvolusr1 /usr1


Note: Be certain to update: /etc/fstab so that volumes are mounted when the system reboots

3-tiers of LVM display commands include:
 a. pvdisplay - physical volumes - represent raw LVM partitions
 b. vgdisplay - volume groups - aggregate physical volumes
 c. lvdisplay - logical volumes - file systems - mount here


Rename of Logical Volume:
 1. lvrename volume_group_name old new - used to rename volumes

Task: Rename 'logvolvar1' to 'logvolopt1'
  a. lvrename volgroup001 logvolvar1 logvolopt1
Note: LVM is updated immediately, even while volume is mounted
However, you must remount the logical volume to see the changes
  b. umount /var1 && mount /dev/mapper/volgroup001-logvolopt1 /opt1
  c. Update /etc/fstab


Remove Logical Volume:
Task: Remove 'logvolusr1' from the logical volume pool
 a. umount /usr1
 b. lvremove /dev/mapper/volgroup001-logvolusr1
 c. use 'lvdisplay' to confirm removal


Resize Logical Volume:
Task: Grow (resize) 'logvolopt1' to 20GB
 a. lvresize -L 20GB /dev/volgroup001/logvolopt1
 b. lvdisplay - to confirm new size of logical volume
 c. df -h - will still reveal the current size
 d. Resize the file system to update the INODE table on the logical volume to account for the new storage in 'logvolopt1'
  'resize2fs -f -p /dev/volgroup001/logvolopt1'

Note: You may resize file systems online if the following are met:
  1. 2.6x kernel series
  2. MUST be formatted with ext3

Task: Shrink (resize) 'logvolopt1' to 15GB
 a. lvresize -L 15GB /dev/volgroup001/logvolopt1
 b. lvdisplay 
 c. df -h 
 d. resize2fs -f -p /dev/volgroup001/logvolopt1
 Note: online shrinking is not supported
 e. df -h

Note: Check disk utilization prior to shrinking to reduce the risk of losing data

LVM GUI Utility:
system-config-lvm







###RAID###
Features:
 1. The ability to increase availability and reliability of data


Tasks:
 1. Create a RAID-1 Device (/dev/md0..n)
  a. fdisk /dev/sdb - to create usable raw partitions
  b. partprobe /dev/sdb - to force a kernel update of the partition layout of the disk: /dev/sdb
  b. mdadm --create /dev/md0 --level=1 --raid-devices=2 /dev/sdb5 /dev/sdb6
  c. cat /proc/mdstat - lists active RAID (md) information
  d. mke2fs -j /dev/md0 - overlays a file system on the RAID device
  e. mount /dev/md0 /raid1
  f. update: /etc/fstab

Note: use 'mdadm --query /dev/md0' to get information about a RAID device


Note: You may create RAID volumes/devices on a single or on multiple disks
Ideally, your RAID volumes should span multiple physical disks to improve:
 a. reliability
 b. performance
 c. availability

 2. Remove the RAID-1 device
 a. umount /dev/md0
 b. mdadm --manage --stop /dev/md0

 3. Create a RAID-5 Volume
 a. fdisk /dev/sdb - to create a partition number 7
 b. partprobe /dev/sdb - to update the kernel's view of the partition table
 c. mdadm --create /dev/md0 --level=5 --raid-devices=3 /dev/sdb5 /dev/sdb6 /dev/sdb7
 d. watch cat /proc/mdstat - refreshes every 2 seconds
 e. Overlay a file system: mke2fs -j /dev/md0
 f. mount /dev/md0 /raid5
 g. Test I/O to RAID-5 device
 h. Update: /etc/fstab













###RPM###
 Features:
  1. Provides package management
   a. Query
   b. Install
   c. Uninstall
   d. Upgrade
   e. Verify
  2. Auto-verifies packages using GPG, MD5, SHA1SUMs
  3. Automatically reports on unresolved dependencies

'rpm'

Query:
  1. rpm -qa - dumps all installed packages
  2. rpm -qa | wc -l - this dumps all packages and provides a count
  3. rpm -qa | grep -i nano
  4. rpm -qi nano - dumps info. about the 'nano' package as it's recorded in the local RPM database
  5. rpm -qf /usr/bin/nano - dumps package membership info. for the 'nano' file
  6. rpm -qpi http://192.168.75.100/RH5/i386/Server/dhcp-3.0.5-7.el5.i386.rpm - dumps info. about the uninstalled 'dhcp' package, which resides on the repository
  7. rpm -ql package_name - returns all included files


Verify:
  1. rpm -Va - verifies ALL packages on the system, returning info. only if there are discrepancies from the original installation

  2. rpm -Vf /usr/bin/nano

Task: Change '/usr/bin/nano' then verify

SM5....T   /usr/bin/nano

S(file size), M(mode or permissions), 5(MD5), T(mod time)
  3. rpm -Vp nano


Install (Does NOT overwrite previous package):
Note: Use this method to install a new version of the kernel
  1. rpm -ivh *.rpm
  2. rpm -ivh http://192.168.75.100/RH5/i386/Server/dhcp-3.0.5-7.el5.i386.rpm



Upgrade (Installs or overwrites existing package):
  1. rpm -Uvh *.rpm
  2. rpm -Uvh http://192.168.75.100/RH5/i386/Server/dhcp-3.0.5-7.el5.i386.rpm

Freshen (Updates an existing package):
Note: Will NOT install the package, if it doesn't exist locally

  1. rpm -Fvh *.rpm - freshens the current version of a package


Removal:
 1. rpm -ev *.rpm - removes a pacakge
Note: removal process considers dependencies and will complain if the removal will break 1 or more packages. To get around this, use '--nodeps' option with 'rpm -ev --nodeps *.rpm'

 2. rpm -ev gftp


Package Management GUI:
 1. Add/Remove Software
 2. system-config-packages


###YUM Configuration###
 Features:
  1. The ability to centralize packages (updates)

Installation & Setup:
  1. Install 'createrepo*rpm'
  2. Setup directory structure
   a. /srv/www/linuxcbt.com/RH5/yum

  3. Run 'createrepo /srv/www/linuxcbt.com/RH5/yum'

  4. Publish the yum repository using HTTP

  5. Configure yum client to use HTTP to fetch the RPMs
   a. /etc/yum.conf
    a1. ###Included as our first repository on the SUSE box###
[0001]
name=linuxcbtsuse1
baseurl=http://192.168.75.100/RH5/yum

Note: Ensure that about 3GBs are available for the yum respository


tar -cjvf yum_metadata.bz2 repodata

Yum Usage:
 1. Search for packages
  a. 'yum search gftp'

 2. Install packages - Requires RedHat GPG Key for RPMs
rpm --import http://192.168.75.100/RH5/i386/RPM-GPG-KEY-redhat-release
  a. 'yum -y install gftp'
  b. 'yum -y install gftp dhcp' installs 2 packages

 3. Remove Package
  a. 'yum -y remove gftp'


###Cron - Scheduler###
 Features:
  1. Scheduler
  2. Rules (Cron entries) are based on times:
   a. minute (0-59)
   b. hour (0-23)
   c. day of the month (1-31)
   d. month (1-12)
   e. day of the week (Sun,Mon,Tue, etc. OR 0-7)
   f. command to execute (shell, perl, php, etc.)
 3. Wakes up every minute in search of programs to execute
 4. Reads cron entries from multiple files
 5. Maintains per-user and system-wide (/etc/crontab) schedules

/etc:
cron.d/       
cron.deny - denies cron execution by user
cron.monthly/ - runs jobs monthly
cron.weekly/ - runs jobs weekly  
cron.daily/ - runs jobs daily
cron.hourly/ - runs jobs hourly
crontab - contains system-wide schedules

Note: '*' wildcard in a time column means to run for all values

Per-user Crontabs:
Stored in: /var/spool/cron

Task: 
  1. Create a cron entry for the user 'student1'
   a. su student1
   b. crontab -e
   c. create an entry, minus the name of the user

Note: 'crontab -l' - enumerates per-user cron entries


System-wide Crontab:
Stored in: /etc/crontab

Task:
  1. Create a cron entry in: /etc/crontab

Note: 'crontab -l -u username' - enumerates per-user cron entries


###SysLogD###
 Features:
  1. Handles logging
  2. Unix Domain Sockets (/dev/log)
  3. Internet Sockets (UDP:514)
  4. Ability to log to local and remote targets

Implented as 'sysklogd' package


Primary configuration file: /etc/syslog.conf

Standard syslog.conf file contains:
 1. Rules
  a.facilities -> applications/daemons/network device/etc.
  b. levels -> Importance of message
   Range: 0-7
   7 = emergency (less information)
   6 = alert
   5 = critical
   4 = error
   3 = warning
   2 = notice
   1 = info
   0 = debug (more information)

 2. Targets
  a. file - /var/log/messages
  b. tty - /dev/console
  c. remote hosts - @IP_ADDR_of_REMOTE_HOST

'*' = catchall/wildcard to mean any facility or level
'.none' = exclusion rule


'man syslog.conf' to learn about the support facilities.levels

Task:
 1. Enable UDP logging for remote Cisco gateway (192.168.75.1)
  a. netstat -nul | grep 514 - reveals UDP:514 listener
  b. nano /etc/sysconfig/syslog
   b1. 'SYSLOGD_OPTIONS="-r"' 
  c. restart syslog and confirm UDP:514 listener
   c1. confirm using 'netstat -nul | grep 514'
  d. Configure the router using facility 'local0' and level 'info'
  e. configure /etc/syslog.conf to accept 'local0.info'
  f. restart or reload 'syslog' 



###Log Rotation###
 Features:
  1. Rotation of logs based on criteria
   a. size
   b. age (daily, weekly, monthly)

  2. Compression
  3. Maintain logs for a defined period


/etc/logrotate.conf - primary (global) config file for all logs
 -can be overriden by context-sensitive files. i.e. apache
 run 'man logrotate' 

/etc/logrotate.d - directory for logs to be rotated
 -httpd - used to rotate Apache logs

/var/log/httpd/*log {
    missingok
    notifempty
    sharedscripts
    postrotate
        /bin/kill -HUP `cat /var/run/httpd.pid 2>/dev/null` 2> /dev/null || true
    endscript
}


Task: Setup rotation rule for Cisco log
 1. Create entry in: /etc/logrotate.d based on /etc/logrotate.d/syslog

 2. Modified the entry to rotate based on new criteria
 3. Rotated using: 'logrotate /etc/logrotate.conf'
Note: Force using: 'logrotatate -f /etc/logrotate.conf'



###Commong Network Utilities###
 Features:
  1. Useful for basic troubleshooting


PING:
 Features:
  1. ability to communicate with hosts using ICMP
   a. PING sends ICMP echo-requests
   b. PING expects to receive ICMP echo-replies

Task: PING some hosts and evaluate the output
  1. ping localhost (127.0.0.1)
  2. ping -c 3 localhost - sends 3 ICMP echo-requests
Note: 'ping localhost' performs name resolution using /etc/hosts
/etc/hosts stores static name-to-IP mappings

Note: 127.0.0.0/8 is fully-reserved to the loopback adapter of ALL IPv4 hosts

  3. ping -c 3 192.168.75.199
  4. ping -c 3 -i 3 192.168.75.199 - delays PINGs to 3 seconds apart

Note: PING defaults to a standard 1-second interval
Note: Firewall(s) may block ICMP traffic, causing PING to fail

TELNET:
 Features:
  1. Great for basic TCP port diagnosis

Task:
  1. Connect to TCP ports on various hosts
   a. telnet 192.168.75.100 22
   b. telnet www.linuxcbt.com 80

NETSTAT:
 Features:
  1. Provides network connection information from /proc/net/*

Task:
  1. Return useful information for various protocols
   a. netstat
   b. netstat -a - returns all protocols/sockets
   c. netstat -ntlp - returns all TCP LISTENERS without name resolution
   d. netstat -nulp - returns all UDP lISTENERS without name resolution

Note: netstat uses /etc/services to translate ports to names
Note: 0.0.0.0:514 - this means that Syslog will accept traffic to any of the defined IP addresses/interfaces on the system

   e. netstat -ntp - returns established connections (sockets)
   f. netstat -rn - returns the routing table


ARP:
 Features:
  1. Resolves layer-2 (OSI model) MAC addresses to layer-3 IP addresses


Task:
 1. Examine MAC addresses using: ifconfig and arp
  a. ifconfig - returns our local MAC addresses
   Link encap:Ethernet  HWaddr 00:02:B3:98:41:08
  b. arp -a - returns MAC to IP mappings

Note: When 2 TCP/IP hosts communicate, ARP is performed to translate the IP address (v6/v4) to a MAC address.

Note: If a one or more routers separate the communicating hosts, then the MAC address of the default router's (gateway's) interface is stored by each client


###IPv4 Configuration & Network Settings###

Network Support:
  1. Boot system into a multi-user mode
  2. /etc/modprobe.conf - contains alias and reference to module(s) to be loaded in order to provide networking
  3. Linux decides if the interface is DHCP or static by viewing the contents of: 
   a. /etc/sysconfig/network - networking=yes|no, IPv6_Support, Default Gateway, etc.
   b. /etc/sysconfig/network-scripts/ifcfg-eth0 - contains ifup, ifdown, and ifcfg-* scripts
   c. /etc/init.d/network - main service

service network status - checks networking

system-config-network-* - network interface configuration

Note: Either update your net configuration manually from the shell, or using the 'system-config-network*' tools to avoid losing settings


/etc/resolv.conf - DNS configuration file
/etc/hosts - static list of hosts

IPv4 Aliases:
 1. ifconfig eth0:1 192.168.75.11
 2. ifconfig eth0:2 10.168.76.11

Note: To ensure that aliases persist do the following:
 1. cp /etc/sysconfig/network-scripts/ifcfg-eth0 ./ifcfg-eth0:1
 2. Modify ifcfg-eth0:1 to reflect aliased IP

Note: Aliases do NOT work with DHCP interfaces

ifconfig eth0:2 del 10.168.76.11 - removes the virtual interface

IPv6 Config:
 Features:
  1. Auto-configured by default gateway (router)
  2. fe80:: - link-local address (loopback/local subnet address)
  3. 2002:: - 6to4 address, that can be configured based on IPv4 embedded address, using HEX notation

ping6 -I eth0 fe80::
traceroute6 - used to trace routes on IPv6 networks


###Kernel Upgrade###
 Features:
  1. Provision of updated/patched kernel

Task:
 1. Update the kernel
  a. use 'uname -a' to reveal current version
  b. use 'rpm -qa | grep -i kernel' - to reveal installed version
  c. cat /etc/grub.conf -> /boot/grub/grub.conf - "" ""

 2. Proper installation method is as follows:
  a. 'rpm -ivh kernel*rpm' - install a separate version

Note: Install the following kernel packages if necessary:
  a. kernel-devel* - if module compilation is necessary
  b. kernel-headers* - if recompilation is necessary


Install:
  a. rpm -ivh kernel-2.6.18-53.el5.i686.rpm  
Note: This will update GRUB (/boot/grub/grub.conf)
Note: Will also place the new kernel in the /boot file system

Examine traces in:
 a. /boot
 b. /boot/grub/grub.conf

3. Remove traces of former kernel using 'rpm -e [--nodeps]'
 a. kernel-2.6.18-8.el5 - removes older version
 b. kernel-headers-2.6.18-8.el5 - force remove ignoring dependencies 'rpm -e --nodeps kernel-headers-2.6.18-8.el5'
 c. kernel-devel-2.6.18-8.el5

4. Install new 'kernel-headers' and 'kernel-devel' packages using YUM:
 a. yum -y install kernel-headers
 b. yum -y install kernel-devel

5. Confirm that the 3 'kernel-*' packages are installed:
 a. rpm -qa | grep kernel

Note: Removal of older kernel-* packages cleans up:
 a. /boot
 b. /boot/grub/grub.conf (menu.lst)



###Runlevel Service Management Tools###
 Features:
  1. The ability to indicate desired runlevels for services
  2. Services are located in: /etc/init.d

/usr/sbin/ntsysv:

Usage:
 1. ntsysv - manages services in the current run-level
 2. ntsysv 35 - manages services for run-levels 3 & 5

Note: ntsysv nor chkconfig starts|stops services

Chkconfig Usage:
 1. chkconfig --list ntpd - returns run-level environment for 'ntpd'
Note: items listed as 'off' have K (kill) scripts
Note: items listed as 'on' have S (start) scripts

 2. chkconfig --level 3 ntpd off - creates a K(kill) script in run-level 3

 3. chkconfig --level 35 ntpd off
 4. chkconfig ntpd on - enables 'ntpd' in levels 2-5
 5. chkconfig ntpd off - disables 'ntpd' in levels 0-6


Note: Use 'chkconfig' from the shell or a script
Note: Use 'ntsysv' from the shell in interactive mode

Note: When controlling services using 'chkconfig', reference the name of the service as it's specified in: /etc/init.d

system-config-services - GUI tool to manage services


###Network Time Protocol (NTP) Implementation###
Features:
 1. The ability to synch your system's clock
 2. Also can be used to synch other clocks
 3. Implemented as: 'ntp-4.2...rpm' package
 4. Is hierarchial, using strata levels to denote time accuracy

/etc/ntp.conf - primary configuration

NTP Strata:
Features:
 1. The ability to denote clock accuracy based on on stratum
 2. With Stratum level 1 being the most accurate, as an NTP server at this level is connected to an external time service (GPS, Radio, etc.)

Use: www.ntp.org - to located public NTP clocks at various strata

Task:
 1. Synch against internal NTP server
  a. /etc/ntp.conf
   a1. server 192.168.75.100
  b. service ntpd start - this starts the 'ntpd' service
  c. chkconfig ntpd on
  d. ntpq -np - this queries the running 'ntpd' server

Note: NTP synchronization is hierarchical. Thus, if we synch against a stratum 3 clock, we become a stratum 4 clock

 2. Prove that 'linuxcbtserv4' is indeed a stratum 4 clock
  a. /etc/ntp.conf - of 'linuxcbtserv1'
   a1. server 192.168.75.199

Note: Ideally, you should supply your: /etc/ntp.conf file with at least 3 clocks for:
 1. Accuracy
 2. Redundancy



###Trivial File Transfer Protocol Daemon (TFTPD)###
Features:
 1. Fast, connectionless (UDP), file transfers
 2. Often used to move files to and fro networked systems (VOIP Phones, PXE configurations, Router/Firewall/Switch configurations, etc.)

Note: Implemented as 2 components:
 a. Client - tftp-*rpm
 b. Server - tftp-server*

Tasks:
 1. Install TFTP client
  a. yum -y install tftp
 2. Install TFTP server
  a. yum -y install tftp-server
Note: this also install 'xinetd' dependency

 3. Configure and start 'tftp' via 'xinetd'
  a. /etc/xinetd.d/tftp - modify this file prior to starting 'TFTPD'
  b. service xinetd start - to start XINETD
Note: TFTPD listens to UDP:69, by default
Note: use 'netstat -nulp | grep 69' to check if 'xinetd' is listening

 4. Copy Cisco Router configuration to TFTP server
  a. copy running-config tftp://192.168.75.199
  b. setsebool -P tftpd_disable_trans=1 - disables SELinux for TFTPD
  c. 'service xinetd restart' - restart XINETD
  d. 'chmod 666 linuxcbtrouter1.config' - to permit TFTPD to write

 5. Use 'tftp' client to download 'linuxcbtrouter1.config' file
  a. tftp 192.168.75.199 -c get linuxcbtrouter1.config
  b. tftp - enters interactive mode

Note: tftp client operates in both non-interactive and interactive modes


###Very Secure File Transfer Protocol Daemon (VSFTPD)###
Features:
 1. FTPD
 2. Chroot jail
 3. anonymous and local-user auth
 4. Rate-limiting

Tasks:
 1. Install 'vsftpd'
  a. yum -y install vsftpd

 2. Start the server
  a. service vsftpd start
  b. netstat -ntlp | grep 21

 3. Configure service to start when system boots into multi-user runlevel
  a. chkconfig vsftpd on
  b. chkconfig --list vsftpd

 4. Connect to the FTPD service:
  a. Use web browser, which defaults to anonymous
  b. Use standard FTP client, as anonymous
  c. setsebool -P ftp_home_dir=1 - permits users access to their home directory
  d. service vsftpd restart - for changes to take effect

 5. Chroot jail local users & disable 'anonymous' access
  a. chroot_local_user=YES - this jails users
  b. service vsftpd restart - for changes to take effect
  c. test connectivity as 'anonymous' and 'non-anonymous' users

 6. Enable IPv6 listener:
  a. listen_ipv6=YES - DO NOT USE WITH 'listen=YES(IPv4)'


 7. Restrict 'non-anonymous' user's transfer rate
  a. local_max_rate=1000 - restricts connections to 1000/bps (1K/s)


###LFTP###
Features:
 1. Sophisticated FTP client
 2. Provides connectivity:
  a. FTP
  b. HTTP/HTTPS
  c. SFTP(SSHv2)
 3. Interactive and non-interactive client
 4. Supports scripting
 5. Reads system-wide (/etc/lftp.conf) and per-user config files (~/.lftprc)
 6. Behaves like the BASH shell
  a. Command history
  b. Permits execution of background jobs. Use CTRL-Z to background.
  c. Tab completion
 7. Supports mirroring (forward and reverse) of content
 8. Supports FTP retransmit/reconnect from where you left off
 9. Supports bookmarks of sites
10. Supports escape to shell using '!command' e.g. '!bash'
11. Supports the execution of BASH programs '!command' e.g. '!ps -ef'



Usage:
 1. lftp - enters interactive mode
  a. 'set -a' - reveals all variables

 2. lftp linuxcbt@192.168.75.199

 3. mget -c - continues downloads

 4. mput -c - continues uploads

 5. lftp -u linuxcbt,abc123 sftp://192.168.75.199 - Connects to SFTP server

 6. mirror -v mirror/ - mirrors a remote directory named 'mirror' to the local system

 7. mirror -Rv mirror/ - Reverse mirror (puts) - items to remote server



###Telnet Server###
Features:
 1. Shell interface on remote system
 2. Binds to TCP:23

Caveat:
 1. Clear-text based application (credentials are transmitted in the clear)
 2. By default, 'root' is NOT permitted access via telnet-server - /etc/securetty

Requirements:
 1. xinetd - installed automatically via yum

Install Telnet Server:
 1. yum -y install telnet-server
 2. nano /etc/xinetd.d/telnet - change 'disable = yes' to 'disable = no'
 3. service xinetd restart - effects changes

Tasks:
 1. Connect to both systems from either system using 'telnet' client
  a. telnet 192.168.75.199 - This will allocate a free pseudo-terminal, if the user authenticates successfully

Note: By default, telnet-server reads and dislplays the contents of: /etc/issue

Note: TCP|UDP ports are 16-bit based: 2**16, OR, 0-65535

Note: ptys are assigned sequentially, by default

 2. Enable 'root' login via telnet
  a. mv /etc/securetty /etc/securetty.disabled

Note: Wherever/whenever possible opt for SSH in place of Telnet Server



###Dynamic Host Configuration Protocol Daemon###
Features:
 1. Provides automatic configuration of IPv4 clients
  a. IPv4 address
  b. Subnet mask
  c. Default gateway
  d. DNS Servers
  e. NTP Servers
  f. WINS Servers

 2. Leases the addreses and related information based on predefined values:
  a. 1 day
  b. 1 week
  c. 1 month


 3. DHCP uses UDP protocol and layer-2 information to request/assign addresses

 4. DHCP Process - DORA
  a. Discovery - client broadcasts on the local subnet for a DHCP server
  b. Offer - returned by the DHCP server
  c. Request - formal address request by client
  d. Acknowledgement/Acceptance - Acknowledgement occurrs

Note: DHCPD records leases in: /var/lib/dhcpd/dhcpd.leases

Tasks:
 1. Install DHCP server
  a. yum -y install dhcp

 2. Configure: /etc/dhcpd.conf - primary config file

 3. Set service up to start when system boots
  a. chkconfig dhcpd on - 2345

 4. Disable service on 192.168.75.100 box
  a. rcdhcpd stop

 5. Start service on localhost:
  a. service dhcpd start

 6. Setup DHCP reservation
  a. Requires the MAC address of the client (00:0C:29:B5:16:92)
  b. Requires the 'fixed-address' - IPv4 address to map to the MAC address
  c. Optional 'option-*' are supported between host { } block
  d. service dhcpd restart - restart to effect changes

###BIND DNS###
Features:
 1. Name-to-IP address mapping
 2. Name resolution for DNS clients
 3. Caching-only server (Default)
 4. Primary DNS server
 5. Slave server
 6. Replication of DNS database information between servers
 7. Dynamic DNS updates
 8. Provides numerous client tools: nslookup, dig, host

Tasks:
 1. Installation of BIND on the remote system: linuxcbtserv4
  a. yum -y install bind

 2. Setup service to auto-start at boot
  a. chkconfig --level 35 named on - enables the service in runlevels: 3,5

 3. Configure a default, caching-only, named.conf file
  a. rpm -ql bind - to see samples
  b. cp /usr/share/doc/bind*/sample/* to /etc/ and /var/named
  c. Modify /etc/named.conf - disable DDNS_KeyGen sections
  d. Start the server - service named start
  
 4. Query the server
  a. dig @localhost www.linuxcbt.com
   a1. Returns: question, answer, authoritative DNS servers, query time
  b. nslookup www.linuxcbt.com OR nslookup - server 127.0.0.1 - www.linuxcbt.com

Note: The server has cached: www.linuxcbt.com, evidenced by the decrementing TTL values for the various records associated with the zone

  c. host www.linuxcbt.com - also performs a lookup

Note: /etc/resolv.conf controls the DNS servers that are consulted by lookup tools such as: Web browser, GFTP, LFTP, nslookup, dig, host, etc.

  d. dig linuxcbt.com MX - queries the domain for mail exchangers

Note: DNS is organized into an inverted tree, with '.' representing the root of the DNS tree. e.g.

dig mail1.linuxgenius.com.
 - . = root
  - .com = top level
   - .linuxgenius = second level
      -mail = third level
Note: A trailing '.' in a DNS query is implied, and may optionally be indicated if desired in any standard Internet application (web browser, FTP client, wget, nslookup, dig, host, etc.)


Primary & Secondary Zones:
 Features:
  1. Ability to service zones
  2. Authoritative support for a zone

Tasks:
 1. Create internal zone named 'linuxcbt.internal'
  a. modify /etc/named.conf to include the new zone

zone "linuxcbt.internal" {
                type master;
                #allow-update { key ddns_key; };
                file "linuxcbt.internal.db";
        };

  b. create the corresponding zone file
  c. restart named
  d. test resolution of DNS primary zone

Note: Install 'caching-nameserver*' for Caching-only DNS server

 2. Create a slave (Secondary) server
  a. yum -y install bind
  b. copy sample files from primary server to secondary server
  c. modify /etc/named.conf and set 'linuxcbt.internal' zone to slave
  d. start named service - 'service named start'
  e. chkconfig --level 35 named on
  f. Update: /var/named/linuxcbt.internal.db to reflect new name server

 3. Create a primary zone on the "secondary" server
  a. create a zone for: linuxcbt.external - in /etc/named.conf
  b. copy/create 'linuxcbt.external.db' zone file
  c. setup 'linuxcbtserv4' to be a slave for the zone: linuxcbt.external


  




 4. Start 'named' as a caching-only DNS server (Default)
  a. service named start
  b. 'dig @192.168.75.199 www.linuxcbt.com' - forces a caching-only lookup query



Forward IPv6 Records:
Implemented primarily as AAAA records:

linuxcbtserv1	IN	AAAA	2002:4687:db25:3:202:b3ff:fe98:4108
linuxcbtserv4	IN	AAAA	2002:4687:db25:3:20c:29ff:feb5:1692
linuxcbtmedia1	IN	AAAA	2002:4687:db25:3:20a:5eff:fe1b:4aad
linuxcbtrouter1	IN	AAAA	2002:4687:DB25:3:21A:2FFF:FEE3:F240

Test IPv6 resolution using:
 1. ping6 linuxcbtrouter1.linuxcbt.internal
 2. dig @192.168.75.10 linuxcbtrouter1.linuxcbt.internal


Reverse Zones:
 Features:
  1. The ability to resolve a name, given an IPv4 or IPv6 address


Tasks:
 1. Define an IPv4 reverse zone for the local subnet: 
  a. Define zone name: '75.168.192.in-addr.arpa' - /etc/named.conf
  b. Update: /etc/named.conf
  c. Create zone file in: /var/named
  d. Update configuration
  e. Restart named
  f. test using 'dig -x 192.168.75.1'

Note: Reverse zones are built from the prefix in IPv4 subnets


IPv6 Reverse Zone:
 Requirements:
  1. /etc/named.conf entry
zone "3.0.0.0.5.2.b.d.7.8.6.4.2.0.0.2.ip6.arpa" {
        type master;
        file "3.0.0.0.5.2.b.d.7.8.6.4.2.0.0.2.ip6.arpa.reverse";
};

Note: IPv6 reverse zone names are in nibble format, with ALL zeros expanded for the network prefix portion of the address, which is usually 64-bits in length


  2. /var/named/zone_file
   a. Include entries using the last 64-bits or IPv6 host part

d.a.a.4.b.1.e.f.f.f.e.5.a.0.2.0 IN PTR linuxcbtmedia1.linuxcbt.internal.

Note: When creating reverse IPv6 entries for hosts, do the following:
 a. reverse the 64-bit portion of the address that corresponds to the host, expanding all zeros
 b. Create PTR record based on the reverse, nibble-format of the address

Test using dig:
 a. dig -x 2002:4687:db25:3:20a:5eff:fe1b:4aad



###Network File System (NFS)###
Features:
 1. Transparent access to remote file systems
 2. Installed by default
 3. Uses RPC for communications



Tasks:
 1. Export a directory on the server using: /etc/exports
  a. /path_to_directory IP_ADDR(rw)
  b. /nfs1	192.168.75.10(rw)
  c. mkdir /nfs1
  d. start NFS server - 'service nfs start'
  e. Confirm export(s) - 'exportfs -v'
 
Note: NFS matches remote user's UID to local /etc/passwd to determine ACLs

 2. Export /nfs2
  a. Create entry in /etc/exports
  b. Update current exports using: exportfs -a

 3. Mount both exports on a remote system
  a. mount -t nfs 192.168.75.199:/nfs1 /nfs1
  b. mount -t nfs 192.168.75.199:/nfs2 /nfs2

 4. Allow local 'root' user the ability to write to /nfs1 export
  a. /etc/exports: (rw,no_root_squash)

 5. Setup mount points so that they're available upon reboot
  a. /etc/fstab
  b. Unmount and confirm that NFS mount points will be available when the client system changes runlevels (reboots, starts, etc.) - 'mount -a'


showmount -a 192.168.75.199 - shows mounts on this system (connected NFS clients)

 6. Attempt to mount /nfs1 & /nfs2 from an unauthorized system
  a. Fails because client's IP does not match server's /etc/exports
  b. Update server's /etc/exports to allow additional hosts/subnet/etc.
  c. exportfs -a - to update the export table


###AutoFS###
Features:
 1. Automatically mounts file systems (NFS, local, SMBFS, etc.) upon I/O request


Requirements:
 1. autofs-*rpm must be installed

/etc/auto.master - primary configuration file
 - also contains mount points and their mappings

/etc/sysconfig/autofs - default startup directives

Note: AutoFS must be running in order to auto-mount directories


Task: 
 1. Create an automount for /shares, which will mount /nfs1 & /nfs2
  a. update /etc/auto.master - '/shares /etc/auto.shares'
  b. cp /etc/auto.misc /etc/auto.shares
  c. update the rules in /etc/auto.shares
  d. Create AutoFS tree: /shares/
  e. Restart the autofs service
  f. Unmount: /nfs1 & /nfs2 if necessary
Note: Do NOT auto-mount directories that are already mounted
  g. Test access to AutoFS controlled directory
   g1. 'ls -l /shares/nfs1'

Note: syntax for auto-mount files is as follows:
<mount-point>  [<options>]  <location>
nfs1	-fstype=nfs 192.168.75.199:/nfs1

###Samba ###

Features:
 1. Provides Windows features (file & print) on Linux | Unix

/etc/samba/smb.conf - primary config file

Clients:
 1. findsmb - finds SMB hosts on the network
 2. smbtree - equivalent to Network Neighborhood/My Network Places (prints workgroups, hosts, and shares)
 3. smbget - similar to 'wget', in that, it will download files from the remote share
  a. smbget -u dean smb://linuxcbtwin1/mtemp/20070524_SAN_Allocations.ods

 4. smbclient - interactive (FTP-like_ utility to connect to shares - permits uploads/downloads from shares
  a. smbclient -U dean //linuxcbtwin1/mtemp
  b. mget file* - downloads file(s)
  c. mput file* - uploads file(s)


 5. smbtar - backs-up smb shares to a TAR archive
  a. smbtar -s linuxcbtwin1 -x mtemp -u dean -t backup1.tar


Samba Server:
/etc/samba/smb.conf - primary config file

SWAT manages /etc/samba/smb.conf

Samba Server Modes:
 1. User
  a. One Samba-defined user is required per Linux user
  b. Authentication of users is handled by Samba server
 2. Server/Domain (PDC/BDC)
  a. Authentication is handled by the Windows NT/2K/2K3/2K8 server
  b. Still requires a local Samba-defined user accounts database
 3. ADS - Active Directory
  a. Authentication is handled by Active Directory
  b. When used with Winbind, locally-defined Samba users are NOT required

Note: Ultimately, users must authenticate to the local Linux file system

Task:
 1. Install SWAT
  a. yum -y install samba-swat
  b. nano /etc/xinetd.d/swat - set 'disable = no'
  c. service xinetd restart
  d. netstat -ntl | grep 901


/etc/samba/smbpasswd maps Windows users to /etc/passwd

 2. Install rdesktop and connect to Windows XP to test connectivity to Samba
  a. yum -y install rdesktop

Winbind:
 Features:
  1. Windows AD integration
  2. Avoids having to define users in 2 places: Windows, Linux
  3. Uses Kerberos for authentication

Requirements:
 1. krb5-* packages
 2. Properly configured Kerberos environment:
  a. /etc/krb5.conf

[libdefaults]
	default_realm = AD2.LINUXCBT.INTERNAL

[realms]
	AD2.LINUXCBT.INTERNAL = {
		kdc = linuxcbtwin3.ad2.linuxcbt.internal
		admin_server = linuxcbtwin3
	}

[domain_realm]
	.linuxcbtwin3.ad2.linuxbt.internal = AD2.LINUXCBT.INTERNAL


Steps:
 1. Update: /etc/krb5.conf
 2. Update Samba configuration to use ADS authentication
 3. Update Samba server's DNS to point to ADS server
  a. /etc/resolv.conf
  b. /etc/hosts - including a pointer to the ADS server (linuxcbtwin3)

 4. Join AD domain:
  a. 'net ads join -U administrator'
 5. Confirm AD membership using: 'Active Directory Users & Computers' Tool

 6. Setup Winbind to authenticate using ADS:
  a. /etc/pam.d/system-auth - account & auth settings
  auth sufficient /lib/security/pam_winbind.so - place before 'pam_unix.so'
  account sufficient /lib/security/pam_winbind.so

  b. /etc/nsswitch.conf
   passwd: files winbind
   group: files winbind

  c. Configure 'idmap' 'uid & gid' mappings - 10000 - 20000
   Use SWAT to update idmap settings for 'uid & gid'
Note: If you want ADS users to be able to logon to your Samba-Winbind Linux box using SSH, Telnet, mingetty, etc., change the 'Template Shell' directive to a valid shell. i.e. /bin/bash

  d. Create 'Template homedir' %D (Domain) directory beneath '/home'
   mkdir /home/LINUXGENIUS

 7. Test Winbind Integration using: wbinfo
  a. wbinfo -u - this enumerates users in AD
  b. wbinfo -g - this enumerates groups in AD
  c. ssh into LINUXCBTSERV1 (Winbind) as ADS user


Task1:
 1. Authenticate using ADS, as 'administrator' from Windows box
 2. Create a user named 'linuxcbt' in AD
 3. Create shared directory on the Samba box, and provide access (Share it)




###Apache Web Server###
 Features:
  1. WWW Web Server
  2. Modular


Tasks:
 1. Install Apache 2.2x
  a. httpd*rpm

/etc/httpd - top-level configuration container on RH5
/etc/httpd/conf - primary configuration directory

/etc/httpd/conf/httpd.conf - primary Apache configuration file

/etc/httpd/conf.d - drop-in configuration directory, read by Apache upon startup

 2. Explorer: /etc/httpd/conf/httpd.conf

  a. HTTPD runs as: apache:apache
  b. Apache maintains, always, a 'main' server, which is independent of Virtual Hosts. This server is a catch-all for traffic that doesn't match any of the defined virtual hosts.

  c. <Directory> directive governs file system access.
Note: The primary Apache process runs as 'root', and has access to the full file system. However, <Directory> directive restricts the web-user's view of the file system.

  d. Test access to '.ht*' files from web root

  e. ErrorLog logs/error_log - default error log file for ALL hosts
  f. logs/access_log - default log file for default server

 Note: Every directory, outside of the 'DocumentRoot' should have at least one: <Directory> directive defined.

 3. Start Apache and continue to explore
  a. service httpd start
root     31324     1  0 10:17 ?        00:00:00 /usr/sbin/httpd
apache   31326 31324  0 10:17 ?        00:00:00 /usr/sbin/httpd
apache   31327 31324  0 10:17 ?        00:00:00 /usr/sbin/httpd
apache   31328 31324  0 10:17 ?        00:00:00 /usr/sbin/httpd
apache   31329 31324  0 10:17 ?        00:00:00 /usr/sbin/httpd
apache   31330 31324  0 10:17 ?        00:00:00 /usr/sbin/httpd
apache   31331 31324  0 10:17 ?        00:00:00 /usr/sbin/httpd
apache   31332 31324  0 10:17 ?        00:00:00 /usr/sbin/httpd
apache   31333 31324  0 10:17 ?        00:00:00 /usr/sbin/httpd

Note: Parent Apache runs as 'root' and can see the entire file system
Note: However, children processes run as 'apache' and can only see files/directories that 'apache:apache' can see

 4. Create an Alias for content outside of the web root (/var/www/html)
  a. Alias /testalias1 /var/www/testalias1
     <Directory /var/www/testalias1>
	AllowOverride Non
	order allow,deny
	allow from all
     </Directory>

 5. Ensure that Apache will start when the system boots
  a. chkconfig --level 35 httpd on && chkconfig --list httpd

Virtual Hosts Configuration:
 Features:
  1. Ability to share/serve content based on 1 or more IP addresses
  2. Supports 2 modes of Virtual Hosts:
   a. IP Based - one site per IP address
   b. Host header names - multiple sites per IP address


Tasks:
  1. Create IP Based Virtual Hosts
   a. ifconfig eth0:1 192.168.75.210
   b. Configure the Virtual Host:

<VirtualHost 192.168.75.210>
	ServerAdmin webmaster@linuxcbtserv4.linuxcbt.internal
	ServerName site1.linuxcbt.internal
	DocumentRoot /var/www/site1
	<Directory /var/www/site1>
		Order allow,deny
		Allow from all
	</Directory>
	CustomLog logs/site1.linuxcbt.internal.access.log combined
	ErrorLog logs/site1.linuxcbt.internal.error.log
</VirtualHost>

  c. Create: /var/www/site1 and content
  d. Update: /etc/httpd/conf/httpd.conf with VHost information


 2. Create Name-based Virtual Hosts using the primary IP address
  a. /etc/httpd/conf/httpd.conf: 
   NameVirtualHost 192.168.75.199:80

<VirtualHost 192.168.75.199:80>
	ServerAdmin webmaster@linuxcbtserv4.linuxcbt.internal
	ServerName site3.linuxcbt.internal
	DocumentRoot /var/www/site3
	<Directory /var/www/site3>
		Order allow,deny
		Allow from all
	</Directory>
	CustomLog logs/site3.linuxcbt.internal.access.log combined
	ErrorLog logs/site3.linuxcbt.internal.error.log
</VirtualHost>
 

###Apache with SSL Support###
 Features:
  1. Secure/Encrypted communications

 Requirements:
  1. httpd
  2. openssl
  3. mod_ssl
  4. crypto-utils (genkey) - used to generate certificates/private keys/CSRs
    a. also used to create a self-signed certificate

Tasks:
  1. Install the requirements
   a. mod_ssl - module for Apache, which provides SSL support
   yum -y install mod_ssl
    /etc/httpd/conf.d/ssl.conf - includes key SSL directives

   b. crypto-utils - provies /usr/bin/genkey

  2. Generate SSL usage keys using: genkey
   a. genkey site1.linuxcbt.internal - creates text-gui interface

  3. Update /etc/httpd/conf.d/ssl.conf to reference the new keys (public/private)

  4. Restart the HTTPD server
   a. service httpd restart
   b. httpd -S
 
  5. Test HTTPS connectivity
   a. https://192.168.75.199

Note: For mutliple SSL sites, copy the: /etc/httpd/conf.d/ssl.conf file to distinct files, that match your distinct IP-based VHosts


###MySQL###
 Features:
  1. DBMS Engine
  2. Compabtible with various front-ends: 
   a. Perl
   b. PHP
   c. ODBC
   d. GUI Management

Tasks:
  1. Install MySQL Client & Server
   a. yum -y install mysql

/etc/my.cnf - primary config file
/usr/bin/mysql - primary client used to interact with the server
/usr/bin/mysqladmin - primary admin utility to return useful info, and perform admin tasks from the shell

   b. yum -y install mysql-server

/usr/libexec/mysqld - DBMS engine

  2. Start MySQL server and modify perms for 'root'
   a. service mysqld start
   b. chkconfig --level 35 mysqld on
   c. mysqladmin -u root password abc123


  3. Install 'mysql' client on a remote system and test connectivity
   a. yum -y install mysql
   b. mysql -u root -p 

Note: mysql command-line options ALWAYS override global (/etc/my.cnf), and/or local (~/.my.cnf) configuration directives


Note: MySQL Users consist of the following:
   a. username i.e. 'root'
   b. host i.e. 'localhost'
A sample username is: 'root@localhost'

  4. Secure 'anonymous' account
   a. DELETE FROM mysql.user WHERE user = '';
   b. flush privileges;

  5. Create Database 'addressbook'
   
create database AddressBook;
use AddressBook;
create table contacts (`first_name` char(20), `last_name` char(20),
`bus_phone1` char(20), `email` char(30), PRIMARY KEY (`email`));


  6. Insert Data into 'contacts' table using INSERT

INSERT INTO contacts (first_name,last_name,bus_phone1,email) VALUES ('Kay','Mohammed','888.573.4943','kay@LinuxCBT.com');

  7. Delete record from 'contacts' table
DELETE FROM contacts WHERE email = 'kay1@LinuxCBT.com';

  8. Update a record in the 'contacts' table
UPDATE contacts SET email='kay2@LinuxCBT.com' WHERE first_name='Kay';







###Postfix MTA###
 Features:
  1. Message Transfer Agent (MTA)
  2. Modular (SpamAssAssin)
  3. Drop-in replacement for Sendmail, as it provides a 'sendmail' binary

Note: Use 'system-switch-mail*' package to switch between Postfix and Sendmail

Tasks:
  1. Install Postfix
   a. yum -y install postfix

/etc/postfix - primary configuration directory
/etc/postfix/main.cf - primary configuration file
/etc/postfix/transport - contains routing rules for domains
/etc/postfix/virtual - contains virtual user mappings

  2. Install 'system-switch-mail' package
   a. yum -y install system-switch-mail

  3. Switch default MTA from Sendmail, to Postfix
   a. system-switch-mail

Note: The default Postfix configuration binds to 127.0.0.1:25

  4. Test local mail delivery
   a. Use 'mutt' to test local delivery

  4. Configure Postfix to receive messages from remote systems
   a. set: inet_interfaces=all
   b. set mydestinations = linuxcbt.internal
   c. service postfix restart
   d. Confirm directives using: 'postconf'
   e. Attempt to send message from LINUXCBTSERV1 -> LINUXCBTSERV4
   f. If it fails, configure MTA on LINUXCBTSERV1 to listen to routable IP
    f1. update /etc/mail/sendmail.mc
    f2. make all -C /etc/mail
    f3. service sendmail restart
Note: Ensure that 'sendmail-cf*' package is installed, in order to updated .mc files to .cf files


###Mail Retrieval using POP3/IMAP###

Features:
 1. Mail retrieval using standard protocols
 2. Common package: dovecot
 3. Supports both: mbox (/var/spool/mail/usernam) & Maildir formats
 4. Supports SSL: POP3S & IMAPS

Tasks:
 1. Install dovecot
/etc/dovecot.conf - primary config file
/etc/pki/dovecot/dovecot-openssl.cnf - SSL config

Note: Default configuration binds to:
 a. POP3 - downloads messages to client
 b. POP3S
 c. IMAP - leaves messages on server
 d. IMAPS

E-mail flow: mutt -> sendmail -> Postfix queue -> remote system -> POP3|IMAP

 2. Configure mail client to download messages using POP3




###Squirrelmail (Web mail) Integration with Apache/Postfix/Dovecot###
Features:
 1. Web mail application
 2. Modular
 3. Implemented with PHP


Tasks:
 1. Install Squirrelmail with support via Apache
  a.Download from squirrelmail.org - *.bz2
  b. Confirm the MD5SUM
  c. Copy the *.bz2 file to the Apache server
  d. yum -y install php php-imap - installs PHP support for Apache/IMAP
  e. mkdir /var/www/mail
  f. Extract Squirrelmail to: /var/www/mail
  g. Optionally, create symlink named 'mail' to point to Squirremail version
  h. Create the Apache Virtual Host

<VirtualHost 192.168.75.199:80>
	ServerAdmin webmaster@mail.linuxcbt.internal
	ServerName mail.linuxcbt.internal
	DocumentRoot /var/www/mail
	<Directory /var/www/mail>
		Options FollowSymLinks
		Order allow,deny
		Allow from all
	</Directory>
	CustomLog logs/mail.linuxcbt.internal.access.log combined
	ErrorLog logs/mail.linuxcbt.internal.error.log
</VirtualHost>
  i. Restart Apache
  j. Configure SquirrelMail defaults: /var/www/mail/mail/config/conf.pl
  k. Create 'attach' and 'data' directories for SquirrelMail: /var/local/squirrelmail/{data,attach}
  l. Update permissions so SquirrelMail may write to 'data' and 'attach' directories: chown -R apache.apache /var/local/squirrelmail
  k. Setup DNS
  l. Attempt to access SquirrelMail
http://mail.linuxcbt.internal/mail
http://mail.linuxcbt.internal/mail/src/configtest.php
Note: If SELinux is enabled, use 'setsebool...' to allow httpd to connect to IMAP and SMTP ports. Consult: /var/log/messages


###Squid Proxy Server###
 Features:
  1. Caching server
  2. Filters access to the Net
  3. Efficient bandwidth usage
  4. Supports a wide criteria of ACLs (dstdomain, src_IP, Time of day, etc.)


Tasks:
 1. Install Squid Proxy server
  a. yum -y install squid

/etc/squid - primary configuration container
/etc/squid/squid.conf - primary configuration file
/usr/sbin/squidclient - used to test Squid Proxy server
/var/log/squid - primary log directory
/var/spool/squid - cache directory containter

 2. Start Squid, and ensure that it starts when the system reboots
  a. service squid start
  b. chkconfig --level 35 squid on

Note: Ensure that ample/fast disk storage is available for: /var/spool/squid
Note: Squid defaults to TCP:3128 

 3. Configure Firefox browser to use Squid Proxy server
 
 4. Configure Squid to allow LAN access through, to resources
  a. nano /etc/squid/squid.conf
  b. acl lan_users src 192.168.75.0/24
  c. http_access allow lan_users

 5. Deny 192.168.75.10, but allow ALL other users from the local subnet
  a. 
acl_lan_bad_users src 192.168.75.10
http_access deny acl_lan_bad_users
  
###SELinux Intro###
 Features:
  1. Restricts access by subjects (users and/or processes) to objects (files)
  2. Provides Mandatory Access Controls (MACs)
  3. MACs extend Discretionary Access Controls (DACs(Standard Linux Permissions))
  4. Stores MAC permissions in extended attributes of file systems
  5. SELinux provides a way to separate: users, processes (subjects), and objects, via labeling, and monitors/controls their interaction
  6. SELinux is integrated into the Linux kernel
  7. Implements sandboxes for subjects and objects
  8. Default RH5 implementation creates sandboxes (domains) for 'targeted' daemons and one sandbox (unconfined_t) for everything else
  9. SELinux is implemented/enabled by RH5, by default
 10. Operates in the following modes:
   a. Permissive - permission is always granted, but denials are logged in: /var/log/messages
   b. Enforcing - strictly enforces 'targeted' policy rules
   c. Disabled - Only DACs are applied

 11. Operating modes can be applied upon startup or while the system is running

SELinux Config files & Tools:
 1. sestatus - displays current SELinux status, including:
  a. policy name 'targeted'
  b. policy version '21'
  c. Operating mode: 'enforcing|permissive|disabled'

 2. /etc/sysconfig/selinux - primary startup|config file for SELinux
 3. /etc/selinux/targeted - top-level container for the 'targeted' policy
 4. setenforce = 0(permissive) 1(enforcing)
 5. '-Z' can be applied to the following tools to obtain SELinux context info:
  a. mv, cp, ls, ps, id
 6. chcon -R -t type file - applies SELinux label to file/directory

Tasks:
 1. Disable SELinux upon boot-up on LINUXCBTSERV4
  a. nano /etc/grub.conf
   a1. Update 'kernel' line to reflect: selinux=0


Note: If files(objects) lose their SELinux context, there are multiple ways to relabel them:
 1. 'touch /.autorelabel && reboot' - init will relable the system according to the 'targeted' policy
 2. 'fixfiles' - use to relabel objects (files) while the system is running

Note: List of daemons protected by the 'targeted' SELinux policy:
 1. apache(httpd)
 2. dchpd
 3. ntpd
 4. named
 5. syslogd
 6. squid
 7. snmpd
 8. portmap
 9. nscd
10. winbind

Note: The 'targeted' policy assigns ALL other subjects and objects to the 'unconfined_t' domain

Note: The default SELinux 'targeted' policy, using MACs, binds subject domains: i.e. 'httpd_t' to object types: i.e. 'httpd_config_t'

Note: SELinux MACs compound Linux DACs












###OpenPGP|GNU Privacy Guard (GPG)###
Features:
 1. Confidentiality - Data (Files or e-mail) are encrypted
 2. Integrity - Digital signatures
 3. Compression
 4. Public Key Infrastructure (PKI)
  a. Public key - used to encrypt data to a recipient
  b. Private key - used to decrypt data from a sender
 5. GPG is OpenPGP compliant

Usage:
 1. gpg --list-keys - this enumerates keys in ~/
 2. gpg --gen-key - generates a PKI keypair for the current user

 3. gpg --encrypt -r LinuxCBT --armor sample.txt - encrypts sample.txt using our 'LinuxCBT's' public key

 4. gpg --decrypt sample.txt.asc
 5. gpg --decrypt sample.txt.gpg
 6. gpg --export -a - dumps public key to STDOUT
 7. gpg --import - waits on STDIN for user to paste a key for import
 8. gpg --decrypt -o sample.txt sample.txt.gpg


###OpenSSHv2###
Features:
 1. Provides data encryption services based on PKI - Confidentiality
 2. Primarily used to protect the transport layer
 3. Encrypted shell sessions, file transfers
 4. Password-less logins
 5. Port forwarding - Pseudo-VPN

SSH Clients:
/etc/ssh/ssh_config - shared system-wide config file for SSH clients

1. scp - secure, non-interactive, copy program
 a. scp sample.txt linuxcbt@linuxcbtmedia1:
 b. scp linuxcbt@linuxcbtmedia1:testRH5/sample.txt sample2.txt

2. sftp - secure, interactive, FTP-like, copy program
 a. sftp linuxcbt@linuxcbtmedia1

3. ssh - shell-based client
 a. ssh linuxcbt@linuxcbtmedia1
 a. ssh linuxcbt@linuxcbtmedia1 "uptime"

4. ssh-copy-id - permits easy propagation of SSH pub/priv keypair
 a. ssh-copy-id -i ~/.ssh/id_rsa.pub root@192.168.75.10

5. ssh-keygen - used to generage SSH pub/priv keypair
Note: Use '-v' with SSH clients to enable verbosity

 a. ssh-keygen -t rsa

Task:
 1. Setup Password-less logins using SSH

###IPTables###
Features:
 1. Firewall for Linux
 2. Interface to Netfilter, which is loaded by the kernel
 3. Operates primarily @ layers 3 & 4 of the OSI model
 4. Modular
 5. Provides Network Address Translation (NAT)
 6. IPTables can also access other layers (2, 5-7), with modules

1. grep -i config_netfilter /boot/config*

Note: Save rules in: /etc/sysconfig/iptables so that when IPTables is restarted, the rules will be applied OR, update /etc/sysconfig/iptables-config to save the rules automatically

/sbin/iptables - primary ACL modifier utility
/sbin/iptables-restore - restores rules to current IPTables instance
/sbin/iptables-save - saves rules to STDOUT, by default, or to a file


IPTables includes 3 default tables, which you cannot remove:
 1. NAT
 2. Mangle
 3. Filter (Default) - filters inbound/outbound traffic

Note: Each table, includes chains, which include Access Control Entries (ACEs)

Usage:
 1. iptables -L

Note: The Filter table includes 3 chains:
 1. INPUT - applies to traffic destined to a service that our system is bound to

 2. FORWARD - applies to traffic being routed through the system

 3. OUTPUT - applies to traffic sourced from our system, heading outbound


Tasks:
 1. Filter inbound traffic to remote RH5 system to SSH
  a. iptables -A INPUT -p tcp --dport 22 -j ACCEPT
  b. iptables -A INPUT -j DROP

 2. Filter outbound traffic to ANY remote SSH port
  a. iptables -A OUTPUT -p tcp --dport 22 -j DROP

 3. Flush ALL rules from OUTPUT chain of the Filter table 
  a. iptables -F OUTPUT

 4. Save rules to file, then flush rules
  a. iptables-save > iptables.rules.1

 5. Reinstate flushed rules
  a. iptables-restore iptables.rules.1


###IPv6 IPTables###
Features:
 1. Firewall for IPv6

/etc/rc.d/init.d/ip6tables - run-script
/etc/sysconfig/ip6tables-config - system-wide config file

/sbin/ip6tables - primary tool for administering IP6Tables
/sbin/ip6tables-restore
/sbin/ip6tables-save

 2. Maintains 3 default tables:
  a. Filter - matches IPTables(IPv4)
  b. Mangle - matches IPTables(IPv4)
  c. Raw

 
Usage:
 1. ip6tables -L

Note: IPv6 firewall rules are administered independently of IPv4 rules

Tasks:
1. Filter inbound traffic to remote RH5 system to SSH
  a. ip6tables -A INPUT -p tcp --dport 22 -j ACCEPT
  b. ip6tables -A INPUT -j DROP

 2. Filter outbound traffic to ANY remote SSH port
  a. ip6tables -A OUTPUT -p tcp --dport 22 -j DROP

 3. Flush ALL rules from OUTPUT chain of the Filter table 
  a. ip6tables -F OUTPUT

 4. Save rules to file, then flush rules
  a. ip6tables-save > ip6tables.rules.1

 5. Reinstate flushed rules
  a. ip6tables-restore ip6tables.rules.1





###NMap###
Features:
 1. Port/Reconnaissance Scanner
 2. Hosts & device detection
 3. Service detection
 4. OS Fingerprinting
 5. Multi-target scanning
 6. Produces various reports

Tasks:
 1. Download and install the latest version of NMap - nmap.org
  a. wget http://download.insecure.org/nmap/dist/nmap-4.53-1.i386.rpm
  b. rpm -Uvh nmap-4.53-1.i386.rpm

/usr/bin/nmap - primary binary
Note: Executing 'nmap' as non-privileged user, causes it to operate in TCP-Connect mode, instead of the stealthy TCP-SYN mode

/usr/share/nmap - top-level container for key NMap files
/usr/share/nmap/nmap-os-db - OS Fingerprinting DB
/usr/share/nmap/nmap-mac-prefixes - Maps MAC prefixes to companies
/usr/share/nmap/nmap-services - resolves service names to port numbers


Usage:
 1. Scan the localhost for open ports
  a. nmap -v localhost

 2. Service detection scan - attempts to resolve services to names & versions
  a. nmap -v -sV 192.168.75.199

 3. OS Fingerprinting scan
  a. nmap -v -O 192.168.75.199

 4. Reporting
  a. nmap -v -oN filename.txt 192.168.75.1 - normal output
  b. nmap -v -oX filename.xml 192.168.75.1 - XML output

 5. OS Fingerprinting & Service detection
  a. nmap -v -A 192.168.75.1

 6. Scan the entire network using '-A' and XML output
  a. nmap -v -A -oX 192.168.75.0.scan.xml 192.168.75.0/24


###Nessus###
Features:
 1. Vulnerability Scanner
 2. Port Scanner
 3. Host | Device detection
 4. Can be used to scan NETBIOS (Windows|Samba) servers
 5. Profiles (Scan Policies) for target scans, with specific exploits to query
 6. Reporting
 7. Client/Server enabled; multiple clients may use the central Nessus server
 8. Client support for Windows, Linux, etc.
 9. Runs as a service, awaiting inbound PenTest requests
10. Penetration testing tool
11. Nessus can be automated
12. Supports plug-ins for vulnerability signatures
13. Supports parallel scanning of targets

Tasks:
 1. Download Nessus from nessus.org and install
 2. Register nessus using 'nessus-fetch', with provided code
  a. /opt/nessus/bin/nessus-fetch --register A65E-5116-4D76-FCD5-FF2A
 3. Install Nessus Client and Explore the interface
  a. rpm -Uvh NessusClient*

 4. Perform a PenTest of the localhost
 5. Perform a PenTest of the local network
 6. Evaluate results

Note: Nessus will auto-update its plug-ins after registration, every 12-hours



###Snort NIDS###
Features:
 1. Network Intrusion Detection System (NIDS)
 2. Packet Sniffer
 3. Packet Logger - logs using TCPDump format

Tasks:
 1. Download and install Snort NIDS
  a. snort.org
  b. Confirm MD5SUM: 'md5sum snort-2.8.0.2.tar.gz' Compare to snort-2.8.0.2.tar.gz.md5
  c. Import GPG key used to sign the current release of Snort
  d. gpg --verify snort-2.8.0.2.tar.gz.sig snort-2.8.0.2.tar.gz

Requirements:
 1. gcc - C compiler
 2. make - creates binaries
 3. libpcre - Provides access to Perl Compatible RegExes
 4. mysql-devel* - provides access to MySQL
 5. libpcap* - provides the TCPDump, packet capture library

 e. Extract and install (compile) Snort NIDS
  e1. tar -xzvf snort-2.8.0.2.tar.gz - creates top-level directory
  e2. ./configure --with-mysql --enable-dynamicplugin - checks for prerequisites, including: mysql-devel, libpcre, gcc, make, etc.
  e3. make - creates binaries
  e4. su (as 'root') and execute 'make install' - places binaries in /usr/local/ accessible location


Usage - Packet Sniffer:
 1. snort -v -i eth0 - reveals layers 3 & 4 of the OSI model
 2. snort -vde -i eth0 - reveals layers 2-7
 3. snort -vde -i eth0 tcp port 23

Usage - Packet Logger:
 1. snort -v -i eth0 -l ./ tcp port 23 - logs binary file in current directory with Unix Epoch suffix
 2. snort -b -i eth0 - attempts to log in: /var/log/snort
 3. snort -b -L test.snort.log -i eth0 - creates: /var/log/snort/test.snort.log.UnixEpochDate

Note: Snort drops less packets when run in binary logging mode than in verbose, dump-to-screen, mode


###Snort NIDS Setup###
 1. Setup MySQL DB environment
  a. create database snort;
  b. grant insert,select on root.* to snort@localhost;
  c. set password for snort@localhost=password('abc123');
  d. grant create,insert,select,delete,update on snort.* to snort@localhost;
  e. grant create,insert,select,delete,update on snort.* to snort;

 2. Import MySQL DB schema
  a. mysql -u root -p < /home/linuxcbt/temp/Snort/snort-2.8.0.2/schemas/create_mysql snort

 3. Setup Snort NIDS /etc/snort environment
  a. mkdir /etc/snort && cp -v /home/linuxcbt/temp/Snort/snort-2.8.0.2/etc/* /etc/snort

Note: Snort's primary configuration file for NIDS mode: /etc/snort/snort.conf

 4. Download the latest Snort rules file and extract to: /etc/snort/rules

Note: Snort rules are available as follows:
 1. Registered users: with delay
 2. Subscriber: no delay - NOT FREE
 3. Unregistered users: release version (very old) of rules
 4. Various third-party sites: i.e. Bleeding Snort, etc.

 a. cd /etc/snort && tar -xzvf snortrules*

 5. Configure: /etc/snort/snort.conf to use MySQL and rules
  a. MySQL - output
  b. Rules - path to the rules

 6. Start Snort in NIDS mode
  a. snort -i eth0 -c /etc/snort/snort.conf -D

 7. Setup BASE web analysis application
  a. wget http://easynews.dl.sourceforge.net/sourceforge/adodb/adodb480.tgz
  b. tar -xzvf adodb480.tgz

Note: adodb480.tgz - provides DB-connectivity for BASE to MySQL

  c. Download BASE from http://base.secureideas.net
  d. Configure: base_conf.php file
   d1. $BASE_urlpath = '/base';
   d2. $Dblib_path = "/var/www/html/adodb";
   d3. $Dbtype = 'mysql';
   d4. alert_dbname = 'snort';
   d5. alert_host = 'localhost';
   d6. alert_password = 'abc123';
 
Note: Ensure that your Apache instance has PHP support
Note: Ensure that 'php-mysql*' package is installed

 8. Connect to BASE via web browser

Note: Consider protecting '/base' application using HTDIGEST or basic auth
























