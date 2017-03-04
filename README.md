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
---</pre>
3. Add content  
Then, commit and wait a few minutes.  
Full example (filename is `2017-03-04-added-pizza-to-life.markdown`):<pre>
---
layout: post
title:  "PIZZAAAAA"
date:   2017-03-04 18:39:36 -0500
categories: pizza
---
So, pizza is yummy. This is an example post.</pre>
