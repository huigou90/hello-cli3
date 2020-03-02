##
# This file is part of WhatWeb and may be subject to
# redistribution and commercial restrictions. Please see the WhatWeb
# web site for more information on licensing and terms of use.
# https://www.morningstarsecurity.com/research/whatweb
##
Plugin.define do
name "Apache-Shiro"
authors [
  "Brendan Coles <bcoles@gmail.com>", # 2011-11-20
]
version "0.1"
description "Apache Shiro"
website "http://www.accellion.com/"

# ShodanHQ results as at 2011-11-20 #
# 1,005 for location courier mail_user_login.html
#   991 for sfcurl=deleted

# Google results as at 2011-11-20 #
# 37 for inurl:"courier/1000@/mail_user_login.html"

# Dorks #
dorks [
'inurl:"courier/1000@/mail_user_login.html"'
]

# Matches #
matches [

# HTTP Set-Cookie Header # sfcurl=deleted;
{ :search=>"headers[set-cookie]", :text=>'rememberMe=deleteMe;'},

]

passive do
  m=[]
  $CUSTOM_HEADERS['Cookie'] = 'rememberMe=1;'
  m
end

end

