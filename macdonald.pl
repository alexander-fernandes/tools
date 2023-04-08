#!/usr/bin/perl
#
#   MAC changer using ifconfig written in perl
#
use strict;
use warnings;

print "- enter the network interface (e.g. eth0): ";
my $interface = <STDIN>;
chomp $interface;

print "- enter the new MAC address (e.g. 00:11:22:33:44:55): ";
my $new_mac = <STDIN>;
chomp $new_mac;

# bring the interface down
print "[.] turning interface down..";
system("ifconfig $interface down");

# change the MAC address
system("ifconfig $interface hw ether $new_mac");

# bring the interface up
print "[.] turning interface up..";
system("ifconfig $interface up");

print "[#] successfully changed MAC";