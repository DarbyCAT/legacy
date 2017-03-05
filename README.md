# How to develop for DarbyCAT.github.io</h2>
## Jekyll
Jekyll is a static site genorator, and it's used for this website. You don't really have to install it or learn it, but if you want to:
[http://jekyllrb.com/docs/home/](link.)
## Creating a post
1. Add a file to the _posts folder, with the title like `YYYY-MM-DD-title-all-lower-case.markdown`
2. Add the metadata like this:
 
  <pre>
---
layout: post
title:  "Title Of Your Post (as seen in the menu)"
date:   YYYY-MM-DD HH:MM:SS -0500
categories: category anotherone
author: author
---</pre>
3. Add content  
Then, commit and wait a few minutes.  
Full example (filename is `2017-03-04-added-pizza-to-life.markdown`):<pre>
---
layout: post
title:  "PIZZAAAAA"
date:   2017-03-04 18:39:36 -0500
categories: pizza
author: jm8
---
So, pizza is yummy. This is an example post.</pre>
##Adding an author
1. Go to `_data/authors.yml`.
2. Add something like this:<pre>
namethatwillbeinmetadata:
    name: Full Name
    web: /location/of/profile/page.html
    </pre>or<pre>
    web: http://website.com/username</pre if you want a social media profile or personal website
<pre>   alias: username</pre>
Full example:<pre>
jm8:
    name: Josh
    web: /profile/jm8.html
    alias: jm8</pre>
##Adding a profile page
1. Go to `/profile/` and create a page called `username.html`.
2. Add this metadata:
<pre>---
layout: default
permalink: /profile/username.html
---</pre>
3. Add a title like `<h2>username Profile</h2>`
4. Add whatever profile information you want.
5. Add it to authors (see Adding an author)
