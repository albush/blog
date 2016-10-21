+++
Author = "Alan Bush"
Date = "2016-06-13T11:45:07-05:00"
Title = "How to ship a book and lose customers in 17 days"
draft = true

+++

[Originally published on Medium](https://medium.com/@albush/how-to-ship-a-book-and-lose-customers-in-17-days-b28bc98c3ef1 "Permalink to How to ship a book and lose customers in 17 days. – Medium")

Last month, the USPS shipped a [book][5] to my sister. The book went from San Antonio, TX to Kansas City, MO. Over the course of 17 days and more than 7700 miles, the package traveled to both coasts, got lost in a loop between Nebraska City and Kansas City, and was unaccounted for on multiple occasions. It was my fault that the package went off course.

{{< img src="http://drops.albush.com/ridiculousjourney.png" title="Here's the full, ridiculous journey." >}}

I take full responsibility for my handwriting. It's never been good, and 15 years in IT has done nothing to improve it. If my handwriting had been legible to the worker at the Post Office, the book would have arrived without delay or comment. But that's not what happened. My sister's zip code 64155 turned into 69155 — that's a 450 mile mistake. That's my mistake. I don't fault the Post Office for my poor handwriting. I absolutely fault them for their policies, procedures, and culture which hindered their ability to be helpful during this situation, even if they wanted to.

I've had a lot of time to think about this situation. While the package was traveling around the country [it was first humorous, then absurd, then frustrating, then maddeningly frustrating, and finally resolved][6]. Now, it's a lesson in customer support; what works, what doesn't, what can **I** do in my customer support job to make sure that I don't create an environment where this happens continually. Please read this as constructive criticism. I don't want this to be too much of a piling on, but rather my own thoughts on what doesn't, but more importantly what does work in customer service. I'd boil it down to three things:

1. Hire people that give a damn;
2. give them tools they need to do their job; and
3. measure them with metrics that provide the right incentives to continue to give a damn about the right things.

#### Impenetrable silos are death to customer support

Each member is just another link in the chain. No one knows anything other than their specific job. "I look at the zip code on the label, and put the package into the corresponding bin." It's like they have blinders on. All of the information they needed to understand the problem, and apply the solution, was in front of them the whole time. My crappy handwriting (it's 2016, I haven't had to write anything of importance in nearly a decade) turned zip code 64155 to 69155. Only one link in the chain was responsible for reading the entire address — the postal sorter at the destination zip code, tasked with getting the package into the truck of the carrier who would ultimately hand the package to my sister. When that team member saw that the zip code obviously didn't match the city and state — let alone the street address — he or she put it on a truck to the city and state listed. End of transaction, on to the next.

{{< tweet 730499629884702720 >}}

Don't forget the big picture. Remind all of the links that they are part of a long chain; links do nothing, chains can accomplish something. It's the lack of the big picture that created the disconnect in the first place. "My job is to look at the zip code." "My job is to look at the street address." "My job is to answer the phone and absorb the wrath of the angry customer while transmuting the call into a 'case.'" I understand the economics of scale behind this. You can't possibly look at _every_ complete address at every stop. Most addresses are correct; this would be a colossal waste of resources.

#### You get what you measure; be careful that what you measure does not provide a disincentive toward poor support

Based on my interactions, I believe that the USPS measures the number of customers that their customer support reps speak to, and the number of "cases" those reps file. If you are a level 1 support rep, your job is to answer the phone when it rings (and it probably never stops ringing), take some abuse from an angry customer, and open a "case" to document the issue. End of transaction, on to the next one. And if you're that customer support rep, and you know you need to answer the phone 40 times during your shift, you're not likely to be willing to spend an extra 5 minutes on the phone empathizing with the customer, or explaining the process to the customer, or even educating yourself on what that process is — because a rigid measurement system has no room for the nuance of great customer support.

Transactional metrics are essential for management to understand support volume trends, staffing and other high managerial level concerns. The front line support staff does not, and should not need to know about these metrics, let alone be graded, rewarded, and promoted against them. Reward curiosity. Does a team member want to know more about the process outside of their specific link in the chain? Great! Show him or her — it can help improve their ability to empathize, prioritize, and ultimately solve customer problems. Don't let your metrics get in the way.

#### You have to hire people that give a damn

Silos and transactional metrics are both hindrances to customer support, but to truly provide service to customers, you need employees that give a damn. To the postal sorter who finds the mislabeled package, discovering the error only presents an obstacle to perfect efficiency in his or her sorting task. This foreign object is in the way of **Productivity**, and must be dealt with as quickly as possible. Throw it onto that truck headed to Kansas City, the people in KC will figure it out. On to the next transaction, hopefully this one will add to my quota.

When you see an error, you owe it to yourself and the customer to take the time to fully understand the error, and find the solution the first time. My package made it to North Platte, NE where it was quickly discovered that the street address didn't actually exist in the suburb of Paxton, NE. Someone in that Post Office looked at the full address and noted that the city and state were all wrong. At least one person made this discovery at the North Platte, NE post office. The package went to that post office twice. Why? Because the carrier route sorter only did the minimum — "this address isn't real, I'll send it back to Kansas, they'll figure it out there." When the package hit Kansas City, that package sorter looked only at the zip code and said "Hey, this zip code isn't around here, I'll send it back to North Platte, they'll figure it out there." 5 minutes of Google Maps searching and writing (or better yet, printing) out a new label, and the package will get to the proper destination without further interruptions. That step never happened. I had to speak to the Post Master for the correct destination Post Office (who, as it happened, had previously worked at the exact Post Office where my book kept returning) before he was able to personally call a friend in Nebraska to have that postal worker physically lay hands on the book and correct the address.

{{< tweet 730395037154992128 >}}

It took weeks of calling, tweeting, and emailing to get to one person who was willing to poke his head out of his silo, break outside of his standard operating procedure, and find the missing package. It took weeks to find that person who gave a damn.

* * *

### How to fix it. Or at least prevent it from being so bad for the next guy

Ok, so to make sure this isn't too much of a piling on against the USPS, here are a few takeaways I learned from this experience. I'm going to make sure that all of the projects I work on take these into consideration.

#### Remove the possibility for human error

The first USPS employee in the chain did not verify that the address was valid. Why does the USPS even allow for the possibility of an incorrect or difficult to read address? Install self-service kiosks to verify the address and print the label for the package. Take away as many chances for mistakes as possible. A self-service kiosk is a 20th century solution. A more contemporary solution would be to take the address directly from the sender's address book on their mobile phone. And why not use USPS APIs to verify that address when the address is entered. The USPS is the authority on addresses; their verification helps not only their own customers, but customers shipping via other carriers.

#### Be there when and where your customers are

USPS has a Twitter account, ostensibly dedicated to helping their customers. However, @USPSHelp is only available Monday through Friday, 9–5, no weekends. The account is essentially a preemptive apology, and a request to contact them via another channel. I'm not sure the point of having a Twitter "help" account, if you don't want to use it to help your customers.

![][7]

This is literally the bio on the @USPSHelps Twitter account.

#### Be Helpful

That's our [motto][8] on the Rackspace Social Support team. Empty interactions don't help. Run interaction through the filter of "is what I'm doing getting the customer closer to a resolution?" If not, it's not in anyone's interest to further that interaction. The biggest culprit for these interactions are in information repetition. Only repeating the known status doesn't help. To be helpful, you need to add more value. "This is your status, and these are options we can take to move forward."

#### **Give your customer support team the tools and resources they need to work on behalf of their customers**

It turns out that the people in operating the @USPSHelp account weren't necessarily trying to be unhelpful, they just can't click links or see screenshots — not even links to other tweets. I understand the need for security, but when your security policies prohibit the employees from doing their job, those policies need to be revisited. Now, the actual humans staffing that account could certainly use their personal phones/internet connections to see the links I sent, again, this requires that the humans are incentivized to do more than the bare minimum.

Other USPS customer support representatives I spoke with were not able to see previous support interactions I'd had. I needed to explain the (ridiculously complicated) issue to each new person I spoke with. The whole team needs to have access to be able to help the customer.

#### If you offer a self-service option, make sure it works

Self-service options are great. More and more customers expect and even prefer to be able to provide their own solution. But that solution has to actually provide a solution. If not, it only ends up angering the customer. I realized what the problem was, Googled it, and found out that I could intercept the package, and send it to a new address. Great. I just needed to give them my tracking number (I've got that) and enter the original destination address (I've got two of those — one that works, even).

When I input my sister's valid address, the system told me that no packages were scheduled to be delivered there. When I entered the address with the incorrect zip code, the system told me that the address is invalid, and I cannot make any routing changes. Their self-service tool, which could have helped me to solve the problem on my own, was incapable of helping anyone in this exact situation. That technical break down made it necessary for me to speak to humans — humans who would go on to tell me my best option was to use the self-service tool.

* * *

If I had the ability to make one change on behalf of the USPS, I'd make sure every address was validated before being accepted by the USPS. Sending a customer away without a shipped package because the customer provided a wrong address is infinitely better than sending that customer away, not knowing that they had provided the wrong address, and causing the package to travel all over the country for weeks. I recently looked at the original receipt from the Post Office. It listed the incorrect zip code. That means that the zip code was misinterpreted there, in the original Post Office. My handwriting was suspect, and one possible interpretation would result in a valid postal address, the other an invalid address. One simple check, before the book goes in the outbox, and this whole ordeal never happens. But that check isn't possible — or at least wasn't offered. I have often wondered what would have happened if I had asked for the Postal Worker to verify the address. Are the Postal Workers expected to, or even able to, verify an address before shipping it?

It's 2016, and I tried to send a physical copy of a book from my house to my sister's house. I used a pen and a piece of paper to compose the address. In 2016. Why did I do that? The Postal Worker immediately entered _at least_ the zip code into her system to print a barcode — I believe it's this barcode that kept getting in the way. I believe that the barcode contained the following instructions for the next link in the chain: "If you're in zip code 69155, read the street address and put it on the truck for delivery; if not, ignore the rest of the address and put the package on the next truck going closer to zip code 69155."


[1]: https://medium.com/
[2]: https://medium.com/m/signin?redirect=https%3A%2F%2Fmedium.com%2F%40albush%2Fhow-to-ship-a-book-and-lose-customers-in-17-days-b28bc98c3ef1
[3]: https://cdn-images-1.medium.com/fit/c/60/60/0*mN0avT81Z0Q6v65z.jpg
[4]: https://medium.com/@albush?source=post_header_lockup
[5]: https://www.amazon.com/Silence-Season-Sungwoo-Chris-Kamler-ebook/dp/B0151WRJD2
[6]: https://storify.com/alanbush/how-to-mail-a-book
[7]: https://cdn-images-1.medium.com/max/800/0*EieJdo-p7fBuzHlp.png
[8]: https://github.com/rackspace/social_media_guidelines
