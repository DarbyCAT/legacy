<b>If you ever need any help, feel free to add an issue.</b>
# How to write pages for DarbyCAT.github.io
## Editing—Using GitHub
### Step One: Make a GitHub account
Go to [https://github.com] and sign up for an account.
### Step Two: Installing Git
Go [https://git-scm.com/book/en/v2/Getting-Started-Installing-Git](here) and follow the instructions.

If you want a GUI, we reccomend [https://desktop.github.com](GitHub desktop) for Mac and Windows, but there are more (https://git-scm.com/downloads/guis)[here.]
### Step Three: 
## Jekyll
Jekyll is a static site genorator, and it's used for this website. You don't really have to install it, but if you want to:
[http://jekyllrb.com/](link.)
## Adding an author
Before you start writing, you should create an author to use for your posts. Go to `_data/authors.yml` to add yourself.
You'll add your information in a second, but to explain what everything means:
name is your first name, with proper capitalization, like `George`<br>
alias is your username, like `george42`<br>
If those were the values, it would look like this:
<pre>
    george42:
            name: George
            alias: george42
</pre>
Notice that the top line and the alias are the same. That's important. Also, make sure to indent.  
<h2>Making your profile</h2>
Next, you need to create a profile page. Create a file in the `profile` folder called `george42.html` (with george42 replaced by your alias.) Inside, add some metadata. If you were George, you would write:
<pre>
---
layout: profile
permalink: /profile/george42
profile: george42
---
</pre>
You would replace any `george42` with your alias. Below that write profile information, such as `42 is the answer to life, the universe, and 21*2`. Now, you can start writing!  
<h2>Writing</h2>
To create a post, go to the folder `_posts` and make a file called `YYYY-MM-DD-title-like-this.markdown` (so on March 5, 2017, to create "I Like Pizza" it would be `2017-03-05-i-like-pizza.markdown`.) The metadata will look like this:
<pre>
---
layout: post
title:  "Title Like This"
date:   YYYY-MM-DD HH:MM:SS -0500
categories: categories seperated by spaces
author: youralias
---
</pre>
or for the example:
<pre>
---
layout: post
title: "I Like Pizza"
date: 2017-03-05 19:06:51 -0500
categories: pizza food greatness
author: george42
---
</pre>
Below that, get writing!
<b>If you ever need any help, feel free to add an issue.</b>
