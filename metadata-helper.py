import datetime
print """
Welcome to Metadata Maker!
This simple tool will genarate the metadata and title for any Jekyll post.
"""
now = datetime.datetime.now()
ltitle = raw_input('What is the title of your post, lowercase with no spaces?\n>>>')
ctitle = raw_input('What is the title of your post, capital with spaces?\n>>>  ')
print now.strftime("Title: %Y-%m-%d-" + ltitle + ".markdown")
print("""
Metadata:
---
layout: post
title: \"""" + ctitle + now.strftime("\"\ndate: %Y-%m-%d %H:%M:%S -0400\n---"))