---
Date: 2014-08-15
Title: Easy Filesharing with Dropzone3 and Rackspace Cloud Files
---

<img class="img-responsive" src="//drops.albush.com/andtherewasmuchrejoicing.gif">

From time to time I need to quickly share an image or file with a colleague, a friend or client, and that's usually something I would do on a one-off basis by emailing, or uploading to Dropbox or something. This is a pretty easy workflow, but it could probably be easier, right? That's where [Alex Chiri][1] and his [Dropzone][2] action come in.

If you're not familiar, Dropzone is a great little Mac utility that allows you to perform quick actions by dragging a file up to the icon on the menu bar. **Disclosure:** After tweeting about how cool I thought this was, Aptonic Software provided me with a free copy of Dropzone 3. This blog post is unsolicited. Some default actions are to upload to Dropbox, but Dropzone also has pretty solid development options, and that's where Alex Chiri comes in. As he outlined [here][3] in his blog post, with some prompt help from John at Dropzone, Alex was able to create an action for Dropzone to upload to Rackspace Cloud Files, and then copy the resulting CDN enabled url to the clipboard.

I saw this blog post and instantly saw where this would be valuable. Now, when I want to send a file to a customer or friend, I can quickly upload it to my own Cloud Files container and send them the link via IM, email, or any other medium. To make it even easier to access, I added a CNAME record, so that I can send a more clean url. Alex then added a feature to specify that CNAME in the initial action configuration. Now, all of my drops have a much easier to remember url. Of course this is best for times that I don't mind if _anyone_ comes by and takes a look - I wouldn't ever use this method for confidential items.

## Adding a file index

After setting up the Dropzone action and the CNAME for easy access, I wanted to be able to see all of the files I've already uploaded. Fortunately Rackspace Cloud Files API has the ability to set a container to list the contents of a container as if it were an index or table of contents. This process requires a bit of command line work, but it's not too difficult to figure out.

#### Find your Token and Endpoints

First you need your Rackspace API Token. You'll need your API Key, and username. You can grab those in your control panel. You'll need to enter the following curl command into your terminal:

	curl -s -d \
	'{
	"auth":
	{
	"RAX-KSKEY:apiKeyCredentials":
	{
	"username": "your_username",
	"apiKey": "your_api_key"}
	}
	}' \
	-H 'Content-Type: application/json' \
	'https://identity.api.rackspacecloud.com/v2.0/tokens' | python -m json.tool

Where "your_username" and "your_api_key" are replaced with your own credentials. (Also use https://lon.identity.api.rackspacecloud.com/v2.0/tokens if you're on the other side of the pond.)

You'll get a big block of json back, and that will give you two items you'll need, your API Token and your Cloud Files endpoints. Everything's pretty well explained, but check out the full documentation [in the Rackspace Support Center][4].

#### Set your container to use an index

Next you'll need to set the container up to supply an index. This involves a few more API calls.

Set web listing to true. [Full documentation here][5]

	curl -I -X POST -H "X-Container-Meta-Web-Listings:true" -H "X-Auth-Token:your_API_token" your_cf_endpoint/your_cf_container

make sure to replace your own token, endpoint, and container with actual data. That should look something like:

	curl -I -X POST -H "X-Container-Meta-Web-Listings:true" -H "X-Auth-Token:abc123def456ghi789" https://storage101.dfw1.clouddrive.com/v1/MossoCloudFS_XXXXXYYYYYYAAAAABBBBCCCCCC/shares
And then check to see if it works:

	curl -I -X GET -H "X-Auth-Token:your_API_token" your_cf_endpoint/your_cf_container

Again, putting in your own token, endpoint, and container. If it works, you'll receive a message similar to this:

	HTTP/1.1 200 OK
	X-Container-Meta-Web-Listings: true
	Content-Length: 79
	X-Container-Object-Count: 5
	X-Storage-Policy: Policy-0
	Accept-Ranges: bytes
	X-Container-Meta-Access-Control-Expose-Headers: etag location x-timestamp x-trans-id
	X-Container-Bytes-Used: 1906910
	X-Timestamp: 1407898587.90657
	Content-Type: text/plain; charset=utf-8
	X-Trans-Id: tb49-0032be47ax5a5b80a358ee5d7edfew153
	Date: Fri, 15 Aug 2014 19:20:30 GMT

Now when you go to your container's url (or the CNAME associated with it) you'll see a clean index of all of the included files.

**Edit:** Updated from a previous version before the action developer added the CNAME functionality. Thanks Alex!

[1]: http://www.alexchiri.com/
[2]: https://aptonic.com/dropzone3/
[3]: http://www.alexchiri.com/rackspace-cloud-files-action-for-dropzone-3/
[4]: http://docs.rackspace.com/loadbalancers/api/v1.0/clb-getting-started/content/Generating_Auth_Token.html
[5]: http://docs.rackspace.com/files/api/v1/cf-devguide/content/Create_Static_Website-dle4000.html
