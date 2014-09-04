Title: Why use a CDN when your entire site is hosted in a CDN
Author: Alan Bush
Status: draft

I've written previously about [how I host my website in Rackspace Cloud Files](http://www.albush.com/Hello%20World.html)[^], and also on how I recently started [using Dropzone to quickly upload files up to Cloud Files](http://www.albush.com/easy-filesharing-with-dropzone3-and-rackspace-cloud-files.html)[^]. This weekend I integrated these two a bit further, and moved all of the images from my blog into another Cloud Files container to be served from there. 

### Wait, why would you server content from two different containers?

It might seem a bit counterintuitive to host your static blog in one container and host the images in another - but I have found that it works 

[^]: I need to update this page, as I've changed up my setup a little.
[^]: It occurs to me that using the upload to Cloud Files action could be simple method for hosting and updating a website - provided that the main action on the site is adding new pages. I should write that out.

