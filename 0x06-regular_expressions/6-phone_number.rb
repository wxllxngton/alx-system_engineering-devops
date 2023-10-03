#!/usr/bin/env ruby
puts ARGV[0].scan(/(?<!\d)(\d{10})(?!\d)/).join
