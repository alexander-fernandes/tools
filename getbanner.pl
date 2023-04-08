#!/usr/bin/perl
#
# a very simple banner grabber, because that's useful
#

use strict;
use warnings;
use IO::Socket::INET;

my $host = shift || die "usage: $0 host\n";
my $port = shift || 80; # defaults to http port 80 if none given

# create a socket
my $socket = IO::Socket::INET->new(
    PeerAddr => $host,
    PeerPort => $port,
    Proto => 'tcp', # usung the tcp protocol
    Timeout => 10
) or die "[#] could not connect to $host:$port: $!";

$socket->send("GET / HTTP/1.0\r\n\r\n"); # then use the socket to create a simple request
print "[#] banner grabbed:";

while (my $line = <$socket>) {
    print $line;
}

close $socket;