#!/usr/bin/perl
my @data;

$s1=0;

while ($s1<5)
{
	print "\n Enter your Name \n";
	$data[$s1][0]=<STDIN>;
	print "\n Enter your Age \n";
	$data[$s1][1]=<STDIN>;
	$s1=$s1+1;

}

$s1=0;

while ($s1<5)
{
	print "Name \t ";
	print $data[$s1][0];
	print "Age \t ";
	print $data[$s1][1];
	$s1=$s1+1;

}
