---
Author: Alan Bush
Date: 2015-10-01
Title: Podcast Hosting
draft: true
---

## Intro

## Base components

### Live Hangout

1. Uses equipment listed in previous post
2. Hangout lives on YouTube after broadcast
2. Use timestamps and full video for embedding

### Convert to Audio

1. Audacity
2. Import and correct any major flaws
3. Export to Ogg and MP3

### Hosting Podcast Files

1. Rackspace Cloud Files
2. Upload each via Dropzone (Link to previous notes on Dropzone)
3. These links will be used in the RSS feed

### Hosting the Website

1.  Hugo
2.  Static HTML site hosted in Cloud Files (Link to Linuturk)
3.  Additional fields in Hugo front matter to capture:
    4. MP3/Ogg file locations, file size, podcast duration, tags, summary, etc.
5.  Created an audio shortcode to embed the audio in the recap blog
    6. Pulls from front matter
    7. Displays the player, links to directly download the audio, and file sizes; also has links to directly subscribe to the podcast RSS.
6.  The website source code is just text. All static content is stored in separate containers
    1. This is especially important if the main site ever goes offline, then it won't take the container with the content with it.

### RSS Feed

1.  Hugo creates a basic RSS Feed.
2.  I submit that feed to FeedBurner, which then adds metadata for podcasting, and syndicates it out.
3.  I submit this FeedBurner feed to iTunes, etc, for syndication.
4.  FeedBurner is set to take any embedded mp3 file (i.e. the audio I embedded via Hugo shortcode) and ""
