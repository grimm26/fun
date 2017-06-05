#!/usr/bin/perl -w
#
use strict;

my $file = shift;
my $rl_addrs = &read_file($file);

#my $tls_count = &count_tls_addrs($rl_addrs);
my $fancy_tls_count = &fancy_count_tls_addrs($rl_addrs);

#print "$tls_count\n";
print "$fancy_tls_count\n";

my $ssl_count = &count_ssl_addrs($rl_addrs);

sub fancy_count_tls_addrs {
  my $rl_addrs = shift;

  my $count = 0;
  foreach my $addr (@$rl_addrs) {
    if ($addr =~ /
      (?= # positive lookahead
        ^
          (?: # group
            (?!.*\[\w*(\w)(?!\1)(\w)(?=\2\1)\w*\]). # negative lookahead
          )*
        $ # No bracketed ABBA
      )
      .* # anything
      (\w)(?!\3)(\w)(?=\4\3)(?!\w+\]) # ABBA!
      (?!.*\[\w*(\w)(?!\5)(\w)(?=\6\5)\w*\]) # No bracketed ABBA 
      /x) {
      $count++;
    }
  }
  return $count;
}

sub count_ssl_addrs {
}

sub read_file {
  my $file = shift;

  open IN, $file or die "Could not open $file to read: $!\n";
  my @lines = <IN>;
  close IN;
  return \@lines;
}

# clunky
sub count_tls_addrs {
  my $rl_addrs = shift;

  my $count = 0;
  foreach my $addr (@$rl_addrs) {
    # Skip bracketed palindromes
    if ($addr =~ /\[\w*(\w)(?!\1)(\w)(?=\2\1)\w*\]/) {
      print "bracketed skip of '$1$2$2$1': $addr\n";
      next;
    }
    elsif ($addr =~ /(\w)(?!\1)(\w)(?=\2\1)/) {
      $count++;
    } else {
      print "no abba: $addr\n";
    }
  }
  return $count;
}
