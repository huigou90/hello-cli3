##
# This file is part of WhatWeb and may be subject to
# redistribution and commercial restrictions. Please see the WhatWeb
# web site for more information on licensing and terms of use.
# https://www.morningstarsecurity.com/research/whatweb
##
Plugin.define do
name "Kibana"
authors [
  "Brendan Coles <bcoles@gmail.com>", # 2015-04-26
  "Andrew Horton", # v0.2 # 2019-07-10 # Added website field.
]
version "0.2"
description "Kibana is an open source data visualization platform that allows you to interact with your data"
website "https://www.elastic.co/products/kibana"

# Default Port: 5601

# Matches #
matches [

# HTTP X-App-Name Header
{ :search=>"headers[x-app-name]", :regexp=>/^kibana$/ },

# Body tag
{ :text=>'<body kibana ng-class' },

# Version Detection
{ :version=>/<script>\s+window\.KIBANA_VERSION='([\d\.]+)';\s+window\.KIBANA_BUILD_NUM='[\d]+';/ },

]

end

