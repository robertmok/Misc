#!/usr/bin/perl
use CGI ':standard';
print "Content-type:text/html\n\n";

print "<link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\">";

print "<h1> Submited Summary  </h1> <br>";

$first = param ('first');
$last = param ('last');
print "<p> Hello $first $last ! </p> <br><br>";

$gender = param('gender');
print "<p> You are a $gender . </p> <br>";

$year = param('year');
print "<p> You are year $year . </p> ";

