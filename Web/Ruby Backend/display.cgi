#!/usr/bin/ruby -w
print "Content-type: text/html\n\n"

require 'cgi'
cgi = CGI.new

puts "<head>"
puts "<script src=\"https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js\"></script>"
puts "<script>
$(document).ready(function(){
        $(\"#one\").fadeIn(6000);
        $(\"#two\").fadeIn(1000);
        $(\"#three\").fadeIn(3000);
});
</script>"
puts "</head>"

name = cgi['nam']
puts "Your name is:"
puts name

puts "<br>"

address = cgi['place']
address = address.split(" ")
address2 =  address[0].capitalize + " " + address[1].capitalize + " " + address[2].capitalize
puts "Your address is:"
puts address2

puts "<br>"

phone = cgi['num']
phone = phone.split("-")
part1 = "(" + phone[0] + ")"
part2 = phone[1]
part3 = "-" + phone[2]
puts "Your phone number is:"

puts "<span id=\"one\" style=\"display:none; color:blue; font-size:150px\">"
puts part1
puts "</span>"

puts "<span id=\"two\" style=\"display:none; color:orange; font-size:150px\">"
puts part2
puts "</span>"

puts "<span id=\"three\" style=\"display:none; color:red; font-size:150px\">"
puts part3
puts "</span>"












