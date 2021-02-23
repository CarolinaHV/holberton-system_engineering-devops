#!/usr/bin/env ruby
from = ARGV[0].scan(/from:(\+?\w+)/).join
to = ARGV[0].scan(/to:(\+?\d+)/).join
flags = ARGV[0].scan(/flags:(\-?\d{1}\:\-?\d{1}\:\-?\d{1}\:\-?\d{1}\:\-?\d{1})/).join

puts "#{from},#{to},#{flags}"
