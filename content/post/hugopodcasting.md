---
Author: Alan Bush
Date: 2015-10-01
Title: Podcast Hosting
draft: true
---

## Intro

I've been producing the [Rackspace Office Hours Hangout](http://ohpodcast.com) for over three years now. From the beginning, we wanted to produce an audio-only version of the podcast, which would mean a website, media storage, an RSS feed, and hosting for all of it. WordPress is the easy, relatively simple answer, but it's also significantly more than we needed. We wanted to do this following our own show's repeated theme of prioritizing what is important, what you are good at, and offloading the rest to experts and services to handle the all of the other parts.

<!--- This needs to be a question, or at least make the reader ask the question. Why is this even noteworthy? --->

After taking our own advice, we decided that we needed our site to do three things:

1. Provide a single landing page where customers can go to always {---always---} see the latest (or even live) show.
2. Require minimum maintenance and upkeep.
3. Be virtually free.


[NEED TO ADD SOME MORE DRAMA HERE. WHY IS IT DIFFICULT TO DO THIS ON A STATIC SITE? WHY DO WE NOT WANT TO MANAGE THE OVERHEAD OF A DYNAMIC SITE, ETC.] We've had significant success using the Hugo Blog platform to host our podcast website and RSS feed. Here's how we do it.

## Base components

### Live Hangout

Most of our podcasts involve two hosts located in the same room, and at least one guest who might or might not be in the same location, all conversing about our given topic. To accommodate all of the panelists in a single location, we use Google Hangouts on Air. We're able to use a higher quality camera and audio gear for the presenters who are "live in studio," and Hangouts handles all of the audio/video switching for the remote guests. I've outlined the majority of our gear in a previous article on the topic.

The Hangout is streamed live as we present, but also lives on indefinitely on Rackspace's YouTube account. We've found that the majority of our traffic for each episode comes from YouTube; specifically from search. YouTube is the 2nd most popular search platform (right behind Google) so it is very important for us to share our shows - which are made with the intent of helping cloud users solve problems - can be discovered by our audience via search.

After the show, our Technical Director records several timestamps for important moments in the show. We append these timestamps to the YouTube description, which allows our viewers to jump to the topic in the show that is the most important to each of them. We also use these timestamps to create a table of contents for the podcast recap, which we'll review later.

- Uses equipment listed in previous post
- Hangout lives on YouTube after broadcast
- Use timestamps and full video for embedding

### Convert to Audio

- Audacity
- Import and correct any major flaws
- Export to Ogg and MP3

### Hosting Podcast Files

- Rackspace Cloud Files
- Upload each via Dropzone (Link to previous notes on Dropzone)
- These links will be used in the RSS feed

## Hosting the Website

### Hugo Static Site Generator

-  Static HTML site hosted in Cloud Files (Link to Linuturk)
-  Additional fields in Hugo front matter to capture:
    - MP3/Ogg file locations, file size, podcast duration, tags, summary, etc.
-  Created an audio shortcode to embed the audio in the recap blog
    - Pulls from front matter
    - Displays the player, links to directly download the audio, and file sizes; also has links to directly subscribe to the podcast RSS.
-  The website source code is just text. All static content is stored in separate containers
    - This is especially important if the main site ever goes offline, then it won't take the container with the content with it.

### RSS Feed

-  Hugo creates a basic RSS Feed.
-  I submit that feed to FeedBurner, which then adds metadata for podcasting, and syndicates it out.
-  I submit this FeedBurner feed to iTunes, etc, for syndication.
-  FeedBurner is set to take any embedded mp3 file (i.e. the audio I embedded via Hugo shortcode) and ""
