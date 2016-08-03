---
Date: 2016-08-03T08:55:24-05:00
Title: Slack is the amplifier, not the problem
slug: "ditch-your-behavior-not-your-slack-channel"
---
Some thoughts in response to [a great bit of discussion popping up around Slack](https://www.facebook.com/kr8tr/posts/10157718444703125), some of the annoyances of the platform, and whether or not Slack is delivering on its promise to "be less busy." In his post on Facebook, Rob has a valid point. Slack _can_ help you be more productive, but people can make it less so. More specifically, a lack of purpose and direction allows user behavior to wreck the user experience, leading to lower adoption rates, and an inadequate collaboration experience.

My career has focused on customer success and onboarding - including many years implementing collaboration platforms. This is a topic I've put a lot of thought and effort into. I've been a part of implementations that worked, and ones that didn't. I can tell you that without clearly defined purpose, clearly defined behavioral expectations, and smart environmental decisions, it is difficult if not impossible to successfully roll out new collaboration tools, and realize the benefits of those tools.

## The tool amplifies the behavior

Many of the problems[^1] folks see with Slack are behavioral. Slack is just a medium for annoyance delivery. Slack is the new shiny (I'm sure there's a newer, shinier out there) and too many teams and organizations rush to implement Slack as a solution when there might not even be a problem to begin with.

Why isn't work email filled with cat gifs?[^2] Because we've deemed our work email "serious," and 20 years of cultural norms and corporate edicts have sprung up around the medium. Many of the annoyances of Slack aren't inherent in the tool, they're behaviors. The good news about behaviors is that they can be directed, shaped and changed. Those same behaviors in email have largely been eliminated through social pressure and direct policies. However, email's ubiquity has also ensconced it as the default collaboration tool. Email does not work for collaboration. New tools spring up to fix the problem, and the newest tool is so successful in the short term, that the company rolls out the tool en masse, often without the rules and conventions needed for success.

### How does it go wrong?

Here's an example of one of the ways Slack (and all of the other quickly implemented, swiftly abandoned, collaboration tools) can go wrong.

In this Slack instance, you'll find a large problem with cat-giffing (a generic term for all of the user behaviors that detract from the usefulness of Slack). The purpose for Slack - the problem we're trying to solve with Slack - was never explained. A handful of different teams were using Slack to solve specific, team-related problems. They were using it effectively, and making heavy use of what is arguably Slack's best feature: integrations. But to communicate with another team within the same company or even the same organization with the company, they would have to add another instance of Slack, communicate in the new silo, then bring the information back their original silo. Many of the benefits of an integrated communication platform start to fade.

So: Solution! Let's get *everyone* in the company on Slack. Then the silos won't be there. So they did. And then an email went out and said "Hi everyone in the company, here's your Slack, enjoy." Because we're already using 3-4 other tools to communicate - many of which are less user friendly (the gifs do have a purpose) - employees started to consolidate communication around the shiny, new, user-friendly, platform. Lacking any reason to use Slack, any instruction on how to use it, and without months and years of organically developed behavioral norms around using the tool, cat-giffing ensued.

Lack of direction and lack of communication left users to their own devices. Without a mission-specific reason to use Slack, the most obvious uses become the only uses. Without clearly defined work vs fun zones, new users don't know where to work, or how to work, and Slack eventually starts to look like a playground. This is offputting to new users trying to get their footing with the new tool, and to the decision makers who can't see the work being done behind all of the cat-giffing. Slack is not renewed. The cycle starts over with the next `$shiny_new_platform`

### So what are some solutions?

1. Have a plan. Don't jump into `$shiny_new_platform` just because the cool kids are doing it; have a real, solvable problem, and address it with the platform. Write down that plan. Share it with your team. Enforce the Rules.
2. Function-specific channels. The most successful channels I've been a part of are specific in their function. This is the room where we work through deploying our application to our dev environment. This is the room where we troubleshoot engineering issues in our production environment. And, yes, this is the room where we blow off steam and engage in cat-giffing. Time bound rooms are useful, too.
3. Use the right tool for the job. When sending communications, think through how they need to be sent, and which channel(s) make the most sense to convey the message. Be consistent. Lead by example.
4. Take away the opportunity for misuse. If you can pare down the features in a way that allows you to focus on the business purpose for Slack, do it. Remove the `/giphy` integration from the production monitoring channel.
5. Leave a place for fun. Slack is fun. It's why adoption is quick and thorough. So leave an area where teams can have fun. That's part of being a team. When you're a remote worker, that might be the only social interaction you have with the team. So create a safe space for that. A previous commenter suggested a `#watercooler` channel. I think that's the key. Slack won't let you disable the `#general` channel, so it's imperative to create a space where the cat-giffing can live. This does two things: it provides that social bonding, especially for remote workers, and it sets the tone and boundaries for cat-giffing. It's overwhelming to jump into a Slack channel - `#general` by default - and become overrun by cat-giffing. Keeping the default channels clear helps set the tone, drive adoption, and avoid confusion in the channel.

[^1]: We have no shortage of examples of structural, pricing, and integration problems with Slack. Today, I'm focusing on usability problems, specific to the [conversation](https://www.facebook.com/kr8tr/posts/10157718444703125) which spawned this piece.
[^2]: Work email _is_ full of a thousand people using reply-all to make sure that their recognition of your recognition is recognized, but that's another (behavioral) story.
