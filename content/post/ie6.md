+++
Aliases = ["ie6"]
author = "alan"
date = "2017-02-23T08:35:15-05:00"
title = "A Blast from the Past: IE6 Compatibility"
images = [
"https://centraldesktophero.files.wordpress.com/2010/02/mktshare.gif?w=480&h=141"
]
tags = [ "#BeHelpful", "central desktop", "browsers", "customer success"]
news_keywords = [ "Customer Success", "Rackspace", "San Antonio", "Career"]
Description = "Facebook just reconnected me with one of my first documented experiences with #BeHelpful."
+++

_Note: My "On this day" over on Facebook just reconnected me with a blog post I wrote 7 years ago, today. Let's hop into the Wayback Machine to understand why the heck I was writing about this 7 years ago._

While working for a health care startup, I researched, evaluated, and eventually implemented a software as a service (SaaS) collaboration platform called Central Desktop (now [iMeet Central](//imeetcentral.com/)) for the company. We used it to collaborate internally and externally on many different projects. Over the course of my time implementing and administering Central Desktop, I relied heavily on their community forums for troubleshooting and answering questions. I gave back to the community, by answering questions and proactively sharing new tips and tricks I had implemented. One day, the trick I wanted to share outgrew their community platform, so I created [Central Desktop Hero](https://centraldesktophero.wordpress.com/) - likely my first foray into WordPress - to give me more control over content publication. Today I learned that site is still online.

In this old post, I reacted to recent criticism of Central Desktop's 2.0 release, and CD's - 100% correct - to end support for Internet Explorer version 6. I ranted a bit about the sorry state of IE6, the sorrier state of those forced to continue to use it, and provided a few tips and tricks to work around what could be a legitimate obstacle. _(2017 Alan is very impressed with 2012 Alan's helpfulness in sharing not just his opinion, but also some very helpful tips for those that needed the additional workarounds.)_

I'm very grateful to have found this old blog post. I know that I've been a practitioner of the \#BeHelpful philosophy for a long time, but it's nice to have a recorded history of it in action. It's fun for me to take a look back at the journey that I've taken since then. About 3 months after I wrote this, I learned that the startup I was working for went out of business. Because of my help in the community forums and the \#BeHelpful attitude of this blog, I was asked to join Central Desktop as employee number 46 to build out an implementation program for their award winning customer success program. I took that experience and moved to Rackspace to build out their proactive customer success program - and then eventually moved into a new role building the technical community at Rackspace - back to the forums. Everything came full-circle. All because I chose to \#BeHelpful.

As I write this, I've found myself looking for [the next step in my career path](//albush.com/post/allgoodthings/). I'm not sure what that will be, but this has served as a great reminder that whatever I do, it will be in the service of \#BeHelpful.
  
So here it is, a 7 year old blog post about a browser that was then 10 years old, in all of its glory.

---

## IE 6 Compatibility: Stop Blaming the People who are Getting it Right

#### [Originally published in Central Desktop Hero: Tips and Tricks from a Central Desktop Nerd](https://centraldesktophero.wordpress.com/2010/02/23/ie-6-compatibiltiy-stop-blaming-the-people-who-are-getting-it-right/)
February 23, 2010


Recently on the CD Forums we’ve seen some chatter about CD 2.0 not working with IE 6, and I say “Great!” Now let’s hope everyone else in the world decides to ditch it.
So many [other people have written](//www.google.com/search?q=why+ie6+must+die) much better explanations for the need to eliminate IE 6, so I won’t go over that ground. But the number one complaint I’ve heard from people who are stuck using a browser which is nearly 10 years old, is that they use [other applications which only support IE 6](//itexpertvoice.com/ad/why-you-cant-pry-ie6-out-of-their-cold-dead-hands/). As it relates to CD, the complaint usually revolves around a partner in collaboration who uses a proprietary software which isn’t compatible with Internet Explorer 7 or greater. That they’re locked into using IE 6 by an oppressive IT regime which won’t even let them update their Facebook pages from time to time, or check out some LOL Cats on their lunch breaks. I feel for you. That must suck.
But, at some point, you have to ask yourself, “who is to blame? Should I blame Central Desktop, for acknowledging that IE 6 is a broken, dying browser full of security holes and unable to provide our customers the best experience? Or should I, rather, direct my righteous indignation at the maker of whatever proprietary software hasn’t, in the last ten years, been able to bring their software up to date?”
Maybe 10 years is a little harsh. IE 7 has been out for 5 years now, however, and that’s 5 years that the maker of whatever proprietary software could have used to only be one iteration of a browser behind. (P.S. They also missed out on the opportunity to pick up any users of Firefox, Safari, Opera or Chrome, etc. etc. etc.)
I guess I’m just amazed that I have seen so much outrage directed at the guys that are getting it right.
How many times have you seen a guy screaming outside of a gas station because they don’t have leaded gasoline for his 1955 Buick? Maybe I should throw a fit and complain to NBC when I can’t watch the 2022 Olympics on my analog television. Maybe I could complain that my Sony BluRay player doesn’t play my BetaMax cassettes. People still use those. They had a better quality than VHS, dang it!

Why are people actually demanding that Central Desktop take a step back, and accommodate an inferior browser that is [losing market share steadily](//www.netmarketshare.com/browser-market-share.aspx?qprid=3&qptimeframe=M&qpsp=109&qpnp=25)? [![](https://centraldesktophero.files.wordpress.com/2010/02/mktshare.gif?w=480&h=141 "mktshare")](//www.netmarketshare.com/browser-market-share.aspx?qprid=3&qptimeframe=M&qpsp=109&qpnp=25)That helps no one. It certainly doesn’t help the 80% of users who use a browser that takes advantage of the latest web standards. It doesn’t help Central Desktop, at all, when they have to spend extra time and money (guess who gets to pick up that extra investment, by the way) to engineer a version that is compatible with a browser that is nearly ten years old. And most importantly, it doesn’t help the few holdouts who produce a product that relies on an archaic browser. If you want to get mad at someone, get mad at the guys that are getting it wrong, and have been for the last decade.

I collaborate over Central Desktop with a vendor who is forced to use IE 6\. The majority of their users use a third party software that “doesn’t support any browser other than IE 6.” The people I work with don’t go near it. But their centralized IT department couldn’t care less about anything but the lowest common denominator. So everyone, in every building, regardless of their actual needs uses IE 6\. I can completely empathize with those who are upset that Central Desktop 2.0 is cramping their style. So, in an effort to not just turn this into a rant, I’ll share a few workarounds ideas.

Install the [portable version of Firefox](//portableapps.com/apps/internet/firefox_portable) on a flashdrive and give it to the point person you work with. Pre-configure it to work with their proxy, set all of the bookmarks she might need to use your CD implementation, and set her loose with it. Portable Firefox, which doesn’t actually install anywhere, can very easily be copied from the flashdrive to the local machine, and executed without a hitch. If you’re geographically limited, you can zip up the whole works, and load it to Central Desktop. Just put some good instructions in the file description.

Of course, the portable Firefox (they also make a Chrome version, but I’ve had problems trying to configure proxies.) method only works if the user can execute a portable app from either the desktop or a flashdrive. This could also meancircumventing another company’s IT policies, which is another issue to consider.

If the portable method doesn’t suit you, try taking advantage of CD’s email capabilities. A user with a limiting browser can participate in discussions, create and comment on tasks, receive files from you (make sure you copy the link that goes directly to the download of the file) or even email new files or discussions to a specific folder, all from the comforts of their email inbox. (Probably Outlook 2000, am I right?) Be sure to check out CD’s [help pages](//helpcenter.centraldesktop.com/help/article/email-in) on using CD through your email. (It looks like some of the help files are down now, as they refresh them for the new UI.)

Along the same lines as email control of CD is the [Outlook Plugin](//helpcenter.centraldesktop.com/help/category/outlook-plugin). With this plugin, a user can sync their calendars and tasks in CD with their outlook calendars and tasks, and also upload files directly into any folder in any workspace they have access to. This method, like the portable Firefox method, is going to be dependent on the level of IT Lockdown the user is experiencing. But if the only argument against a decent browser is ‘we need IE 6 for our software,’ then the IT department might be able to be persuaded to allow the installation of the Outlook Plugin.

One of these options might work for you, if you’re stuck with IE 6\. While I can’t guarantee that any one of these proposals would spell an end to the woes of using a ten year old browser, I can guarantee that trying one of these ideas would be more productive than asking a forward thinking company to take a step backward.
