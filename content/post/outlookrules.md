+++
title = "How to make Outlook act like Google Inbox"
date = "2016-11-29T12:02:44-06:00"
slug = "how-to-make-outlook-act-like-google-inbox"
author = "alan"
images = [
"http://drops.albush.com/outlook-rawquery.png"
]
news_keywords = [ "Google Inbox", "Microsoft Outlook", "Productivity", "GTD", "Getting things done"]
+++

Last year I shared a colleague's [method to deal with email overload]({{< relref "unbreakemail.md" >}}). I've been using it for a year, and these three simple rules have been a great help for email sanity at work. In my personal life, Google's Inbox has provided a great way for me to "snooze" email that isn't relevant until a certain date. This keeps my inbox clean, and prompts me to action at the appropriate time. I've been looking for something similar in Outlook, for my work email. Today I think I figured it out.

My hack uses Smart Folders, and the "Raw Query" feature in Outlook for Mac 2016; I'm not sure how this equates to Outlook for Windows or Outlook Web Access/Office 365[^1]. The goal is to have one smart folder "Do it now" display unread email only from my inbox (remember, I've triaged that with the 3 rules from Cody's post above so it's only the most relevant), and email I've marked for follow up with a due date of today or earlier. These are the things I need to triage, or work on right now; everything else can wait.

![](http://drops.albush.com/outlook-rawquery.png)

Outlook doesn't support `OR` booleans with their query builder, so we have to use the "Raw Query" functionality. It's the last item in the drop down menu for the type of search. If you're only looking for items that are due, not unread, you can just use this query:

```
com_microsoft_outlook_completed != 1 && kMDItemDueDate < $time.today(+1)
```

That looks for anything flagged for follow up, still incomplete, with a due date of today or later. If you want to include the "Inbox" folder that's already filtered, you'll need to find the folder number. [This post on macwork.co](//www.macwork.co/home/2016/3/16/action-outlook) was extremely valuable for putting this all together. Check it out for the full instructions.

**TL;DR** Use `get selected folder` in Apple Script to retrieve the folder number, replace the 'XXX' in the query below with that folder number.

```
com_microsoft_outlook_folderID == XXX && com_microsoft_outlook_unread != 0 || (com_microsoft_outlook_completed != 1 && kMDItemDueDate < $time.today(+1))
```

Now save that search, and it becomes a Smart Folder. You can name it whatever  you want. Refer to it often. Get work done, when it's time to do it.

[^1]: It looks like OWA doesn't sync the Smart Folders. So YMMV.
