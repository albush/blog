Title: Hello World
Date: 2014-06-02 20:14
Template: blog/article
Slug: Hello World
Author: Alan Bush

### The part where I welcome you to version X.Y of my blog. 

###### Where "X" and "Y" are numbers larger than I would like to admit. 

Let's just call it iteration number ten. I've built this blog on the Pelican Framework, with a large dose of help from [Justin Phelp's two](http://www.onitato.com/no-hassle-blog-automation.html) [guides to blog automation](http://www.onitato.com/no-hassle-blog-automation-redux.html) with [Pelican](http://blog.getpelican.com/). 

### Why Pelican? 

I wanted to build a simple, static site that I can post directly as HTML - either through my own server, or on a Rackspace Cloud Files Container. (That's where we are now.) I also wanted to keep the actual authoring component in-line with my current workflow. I write anything that needs formatting in Markdown, and I like to keep notes in nvALT - which works extremely well with Markdown. I want to be able to quickly move from a note, to a draft, to a live post. Pelican fits that bill. (See what I did there?)

### Additional Modifications

Pelican is configured out of the box to work as a dead-simple blog. You write a post in the content folder, then Pelican generates the static files for you - and index page with your latest posts listed, and those individual post pages. But I wanted something which would offer me the option to add an entire static site in front of the blog. And that's easy enough to do with Pelican.   
After a bit of Googling, I found a very useful comment outlining [how to build a static site with a blog in a subfolder with Pelican](http://stackful-dev.com/static-site-jinja-pelican-shared-templates.html#comment-901669793). This allowed me to put up a static shell, and then add my blog posts at ambush.com/blog. Anything I want to keep in the forefront, I'll share as a static page.   
I also wanted to move away from the standard theme, and I'd already built a simple, one-page site with bootstrap, so I grabbed the [Pelican-Bootstrap3 template](https://github.com/DandyDev/pelican-bootstrap3), which allowed me to add in my own style changes to match my existing blog. I've essentially just added a /blog folder, and greatly enhanced my ability to quickly add additional pages and content. Its a great improvement. 

### What's Next? 

Who knows? If history is any indication, probably four or five more blog posts, and then a brief break, followed by a slower release of helpful posts. I'm also working to import some of my better content from my previous blog iterations. 
