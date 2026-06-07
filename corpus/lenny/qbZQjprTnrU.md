# Building product at Stripe — Jeff Weinstein | Lenny's Podcast
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=qbZQjprTnrU
- **Format:** Transcript (auto-generated captions)
---
Watching you operate on Twitter,&nbsp;&nbsp;
you're just breaking this wall&nbsp; between the PM and the customer.
The moment the customer felt compelled enough to&nbsp; go out of their way to talk about some problem,&nbsp;&nbsp;
that's a unbelievable gift. I will leave&nbsp; a meeting to just get one message back&nbsp;&nbsp;
to them. If you're text message&nbsp; friendly with five or 10 of those,&nbsp;&nbsp;
you are going to have so much&nbsp; direct signal that is infectious.
Many people told me I need to&nbsp; ask you about picking metrics.
Well, what was the value that we're trying to&nbsp; produce for the customer and can we measure it&nbsp;&nbsp;
from their perspective? And okay, how do you&nbsp; know you have product market fit? Charts that&nbsp;&nbsp;
showcase things are going up into the right&nbsp; on one hand and then tweets on the other.
You started at Stripe&nbsp; something called study groups.
We show up four to eight people total&nbsp; pretend to be some company with some&nbsp;&nbsp;
outcome problem. Rule one is you do not&nbsp; work at Stripe and rule two is we're not&nbsp;&nbsp;
here to solve any problems. This is just&nbsp; about practicing empathy for the customer.
Today my guest is Jeff Weinstein. Over the&nbsp; course of his six plus years at Stripe,&nbsp;&nbsp;
Jeff was the product lead for Stripe's payment&nbsp; infrastructure teams. We helped scale Stripe&nbsp;&nbsp;
payments to hundreds of billions of dollars in&nbsp; volume a year. He also led PMs and Teams on a&nbsp;&nbsp;
number of zero to one bets at Stripe, and most&nbsp; recently took on the scaling of Stripe Atlas,&nbsp;&nbsp;
which as of the day this podcast launches allows&nbsp; you to incorporate a new company in a single day,&nbsp;&nbsp;
including handling 83B elections, incorporation&nbsp; documents, getting your EIN, share purchases,&nbsp;&nbsp;
and all the things that used to take weeks or&nbsp; months before a company could begin operating.&nbsp;&nbsp;
At this point, one in six new Delaware&nbsp; corporations are started on Stripe Atlas,&nbsp;&nbsp;
which blows my mind. This episode ended up&nbsp; being the longest in my podcast history because&nbsp;&nbsp;
I wanted to basically do an archeology of an&nbsp; incredibly effective and admired product leader.&nbsp;
We spent the entire conversation digging deep into&nbsp; the many skills that Jeff has built that enable&nbsp;&nbsp;
him to consistently build successful and beloved&nbsp; products. We get into his go-go- go plus optimism,&nbsp;&nbsp;
long-term compounding philosophy of building&nbsp; products, how to think about and operationalize&nbsp;&nbsp;
product craft and quality. He shares a popular&nbsp; program that he started at Stripe called Stripe&nbsp;&nbsp;
Study Groups that I think you should steal.&nbsp; We also talk about how to effectively talk&nbsp;&nbsp;
to customers, how to know if you have product&nbsp; market fit for your new product, how to pick&nbsp;&nbsp;
great metrics for your team, what he's learned&nbsp; about getting shit done at a big company. Also,&nbsp;&nbsp;
advice that he's gotten from the founders of&nbsp; Stripe and so much more. This episode is for&nbsp;&nbsp;
anyone who's looking to level up their product&nbsp; building chops in every way. If you enjoy this&nbsp;&nbsp;
podcast, don't forget to subscribe and follow&nbsp; it in your favorite podcasting app or YouTube.&nbsp;&nbsp;
It's the best way to avoid missing future episodes&nbsp; and it helps the podcast tremendously. With that,&nbsp;&nbsp;
I bring you Jeff Weinstein. Jeff, thank you so&nbsp; much for being here and welcome to the podcast.
Thank you Lenny of Lenny's Podcast.&nbsp; I knew what to expect, but it's fun&nbsp;&nbsp;
to see the first name and the podcast all&nbsp; line up. I really appreciate you asking.
So I wanted to start with a quote that I found&nbsp; from you that I think gives a little perspective&nbsp;&nbsp;
into how you think and how you approach the&nbsp; world. So here's the quote. "Very frequently&nbsp;&nbsp;
I would do poorly on tests in school and then&nbsp; the professor would say very reasonably, 'Hey,&nbsp;&nbsp;
I think you should bump down a level to the&nbsp; previous semester's pace,'" and you said,&nbsp;&nbsp;
"I actually know that, that's why I'm in&nbsp; this class. I want to be in the class that&nbsp;&nbsp;
I'm potentially the worst at." This isn't how&nbsp; most people think. This isn't how most people&nbsp;&nbsp;
operate. Usually people want to get good&nbsp; grades, they want to be at the top of their&nbsp;&nbsp;
class. Clearly you have a different approach&nbsp; and a different mindset. Where did this come&nbsp;&nbsp;
from for you and how did this shape the way you&nbsp; think about product and the work that you do?
Some of it was just the fact that I wasn't&nbsp; particularly good at the class and had to&nbsp;&nbsp;
rationalize it for myself in some form.&nbsp; So in retrospect that sounds highfalutin,&nbsp;&nbsp;
but at the time I just wasn't particularly&nbsp; good at the classes I was in. But I think&nbsp;&nbsp;
it comes from growing up. I went to a pretty&nbsp; hippy-dippy K through 12 school in Baltimore,&nbsp;&nbsp;
Maryland where we were really asked to think&nbsp; about why we were in school and to pick any of the&nbsp;&nbsp;
courses that were of interest to us outside of AP&nbsp; programs or grades or any particular requirements.&nbsp;&nbsp;
You really got to choose your own path. And I&nbsp; recall one particular class in high school, which&nbsp;&nbsp;
was somewhat a science class, but it was called&nbsp; the History of Science, and we actually walked&nbsp;&nbsp;
through and studied all of the, at the time,&nbsp; best understood ways the world worked in science,&nbsp;&nbsp;
but then later were turned out to be wrong, right? In the 1500s we believed X, Y, and Z. In the&nbsp;&nbsp;
1600s we believed A, B and C. just very&nbsp; confidently. In 1500s we thought something&nbsp;&nbsp;
and then the 1600s we thought something very&nbsp; different. And so this class was quite impactful&nbsp;&nbsp;
on me where we spent an entire year studying&nbsp; things that are not true. It was fascinating. That&nbsp;&nbsp;
particular teacher employed another trick on us&nbsp; during that class, which was it took the tuition&nbsp;&nbsp;
fee of our school and divided it by the number&nbsp; of hours and wrote the cost on a ticket and then&nbsp;&nbsp;
handed us in the beginning of the year. Tickets&nbsp; for every single one of the classes and he would&nbsp;&nbsp;
stand at the door and you would have to give him a&nbsp; ticket at the end of the class that he thought it&nbsp;&nbsp;
was worth it. And just like that practice of deep&nbsp; intellectual understanding of how people evaluated&nbsp;&nbsp;
something at the time and choosing for yourself&nbsp; to spend the time on it by just the physical&nbsp;&nbsp;
act of handing that ticket to the teacher. That really clicked for me. And so when I got&nbsp;&nbsp;
to college and it was a real college university,&nbsp; people are coming from often quite more rigorous&nbsp;&nbsp;
backgrounds of things that were true. I was a&nbsp; bit unprepared and I remember actually taking&nbsp;&nbsp;
a microeconomics class that was quite advanced&nbsp; and had a close friend and we studied exactly&nbsp;&nbsp;
the same information. We sat and looked at the&nbsp; same cheat sheets, we practiced the same quizzes,&nbsp;&nbsp;
we read the same books, and he got the top&nbsp; grade in the class and I got the bottom and&nbsp;&nbsp;
that's from where that quote came from where&nbsp; the professor said, I think you should bump,&nbsp;&nbsp;
potentially bump down. I was like, "I already&nbsp; know that stuff. I'm interested in this topic.&nbsp;&nbsp;
I'm going to try to improve, but look just because&nbsp; I'm significantly worse than the other kids in the&nbsp;&nbsp;
class that has little to do with if I should&nbsp; leave." And he was particularly cool with it.
This episode is brought to you by Pendo, the&nbsp; only all-in-one product experience platform for&nbsp;&nbsp;
any type of application, tired of bouncing around&nbsp; multiple tools to uncover what's really happening&nbsp;&nbsp;
inside your product? With all the tools you need&nbsp; in one simple to use platform, Pendo makes it easy&nbsp;&nbsp;
to answer critical questions about how users are&nbsp; engaging with your product and then turn those&nbsp;&nbsp;
insights into action. Also, you can get your users&nbsp; to do what you actually want them to do. First,&nbsp;&nbsp;
Pendo is built around product analytics, seeing&nbsp; what your users are actually doing in your apps&nbsp;&nbsp;
so that you can optimize their experience. Next,&nbsp; Pendo lets you deploy in-app guides that lead&nbsp;&nbsp;
users through the actions that matter most. Then Pendo integrates user feedback so that&nbsp;&nbsp;
you can capture and analyze what people actually&nbsp; want. And the new thing in Pendo, session replays,&nbsp;&nbsp;
a very cool way to visualize user sessions. I'm&nbsp; not surprised at all that over 10,000 companies&nbsp;&nbsp;
use it today. Visit Pendo.io/Lenny to&nbsp; create your free Pendo account today&nbsp;&nbsp;
and start building better experiences&nbsp; across every corner of your product. PS:&nbsp;&nbsp;
you want to take your product-led know-How a&nbsp; step further, check out Pendo's lineup of free&nbsp;&nbsp;
certification courses led by talk product experts&nbsp; and designed to help you grow and advance in your&nbsp;&nbsp;
career. Learn more and experience the power&nbsp; of the Pendo platform today at Pendo.io/Lenny.&nbsp;
Today's episode is brought to you by Cycle. The&nbsp; AI-powered feedback platform for product teams.&nbsp;&nbsp;
Is your customer feedback, a tangled mess of&nbsp; Slack threads, survey responses and overflowing&nbsp;&nbsp;
inboxes? Wish that you could know what your&nbsp; customers really need? Cycle unifies all of&nbsp;&nbsp;
your customer interactions from support chats to&nbsp; user research, gong calls and app store reviews&nbsp;&nbsp;
into one neat collaborative space. Cycle's AI&nbsp; then extracts actionable insights on autopilot.&nbsp;&nbsp;
Cycle will learn what you're building so that&nbsp; it can label incoming feedback automatically.&nbsp;&nbsp;
That means you'll get a full voice-of-customer&nbsp; report without manually triaging feedback.&nbsp;&nbsp;
Then simply you Cycle Ask to dig deeper into any&nbsp; topic and generate custom AI-generated summaries&nbsp;&nbsp;
across your entire feedback repository. What makes&nbsp; Cycle different is the way that it lets you close&nbsp;&nbsp;
feedback loops in each release. Feedback is not&nbsp; used just as a way to prioritize what to build,&nbsp;&nbsp;
but also as a tool that creates trust with all&nbsp; stakeholders. Sign up for a free cycle trial&nbsp;&nbsp;
today at cycle.app/Lenny and put your feedback&nbsp; on autopilot. That's C-Y-C-L-E.app/Lenny.&nbsp;
It's really interesting that you went to this&nbsp; liberal artsy hippy dippy school as you described,&nbsp;&nbsp;
which a lot of people bash on. Why spend all&nbsp; this college money and time on a liberal artsy&nbsp;&nbsp;
education and you ended up being really successful&nbsp; in a very technical, highly analytical data-driven&nbsp;&nbsp;
company, and it's interesting that that experience&nbsp; still helped you succeed in this other path.
It did take a change though because I started&nbsp; in... English was my selected major in school,&nbsp;&nbsp;
but then I kept playing with computers and I&nbsp; kept liking math and I looked at the roles of&nbsp;&nbsp;
the backgrounds of the people who were running the&nbsp; types of companies I loved. At the time Facebook&nbsp;&nbsp;
was getting super phenomenally successful. Apple&nbsp; was already on their up and up again and everyone&nbsp;&nbsp;
who was leading those places had technical&nbsp; backgrounds and I liked computers a lot,&nbsp;&nbsp;
so I added computer science as an engineering&nbsp; degree midway through school. So I had to take&nbsp;&nbsp;
the real science classes with the pre-med kids&nbsp; and the rest of it, and I did similarly poorly,&nbsp;&nbsp;
but I did end up with a computer science degree&nbsp; and a liberal arts degree. So it was a journey,&nbsp;&nbsp;
but I had to make a pretty big switch&nbsp; in the middle to get on that path.
I asked you if there was one thing&nbsp; that you'd love to get across in&nbsp;&nbsp;
this podcast. I asked you what would it&nbsp; be and here's what you said. Here's the&nbsp;&nbsp;
first item on this list that you sent me,&nbsp; "Go, go, go ASAP plus optimistic comma,&nbsp;&nbsp;
long-term compounding approach." Can you&nbsp; just talk about what you mean by that?
Yeah, there's two things going on here. So I&nbsp; see the world as immediately we have just such&nbsp;&nbsp;
opportunity to take action in front of us. We can&nbsp; be optimistic and go, go, go as soon as possible.&nbsp;&nbsp;
I think that a lot of life is you get as much&nbsp; furniture as you've room in the house. We will&nbsp;&nbsp;
do the work the night before it's due, so let's&nbsp; just make it due tomorrow. Can we turn tomorrow&nbsp;&nbsp;
into today? So just optimistically seeing if we&nbsp; can just inject energy to go, go, go has produced&nbsp;&nbsp;
surprising results and I think it ignites in&nbsp; other people that same interest and then it feeds&nbsp;&nbsp;
off each other. And that's I think really in my&nbsp; bones from growing up. And then I added over time,&nbsp;&nbsp;
had to learn this longer term, compounding, more&nbsp; strategic mindset where some of the things we want&nbsp;&nbsp;
to accomplish, be it at my startups in the past or&nbsp; at Stripe, they can't be solved in an afternoon.&nbsp;
They're going to require layers of infrastructure&nbsp; and services and applications and UI and&nbsp;&nbsp;
partnerships that really look like that iceberg&nbsp; drawing you see where you just see the top,&nbsp;&nbsp;
but then there's the whole thing underneath&nbsp; and I've had to learn over time to pair&nbsp;&nbsp;
my instinct of like, "Let's get&nbsp; it done today, let's move forward,&nbsp;&nbsp;
let's see what we can get done. Let's make&nbsp; some mistakes, let's try it out." With,&nbsp;&nbsp;
"Where are we going? What needs to be true over&nbsp; time? Where can we always invest? What will we&nbsp;&nbsp;
never regret spending time in?" We'll never regret&nbsp; spending time making the latency of our payments&nbsp;&nbsp;
APIs at Stripe faster. We'll never regret making&nbsp; it more reliable to send 83B election mails to&nbsp;&nbsp;
the IRS. Like we'll never regret those things.&nbsp; So let's just always compound those capabilities&nbsp;&nbsp;
over time. Then the trick is how do you mix this&nbsp; go, go, go attitude with a long-term compounding?&nbsp;&nbsp;
That's something I still struggle with, but I&nbsp; try to purposely balance it more than I used to.
It's such a good way of summarizing just how&nbsp; to be successful in a lot of things. Go, go,&nbsp;&nbsp;
go ASAP, stay optimistic. Focus on long-term&nbsp; compounding growth. Is there an example of&nbsp;&nbsp;
that in action? I know we're going to talk about&nbsp; Atlas a bunch, but I guess is there an example of&nbsp;&nbsp;
that working for you or a product you worked on?
I work at Stripe, which is a infrastructure&nbsp; company. We build things that help businesses&nbsp;&nbsp;
do online commerce in various forms, and I've&nbsp; had a few roles at Stripe. I'm in our beautiful&nbsp;&nbsp;
office here in South San Francisco, one of which&nbsp; was the product person that helped us decide how&nbsp;&nbsp;
we were going to go global and how we were&nbsp; going to offer multiple ways for people to&nbsp;&nbsp;
pay. It turns out there's more than just credit&nbsp; cards in the world. There's small hundreds of&nbsp;&nbsp;
ways that people will naturally want to pay for&nbsp; things online and as a business you're going to,&nbsp;&nbsp;
of course, just want to accept whatever it&nbsp; is people want to pay with. And for the first&nbsp;&nbsp;
seven or eight years of Stripe, well prior to my&nbsp; being here, the incremental country ads and the&nbsp;&nbsp;
incremental new payment methods was relatively&nbsp; flat over time and that was surprising to all of&nbsp;&nbsp;
us who worked here because the world wanted&nbsp; it and we had a lot of people working on it&nbsp;&nbsp;
and we were working very hard, but it wasn't&nbsp; producing returns in the way that we wanted.&nbsp;
And so actually the optimistic as soon as&nbsp; possible go-go attitude was not working. No&nbsp;&nbsp;
matter how much energy we poured into building&nbsp; Thailand payment methods or UK bank transfers&nbsp;&nbsp;
or an in-person payment system in Latin America,&nbsp; we just couldn't rack up points and get it done.&nbsp;&nbsp;
So we had to step back and say, "Well, what is&nbsp; the world going to look like in 10 years? What&nbsp;&nbsp;
was going to need to be true and how can we start&nbsp; to go there now?" Which meant going a lot slower,&nbsp;&nbsp;
building internal platforms, sending people around&nbsp; the world to start to build these payment methods,&nbsp;&nbsp;
uproot their lives, pay for their apartments,&nbsp; get them on airplanes, start using these payment&nbsp;&nbsp;
methods actually in the world. And so it really&nbsp; our line flat line for a while and we're like,&nbsp;&nbsp;
"Okay, is this strategy working? Is it not&nbsp; working?" But then over time we start to see it&nbsp;&nbsp;
switch to nonlinear again and go from whatever&nbsp; it was, 10 payment methods at the time.&nbsp;
And now Stripe accepts over 100. So we got to&nbsp; 50 really quickly and then skyrocketed to 100.&nbsp;&nbsp;
And I remember there being a meeting where we&nbsp; said, "Well, maybe we should just lock everyone&nbsp;&nbsp;
in the basement and see if we can get from 10&nbsp; to 50." That would be the intensity startup go&nbsp;&nbsp;
attitude. But we looked at the individual&nbsp; components of what it meant to get this&nbsp;&nbsp;
done and how long we wanted this to be true&nbsp; for and we had to go a lot slower. That was&nbsp;&nbsp;
a very formative decision where you had to mix&nbsp; the go, go, go with the long-term compounding.
Awesome. Okay, so let's start to delve deeper&nbsp; into some of the specific seals that I hear&nbsp;&nbsp;
you're incredible at and that I've seen you&nbsp; be incredible at on Twitter and LinkedIn and&nbsp;&nbsp;
things like that. So the first is craft, craft&nbsp; and quality. I'm told by many people that you&nbsp;&nbsp;
have a very strong obsession with craft and&nbsp; user experience and quality and even more so&nbsp;&nbsp;
I'm told that you teach people at Stripe how&nbsp; to be obsessed with craft and quality and user&nbsp;&nbsp;
experience in a very systematic way. I feel like&nbsp; this is something a lot of people are starting&nbsp;&nbsp;
to realize is really important and or are trying&nbsp; to get better at, either personally or at their&nbsp;&nbsp;
company. So first of all, let me just ask why&nbsp; is this so important to you? Why do you think&nbsp;&nbsp;
craft and experience and quality is so important?&nbsp; Why do you put so much emphasis on it yourself?
I think I'm really working backwards from failures&nbsp; in the past and avoiding them. And so maybe just a&nbsp;&nbsp;
quick story. I started a company several years ago&nbsp; based on just a personal pet peeve of mine, which&nbsp;&nbsp;
was I was a SQL analyst. Many you listening might&nbsp; have written SQL in the past, maybe the robots&nbsp;&nbsp;
write the SQL for you now, but you still need to&nbsp; write SQL yourself. And every single time I wrote&nbsp;&nbsp;
a SQL query, I wanted to run the same subsequent&nbsp; analysis. I wanted great version control, I wanted&nbsp;&nbsp;
all the cool stuff that GitHub had for code but&nbsp; for writing data code. And so my friends and I&nbsp;&nbsp;
built a little Python tool which basically let you&nbsp; run our style queries. It lets you draw charts and&nbsp;&nbsp;
pivot tables quickly and sharing all this modern&nbsp; SaaS application stuff. But applied to SQL a few&nbsp;&nbsp;
years ago and we turned that into a company. We got some progress, but then there was this&nbsp;&nbsp;
moment one day where we had maybe a couple 100&nbsp; customers and we had an error where we basically&nbsp;&nbsp;
by accidentally shut down the service and it&nbsp; was bricked for 10 or 20 minutes. And at the&nbsp;&nbsp;
time we were hustling in our little dinky office&nbsp; to get the application back online. And we really&nbsp;&nbsp;
were proud of ourselves about how reasonably&nbsp; quickly we did and people went back to using&nbsp;&nbsp;
it. It wasn't a super long outage and we didn't&nbsp; lose any data. We were just high-fiving each&nbsp;&nbsp;
other. And we went about our day and about&nbsp; a year later I realized that that was a...&nbsp;
I missed a huge moment that I should have pounced&nbsp; on, which is that during those 20 minutes,&nbsp;&nbsp;
our customers weren't furious. They weren't&nbsp; emailing us like crazy, they weren't texting us,&nbsp;&nbsp;
they weren't trying to find us on Google&nbsp; Maps and knock on our door and say, "Hey,&nbsp;&nbsp;
I need this thing back online immediately."&nbsp; We heard a couple comments from them,&nbsp;&nbsp;
it was little murmurs. And I didn't realize at&nbsp; the time that was the signal that we did not&nbsp;&nbsp;
have product market fit. And I ended up wasting&nbsp; many more years on that project. And wasting is&nbsp;&nbsp;
a big word. We built amazing software, people&nbsp; liked it, we were able to sell the company.&nbsp;
It helped many of us learn how to really build&nbsp; software. But I'm really trying to avoid that&nbsp;&nbsp;
situation again. And I think craft is a dessert&nbsp; that you get after the meal of does your thing&nbsp;&nbsp;
solve a real problem in the world and are people&nbsp; clamoring, needing it badly? And that's really my&nbsp;&nbsp;
obsession is in finding problems in which people&nbsp; will pause their entire day to solve. They will&nbsp;&nbsp;
leap through the computer to be like, "Oh my God,&nbsp; I have that problem. Do you have a solution?"&nbsp;
And if you focus on that style of product&nbsp; development and we can get into just how do you&nbsp;&nbsp;
listen for that and then turn that into product.&nbsp; Later, you might get the opportunity to really&nbsp;&nbsp;
provide craft and beauty and touches and moments&nbsp; and delight. But certainly there is no amount of&nbsp;&nbsp;
craft, there is no amount of beauty, there's no&nbsp; amount delight or touches you can add to a thing&nbsp;&nbsp;
that will solve the problem we had at our startup,&nbsp; which is that people didn't really need this. And&nbsp;&nbsp;
that's the biggest error is picking something in&nbsp; which people don't really need it. And then going&nbsp;&nbsp;
through these practices of trying to make it great&nbsp; when maybe it shouldn't exist in the first place.
I think a lot of people see all these&nbsp; tweets and messages about just obsessed&nbsp;&nbsp;
with the craft of what you're building and&nbsp; you can easily lose sight of... Nobody even&nbsp;&nbsp;
cares about what you're building. It could be&nbsp; the most incredible experience ever designed,&nbsp;&nbsp;
but if it's not something anyone&nbsp; ever wants, it doesn't really matter.
People don't really get out of bed for their&nbsp; second problem. They get out of bed for their&nbsp;&nbsp;
first problem. And you have to carefully listen&nbsp; and not pitch your customer or your prospective&nbsp;&nbsp;
customer as you're trying to figure this out.&nbsp; And I think this advice, not even advice just&nbsp;&nbsp;
style applies to small companies, big companies,&nbsp; anyone which is people don't want to be pitched.&nbsp;&nbsp;
I'm sometimes on a UXR call with a very&nbsp; well-meaning person or a founder who has&nbsp;&nbsp;
a new product that they want advice on or they&nbsp; want to find customers. And the first thing that&nbsp;&nbsp;
they start talking about when we get on the call&nbsp; is, "Hi, I'm the CEO of X, Y, and Z company. We do&nbsp;&nbsp;
one, two, and three. I want to show you a demo."&nbsp; It's like, "Hold up, I'm a customer. I have..."&nbsp;&nbsp;
What a wasted opportunity you've just done here. I have so many problems, you're guessing ahead of&nbsp;&nbsp;
time, what is my top problem and now that&nbsp; you've anchored and limited to the pitch&nbsp;&nbsp;
you're going to miss, you very likely going to&nbsp; miss the burning problem that they have on the&nbsp;&nbsp;
top of their mind. And it's not the customer's&nbsp; job to interrupt you and say, "Hey, could you&nbsp;&nbsp;
stop your pitch? I want to tell you about my top&nbsp; problem." And you can see this down the stream,&nbsp;&nbsp;
which then companies who launch things, put craft,&nbsp; have a great launch, raise money are then later&nbsp;&nbsp;
gone. And it's because they built something that&nbsp; wasn't solving a burning need. And I think you&nbsp;&nbsp;
can stem it all the way back to they were just&nbsp; pitching rather than sitting in silence and just&nbsp;&nbsp;
waiting for their customer to just open their&nbsp; heart out about what's the most burning thing.&nbsp;
And sometimes I'll prompt our customers, I'll&nbsp; say, "Hey, do you mind just opening up your email?&nbsp;&nbsp;
What's in there?" Or, "If you weren't talking to&nbsp; me right now, what would you be working on?" Or,&nbsp;&nbsp;
"Hey, last week, what grinds your gears? What&nbsp; are you not looking forward to?" Or magic wand,&nbsp;&nbsp;
"What do you wish you could just have off your&nbsp; plate immediately? Forget Stripe, forget about&nbsp;&nbsp;
thing, work on just in your whole life. What is it&nbsp; that you do not want to be doing?" Or, "A massive&nbsp;&nbsp;
opportunity you wish was just one door away?" And&nbsp; it's a little awkward because they don't know why&nbsp;&nbsp;
you're asking that kind of question, but then you&nbsp; just sit there in silence. And for the most part,&nbsp;&nbsp;
if you have amazing customers who are&nbsp; smart and ambitious and are trying to&nbsp;&nbsp;
build their own business, they're going to want&nbsp; to offload their hardest thing to somebody else.&nbsp;
If you've earned trust along the way, and&nbsp; certainly not pitching is a great way of earning&nbsp;&nbsp;
trust. You're just listening. We've learned a&nbsp; lot at Stripe from that. And that's where you&nbsp;&nbsp;
can start to find adjacencies, right? "Well, hey,&nbsp; I don't know if Stripe could really help me with&nbsp;&nbsp;
this, but wouldn't it be cool if we could identify&nbsp; if the person signing up on our site wasn't&nbsp;&nbsp;
fraudulent or is who they say they are or isn't&nbsp; a bot, or are they really a dog on the internet?"&nbsp;&nbsp;
And we're like, "We keep this as the major&nbsp; complaint from all of our customers, but we're&nbsp;&nbsp;
not an identity company." It's like, "Well, I&nbsp; guess now we are because all of our customers who&nbsp;&nbsp;
are trying to build their business all have this&nbsp; problem." And so via silence, you can just create&nbsp;&nbsp;
your roadmap pretty quickly and drop a lot of the&nbsp; long UXR, long survey, long build cycle approach.
So I love where we're going with this. This is&nbsp; where I was going to actually talk about next&nbsp;&nbsp;
is just your ability to talk to customers&nbsp; and user research. It feels very unique,&nbsp;&nbsp;
watching you operate on Twitter, you're&nbsp; just sharing your email constantly,&nbsp;&nbsp;
getting on calls with people constantly. There's&nbsp; this, you're breaking this wall between... That&nbsp;&nbsp;
a lot of people imagine there is between the&nbsp; PM and the lead of a team and the customer.&nbsp;&nbsp;
You're not relying easy research. You're not&nbsp; waiting for someone else to do this work for&nbsp;&nbsp;
you. Talk about just why and how you do this.&nbsp; I think there's so much to learn from just how&nbsp;&nbsp;
you operate in finding opportunities, picking&nbsp; problems to solve by talking to customers.
It's where the business comes from is customers.&nbsp; It is not a long shot hypothesis about why to talk&nbsp;&nbsp;
to them. It's like if they love your stuff, they&nbsp; will tell their friends and pay fair prices for&nbsp;&nbsp;
the product. We're so fortunate through the&nbsp; internet that people announced themselves as&nbsp;&nbsp;
being interested in a topic. Sometimes they're&nbsp; interested in it by posting on Reddit a long&nbsp;&nbsp;
thread or a screenshot of a customer service&nbsp; interaction that bugged them or hopeful that&nbsp;&nbsp;
from their dorm room in country X, someone else&nbsp; in the world has solved the same problem. And&nbsp;&nbsp;
the internet has given us all this absolutely&nbsp; magical forum that you can just yell out the&nbsp;&nbsp;
window and then billions of people could actually&nbsp; listen to what you said out the window. Now,&nbsp;&nbsp;
that's not all the time true for all people&nbsp; in all situations, but dramatically more&nbsp;&nbsp;
true now than ever before in human history. And so the fact that people wouldn't be listening&nbsp;&nbsp;
to their customers and really jumping through the&nbsp; computer to talk to them surprises me. It's like I&nbsp;&nbsp;
always sometimes think, "Do they have some other&nbsp; strategy? Are they so confident in what they're&nbsp;&nbsp;
building that they don't need to hear directly&nbsp; from the people who will be using it?" And I think&nbsp;&nbsp;
some of it is my own fear that I'm going to&nbsp; make the same mistake I've made in the past,&nbsp;&nbsp;
which is build something that people like they're&nbsp; using but isn't solving a burning enough problem&nbsp;&nbsp;
such that they're going to stop their day, they're&nbsp; going to tell their friends, we're going to be&nbsp;&nbsp;
able to sustain the company economically over a&nbsp; long period of time. And that really just comes&nbsp;&nbsp;
from hearing people's most burning problems&nbsp; and then just jumping through the computer&nbsp;&nbsp;
and talking to them takes a little bit of nervous&nbsp; gumption, like walking up to a person at a bar or&nbsp;&nbsp;
cocktail party and saying, "Hi, my name is Jeff." It can be a little awkward, but then you get it.&nbsp;&nbsp;
It's a rush once it starts to work. And once&nbsp; you get the iterative loop that they're excited&nbsp;&nbsp;
to talk to you, they have problems, they see&nbsp; you as a trusted, not salesy, not pitching,&nbsp;&nbsp;
not narrow-minded to just my product and&nbsp; my position, but I'm here to hear about all&nbsp;&nbsp;
of your problems and see where we can help.&nbsp; Not promising we can help solve everything,&nbsp;&nbsp;
but let's listen. That is infectious, both between&nbsp; the customers and internally. And so I'm able to&nbsp;&nbsp;
bring more people into that practice. At Stripe,&nbsp; I'm able to quickly grab an engineer and hop on&nbsp;&nbsp;
a call. I can forward a message over to a Slack&nbsp; group. And they know that because the customer's&nbsp;&nbsp;
speaking directly, it somewhat trumps everything&nbsp; that's happening during the day. We could go to&nbsp;&nbsp;
our meeting where we're going to guess what the&nbsp; customer wants or we could talk to them directly.&nbsp;
And you have to use a little bit of art to decide&nbsp; which customers you want to listen the closest to.&nbsp;&nbsp;
But even at Stripe's scale, where we're dealing&nbsp; with many millions of businesses and many hundreds&nbsp;&nbsp;
of millions of consumers on the other end of&nbsp; those businesses, you can pattern match relatively&nbsp;&nbsp;
quickly. What are the styles of customers&nbsp; that represent where the world is going, the&nbsp;&nbsp;
most ambitious, the most technical, the fastest&nbsp; growing, the most detailed. And you don't need&nbsp;&nbsp;
10,000 of those people to talk to. If you're text&nbsp; message friendly with five or 10 of those, you are&nbsp;&nbsp;
going to have so much direct signal about where&nbsp; to go that you forget how you did it in the past.
I love these. So I'd love to learn more about&nbsp; these tactics that you've found helpful.&nbsp;&nbsp;
So you've shared this idea of silence,&nbsp; talking to someone and just being silent,&nbsp;&nbsp;
and I forget the phrase you used, but just like&nbsp; ideas emerge, like your whole road map can emerge&nbsp;&nbsp;
from that silence. So let me share a few of&nbsp; the things you shared so far and I'm curious&nbsp;&nbsp;
what else. Two is tweeting just like, "Hey,&nbsp; I'm looking to improve Atlas right now. What&nbsp;&nbsp;
bugs do you have? Here's my email address."&nbsp; You talked about text messaging, just like,&nbsp;&nbsp;
"Hey, can I get your number? And I'll just text&nbsp; you when I have questions." If there's anything&nbsp;&nbsp;
else to add to these, that'd be awesome.&nbsp; And then what else have you found? Just&nbsp;&nbsp;
ways to actually get to a customer and&nbsp; find opportunities that are important.
Speed is an important one, which is just reducing&nbsp; the time between the moment the customer felt&nbsp;&nbsp;
compelled enough to go out of their way to talk&nbsp; about some problem. They're busy, there are snacks&nbsp;&nbsp;
to eat, they have families, they have other things&nbsp; to do. There's a lot going on in the world, a lot.&nbsp;&nbsp;
Your dumb product, it's amazing that they&nbsp; would spend any of their time discussing it&nbsp;&nbsp;
at all. I mean, most of the time if you don't&nbsp; like something, you just move along. You just&nbsp;&nbsp;
apathetically, silently move forward in&nbsp; the world. And so the fact that someone&nbsp;&nbsp;
took their finite time to succinctly with&nbsp; curiosity, communicate to the world or you&nbsp;&nbsp;
about your product, that's a unbelievable gift. That should be P-zero alert level intensity. And&nbsp;&nbsp;
so I will leave a meeting, I will change what&nbsp; I'm doing to just get one message back to them.&nbsp;&nbsp;
Even if it's, "Hey, I got this. I'm about to go to&nbsp; dinner. Can I hit you up tomorrow?" They're like,&nbsp;&nbsp;
"Oh yeah, thank you. Awesome. I can't even&nbsp; believe you responded." That puts us in the&nbsp;&nbsp;
camp of on the right trajectory where they're&nbsp; going to feel that they have a almost secret&nbsp;&nbsp;
portal between this big brand of a company and&nbsp; another human who's just actually curious...
... brand of a company and another human&nbsp; who's just actually curious what's going on,&nbsp;&nbsp;
that's night and day. And it's also, fun fact,&nbsp; tip, when people are really hot on an issue and&nbsp;&nbsp;
it could blow up on social or they're going to&nbsp; start becoming a detractor, we make mistakes,&nbsp;&nbsp;
we have SLA breaches, we have errors, you're&nbsp; going to want to get on that stuff fast. And in&nbsp;&nbsp;
those situations, my bar for how we will respond&nbsp; to those folks is not to just solve the problem,&nbsp;&nbsp;
but it is to turn them into a promoter,&nbsp; and most of the time we're able to,&nbsp;&nbsp;
even if there was a pretty relevant issue. I remember one time at Atlas, we had this&nbsp;&nbsp;
bug in which for a handful of our legal&nbsp; docs, they were handing out let's say,&nbsp;&nbsp;
25 shares rather than 25% of the shares. We&nbsp; dropped the percentage sign, and thankfully&nbsp;&nbsp;
a founder noticed this in the docs and tweeted&nbsp; about it. My heart paused and I was like, "Oh no,&nbsp;&nbsp;
this could be a really serious issue." And we&nbsp; were able to fix it and regenerate the documents&nbsp;&nbsp;
relatively quickly for everyone that was impacted.&nbsp; And I was thinking to myself, "Wow, we really let&nbsp;&nbsp;
this person down. We have one job to do, which&nbsp; is to get their company right and we didn't."&nbsp;
And that person was incredibly gracious about&nbsp; the situation and said, "Anytime you want me&nbsp;&nbsp;
to just read your docs, I'd be happy to. I have&nbsp; a law degree. I care about this topic. I want&nbsp;&nbsp;
to brainstorm with you about ways that Atlas&nbsp; could do more document creations." I was like,&nbsp;&nbsp;
"Wow, I can't believe I was in this sort&nbsp; of defense position, and now we've gained&nbsp;&nbsp;
a friend in the world who can be eyes and ears&nbsp; and brainstorm with us." And the team maintains&nbsp;&nbsp;
a really close relationship with that person as&nbsp; they do with many, many founders who use Atlas.&nbsp;
And so, just again, we're so quick to put&nbsp; the outside world in this other camp where&nbsp;&nbsp;
we need to touch it with kid gloves and treat&nbsp; it as a big blob and a cohort and a statistic,&nbsp;&nbsp;
when it is a human with a problem who likes&nbsp; snacks, who is busy, and it's fun to do and&nbsp;&nbsp;
it turns out to be an incredibly easy,&nbsp; fast way to figure out what to build.
There's a bunch of stuff I want to follow up&nbsp; here. One is, people may be hearing this and like,&nbsp;&nbsp;
"Oh my God, I'd be overwhelmed with feedback&nbsp; and people to fix problems for and bugs and&nbsp;&nbsp;
texting of people." They're just like,&nbsp; "There's so many people that potentially&nbsp;&nbsp;
I'd have to be interacting with." How do&nbsp; you try to narrow that down? I know Atlas&nbsp;&nbsp;
is a very highly adopted product. There's&nbsp; a ton of people, there's probably bugs,&nbsp;&nbsp;
often people sending you feedback. How&nbsp; do you pick the people to zero in on?
I think there are two parts to this. One, what a&nbsp; problem to have. Of all the problems in the world,&nbsp;&nbsp;
"I'm overwhelmed by customer interest," is&nbsp; on the top list of problems I want to have.&nbsp;&nbsp;
I think most entrepreneurs would purchase that&nbsp; problem as a state. And so, if you're in it,&nbsp;&nbsp;
I think, take a deep breath and look at the&nbsp; sunrise or sunset and just enjoy the fact that&nbsp;&nbsp;
you've built something that is meaningful enough&nbsp; that people would spend their time. Again, there&nbsp;&nbsp;
are amazing snacks that they could be spending&nbsp; the time on otherwise, so that's a huge deal.&nbsp;&nbsp;
And then two, you need the art. There's&nbsp; an art and science to picking where to&nbsp;&nbsp;
go deep. I will happily respond to folks&nbsp; with, "I really appreciate that. Do you&nbsp;&nbsp;
mind sending me a screenshot or a video?"&nbsp; And some of them don't. Okay, that's fine.&nbsp;
You kind of get a sense of quickly looking at how&nbsp; they wrote about it or just pattern matching how&nbsp;&nbsp;
detailed they were, or how much they seem that&nbsp; they want to engage and kind of balance it that&nbsp;&nbsp;
way. Otherwise, you can tell folks, "This&nbsp; is really awesome. Do you mind sending me&nbsp;&nbsp;
an email with three to five bullet points about&nbsp; the details of how you got to this issue?" And&nbsp;&nbsp;
that's not a 30-minute meeting. You don't need&nbsp; to blow up your whole life to get on the phone&nbsp;&nbsp;
with them. It's not a huge homework assignment&nbsp; to them, but it's enough structure that it will&nbsp;&nbsp;
self-select those who want to go deep, and then&nbsp; from there, you really do owe it to them to follow&nbsp;&nbsp;
up if they're going to be that detailed. And&nbsp; at that point, you really have made a product&nbsp;&nbsp;
friend for life and you'll kind of continuously&nbsp; go back to them. So you have to kind of tune it.&nbsp;
I also will bound some of these efforts, so I'll&nbsp; just completely make up one day a program. So,&nbsp;&nbsp;
"Hi, Stripe's doing a bug-finder program." I made&nbsp; that up as I was driving to work one morning,&nbsp;&nbsp;
tweeted it, was curious if anyone would send&nbsp; anything. "We'll be taking videos for the next&nbsp;&nbsp;
three days to go super deep." And people are&nbsp; like, "Oh my goodness, I would love to be part&nbsp;&nbsp;
of the Stripe bug-finder program. May I apply?"&nbsp; I'm like, "Oh, it's very selective. But yes,&nbsp;&nbsp;
of course for you." It's just giving people&nbsp; permission through a program, even if it is&nbsp;&nbsp;
deeply arbitrary, I find helps with bounding it,&nbsp; and then later I can follow up with the world,&nbsp;&nbsp;
"Hey, we ran our first program, we got 65 videos,"&nbsp; which we did. "We found dozens of issues," which&nbsp;&nbsp;
we did. It was an incredibly valuable use of our&nbsp; time and it really came from just a single tweet.
Something I saw you mention somewhere is&nbsp; that you only pay attention to feedback from&nbsp;&nbsp;
people that are paying customers and ignore&nbsp; everything else. Can you talk about that?
People who build things for people tend to be&nbsp; empathetic and interested and curious folks who&nbsp;&nbsp;
have friends, and then those friends want to use&nbsp; your stuff because they know you and they like&nbsp;&nbsp;
you and they'll have good feedback. But you need&nbsp; to figure out, is that actually your customer,&nbsp;&nbsp;
or is that your friend trying it? Who is actually&nbsp; your target customer exactly? Not a company or a&nbsp;&nbsp;
segment, not digital natives that are X big.&nbsp; I'm talking about Sarah in this department,&nbsp;&nbsp;
who has these tabs open and just faced this&nbsp; problem and needs to solve it by 4:00 PM.&nbsp;&nbsp;
That level of specificity. If that's your&nbsp; customer, and I'm talking mostly about B2B,&nbsp;&nbsp;
which is where I spend a lot of my time as the&nbsp; social network, B2C stuff I have less intuition&nbsp;&nbsp;
on, they're very willing to exchange money for&nbsp; solving their problems, incredibly so. Oftentimes,&nbsp;&nbsp;
if you listen with enough silence, they&nbsp; might even say, "I'll pay you money to solve,&nbsp;&nbsp;
blah." If you sit there long enough in silence. And so, you could listen to your friendly friend&nbsp;&nbsp;
who you got to play with your beta version&nbsp; and they'll say they liked it and they will&nbsp;&nbsp;
click around. But that is extremely different from&nbsp; Sarah, who has the actual problem and is willing&nbsp;&nbsp;
to pay. And it is so tempting to go down the first&nbsp; path with the friend group that I sort of needed a&nbsp;&nbsp;
rule, which was like, "Okay, rather than..." I was&nbsp; like, "Well, don't pay attention to that quite as&nbsp;&nbsp;
much. Really pay attention to, who is your target&nbsp; customer and are you in a fast iteration cycle&nbsp;&nbsp;
for them and are they telling their friends?" But that wasn't enough, because people are so&nbsp;&nbsp;
drawn, myself included, drawn to the friendliness&nbsp; that I just set a rule, which is, "We discount all&nbsp;&nbsp;
of that feedback from our friends to zero." That&nbsp; is not of interest to us. We don't even write it&nbsp;&nbsp;
down. It's just not part of what we're talking&nbsp; about at all. We are only interested in Sarah,&nbsp;&nbsp;
our target customer, and can we get her to solve&nbsp; whatever the problem is as quickly as possible,&nbsp;&nbsp;
as jangly as possible and go from there? And then the paying part is a forcing&nbsp;&nbsp;
function because again, even with Sarah, because&nbsp; you're paying attention to her and solving her&nbsp;&nbsp;
problem a bit, she'll say, "Of course, oh, this is&nbsp; great. I want feature X, Y and Z. Can it do one,&nbsp;&nbsp;
two, and three?" Naturally, she would say that.&nbsp; But if you said, "And by the way, this thing is&nbsp;&nbsp;
$10,000. We'll happily refund your money 100% the&nbsp; second you don't like it," she might say, "Whoa,&nbsp;&nbsp;
whoa, wait a second. Yeah, I like this thing, but&nbsp; not $10, 000. For $10,000, it would need to solve&nbsp;&nbsp;
X." And you're like, "Oh, there it is." That&nbsp; was actually what the thing that was of value,&nbsp;&nbsp;
and we were all kind of dancing around&nbsp; this. It's useful, we're on the right track,&nbsp;&nbsp;
and because I've fallen down that path&nbsp; myself so many times, I just set a rule.
This is great. I was actually going to ask.&nbsp; This technique of using silence, to help&nbsp;&nbsp;
people actually practice it, you just shared this&nbsp; quote of, "For you to pay $10,000 it would've to&nbsp;&nbsp;
do X." That's a really cool line to use. Is&nbsp; there any other advice there of just how to&nbsp;&nbsp;
practice this idea of creating silence to help a&nbsp; potential customer share what they actually need?
I encourage people to take an improv training&nbsp; class or two, just to get people out of their&nbsp;&nbsp;
skin a bit. By the way, this advice applies&nbsp; to big companies also, not just small ones.&nbsp;&nbsp;
And we have issues, and I hear other larger&nbsp; companies have issues where a big company will&nbsp;&nbsp;
say, "Hey, we're an enterprise and we're going to&nbsp; pay you this big contract. All you need to do is&nbsp;&nbsp;
build features one, two, three, four, five, six,&nbsp; seven, eight, nine, and go through security steps,&nbsp;&nbsp;
A, B, C, D, E, F, G." And this siren song of the&nbsp; big three-year contract of your first enterprise&nbsp;&nbsp;
buyer, even when you're already big, you&nbsp; can go from Fortune 1000 to Fortune 500 to&nbsp;&nbsp;
Fortune 10 to Fortune 1. There's always&nbsp; more. There are so many stories of the&nbsp;&nbsp;
rug being pulled in the middle and they never&nbsp; actually use it and the contract never lands.&nbsp;
Same in partnerships. And so, I would say the same&nbsp; thing, which is, "If we're super serious about&nbsp;&nbsp;
this, send us $1 million. Wire us $1 million.&nbsp; We'll happily wire it back anytime you need it,&nbsp;&nbsp;
but let's actually put some stake in the ground&nbsp; about the value." And I find that in the cases in&nbsp;&nbsp;
which they're like, "Whoa, wait a second, no,&nbsp; absolutely not. We can't commit here." That's&nbsp;&nbsp;
really a good signal because you're about to spend&nbsp; a huge amount of time building something that&nbsp;&nbsp;
might not ever be used, and that's the majority&nbsp; case I hear. Or you might get the opposite, which&nbsp;&nbsp;
is, "Sounds great. Let's make sure our teams are&nbsp; trained on it faster. How can we get you to our&nbsp;&nbsp;
office to explain it? We need it to really work&nbsp; with this system we haven't talked about yet. And&nbsp;&nbsp;
now that we're paying, we want it even faster." And so, I find that it puts a fork in the road&nbsp;&nbsp;
towards faster success or avoiding the non-success&nbsp; case. And even at Stripe scale, I've heard our&nbsp;&nbsp;
founders somewhat push this methodology on&nbsp; us, where one from the outside might think,&nbsp;&nbsp;
"Well, it's a 8,000 person company. Surely they&nbsp; have just regular ways of building things for&nbsp;&nbsp;
larger customers, and we too need these style of&nbsp; commitments if we're going to go off roadmap."
So a big lesson you're sharing here is&nbsp; essentially, make sure people are ready&nbsp;&nbsp;
to pay for something that they're asking&nbsp; for. That is the ultimate sign that they-
And by the way, ready to pay is different&nbsp; than paying. Significantly different,&nbsp;&nbsp;
significantly different. I've also thought&nbsp; of, "Well, as long as they're ready to pay&nbsp;&nbsp;
and they said they would pay and they look at the&nbsp; contract, we should feel good." That is not the&nbsp;&nbsp;
same as paying. Paying is an independent group&nbsp; of people saying, "My problem is burning enough&nbsp;&nbsp;
that I'm willing to exchange something I have&nbsp; that has value for the promise of what you're&nbsp;&nbsp;
going to do." And now it's a real commitment.&nbsp; That is extremely different than ready to. So&nbsp;&nbsp;
I will often be on the phone or video, whatever&nbsp; with a founder and I will have them practice&nbsp;&nbsp;
charging me. I'll just say, "Hey, I'm just&nbsp; a friend. I'm trying to help you out. It's a&nbsp;&nbsp;
little bit self-serving because I work at Stripe&nbsp; and I want to get feedback on our products."&nbsp;
I'll say, "Feel free to sign up for any invoicing&nbsp; or payment service. I don't really care which&nbsp;&nbsp;
one. You're welcome to choose Stripe if it's easy&nbsp; enough for you, I'd love to hear your two cents,&nbsp;&nbsp;
and send me an invoice or a payment link&nbsp; for $1 right now, right now. That way,&nbsp;&nbsp;
when it comes time to actually charge your first&nbsp; customer, it won't be your first time. It won't&nbsp;&nbsp;
feel weird. You'll have already done this, you&nbsp; already have a dollar in your account, you already&nbsp;&nbsp;
have your logo on the top right of the invoice.&nbsp; It'll feel great." And I probably could go through&nbsp;&nbsp;
my email inbox and just see $1 receipts to random&nbsp; people because I'm just so convinced that the&nbsp;&nbsp;
difference between paying and willing, ready, I&nbsp; thought they would pay is night and day different.
Yeah, there's this term, willingness to&nbsp; pay that I feel like it should change,&nbsp;&nbsp;
as you're saying, to just cross&nbsp; that willingness to even just-
Paying.
Paying, exactly.
Yeah. And we can refund the money. There's&nbsp; no issue at all. Just other tricks on how to&nbsp;&nbsp;
get people going is, ask them about their regular&nbsp; life as a human, "What did you do yesterday?" And&nbsp;&nbsp;
they'll be like, "Oh, at work?" I'm like, "Or not.&nbsp; Whatever." And people, they'll start to spill,&nbsp;&nbsp;
they'll just start to spill and eventually they'll&nbsp; get to their biggest problem pretty quickly.
Let's talk about metrics, going in a&nbsp; different direction. Many people told me&nbsp;&nbsp;
I need to ask you about picking metrics and&nbsp; the importance of metrics and how you think&nbsp;&nbsp;
about metrics. So let me just maybe start&nbsp; with a question of, just why do you think&nbsp;&nbsp;
picking the right metric and why are metrics&nbsp; so important in building successful products?
I somewhat walk around with the belief that&nbsp;&nbsp;
the product manager's responsibility is to produce&nbsp; product market fit. And okay, how do you know you&nbsp;&nbsp;
have product market fit? Charts that showcase&nbsp; things are going up into the right on one hand,&nbsp;&nbsp;
and then tweets on the other. So metrics like&nbsp; quantitative and qualitative, and I really see&nbsp;&nbsp;
them as deep siblings and equals, you really need&nbsp; both. It's not oh, OKRs versus something. There&nbsp;&nbsp;
are some things you want the texture of the person&nbsp; on video showing how complicated a thing was. And&nbsp;&nbsp;
then also, we're trying to make an economically&nbsp; viable system that we can run at large scale and&nbsp;&nbsp;
you can't keep all that stuff in your head and&nbsp; need to measure it. And so, I think metrics at&nbsp;&nbsp;
their best are a numerical representation of&nbsp; the value we're providing for the customer.&nbsp;
One could measure anything. You can just start&nbsp; counting events and log lines. We've made it&nbsp;&nbsp;
incredibly cheap to count stuff. And so, now&nbsp; we have this big privilege of choosing what&nbsp;&nbsp;
to measure. And I really just try to map it all&nbsp; the way back to, "Well, what was actually the&nbsp;&nbsp;
value that we're trying to produce for the&nbsp; customer and can we measure it from their&nbsp;&nbsp;
perspective?" Whereas I think it's natural,&nbsp; both because when you work inside of a company,&nbsp;&nbsp;
you're just thinking internally, but also the&nbsp; way that the metrics are collected inside your&nbsp;&nbsp;
application to be more internal-oriented. How many&nbsp; people logged in? Okay, that's a fine measure,&nbsp;&nbsp;
but how many people accomplished what they&nbsp; were trying to do after they logged in,&nbsp;&nbsp;
is not just necessarily sitting there as a&nbsp; single event in your database. You have to&nbsp;&nbsp;
think about it a bit. Another reason why I spend&nbsp; a lot of time crafting a small number of these&nbsp;&nbsp;
metrics is, they force trade-offs and decisions. So we could all sit around all day and say, "Hey,&nbsp;&nbsp;
I heard all these customer problems, we should&nbsp; build X, Y, and Z." And another person could&nbsp;&nbsp;
absolutely reasonably say, "Well, I heard from&nbsp; these customers, we should build one, two and&nbsp;&nbsp;
three." And they're all true. We could have a lot&nbsp; of success in both, but the majority case is that&nbsp;&nbsp;
we don't build either and we sit around and&nbsp; argue and bicker and we go slowly. "What are&nbsp;&nbsp;
we going to do to naturally, organically every&nbsp; day, orient a larger group of people in the right&nbsp;&nbsp;
direction and see if our tactics are generating&nbsp; progress over time for a customer from their&nbsp;&nbsp;
perspective?" And metrics on the left and a series&nbsp; of tweets on the right is a pretty great combo.&nbsp;
Here's an example. A couple years ago I had been&nbsp; working in our payments group at Stripe for a bit,&nbsp;&nbsp;
and then I started working on some of our&nbsp; banking and incorporation services. In Atlas,&nbsp;&nbsp;
when I started working on it, it had had some&nbsp; success. It had already existed for four or&nbsp;&nbsp;
five years prior to me spending time on it. But&nbsp; when I started to look at the support tickets,&nbsp;&nbsp;
people were pretty unhappy frequently. They had&nbsp; a DocuSign stuck in their email box. They needed&nbsp;&nbsp;
a co-founder's address, but they didn't know&nbsp; their co-founder's address. They couldn't log&nbsp;&nbsp;
into the dashboard to figure out their 83(b)&nbsp; manual filing instructions. And we saw this&nbsp;&nbsp;
basically in the first week of spending time&nbsp; on Atlas. I was just like, "Just show me all&nbsp;&nbsp;
the support tickets. Are they happy support&nbsp; tickets? People writing in being like, 'Oh,&nbsp;&nbsp;
I love this service, it's absolutely fantastic.&nbsp; Can you just do A, B, C more for me?' Or are they&nbsp;&nbsp;
sad support tickets?" And they're like, "Oh&nbsp; my God, they're all sad support tickets."&nbsp;
And so, we're just asking ourselves, "Well, why&nbsp; would someone recommend Atlas to a friend?" I was&nbsp;&nbsp;
like, "Well, it would have to accomplish A,&nbsp; B and C activities for them. It would have to&nbsp;&nbsp;
get their company, it would have to handle getting&nbsp; their tax ID from the IRS. It'd have to handle all&nbsp;&nbsp;
the downstream administrivia." But surely, if&nbsp; they had a bunch of support tickets at the end,&nbsp;&nbsp;
they're not going to go tell their friends to&nbsp; use this thing. We could measure all of the&nbsp;&nbsp;
intermediate parts, we could measure the success&nbsp; rate and the frequency of incorporation services&nbsp;&nbsp;
and we do all those things, but if you looked&nbsp; at the support tickets, there's just no way if&nbsp;&nbsp;
you had a support ticket, you would recommend it&nbsp; to a friend. And so, we suggested this metric to&nbsp;&nbsp;
ourselves, companies that have no support&nbsp; tickets through the incorporation service.&nbsp;
The whole process, from the moment you start the&nbsp; application open, actually the first page load&nbsp;&nbsp;
at the very beginning, all the way through the&nbsp; process waiting for the government, waiting for&nbsp;&nbsp;
the IRS, and we give you two more weeks to write&nbsp; into support. We give an extra buffer two weeks.&nbsp;&nbsp;
And if you get through that whole thing with no&nbsp; support tickets, that's a yes. If you have any&nbsp;&nbsp;
number of support tickets, that's a no. And we&nbsp; just looked at the percentage of founders that&nbsp;&nbsp;
were going through the service with zero support&nbsp; tickets, which is very different than looking at&nbsp;&nbsp;
an average, right? You could have the average&nbsp; as 0.3, but that doesn't necessarily mean that&nbsp;&nbsp;
they're getting to 0.2 is going to cause them&nbsp; to tell their friends more. And we looked, and&nbsp;&nbsp;
only 15% of founders were getting through Atlas&nbsp; with zero support tickets through that metric.&nbsp;
And I just thought, "Okay, well let's just drive&nbsp; that number way up, and let's look at the support&nbsp;&nbsp;
tickets aside what people are needing and we'll&nbsp; bake it into the product, and presumably it'll&nbsp;&nbsp;
fix it. People will like that more and then tell&nbsp; their friends." And over about 18 months, we took&nbsp;&nbsp;
that number from 15% to 85. We basically just&nbsp; flipped it. And you can look at the market share&nbsp;&nbsp;
plotted on the same timeframe and it's the same&nbsp; shape. And I think you have to find a measure&nbsp;&nbsp;
by which it speaks directly to what the customer&nbsp; wanted, and that if you accidentally leaked your&nbsp;&nbsp;
dashboard to them, your customer would be ecstatic&nbsp; to learn that that's what you were measuring the&nbsp;&nbsp;
whole time. If we were to showcase the internal&nbsp; Atlas metrics, which we often just screenshot&nbsp;&nbsp;
and publish, I think they'd be pretty happy&nbsp; to hear that we were spending all of our time&nbsp;&nbsp;
making sure that none of them had support tickets. And it was incredibly encouraging and motivating&nbsp;&nbsp;
to the engineers on the team because we could&nbsp; just assign them a topic. "Hey, look at all&nbsp;&nbsp;
these support tickets. Why don't you come up with&nbsp; the product spec, the scope, the solution? Oh,&nbsp;&nbsp;
want to learn more? Just reply to the support&nbsp; ticket email, figure out what they need." And so,&nbsp;&nbsp;
we kind of turned all of the engineers on the team&nbsp; into PMs to go and one issue at a time, figure&nbsp;&nbsp;
out what needed to change and build products for&nbsp; it. And that's where we pushed forward on 83(b)&nbsp;&nbsp;
elections, automating it, sending in the mail&nbsp; for folks. We built our own signing service.&nbsp;
We turned everything into a click. We did just did&nbsp; sort of the obvious things we saw in the tickets,&nbsp;&nbsp;
but as the PM, I was able to just sort of,&nbsp; not on autopilot, but really sit back and have&nbsp;&nbsp;
content full conversations with engineers who&nbsp; were bringing solutions and ideas for product,&nbsp;&nbsp;
rather than one person going through all of the&nbsp; potential ideas, scoping them and assigning them.&nbsp;&nbsp;
And because it was based in what people were&nbsp; saying and wanted, it was very motivating for&nbsp;&nbsp;
everyone on the team. So somewhat long answer,&nbsp; but figuring out something in which every day&nbsp;&nbsp;
we can wake up and look at the same metric&nbsp; and with some confidence know what to do,&nbsp;&nbsp;
is so much better than, "Let's figure out what&nbsp; to do each month, and starting from scratch."
I think this is amazing and important advice,&nbsp; just the power of a single metric that everyone&nbsp;&nbsp;
on the team can understand, rally around and use&nbsp; to prioritize the work they're doing. I've seen&nbsp;&nbsp;
exactly the same sort of impact. Funny enough,&nbsp; Airbnb, one of the teams actually had a metric&nbsp;&nbsp;
sort of like this, basically reducing the people&nbsp; contacting Airbnb with support issues. But what&nbsp;&nbsp;
ended up happening is, their team started just&nbsp; making it harder to contact support because&nbsp;&nbsp;
they're like, "Maybe they don't need to contact&nbsp; support about all these trivial issues, so maybe&nbsp;&nbsp;
let's encourage them to figure it out themselves."&nbsp; Is there anything you've learned about to try&nbsp;&nbsp;
to avoid these kind of second order effects&nbsp; that are of perverse incentives of a metric?
We look at multiple metrics, but we will optimize&nbsp; around one and you have to use your own judgment&nbsp;&nbsp;
to look at some of these countermeasures and pick&nbsp; them. We would also, that would sort of be our&nbsp;&nbsp;
overarching metric for a year, but then we would&nbsp; pick specific tactical metrics about how we would&nbsp;&nbsp;
accomplish it. So just an example that both is how&nbsp; we solved a problem, but also it's just a style of&nbsp;&nbsp;
metric that was useful to us. Of course, some of&nbsp; these support tickets included things like, "I'm&nbsp;&nbsp;
waiting to hear back from Atlas about, if they're&nbsp; going to approve my application because Stripe is&nbsp;&nbsp;
required for very good reasons to evaluate certain&nbsp; business types, or sanctions, lists and the&nbsp;&nbsp;
worldwide products." So there is some, should be&nbsp; incredibly quick, but there is a bit of a review&nbsp;&nbsp;
process, and of course if you were not hearing&nbsp; back from us, you would be upset because you're&nbsp;&nbsp;
trying to make your company immediately, "This&nbsp; is ridiculous. Let's get back to us quickly."&nbsp;
And so, we knew that one of the reasons that&nbsp; people were writing to support was like, "Hey,&nbsp;&nbsp;
what's up with my review? What's going on?" And&nbsp; we knew that our tactic was just to drive up how&nbsp;&nbsp;
quickly we got to a final decision on folks and&nbsp; to reduce the number of overturned rejections,&nbsp;&nbsp;
where someone writes back in saying, "Hi, come&nbsp; on, I'm totally just making something reasonable.&nbsp;&nbsp;
What's up? Why did you reject me?" And so, we&nbsp; would pick these overarching single metric,&nbsp;&nbsp;
which was the companies with zero support tickets,&nbsp; but then we would have a specific KR that was&nbsp;&nbsp;
owned by an engineer, which is the tactic that&nbsp; we're going to do. And so, we would not allow&nbsp;&nbsp;
ourselves the perverse tactics to sort of just&nbsp; casually exist. We would choose which tactics&nbsp;&nbsp;
we're going to do and then set a metric for it. And the other reason I love this metric is,&nbsp;&nbsp;
it's a cohort metric by which you're trying&nbsp; to drive something up into the left. Sometimes&nbsp;&nbsp;
people will get excited about a chart that goes&nbsp; up into the right, it's kind of a meme, "Oh,&nbsp;&nbsp;
that's going up to the right." I'm really excited&nbsp; about charts that go up into the left. So you have&nbsp;&nbsp;
to figure out some optimization that you're trying&nbsp; to maximize. And so, in this particular case of&nbsp;&nbsp;
this risk review, we would look at, "Hey, for&nbsp; the cohort of customers that started last month,&nbsp;&nbsp;
how quickly did we get them to their final risk&nbsp; review by number of days since they submitted?"&nbsp;&nbsp;
And so, you want a chart that looks a lot&nbsp; like, "Here we go, right up to the top."&nbsp;&nbsp;
Because you want 100% of your customers to get&nbsp; their final decision as quickly as possible.&nbsp;
Wouldn't you know it, when we looked at&nbsp; the chart, it was doing this. And so,&nbsp;&nbsp;
each month we would just make it a little better,&nbsp; a little better, a little up and to the left,&nbsp;&nbsp;
up and to the left, up and to the left. And now&nbsp; basically 100-ish percent of people get their risk&nbsp;&nbsp;
review within an hour, from a long tail taking a&nbsp; long time. And so, we would constrain the tactic&nbsp;&nbsp;
through a metric and then watch it through an&nbsp; optimization function. And then when we got to&nbsp;&nbsp;
a point where we were happy with the target, we&nbsp; could put down the tactic. That's another really&nbsp;&nbsp;
useful thing about metrics, you can decide when&nbsp; to stop a tactic because you get to some level of&nbsp;&nbsp;
success that you're comfortable with and you&nbsp; can always choose to pick it back up later.
So there's some really cool lessons here of&nbsp; just how to pick a good metric. Just to kind&nbsp;&nbsp;
of maybe summarize what I'm hearing is, you&nbsp; kind of worked backwards from essentially NPS,&nbsp;&nbsp;
like, "Why aren't people recommending&nbsp; Atlas?" You found, "Okay, well people&nbsp;&nbsp;
that are complaining and having issues&nbsp; with support and running into problems,&nbsp;&nbsp;
most likely are going to be detractors,&nbsp; not going to want to recommend Atlas,&nbsp;&nbsp;
so let's have those really ambitious goals.&nbsp; Eventually nobody has a support ticket/let's&nbsp;&nbsp;
just track how many people have zero issues." And&nbsp; then you identify, "Okay, what's driving a lot&nbsp;&nbsp;
of these support tickets? It looks like this risk&nbsp; timeline till they get to this certain milestone,&nbsp;&nbsp;
let's make that our goal for the next quarter&nbsp; or whatever, and let's focus there and then&nbsp;&nbsp;
make an impact." And then I imagine move on to&nbsp; other levers within this bucket of zero context.
You have to pick the right metric for your&nbsp; audience in... I wouldn't wouldn't fully export&nbsp;&nbsp;
that metric to everyone. That was not a terrible&nbsp; one to export, but in the founders choosing where&nbsp;&nbsp;
to get started mindset, again, this isn't just&nbsp; deeply spending time listening to your customers.&nbsp;&nbsp;
They all ask their friends, "Hey, how did you&nbsp; start your company?" They want to talk to an&nbsp;&nbsp;
older sibling of sorts about how it went. And so,&nbsp; we decided that our go-to-market strategy would be&nbsp;&nbsp;
to delight our current customers such that they&nbsp; would tell their friends. And other businesses,&nbsp;&nbsp;
that's always somewhat useful, but you can also&nbsp; reach people with billboards and Google ads and&nbsp;&nbsp;
other types of upsells. That's very difficult&nbsp; in the moment that someone is starting a company&nbsp;&nbsp;
that's sort of a National Geographic, can you get&nbsp; the picture of the bird at exactly the right time?&nbsp;
How are you even supposed to go find people&nbsp; who are about to start companies? Thankfully,&nbsp;&nbsp;
they have this practice of just asking their&nbsp; friends. And so, if their friends loved it,&nbsp;&nbsp;
they're going to just recommend it. And that has&nbsp;&nbsp;
the metric and the tactic and the go-to-market&nbsp; all lined up, rather than sometimes in cases&nbsp;&nbsp;
you might hear someone say, "Well, let's make&nbsp; the product quality better." Well, we all make&nbsp;&nbsp;
the product quality better, but why? Why is this&nbsp; actually going to move what our customers want,&nbsp;&nbsp;
and the business board? And when you can line them&nbsp; all up, it can be quite beautiful, especially when&nbsp;&nbsp;
you can see it month-over-month for a long period&nbsp; of time. One other metric I think that I would&nbsp;&nbsp;
export to anybody, is if you are unsure what&nbsp; to measure, we have this, I don't know if we&nbsp;&nbsp;
stole it from somebody else or if we came up with&nbsp; internally, whatever, is just users having a bad&nbsp;&nbsp;
day, where we will just emit a log line anytime&nbsp; we think that a user bumped into a problem.&nbsp;
So maybe they hit a 404, or maybe their&nbsp; payout was one day after the ETA, or they&nbsp;&nbsp;
had more than 10 payment declines, you can kind&nbsp; of brainstorm again or just listen to customers,&nbsp;&nbsp;
what would cause you to personally have a&nbsp; bad day, and then just emit an event when&nbsp;&nbsp;
that occurs. And then you could just make a&nbsp; stacked bar chart of all the bad day reasons&nbsp;&nbsp;
and the frequency by which they're happening,&nbsp; and it's eye-opening to see those frequencies.&nbsp;&nbsp;
And it's kind of a metric I hadn't thought about&nbsp; until Stripe's scale, in which you just don't&nbsp;&nbsp;
know what's happening until you emit the log&nbsp; line and count it. The frequencies could be...
... emit the log line and count it. The&nbsp; frequencies could be kind of mind-blowing. And&nbsp;&nbsp;
I think for almost any scale business, if you are&nbsp; bored one day and you're not sure what to measure,&nbsp;&nbsp;
just make a user having a bad day chart, emit&nbsp; a log line and count it as a bar chart and then&nbsp;&nbsp;
anybody else can add their own bar chart on top of&nbsp; it. And so, it's become a way for teams to scale&nbsp;&nbsp;
their understanding of users through metrics&nbsp; by just saying, "Hey, look, anytime anybody&nbsp;&nbsp;
has an idea about why a customer is having a bad&nbsp; day, just emit a log line, put it on this chart,&nbsp;&nbsp;
and then we can choose over time which bad&nbsp; day reasons we want to burn down and hopefully&nbsp;&nbsp;
just eradicate them, not just minimize them. But it gave us kind of a background noise counting&nbsp;&nbsp;
system for where there are problems and anytime&nbsp; there's an incident or some customer issue,&nbsp;&nbsp;
the first thing I think is, "Ooh, I wonder if we&nbsp; have a bad day reason for this." And if we do,&nbsp;&nbsp;
I actually feel okay. I'm like, "Oh yeah, it is a&nbsp; bad day for this customer." I wish I didn't have&nbsp;&nbsp;
it, but at least we're aware and we can evaluate&nbsp; it against other bad days that we want to burn&nbsp;&nbsp;
down. What does sometimes a little bit grind&nbsp; my gears or gives us an opportunity is like&nbsp;&nbsp;
when we didn't know about that bad day. And it's&nbsp; a surprise to us too, that is for me is immediate&nbsp;&nbsp;
action. It's like, okay, cool. We have to figure&nbsp; out a way to count this bad day. We got to get it&nbsp;&nbsp;
on the chart. That way we can make an informed&nbsp; decision about when to invest improving it.
And I love this idea. I haven't heard&nbsp; this before. So the idea is just make a&nbsp;&nbsp;
list of what happens to a potential&nbsp; customer that would cause them to&nbsp;&nbsp;
have a bad day. What are some examples&nbsp; for Striper Atlas that you guys have?
Are you a Stripe customer, Lenny?
I am with my newsletters. The payments go&nbsp; through Stripe. I check my dashboard every day.
Cool. So what would be a bad day for you?
Oh, I see some silence happening here.&nbsp; It not loading. The numbers taking a&nbsp;&nbsp;
long time to show up. Something&nbsp; being completely off in there,&nbsp;&nbsp;
not being able to log in. The silence&nbsp; is good. I just want to keep going.
The question is how much to the audience&nbsp; is how much of the silence will we edit&nbsp;&nbsp;
out before it goes live? But this is what I'm&nbsp; talking about, right, is I could guess them,&nbsp;&nbsp;
right? And as you were saying those,&nbsp; I know the URL of those charts. I know&nbsp;&nbsp;
the login one because I feel that too. So I&nbsp; play with Stripe all the time and then you&nbsp;&nbsp;
get a two FA too frequently and come on, I had&nbsp; the same cookie. I was just here yesterday. So&nbsp;&nbsp;
we count all that stuff and try to make it&nbsp; better over time. But I'm so excited when&nbsp;&nbsp;
someone brings me a new bad day I hadn't thought&nbsp; about yet because that's like product cabinet.
I love it. And your advice here is this doesn't&nbsp; necessarily have to be your goal or metric. It's&nbsp;&nbsp;
just watching this thing that could lead&nbsp; to a lot of interesting ways of operating.
A couple other just like quick metrics things&nbsp; because it's a bit of a... I don't know,&nbsp;&nbsp;
some people like cycling or something. I guess,&nbsp; I like metrics. People get a really nice bike.&nbsp;&nbsp;
I want a really great metric. Picking metric&nbsp; titles that make you feel something. So we could&nbsp;&nbsp;
have called that measure of companies, number of&nbsp; companies that do not send a support ticket over&nbsp;&nbsp;
X period and Y period with min... You sometimes&nbsp; see these charts where the metric itself named&nbsp;&nbsp;
itself. This is just companies with zero support,&nbsp; that's it. And the brevity and the focus and the&nbsp;&nbsp;
customer mindset built into the chart name can&nbsp; become currency inside the company. It's like,&nbsp;&nbsp;
oh, I'm working on making this chart go&nbsp; up and it feels good to just say the name&nbsp;&nbsp;
out loud rather than some complicated&nbsp; underscores and mins and maxes and the&nbsp;&nbsp;
database field name is still in the chart title. These are aesthetic choices, but I think make&nbsp;&nbsp;
dramatic differences in the cultural willingness&nbsp; for people to buy in and get excited about it and&nbsp;&nbsp;
reduce the need of a product person to just&nbsp; remind everyone every day why they're doing&nbsp;&nbsp;
it. It's like the metric is motivating us because&nbsp; it's a motivating thing to talk about. And then&nbsp;&nbsp;
lastly on metrics is there's just good hygiene&nbsp; that people should bring to their measures.&nbsp;&nbsp;
Percentages shouldn't have 41 significant digits&nbsp; if only two of the digits are relevant. You should&nbsp;&nbsp;
keep all the measures of your dashboard on the&nbsp; same X-axis. These are just stylistic things that&nbsp;&nbsp;
increase the frequency that people want to just&nbsp; wake up every day and open the dashboard and look&nbsp;&nbsp;
at it. And that is so powerful if your whole team&nbsp; is looking at the same set of information that has&nbsp;&nbsp;
the heartbeat of the customer every single day. In fact, we can measure at Stripe the usage of&nbsp;&nbsp;
our dashboards by team, and so we can see which&nbsp; teams are themselves looking at their own metrics&nbsp;&nbsp;
and that is an incredibly useful predictor of&nbsp; how on the same page they are and how customer&nbsp;&nbsp;
obsessed they are. So I just think it's not&nbsp; an area that's sort of behind the scenes,&nbsp;&nbsp;
bean counting reliability is the machine hot.&nbsp; You can make metrics that mean something to the&nbsp;&nbsp;
customer and you would be proud if they were to&nbsp; be screenshot and put on the internet and be like,&nbsp;&nbsp;
"Wow, I feel like that company is taking&nbsp; their promise to me seriously. And I can&nbsp;&nbsp;
see myself on those metrics as a customer."&nbsp; That's where we're really shooting for.
So [inaudible 01:08:19] back&nbsp; what you just said there,&nbsp;&nbsp;
which I think is a subtle point potentially,&nbsp; is just making the dashboard look nice,&nbsp;&nbsp;
like the hygiene of the naming conventions&nbsp; and the decimal points and the chart. In&nbsp;&nbsp;
your experience, you find that&nbsp; really powerful and important.
A couple of years ago, Stripe did internal work&nbsp; to make an internal metrics kind of dashboard&nbsp;&nbsp;
system. And we have a special place called Go&nbsp; Metrics. Many people use a go/service where&nbsp;&nbsp;
you can just quickly go to a URL. And again,&nbsp; I have to sometimes do a rule rather than a&nbsp;&nbsp;
policy. My rule is if it's not on Go Metrics,&nbsp; I'm not going to look at it. So if people can&nbsp;&nbsp;
send me one-off queries or charts or screenshots&nbsp; or presentations or emails of charts and data,&nbsp;&nbsp;
but that is in the wind, we can't interrogate&nbsp; the query metrics are almost always wrong. For&nbsp;&nbsp;
many weeks, we didn't quite get the definition&nbsp; correctly. You have to live in the metric for&nbsp;&nbsp;
quite a while before you really believe in it.&nbsp; And so, if you're always looking at some one-off&nbsp;&nbsp;
version, it's just very difficult for it to&nbsp; rise up to the level of importance that is&nbsp;&nbsp;
a thing we should trust to help us decide what to&nbsp; do. That's an incredibly high bar. And so, I just&nbsp;&nbsp;
find you have to look at it frequently enough. And if you're going to look at it frequently&nbsp;&nbsp;
enough, it means it needs to be in a discoverable&nbsp; place. You almost go through a couple stages of&nbsp;&nbsp;
grief about it because we'll kind of put a metric&nbsp; up in a place and everyone initially is like,&nbsp;&nbsp;
"Wow, this is great. I was so excited to finally&nbsp; see this." And then a couple of days later,&nbsp;&nbsp;
"I don't quite understand it. What does it&nbsp; actually mean? I saw this other metric from&nbsp;&nbsp;
this other angle that kind of makes it feel&nbsp; counterintuitive that it's like this." And&nbsp;&nbsp;
then you kind of look into it, "Wait a second,&nbsp; we've been counting it wrong the whole time. Oh,&nbsp;&nbsp;
no." And then you look at it the third week&nbsp; and it's a completely different version and&nbsp;&nbsp;
then you hope that we forget about it and&nbsp; maybe we'll go onto something else and nope,&nbsp;&nbsp;
we're not going to forget about it. Week four&nbsp; comes around, you're like, "Wait a second. Okay,&nbsp;&nbsp;
this is..." Then the team meeting starts, "Hey,&nbsp; just a reminder, let's just bring up the metric&nbsp;&nbsp;
again, not a screenshot of it. Go to the URL." And just that level of frequency and specificity&nbsp;&nbsp;
and ritual around it is what brings it into&nbsp; the decision-making culture. And again,&nbsp;&nbsp;
we treat it the exact same as we do tweets.&nbsp; It's the quantitative and qualitative right&nbsp;&nbsp;
next to each other. And because you're&nbsp; putting that amount of attention to it,&nbsp;&nbsp;
you can't have a 1,000 metrics. We just don't&nbsp; physically have time the day to bring that level&nbsp;&nbsp;
of care and understanding to so many things.&nbsp; So then it forces you to know so many things&nbsp;&nbsp;
you could care about down to a small number of&nbsp; things that you really must care about. And again,&nbsp;&nbsp;
that practice goes back to do you really&nbsp; understand what your customer wants? And so,&nbsp;&nbsp;
for all these tactics, it's about finding out&nbsp; what your customer wants and then different&nbsp;&nbsp;
versions of how do we sort of know it's&nbsp; true over time and our tactics improving?
It sounds so simple when you describe it that way.&nbsp; This episode is brought to you by Anvil. Their&nbsp;&nbsp;
document SDK helps product teams build and launch&nbsp; software for documents fast. Companies like Carta&nbsp;&nbsp;
and Vouch Insurance use Anvil to accelerate&nbsp; the development of their document workflows.&nbsp;&nbsp;
Getting to market fast is a top priority for&nbsp; product teams. And the last thing that you&nbsp;&nbsp;
or your developers want is to build document&nbsp; workflows from scratch. It's time-consuming,&nbsp;&nbsp;
expensive and distracts from core work.&nbsp; You could stitch together multiple tools&nbsp;&nbsp;
and manage those integrations. Or you can use an&nbsp; all-in-one document SDK. Most product managers&nbsp;&nbsp;
will tell you paperwork sucks. Anvil's document&nbsp; SDK helps teams get to market fast, incorporate&nbsp;&nbsp;
your brand style and give you back time to focus&nbsp; on your company's core differentiated features.&nbsp;
For your users, paperwork often starts&nbsp; with an AI powered web form styled and&nbsp;&nbsp;
embedded in your application. From there, you&nbsp; can route data to your backend systems and to&nbsp;&nbsp;
the correct fields in your PDFs via API.&nbsp; Complete the process with a white labeled&nbsp;&nbsp;
e-signature. The best part about Anvil is the&nbsp; level of customization their SDK provides.&nbsp;&nbsp;
Non-technical folks love Anvil's Dragon Drop&nbsp; Builder and developers love their flexible&nbsp;&nbsp;
APIs and easy to understand documentation.&nbsp; Build documents software fast with Anvil,&nbsp;&nbsp;
that's useanvil.com/lenny to learn more or start a&nbsp; free trial. That's useanvil.com/lenny. Kind along&nbsp;&nbsp;
these same lines, there's something that I've&nbsp; learned you started at Stripe to help people&nbsp;&nbsp;
obsess with user experience and get quality&nbsp; to where it needs to be and move a lot of&nbsp;&nbsp;
these metrics, something called Study Groups.&nbsp; Talk about what that is. I'm very curious.
Okay, let's imagine we understand our customer,&nbsp; we've understand their burning problem. We've&nbsp;&nbsp;
built a solution that's in their hands,&nbsp; they're using, it's hopefully better than&nbsp;&nbsp;
their alternatives and they're starting to&nbsp; use it and we have some real traction. You&nbsp;&nbsp;
could still measure the success, you could still&nbsp; look at the tweets and then, of course, you go&nbsp;&nbsp;
to pick it up yourself and you're like, "Wait a&nbsp; second, this thing is horrible. How did it get so&nbsp;&nbsp;
bad?" Anyone who's built a product that has gone&nbsp; over the horizon of it's actually in production&nbsp;&nbsp;
and being used for a year or more as you go to&nbsp; iterate on it, especially when you're in a larger&nbsp;&nbsp;
company and there's multiple teams and multiple&nbsp; products going on, there's just some entropy in&nbsp;&nbsp;
the world that causes these things to go bad. I&nbsp; actually have a hard time naturally explaining it.&nbsp;
You kind of think to yourself, well, it's code.&nbsp; It just must be running the same every day. But&nbsp;&nbsp;
somehow you do enough things in a row. And&nbsp; what was once a smooth end-to-end flow for&nbsp;&nbsp;
accomplishing a test or a customer is all of a&nbsp; sudden some Byzantine complicated broken mall&nbsp;&nbsp;
where all the doors are busted and you have to&nbsp; know exactly the way to get through the dashboard&nbsp;&nbsp;
to solve your problem. "Wait a second, I thought&nbsp; this was great just a second ago." And many of&nbsp;&nbsp;
us have experienced that. Now, okay, what are we&nbsp; going to do about it? Well, one is it is really&nbsp;&nbsp;
difficult to take time during the day to allow&nbsp; yourself to even know that this is true. Because&nbsp;&nbsp;
if you're working on one particular team, you're&nbsp; going to have some next thing you're shipping,&nbsp;&nbsp;
you're going to have your customers, you're&nbsp; going to be doing great product work.&nbsp;
Meanwhile, your current thing kind of starts&nbsp; to rot in the world and decrease all the trust&nbsp;&nbsp;
you've earned to build what you're building&nbsp; now. It is actually difficult to decide, well,&nbsp;&nbsp;
what hours during the week am I going to block&nbsp; off from my future progress to see it from the&nbsp;&nbsp;
customer's perspective today? And there are&nbsp; various techniques to try to incentivize or&nbsp;&nbsp;
to structure a group of people to do that. Stripe&nbsp; has a thing called friction logs as well, which is&nbsp;&nbsp;
a single individual will pretend to be a customer&nbsp; and go through a product experience end-to-end and&nbsp;&nbsp;
write it down. And that has been quite successful&nbsp; at Stripe for very motivated people who can block&nbsp;&nbsp;
off the time and have the wide enough context to&nbsp; do a complicated thing end-to-end and have the&nbsp;&nbsp;
time to write it up and the position the company&nbsp; to send it out as a critique potentially to not&nbsp;&nbsp;
just your own team but in a whole organization. So that's actually a pretty high bar to crossover.&nbsp;&nbsp;
So I was kind of brainstorming what could we do&nbsp; to make this more fun and have the frequency which&nbsp;&nbsp;
we're looking at our own products dramatically&nbsp; increase? And we kind of iterated few through&nbsp;&nbsp;
ideas. And I landed on this thing called Study&nbsp; Group, which is basically a random group of people&nbsp;&nbsp;
inside the company. They might not work on any&nbsp; particular team. They might not all be PMs,&nbsp;&nbsp;
just like literally anyone who wants to&nbsp; sign up, a support person, a sales person,&nbsp;&nbsp;
someone who's on our events team, an engineer&nbsp; and our infrastructure stack. Anybody can sign&nbsp;&nbsp;
up for a Study Group. We show up maybe four&nbsp; to eight people total. We pretend to be some&nbsp;&nbsp;
company with some outcome problem. Maybe we&nbsp; want to accept money in person at an upcoming&nbsp;&nbsp;
farmer's market, or we want to run a multi-country&nbsp; global business where we have software&nbsp;&nbsp;
that another business would use to run their&nbsp; business. If it was something quite complicated.&nbsp;
We could pick any motivating goal. And there&nbsp; are two rules to Study Group rule one is you&nbsp;&nbsp;
do no longer work at Stripe. You do not work&nbsp; at Stripe, not pretend, don't work at Stripe,&nbsp;&nbsp;
not try to forget you do not work at Stripe,&nbsp; you've never worked at Stripe. You work at... And&nbsp;&nbsp;
we make up a name of the company, Dolphin Aquarium&nbsp; Industries, and we will pick a CEO of the company&nbsp;&nbsp;
from the group amongst us. And okay, Jenny is the&nbsp; CEO. "Hey, Jenny, what do you want to do today?"&nbsp;&nbsp;
"Well, I want to sell in-person tickets to the&nbsp; Dolphin Aquarium." It's like, "Cool, where would&nbsp;&nbsp;
just start?" So we actually embody the customer.&nbsp; We will not break character, it's a little bit&nbsp;&nbsp;
of the improv thing and as the kind of maestro&nbsp; of Study Group, I will firmly but kindly, if I&nbsp;&nbsp;
hear you use any internal Stripe knowledge, which&nbsp; is natural to do, because, well, you worked on a&nbsp;&nbsp;
team and you know where that button really is. And the docs link goes a little bit to the wrong&nbsp;&nbsp;
place, but if you click the other link, you'll get&nbsp; to it. If I can see you use any internal Stripe&nbsp;&nbsp;
knowledge, I'll just pause and say, "Hey, let's&nbsp; redo the sentence or redo what we did with no&nbsp;&nbsp;
Stripe knowledge. As a reminder, you don't work&nbsp; at Stripe." And it takes us a couple of times,&nbsp;&nbsp;
but people really get into it and all of a sudden&nbsp; we'll start making up characters and the CEO will&nbsp;&nbsp;
be like, "Oh, Tim, you're our designer. Where&nbsp; are we going to get the color palette?" All of&nbsp;&nbsp;
a sudden there's a person who's not a designer&nbsp; in real life is now all of a sudden having to&nbsp;&nbsp;
practice the empathy to be in a customer's&nbsp; position. And because we're going to be doing&nbsp;&nbsp;
it for an hour, hour and a half at a time, you&nbsp; actually start to believe that you don't work&nbsp;&nbsp;
at Stripe and you work at Dolphin Aquarium&nbsp; Industries and you start to really feel it.&nbsp;
So that's rule one. You don't work at Stripe. And&nbsp; rule two is we're not here to solve any problems.&nbsp;&nbsp;
We're not here to critique, we're not here to&nbsp; solution or suggest, we're not here to file bugs.&nbsp;&nbsp;
All of those things is recorded. We can do that&nbsp; later, whatever. This is just about practicing&nbsp;&nbsp;
empathy for the customer and going through the&nbsp; product. And we have done more than 25 of these at&nbsp;&nbsp;
Stripe thus far in just this year, last few months&nbsp; of 2024, more than 250 people have participated in&nbsp;&nbsp;
the Study Group. And it is deeply eyeopening for&nbsp; those involved. The responses are sort of business&nbsp;&nbsp;
emotional, not super emotional, but just, "Wow,&nbsp; I can't believe how hard it was to accomplish X,&nbsp;&nbsp;
Y and Z. I thought we were amazing at blah." It's&nbsp; like, "Well, we actually are still pretty good,&nbsp;&nbsp;
but we need to get back towards amazing" or&nbsp; Wow, "I didn't even know that internally people&nbsp;&nbsp;
wouldn't know that our products did 1, 2, and 3." And this has become so internally popular that&nbsp;&nbsp;
teams have adopted for themselves. And so, we've&nbsp; kind of franchised Study Group internally already&nbsp;&nbsp;
where different teams will run it. But I think&nbsp; we're going to continue it because I think a&nbsp;&nbsp;
little bit is coming out of the pandemic.&nbsp; People just want more group activities. I&nbsp;&nbsp;
think some of it is the slowness by which we do&nbsp; it. We're not rushing through it. Which another&nbsp;&nbsp;
reason I appreciate your podcast as well is let's&nbsp; really get into the details and not be rushed for&nbsp;&nbsp;
time. You forget that you have a meeting&nbsp; at the end kind of amount of time. No one&nbsp;&nbsp;
is to blame or defensive because it's not your&nbsp; product at all. It's a random group of people.&nbsp;&nbsp;
We don't even introduce ourselves about what team&nbsp; we worked on. We're just all here as participants&nbsp;&nbsp;
to embody the customer. And then I think lastly,&nbsp; a reason why it's worked, and these are many of&nbsp;&nbsp;
these just been actually super surprising to me. I wouldn't have been able to prick ahead of time,&nbsp;&nbsp;
is it's just fun. People want to make up&nbsp; the name of the company. They're excited&nbsp;&nbsp;
about what Dolphin Industries would sell. A&nbsp; person who's not a CTO in real life gets to&nbsp;&nbsp;
pretend to be a CTO and there's little theatrics&nbsp; to it, but it has been different enough from our&nbsp;&nbsp;
other approaches for a company like Stripe,&nbsp; which is already pretty focused on this topic,&nbsp;&nbsp;
that we think that there's enough legs here that&nbsp; we're going to keep it and kind invest in groups&nbsp;&nbsp;
pretending to be the customer and going through&nbsp; it painstakingly slowly rather than only demos or&nbsp;&nbsp;
only writing, which has other benefits, but misses&nbsp; the participation of a larger group and more fresh&nbsp;&nbsp;
eyes. So it's been fun and we named it Study&nbsp; Group. I guess, I named it Study Group because I&nbsp;&nbsp;
wasn't sure it would be initially. So I just came&nbsp; up with something that sounded cutesy, but gave&nbsp;&nbsp;
me enough leeway that we could kind of adjust&nbsp; it over time. And this is where we've landed.
It's fascinating that there's so much theatrics&nbsp; and ceremony necessary for a product team and a&nbsp;&nbsp;
company to find out these things about their&nbsp; product. You would think people are like,&nbsp;&nbsp;
"Oh, we know how onboarding looks. We&nbsp; know all these things," but basically&nbsp;&nbsp;
what you're saying is you don't,&nbsp; and you need to do these sorts of&nbsp;&nbsp;
things in order to really know what&nbsp; your product is like these days.
The customer does not live in our walls. They&nbsp; aren't. They're not here. They don't know our&nbsp;&nbsp;
lingo. And it is just so natural for our internal&nbsp; mindset and lingo to flow into the application&nbsp;&nbsp;
over time. And you need some counterbalance to&nbsp; get there. And I think it has to be an unnatural&nbsp;&nbsp;
counterbalance. It used to frustrate me actually&nbsp; more like, "Wow, why aren't we doing this?" Well,&nbsp;&nbsp;
we're actually doing great work to move&nbsp; something forward and we have our local&nbsp;&nbsp;
optimizations. It'd be difficult to get to&nbsp; this level of specialization that multi-product&nbsp;&nbsp;
companies are trying to do without that level&nbsp; of focus on a per team basis, but then you need&nbsp;&nbsp;
something unnatural to help us bring it back. And so, I'm constantly looking for non-punitive&nbsp;&nbsp;
fun ways objectively to get more perspectives from&nbsp; the outside in. If it's breaking the fourth wall&nbsp;&nbsp;
to get on the phone on Twitter, if it's looking at&nbsp; a metric of users having a bad day, which is just&nbsp;&nbsp;
like counting what's happening, you can't argue&nbsp; with that. Or a random group of people just kind&nbsp;&nbsp;
of scratching their head trying to find a button,&nbsp; those are truths in the world that we're trying to&nbsp;&nbsp;
make sure are inputs to all of our teams. And&nbsp; if you don't have those inputs, I can totally&nbsp;&nbsp;
naturally see where the entropy of the world leads&nbsp; you to have Frankenstein bad products, even when&nbsp;&nbsp;
all the individual parts are well oiled and run&nbsp; by great people. So you need something unnatural.
There's an interesting trend and thread through&nbsp; our talk so far broadly, there's just an obsession&nbsp;&nbsp;
with making something great and awesome. And&nbsp; then a layer below is just an obsession with&nbsp;&nbsp;
the user experience being as great as possible.&nbsp; And for a lot of PMs, there's not a direct line&nbsp;&nbsp;
between make the experience as amazing as possible&nbsp; to growth and revenue and success and things like&nbsp;&nbsp;
that. And it feels like for you and for Stripe&nbsp; broadly, there's this innate implication. If&nbsp;&nbsp;
we're making the experience better and better and&nbsp; better, we will grow. You're nodding your head a&nbsp;&nbsp;
little sideways a little bit, so I'd love to hear&nbsp; just your thoughts on just this obsession with&nbsp;&nbsp;
experience and user issues. But we also have to go&nbsp; to the business. What are the metrics are moving?
If someone else has a strategy for moving revenue&nbsp; that isn't getting it from customers, I want to&nbsp;&nbsp;
know about it because it's so hard to get it&nbsp; from customers. If there's some faster path,&nbsp;&nbsp;
please tweet me and tell me about it because this&nbsp; is very hard, a lot of work to do. So if there's&nbsp;&nbsp;
something else, I want it on the table, but I&nbsp; often find it's part of the product experience.&nbsp;&nbsp;
So maybe it's internal sales tools. We can&nbsp; do a Study Group about our internal sales&nbsp;&nbsp;
tools process and our deal desk and our margin&nbsp; structure. We can do a friction log on our third&nbsp;&nbsp;
party vendor process or a migration service&nbsp; or the way an ecosystem partner helps deploy&nbsp;&nbsp;
our services into a big enterprise. Nothing&nbsp; is sort of off limits from product. In fact,&nbsp;&nbsp;
I was chatting with a friend who runs the company&nbsp; and they were small company on the verge of&nbsp;&nbsp;
product market fit starting to feel, customers&nbsp; starting to pull and they're like, "Oh, but our&nbsp;&nbsp;
self-service funnel, it's so leaky and we have&nbsp; all this support coming through self-service."&nbsp;
First of all, congratulations, unbelievable&nbsp; that they're going through your product,&nbsp;&nbsp;
even attempting self-service and contacting&nbsp; you. The majority case would be no one tries&nbsp;&nbsp;
or they try and fail and don't contact you.&nbsp; So again, what a problem to have. And two,&nbsp;&nbsp;
they wanted to minimize the support. In&nbsp; that particular case, it's like, "Well,&nbsp;&nbsp;
what's actually in those support tickets?&nbsp; What's in those sales? Those are really sales&nbsp;&nbsp;
contacts." They're like, "Oh, they want to&nbsp; learn more about how they get started." They&nbsp;&nbsp;
want to know the expertise about... This is a&nbsp; particular company, it's a healthcare related&nbsp;&nbsp;
company. They wanted to know the healthcare&nbsp; choices available. They wanted to know how&nbsp;&nbsp;
to migrate from some old system they had to it. I was like, "That's the product. The thing you're&nbsp;&nbsp;
talking about is the product." Turn those moments&nbsp; during your self-serve process into not self-serve&nbsp;&nbsp;
and make the product experience be let's get you&nbsp; on the phone. And now when they get on the phone,&nbsp;&nbsp;
they know the first name of the person&nbsp; they're talking to because they have it&nbsp;&nbsp;
from the onboarding forum and all of a sudden&nbsp; it feels like you are still in the product,&nbsp;&nbsp;
but it's not software. Now it's a person, but it's&nbsp; a person backed by internal software, which knows&nbsp;&nbsp;
as much as they can about the customer and what&nbsp; they want. And I was really inspired by Fidelity,&nbsp;&nbsp;
which is a big financial institution where many&nbsp; people listening might have switched jobs and had&nbsp;&nbsp;
to move their 401(k) or something like this from&nbsp; job A to job B. Maybe in some universe it'll be&nbsp;&nbsp;
three clicks, but not today or certainly not when&nbsp; I tried a couple of years ago. You got a call and&nbsp;&nbsp;
go on a phone tree and all the shenanigans, and&nbsp; then I got on the line with someone from Fidelity.&nbsp;&nbsp;
They're like, "Hi, Jeff. They knew about the old&nbsp; company. They confirmed my address." They said,&nbsp;&nbsp;
"By the way, this is not a digital process yet.&nbsp; We're going to FedEx you an envelope and inside&nbsp;&nbsp;
it is going to be the thing for you to sign.&nbsp; Here's going to be exactly where to sign. Here's&nbsp;&nbsp;
a picture we're going to sign. We've put another&nbsp; envelope inside that envelope ready to go. And so,&nbsp;&nbsp;
you just take the papers from envelope one, sign&nbsp; them where it says and put them in envelope two&nbsp;&nbsp;
and put it back to the [inaudible 01:29:16]." It's like, "Wow, that is product." That is a&nbsp;&nbsp;
product experience where I think some people&nbsp; would say, "Oh look, the product experience&nbsp;&nbsp;
has to only be in software." So I feel when&nbsp; people think, oh, product quality and craft&nbsp;&nbsp;
has some limit towards business value, there's&nbsp; some asymptote that you have to be like, well,&nbsp;&nbsp;
kind of product plate time quality is over. We&nbsp; need to talk about business. It's like, let's&nbsp;&nbsp;
figure out exactly what is causing the business to&nbsp; happen and make a product, even if it doesn't look&nbsp;&nbsp;
naturally the same as our SaaS, software, browser,&nbsp; mobile, whatever versions. I think we can see the&nbsp;&nbsp;
entire experience as it. And from there, I include&nbsp; the sales process, I include the support process,&nbsp;&nbsp;
I include tools that help with compliance and&nbsp; everything else. And again, if people have a&nbsp;&nbsp;
way to make all those things bad and lead to great&nbsp; increasing revenue over time in sustainable ways,&nbsp;&nbsp;
I want to know about that because that sounds so&nbsp; much easier than the version that we're trying.
I love that and clearly it's worked for&nbsp; Stripe. Just one last question. I want&nbsp;&nbsp;
to talk about Atlas and dive into just&nbsp; like what is Atlas and how is it doing&nbsp;&nbsp;
and things like that. I know there's some&nbsp; new stuff coming that you're going to share,&nbsp;&nbsp;
but one last question about Study Groups. How&nbsp; do you decide what product you're going to pick&nbsp;&nbsp;
to do a Study Group on? And then what is the&nbsp; expectation with the result? I imagine there's&nbsp;&nbsp;
a PM sitting around like, "Oh my God, I just&nbsp; got this 10 page report on all the problems."
So initially, I just made up a list of stuff&nbsp; that I thought would be fun to Study Group to&nbsp;&nbsp;
kind of kick it off. And now, because it has&nbsp; a bit of an internal brand and it's exciting,&nbsp;&nbsp;
and people who have gone to a Study Group&nbsp; say nice things about Study Group there,&nbsp;&nbsp;
they actually proactively say, "Hey, we should&nbsp; Study Group blah," or "We're launching something&nbsp;&nbsp;
next week. We should Study Group it before&nbsp; it goes out the door." Or now I actually just&nbsp;&nbsp;
have a huge backlog of things to Study Group&nbsp; based on what people want. And now we're again&nbsp;&nbsp;
franchising it. So we're going to have Study Group&nbsp; captains and people run their own Study Groups,&nbsp;&nbsp;
and so we can really scale this behavior. But&nbsp; we did our first Study Group of an internal&nbsp;&nbsp;
tool recently. And so, that I think is going&nbsp; to catch on just anything at all can be Study&nbsp;&nbsp;
Group. It just takes about an hour and a couple&nbsp; of people and you open up the Zoom and that's it.&nbsp;
And then for expectation wise, look, it&nbsp; is so tempting to put more regulation on&nbsp;&nbsp;
something. Okay, well, everything coming&nbsp; out of this program needs to be scored and&nbsp;&nbsp;
rubricked and have SLAs. That is extremely&nbsp; reasonable. As some of these next steps,&nbsp;&nbsp;
we do notice things that are of serious issues and&nbsp; we have some formal processes inside of Stripe for&nbsp;&nbsp;
elevating bugs to certain priority levels that get&nbsp; tagged and have SLAs for teams to acknowledge and&nbsp;&nbsp;
review. And so we kind of funnel the outputs&nbsp; of a Study Group into our already existing&nbsp;&nbsp;
formal processes rather than having some new&nbsp; special thing that's going to bother a particular&nbsp;&nbsp;
team. I will say though that it is difficult to&nbsp; watch one of these Study Groups and if you are&nbsp;&nbsp;
the team involved in some piece of it and not want&nbsp; to act on it, because seeing your fellow teammates&nbsp;&nbsp;
struggle to use your thing in some way is more&nbsp; motivating than the customer because you can kind&nbsp;&nbsp;
of always say to the customer, " Well, they didn't&nbsp; really know," or "They have some special setup."
Well, they didn't really know or they have some&nbsp; special setup. You probably shouldn't say those&nbsp;&nbsp;
things, but you can kind of rationalize it,&nbsp; whereas a group of people incentivized to have&nbsp;&nbsp;
actually accomplished it, who got together to do&nbsp; so painstakingly slowly not being able to do so if&nbsp;&nbsp;
that's not what excites you as a product person&nbsp; to want to solve, this thing's not for you. But&nbsp;&nbsp;
then again, you have your own organization&nbsp; system, you have your own things you need&nbsp;&nbsp;
to ship and study group doesn't have a mandate&nbsp; that comes from it. We have our own. It's more&nbsp;&nbsp;
of a cultural piece of information that is very&nbsp; high signal and then people tend to use that high&nbsp;&nbsp;
signal for good prioritization. I will say though,&nbsp; that we have added the SLAs to certain bug levels&nbsp;&nbsp;
that begin to match a bit of our incident process. So in an incident strike, like in many companies,&nbsp;&nbsp;
pencils down, fix the problem, severity levels,&nbsp; non-negotiable Slack rooms happen, war rooms, all&nbsp;&nbsp;
that stuff. You don't want to do that with every&nbsp; single bug, but we have a rubric of craft related&nbsp;&nbsp;
tags for our bug system. And if it is a sort of&nbsp; a P0 bug, which is not an incident, right, it&nbsp;&nbsp;
doesn't mean to put down your pencils. You do need&nbsp; to acknowledge it at Stripe within seven days. And&nbsp;&nbsp;
even if it doesn't mean to fix it, it's like a&nbsp; person looks at it and says, "Hey, we're going&nbsp;&nbsp;
to do it or not do it." That's a still pretty&nbsp; strong bar for a non-incident related craft issue.
It feels just at Stripe, there's this cultural&nbsp; focus on we want to make the product great, we&nbsp;&nbsp;
want to make the experience as great as possible.&nbsp; A lot of companies, it's just teams. We have this&nbsp;&nbsp;
goal. We're not going to do anything that isn't&nbsp; driving this metric and goal that we have. And&nbsp;&nbsp;
I think for teams like that, it's hard to hear&nbsp; just like, oh, someone's going to send you all&nbsp;&nbsp;
of these problems that you experience. There's the&nbsp; negative version where the founders goes through&nbsp;&nbsp;
the product like a CO of a larger company, just,&nbsp; oh my God, look at all these problems. You need&nbsp;&nbsp;
to fix these immediately. And a lot of times it's&nbsp; completely distracting from the things they need&nbsp;&nbsp;
to do, the goals they're trying to drive, things&nbsp; that really, really matter that the CO may not be&nbsp;&nbsp;
thinking about. And it feels like you're trying to&nbsp; find this balance of here's problems that exist.&nbsp;&nbsp;
You don't need to fix them. You probably should.&nbsp; Here's the most important stuff. But also there's&nbsp;&nbsp;
often you find a correlation between make the&nbsp; experience better, you're going to do better.
There's a huge amount of trust here involved in&nbsp; your colleagues, which is we want to provide teams&nbsp;&nbsp;
great information and the best teams welcome that&nbsp; information. It doesn't mean that it comes with a&nbsp;&nbsp;
auteur opinion from the outside world that says&nbsp; you must do X. We have a rubric on some of the&nbsp;&nbsp;
craft related bugs, but again, we let the teams&nbsp; relabel them. And so maybe it's actually not a&nbsp;&nbsp;
P0 from their eyes and that's the trust we put&nbsp; in the teams. I think that the failure mode is&nbsp;&nbsp;
when you don't look. And so we need unnatural,&nbsp; safe, fun lore that gets us out of our chair and&nbsp;&nbsp;
into the customer's mindset. Best is if it's you&nbsp; and you're your own customer, okay. Second best&nbsp;&nbsp;
would be sitting right next to the customer in the&nbsp; outside world and then like, okay, fine, I'll take&nbsp;&nbsp;
a third best, which is pantomime the customer and&nbsp; enforcing you don't use any internal knowledge. If&nbsp;&nbsp;
you have practices in those three categories,&nbsp; I'm comfortable with the failure modes.
I love that. This is definitely going to&nbsp; be the longest episode I've ever done,&nbsp;&nbsp;
which is exactly what I expected&nbsp; and I'm happy that we're doing this.
Everyone go 1.75X or something.
I like when people are like, oh, this&nbsp; episode is really good. I had to slow&nbsp;&nbsp;
down to 1.75 or something. How are&nbsp; you even listening at that speed? No,&nbsp;&nbsp;
it's 1.0 speed. That's what this episode needs&nbsp; to be. There's two more areas I want to spend&nbsp;&nbsp;
some time on. One is Atlas. We've talked a&nbsp; lot about on the surface of Atlas. I want&nbsp;&nbsp;
to help people understand what the hell it is&nbsp; and the stuff that's happening there. And two,&nbsp;&nbsp;
I want to talk about getting stuff done at&nbsp; a big company, something that you've done&nbsp;&nbsp;
at Stripe and I hear you have a lot of good&nbsp; advice on. So first of all, what is Atlas?&nbsp;&nbsp;
We've talked a bit about it. What's the best way&nbsp; to understand what Atlas is and who it's for?
In 2016, a bunch of Stripes were traveling the&nbsp; world, Stripes is what we call teammates here,&nbsp;&nbsp;
and they're just hearing stories from&nbsp; entrepreneurs around the world. And&nbsp;&nbsp;
you would hear this unbelievable story from&nbsp; incredible entrepreneurs who have a laptop,&nbsp;&nbsp;
which is that they'd have to fly to the United&nbsp; States on an airplane to make a US company in&nbsp;&nbsp;
order to get access to use financial system,&nbsp; to raise money from US or global investors,&nbsp;&nbsp;
often to take USD or to charge US customers. And&nbsp; you could have sat around and said, huh, is that&nbsp;&nbsp;
illegal? They don't live in the US. Can they have&nbsp; a US company? Absolutely. The US loves this. It is&nbsp;&nbsp;
incredibly encouraged for people from around the&nbsp; world to make a US company and many people do.&nbsp;
Now, why did it require an airplane, right?&nbsp; And so you start to hear that kind of thing&nbsp;&nbsp;
at a coffee shop amongst someone with a laptop&nbsp; who has access to the whole internet. And that&nbsp;&nbsp;
is a burning problem. Right. That is not a tier&nbsp; three issue. I am not able to run my business&nbsp;&nbsp;
without getting on an airplane should be sending&nbsp; alerts off in your whole psyche that you have&nbsp;&nbsp;
discovered something important. And so I wasn't&nbsp; at Stripe at the time, but I'm very thankful that,&nbsp;&nbsp;
I was running my own startup at the time. I was&nbsp; very thankful that the people at Stripe decided&nbsp;&nbsp;
to try to tackle that problem. And so Atlas&nbsp; is a way to start a company in a few clicks,&nbsp;&nbsp;
and we think that's an incredibly big deal&nbsp; because while there are smart humans across&nbsp;&nbsp;
the whole planet, the opportunity that they have&nbsp; is not uniform. But it's a little strange because&nbsp;&nbsp;
it's all the same MacBooks and it's a little&nbsp; strange because it's all the same IP addresses&nbsp;&nbsp;
and we all have plenty of bandwidth and smarts. And so what can we do to dramatically lower the&nbsp;&nbsp;
barrier to great people solving problems? And&nbsp; we've found over and over again that increasing&nbsp;&nbsp;
the ease and simplicity and decreasing the cost&nbsp; and complexity tends to lead to just more of that&nbsp;&nbsp;
thing. And we have a fundamental belief that there&nbsp; should be more startups and they're not finite.&nbsp;&nbsp;
And that belief comes from both just a core hope&nbsp; because there are so many problems in the world&nbsp;&nbsp;
that don't seem to be being solved fast enough by&nbsp; our current institutions and larger companies that&nbsp;&nbsp;
we think will actually, we need entrepreneurial&nbsp; energy to tackle them. And then it's also comes&nbsp;&nbsp;
from experience of seeing it happened. Instacart&nbsp; signed up for Stripe with a Gmail address and then&nbsp;&nbsp;
Covid happened and they delivered critical&nbsp; food to everyone when people were reasonably&nbsp;&nbsp;
not allowed to go to the grocery store easily. So you just don't know what the next Gmail address&nbsp;&nbsp;
is going to do. And so in Atlas, we radically&nbsp; try to simplify the process of getting a company&nbsp;&nbsp;
started and that mission has taken us to just&nbsp; solve more of the problem over time. And so over&nbsp;&nbsp;
the last few years, for those who have either used&nbsp; Atlas or have started a company or maybe follow&nbsp;&nbsp;
along on Twitter a bit, you might've seen just&nbsp; a progression of complexity that used to exist&nbsp;&nbsp;
being automated. And so a big one that we did&nbsp; about a year ago was this 83(b) election, which&nbsp;&nbsp;
is this absolutely Byzantine silliness system by&nbsp; which you have 30 calendar days to send a one-page&nbsp;&nbsp;
document to the IRS that could radically change&nbsp; the economics of how you are incentivized as a&nbsp;&nbsp;
founder. And this is not one of these greedy&nbsp; loophole. The IRS in the 1980s made this IRS&nbsp;&nbsp;
rule in order to spur more entrepreneurship. They want this. And the only issue is they&nbsp;&nbsp;
made it extremely difficult to accomplish. You&nbsp; have to send a snail mail in to an IRS address&nbsp;&nbsp;
in a particular format, in a particular way with&nbsp; no verification that it happened at all. And if&nbsp;&nbsp;
you do it 31 calendar days, there's no redo.&nbsp; Okay. Now again, if you're a product person,&nbsp;&nbsp;
you hear the founders terrified all day long&nbsp; about this same issue, just alarm bells in your&nbsp;&nbsp;
head whole time. And so I had experienced&nbsp; it for myself as a founder several times,&nbsp;&nbsp;
and I also just heard story after story and&nbsp; I just put on my to-do list for the team,&nbsp;&nbsp;
we are going to solve this 83(b) election thing.&nbsp; And there are very good reasons not to do it&nbsp;&nbsp;
because it comes with potential huge liability.&nbsp; Don't want to screw it up, it's snail mail.&nbsp;
You're really going to monetize this. It's a&nbsp; competitive advantage to do it. You can kind of&nbsp;&nbsp;
argue yourself not to do it in a million ways.&nbsp; But again, back to the mission of just taking&nbsp;&nbsp;
all of this complexity and turning into a single&nbsp; click. It was obvious to us and we got started on&nbsp;&nbsp;
it. Infrastructurally, we've been automating these&nbsp; steps and when this podcast airs, I guess today,&nbsp;&nbsp;
it will be true that when you go to start a&nbsp; company on Atlas, it will just be a single click.&nbsp;
You go to type in your friend's names,&nbsp; what the name of the company will be,&nbsp;&nbsp;
it'll tell you if it's available automatically&nbsp; or not. You can split the company up 50, 50 or&nbsp;&nbsp;
whatever you want to do, fill out a few things&nbsp; and you click go and then like a burrito coming&nbsp;&nbsp;
to you, like a pizza tracker, we will just handle&nbsp; all of the downstream activities that used to be,&nbsp;&nbsp;
hey, remember to come back in and purchase your&nbsp; shares. Why am I purchasing my shares? I'm just&nbsp;&nbsp;
getting started. Why am I writing a check for $10&nbsp; and putting into a bank account that I can't even&nbsp;&nbsp;
open yet? And then I have to wait for that to be&nbsp; done to get the 83(b) [inaudible 01:44:09]. All&nbsp;&nbsp;
of those steps are now just handled&nbsp; in the background so that we can get&nbsp;&nbsp;
you ready for business in a day or two. And so this is our vision. So you can&nbsp;&nbsp;
quit your job on a Sunday night, get the&nbsp; Sunday scaries, I'm done with this thing,&nbsp;&nbsp;
and on Monday morning fill out this form and the&nbsp; next day be able to run a billion-dollar business&nbsp;&nbsp;
because we will have automatically handled getting&nbsp; you access to banking systems, to payment systems,&nbsp;&nbsp;
to handling all the equity paperwork,&nbsp; filing your 83(b) election where you can&nbsp;&nbsp;
just shift from having worrying about the company&nbsp; starting process to just building and shipping.&nbsp;
And you'll just get kind updates in the&nbsp; background. Cool, the IRS is giving you a&nbsp;&nbsp;
tax ID. Cool, your 83(b) election is filed. Cool,&nbsp; all the founders have their equity and you're&nbsp;&nbsp;
ready to go on the cap table. And we've done this&nbsp; by deeply integrating with the governments and&nbsp;&nbsp;
deeply integrating with banking partners where&nbsp; we can get you access to the financial system&nbsp;&nbsp;
before the IRS and the other governments come&nbsp; back with their sort of official yeses because&nbsp;&nbsp;
we take care of the problem in the background by&nbsp; which we're faxing, phone calling, filling out&nbsp;&nbsp;
forms on your behalf. And so we just want to take&nbsp; all that complexity and just erase it so that you&nbsp;&nbsp;
get the same thing the YC group gets when they&nbsp; start, that checklist that they go through. We&nbsp;&nbsp;
just have the robot do exactly the same thing. And so in some ways it is a really big deal in a&nbsp;&nbsp;
big ship because it completely automates the&nbsp; company starting process. But in other ways&nbsp;&nbsp;
it's an incredibly incremental step that it's&nbsp; taken us three years to get to where we had to&nbsp;&nbsp;
systematically automate the internal steps, each&nbsp; one and now we've done the work to wrap it all&nbsp;&nbsp;
up into one button. And you can just watch&nbsp; how your company's doing in the dashboard.
Well, first of all, congrats Jeff and&nbsp; the Atlas team on shipping this. I know&nbsp;&nbsp;
this is a big milestone and&nbsp; it's been a long time coming.
Yeah, Atlas was actually a little reasonable&nbsp; before we decided to do all this work. It's&nbsp;&nbsp;
like why do this next step of completely&nbsp; automating it when it was actually fairly&nbsp;&nbsp;
straightforward before. Atlas has above 80 NPS,&nbsp; which is quite high. Apple is in the low 60s,&nbsp;&nbsp;
AirPods is 75. I love my AirPods. So Atlas&nbsp; in the 80s with almost 50% response rate is&nbsp;&nbsp;
quite high. And so we still chose to do another&nbsp; year of work to automate all of this work behind&nbsp;&nbsp;
the scenes because we see that companies are&nbsp; charging their customers sooner when they go&nbsp;&nbsp;
through this automated process versus waiting.&nbsp; And it's a little strange. You just started your&nbsp;&nbsp;
company. Well, what does it really matter to&nbsp; wait an extra seven days or 20 days before you&nbsp;&nbsp;
can really get going on business? Those are&nbsp; really fragile days which you're building.&nbsp;&nbsp;
And to some of our conversation earlier, that&nbsp; amazing feeling of getting your first customer&nbsp;&nbsp;
and being in it with them and money actually&nbsp; exchanging hands and getting that relationship.&nbsp;
If we can slide that forward in the&nbsp; world by a couple of days or weeks,&nbsp;&nbsp;
which we're seeing, like half the time&nbsp; it takes to get to your first customer,&nbsp;&nbsp;
just shave a whole week off of your company&nbsp; and you can kind of see GDP being born sooner.&nbsp;&nbsp;
And went my whole life knowing that okay, GDP is&nbsp; not finite and it can grow, but I've never really&nbsp;&nbsp;
seen it and now I've actually seen it grow faster,&nbsp; sooner. And I think anything we could do to just&nbsp;&nbsp;
move that forward is going to inspire and lower&nbsp; the bar for more people to be an entrepreneur&nbsp;&nbsp;
because they'll see how satisfying that can be. And another stat, which really&nbsp;&nbsp;
was interesting to me recently is that we have&nbsp; seen since doing much of this automation work,&nbsp;&nbsp;
that more solo founders are using Atlas than ever&nbsp; before. And I think it's because you can just do a&nbsp;&nbsp;
lot more on the internet as a founder with no-code&nbsp; tools and everything else and get going. Very cool&nbsp;&nbsp;
to see that bringing the best of the internet and&nbsp; making it available worldwide can be correlated&nbsp;&nbsp;
with more people becoming entrepreneurs.&nbsp; And I think we should just keep doing that.
It's incredibly inspiring and I think this is&nbsp; going to be a huge deal. It's hard to think&nbsp;&nbsp;
about how many, what sorts of changes in tech&nbsp; could transform how many companies are started&nbsp;&nbsp;
and how many companies not just started&nbsp; but actually happen because to your point,&nbsp;&nbsp;
you may start and they're like, nah, nevermind a&nbsp; few days later if it's still stuck in some queue.
Totally. And then you don't know where these&nbsp; things are going to go. We have the sort of&nbsp;&nbsp;
cohort of 2024 startups in Atlas got to $50&nbsp; million in revenue twice as quickly as the&nbsp;&nbsp;
cohort in 2023. And so we kind of also think&nbsp; sometimes, oh, it was the pandemic that pushed&nbsp;&nbsp;
everything online. Those are our best years.&nbsp; It's like we're seeing the earliest cohort&nbsp;&nbsp;
charts of new startups just cracking up into&nbsp; the right. And that's very exciting because&nbsp;&nbsp;
you also hear sometimes, well the funding&nbsp; market is down and valuations and this and&nbsp;&nbsp;
that and the other. That is much more of a point&nbsp; in time capital analysis and much less business,&nbsp;&nbsp;
like just how businesses are working day to day.&nbsp; It's really in the revenue that is representative&nbsp;&nbsp;
of their futures and that looks amazingly bright. And then of course these companies go off to do&nbsp;&nbsp;
pretty wild things. Companies that have started&nbsp; through Atlas, there's been 55,000 of them to date&nbsp;&nbsp;
are doing $5 billion a year in revenue. I think it&nbsp; actually resets their expectations of what other&nbsp;&nbsp;
tools will be in the future. It's like, well, if&nbsp; it was so easy for me to get my company started,&nbsp;&nbsp;
well why is it so hard to do banking?&nbsp; Well, thankfully there are some great&nbsp;&nbsp;
services for it, but I think if we can&nbsp; push people towards expectations higher,&nbsp;&nbsp;
then they will want to make their companies&nbsp; better and we'll just all benefit from that.
How much of this is based on you guys&nbsp; sending faxes and sending mail yourself,&nbsp;&nbsp;
like I don't know how much you can&nbsp; talk about the behind the scenes,&nbsp;&nbsp;
but is there a lot of, through this&nbsp; ops element to automating some of this?
Atlas is in total 10 people, which is I think&nbsp; a relatively small group for the role that it&nbsp;&nbsp;
plays in the wider startup ecosystem. And we just&nbsp; don't pick up work we can't automate because we&nbsp;&nbsp;
know that we need the leverage. And so we're&nbsp; not going to put ourselves in situations in&nbsp;&nbsp;
which we have to compete to be the best. We're&nbsp; going to put ourselves in situations where we&nbsp;&nbsp;
can automate it and be the only, and that's a&nbsp; different mindset. So in terms of why we picked&nbsp;&nbsp;
up 83(b) election as a topic, when we made that&nbsp; decision, we made a commitment that we're going&nbsp;&nbsp;
to do this forever. We're going to do this&nbsp; forever. This is a piece of infrastructure&nbsp;&nbsp;
for the rest of the internet. That is a very&nbsp; high bar to set as the thing you're going to do.&nbsp;
And so we're happy to take our time. This is&nbsp; part, versus like go-go-go versus the long-term&nbsp;&nbsp;
compounding. Go-go-go was when we assigned one&nbsp; engineer, hey, it's your job today to send one&nbsp;&nbsp;
piece of paper to the office with this third party&nbsp; mail service. Why? Doesn't matter. Today, just&nbsp;&nbsp;
send a single piece of paper to the office and an&nbsp; incredible engineer, and she went on to lead all&nbsp;&nbsp;
of 83(b) election work. She sent it. And the proof&nbsp; of just receiving the piece of paper at the office&nbsp;&nbsp;
that we had just sent yesterday is incredible&nbsp; proof. Right. We're like, well look. I mean,&nbsp;&nbsp;
the 83(b) election is just sending this piece&nbsp; of paper to the IRS, like we just did it. Right.&nbsp;
That go-go-go as soon as possible was&nbsp; extremely useful because it's just like,&nbsp;&nbsp;
look, this exists. We can do it. Come on. On the&nbsp; long-term compounding part, we were extremely&nbsp;&nbsp;
serious about how we picked our third party&nbsp; vendors, and backup vendors, and what promises,&nbsp;&nbsp;
and SLAs, and reporting systems, and alerts, and&nbsp; playbooks, and backup processes, like it's in a&nbsp;&nbsp;
very intense amount of internal structure we use.&nbsp; But again, we have to look at where the value is.&nbsp;&nbsp;
The value is in making sure it happens. Does it&nbsp; need to be us sending the mail? Does it need to&nbsp;&nbsp;
be us talking to government? Not necessarily. And&nbsp; we have chosen to work with third parties and many&nbsp;&nbsp;
backup third parties as well because one, there's&nbsp; expertise in the world of physically printing and&nbsp;&nbsp;
sending mail that the 10 of us are not going&nbsp; to today become experts in. And two, I think it&nbsp;&nbsp;
also causes us to build better software in that&nbsp; we now need to evaluate if something's actually&nbsp;&nbsp;
working because it's happening externally. Whereas when you build it yourself, again, you&nbsp;&nbsp;
have this natural feeling, well, we built it. It&nbsp; must be working. Oh, later we'll add alerts. Later&nbsp;&nbsp;
when there problems, we'll figure out playbooks.&nbsp; Well look, when it's a third party building it,&nbsp;&nbsp;
you're like, wait a second. What happens if they&nbsp; screw up? Like cool, we better figure that out.&nbsp;&nbsp;
We better OCR all the results. We better do all&nbsp; these check sums, we better... And it would be&nbsp;&nbsp;
awesome if we could always treat our internal&nbsp; work that way, but because it was external,&nbsp;&nbsp;
it forced us to be more rigid where we needed&nbsp; to be rigid and create interfaces and kind of&nbsp;&nbsp;
commitments. And again, we work with a bunch of&nbsp; great third parties and back up third parties to&nbsp;&nbsp;
execute this. And each year we write a document&nbsp; called Should We Do This Ourselves? And we look&nbsp;&nbsp;
at the other nine of us around the room and go,&nbsp; of course we shouldn't. Let's go on to something&nbsp;&nbsp;
else. So again, we're just really stitching&nbsp; it together, but ensuring that it happens.
Awesome. Okay. I was imagining fax machines just,-
There are fax machines occurring.&nbsp; There are fax machines occurring,-
Not in the Stripe [inaudible 01:54:38].
And there are phone calls being made and there&nbsp; are robots waiting on phones on hold as well.
Oh, amazing.
There's quite a lot going on.
AI is here. I saw a stat that one&nbsp; in six new Delaware corporations&nbsp;&nbsp;
are now started on Stripe Atlas. That's absurd.
Yep. I'm very excited to tell you when&nbsp; it's one in five, but it is not today.
Okay, sounds like we're close.
We're on our way.
Sounds like we're close. The other stat I have&nbsp; here is that the fastest growing cities for&nbsp;&nbsp;
startups. Here's what I have, I don't know if you&nbsp; know this, but Boulder, Shenzhen, and Las Vegas.
They're everywhere. One of the, it's like stat&nbsp; we kind of came up with a little bit last year&nbsp;&nbsp;
that I'm just personally deeply obsessed with is&nbsp; founding teams in which the co-founders are in&nbsp;&nbsp;
multiple countries. So we kind of nickname this.&nbsp; Again, it's like giving things a good title,&nbsp;&nbsp;
headlines. Cross-Border Founders. Wow. More&nbsp; than 20% of multi-founder teams have at least&nbsp;&nbsp;
one founder from another country. That is&nbsp; astounding to me, that the internet could&nbsp;&nbsp;
bring people together like that. And I think&nbsp; that's going to provide more perspectives,&nbsp;&nbsp;
more solutions will be local and global.&nbsp; Just all perspectives are great. And again,&nbsp;&nbsp;
I think the Atlas team itself represents&nbsp; this. We were very intentional of how&nbsp;&nbsp;
we built the Atlas team. It's majority&nbsp; women and we have more diversity to hire,&nbsp;&nbsp;
but we're just very intentional to make it a&nbsp; team that had diverse perspectives. You've been&nbsp;&nbsp;
on teams that don't have diverse perspectives of&nbsp; any type. They are so much worse. There's no real&nbsp;&nbsp;
science necessary here. We just enforce that. We&nbsp; had the opportunity to build this team that way.&nbsp;
And it was really important to me that it&nbsp; represented a world we wanted things to&nbsp;&nbsp;
look like and to represent. And it just had to&nbsp; be very intentional about it because I've made&nbsp;&nbsp;
mistakes in my career previously where my startup&nbsp; was all men when we sold to box one of them. And&nbsp;&nbsp;
on each hire it was harder and harder and harder&nbsp; to hire someone of a different background. Just&nbsp;&nbsp;
naturally folks didn't want to join that type&nbsp; of team. And that was the last time I've ever&nbsp;&nbsp;
going to make that mistake, which is that early&nbsp; the candidate poll must match where you want the&nbsp;&nbsp;
team to go. It's not a down funnel problem, it is&nbsp; an up funnel problem. And where you have to just&nbsp;&nbsp;
make sure that for each role you're comfortable&nbsp; with the distribution of people and backgrounds&nbsp;&nbsp;
in your candidate pool and go from there.&nbsp; And I think that is one of the reasons why&nbsp;&nbsp;
that 10 person group is so effective, is it&nbsp; has just a lot of diversity and perspective.
Another skill Jeff Weinstein is incredible&nbsp; at that I wasn't even aware of. We're going&nbsp;&nbsp;
to add them to the list and I actually saw a&nbsp; photo of the team and I noticed that. And so&nbsp;&nbsp;
great work. Is there anything else on Atlas&nbsp; that you wanted to share before I get into&nbsp;&nbsp;
how you actually made Atlas happen at a company&nbsp; like Stripe that has a billion things to do?
We just want to hear about what's hard for you.&nbsp; If you look back in your emails and if you started&nbsp;&nbsp;
a company recently, you're starting a company&nbsp; right now, the whole world is counting on you&nbsp;&nbsp;
to pick a customer, solve their problem 10 times&nbsp; better than their alternative, get it to them,&nbsp;&nbsp;
charge for it, become economically viable and&nbsp; build a great business that provides great&nbsp;&nbsp;
services. We are not counting on you to become&nbsp; experts at this silliness of administratively&nbsp;&nbsp;
running your company. Imagine life without&nbsp; Google Docs where you'd have to hire an IT&nbsp;&nbsp;
person to run your IT back end on employee three.&nbsp; You'd have an IT person or imagine the world&nbsp;&nbsp;
without AWS for EC2 or S3 or any of these cloud&nbsp; services and you're racking computers yourself.&nbsp;
You're just absolutely not going to try as&nbsp; many things. We just see the company structure,&nbsp;&nbsp;
the structure, bringing people together to be&nbsp; like that, and we want to automate more and more&nbsp;&nbsp;
and more of it and turn it into software. So we're&nbsp; looking for the next things to work on. We have a&nbsp;&nbsp;
couple ideas, but we expect to turn more of groups&nbsp; of people working together, that administration&nbsp;&nbsp;
into software. And I think it's just going to&nbsp; unlock huge amount more people choosing to do it.
Interesting. I'm so curious what that ends up&nbsp; being. If you really think about what you're doing&nbsp;&nbsp;
here, if you believe that entrepreneurship and&nbsp; innovation and technology make the world better,&nbsp;&nbsp;
you're creating such an unlock to&nbsp; allow more of that. And like I said,&nbsp;&nbsp;
I think it's hard to imagine and think of other&nbsp;&nbsp;
examples that could be as transformative&nbsp; and impactful as just making this process.
It's funny because I go back to again, I also&nbsp; hear from founders, entrepreneurs like, oh,&nbsp;&nbsp;
I can't think of an idea. Like, ah, I need a&nbsp; startup idea. And yet everything in the world&nbsp;&nbsp;
is broken. And I also recall my first startup&nbsp; early 2010, 2012 ish, I joined a friend's&nbsp;&nbsp;
company. That was started at the same time that&nbsp; the Stripe founders started Stripe. And that is,&nbsp;&nbsp;
I think about that a lot because with the same&nbsp; information, knowing how hard it was to accept&nbsp;&nbsp;
online payments, I chose to work on something&nbsp; else where they didn't. They worked on making it&nbsp;&nbsp;
easy in seven lines of code to accept payments&nbsp; online, which turned out to be really useful.&nbsp;
So I really encourage people to be very sensitive&nbsp; to the problems that they see and just not let any&nbsp;&nbsp;
little hiccup go unnoticed. And I think Atlas is&nbsp; really a manifestation of that, which is, let's&nbsp;&nbsp;
actually look at every single thing. You went from&nbsp; hobby to economically successful operation and&nbsp;&nbsp;
which of any moment along the way you shouldn't&nbsp; have had to do. And we think those things&nbsp;&nbsp;
are a fair game to play with in any topic. I think&nbsp; that there are many more gigantic businesses,&nbsp;&nbsp;
important things to be solved sitting in plain&nbsp; sight. I can't see them always, but when you hear,&nbsp;&nbsp;
if you sit in enough silence and you hear the same&nbsp; people complain about problems, you too might find&nbsp;&nbsp;
something as big as online payments are hard,&nbsp; which was sitting right in front of all of us.
And I think it's important to note, it doesn't&nbsp; necessarily have to be a venture-backed,&nbsp;&nbsp;
venture scale company. Right. There are many, most&nbsp; businesses in the world are non venture-backed,&nbsp;&nbsp;
venture scale billion-dollar companies.&nbsp; You can build a profitable company.
It's kind of funny. We've all put this&nbsp; badge of honor of giving away a lot of&nbsp;&nbsp;
your company. People really love owning a&nbsp; lot of their company and being successful.&nbsp;&nbsp;
So you just got to pick the right&nbsp; capital structure for your business.
And again, the amount of money that has been&nbsp; generated of the companies that started through&nbsp;&nbsp;
Atlas, you said $5 billion, basically&nbsp; that's the GDP of Atlas. That Atlas is,-
And that's like revenue per&nbsp; year and that's growing,-
Per year.
Yeah.
Yeah. And obviously a lot of it would've happened&nbsp; anyway, but still it accelerated. It's probably&nbsp;&nbsp;
growing faster. A lot of it probably&nbsp; never would've happened otherwise. Yeah.
We ran a survey a little bit ago, we need to&nbsp; rerun this, where we just asked people would&nbsp;&nbsp;
they have started their business without Atlas.&nbsp; And about 20% of people said they wouldn't have&nbsp;&nbsp;
or wouldn't had then. And again, these things are&nbsp; fragile. Right. And it's not all Google employees&nbsp;&nbsp;
leaving their job to the build something.&nbsp; It's people from every possible background,&nbsp;&nbsp;
every possible role, every possible job,&nbsp; every possible age group who see problems&nbsp;&nbsp;
and can solve it. So it's dramatically&nbsp; more fragile than people think.
Well, great work, Jeff, and team&nbsp; Atlas and Stripe in general.
Fun.
Let's talk about one last thing. There's so&nbsp;&nbsp;
many more things I still want to&nbsp; talk about. Maybe we'll have a,-
We can go quick. Yeah, we&nbsp; can [inaudible 02:03:08].
Make it 2X speed. So Atlas is basically a zero to&nbsp; one product. I know you didn't start initially,&nbsp;&nbsp;
it was there, but you took it from, I don't&nbsp; know, maybe you took it from 0.5 or something&nbsp;&nbsp;
to one in 100 now, and a lot of people&nbsp; struggle with starting things like this&nbsp;&nbsp;
within larger companies. Like Stripe's a large&nbsp; company, right? It's like a very innovative,&nbsp;&nbsp;
well run company, but it's also a large&nbsp; company. And clearly you made shit happen,&nbsp;&nbsp;
you and your team. What kind of things have&nbsp; you learned? Actually, let me read a quote.&nbsp;&nbsp;
Here's a quote that kind of describes you being&nbsp; good at this from one of your former colleagues&nbsp;&nbsp;
who will go unnamed. "Jeff is really good&nbsp; at cutting through the BS. You hear so much&nbsp;&nbsp;
about frameworks and all this complicated&nbsp; stuff that people talk about, NPM circles,&nbsp;&nbsp;
one of the most straightforward, obvious things&nbsp; probably right. I get so annoyed after calls with&nbsp;&nbsp;
Jeff sometimes because I know he's right about&nbsp; something. I banged my head against the wall for&nbsp;&nbsp;
months." And so talk about just what you've done,&nbsp; what you've learned about getting stuff done.
Talk about what you've done, what&nbsp; you've learned about getting stuff&nbsp;&nbsp;
done at a large company. What do you need to do?
Not having things be your idea I think is&nbsp; really powerful. I just talked to 50 customers&nbsp;&nbsp;
who all yelled the same thing. Here they are in&nbsp; varieties of quotes and forms and the rest of it,&nbsp;&nbsp;
and you put some three bullet points of strategy&nbsp; around why it's important, it's going to help you&nbsp;&nbsp;
win more market share, and the rest of it and how&nbsp; you can do it well. Cool. What else could we want&nbsp;&nbsp;
to do? Maybe somebody has something where&nbsp; 51 people have the same burning thing, but&nbsp;&nbsp;
the majority failure mode is we do nothing. That's&nbsp; the majority failure mode. So one, aligning people&nbsp;&nbsp;
with deep customer stories story boarding some&nbsp; solution visually with a Sharpie and not a pencil,&nbsp;&nbsp;
not Figma initially, not high or low fidelity. I&nbsp; can never remember which one is the detailed one,&nbsp;&nbsp;
but Sharpie. What is the unconstrained&nbsp; perfect solution to this burning problem?&nbsp;
That's Pixar-style storyboard. You don't need to&nbsp; be a designer. You can just draw stick figures&nbsp;&nbsp;
on a piece of paper or whimsical or whatever you&nbsp; want to do. And with those things, if you're not&nbsp;&nbsp;
asking for the sun and the moon on headcount&nbsp; and team size to make some forward progress,&nbsp;&nbsp;
who could stop you? Let's get some first version&nbsp; working. It was very motivating to get that single&nbsp;&nbsp;
piece of paper in the mail, which was blank,&nbsp; to kick us off on the 83(b) election. Again,&nbsp;&nbsp;
by the time this podcast airs, we'll have&nbsp; crossed 10,000 83(b) elections filed,&nbsp;&nbsp;
and we will have done them all 100.00% on&nbsp; time. With the burning use case, why customers&nbsp;&nbsp;
are going to need it, why we can do it cheaply,&nbsp; effectively, safely over a long period of time,&nbsp;&nbsp;
and here's the way to get tangible, forward&nbsp; progress quickly against the stick figure vision,&nbsp;&nbsp;
but with something in the browser or one version&nbsp; of it. Let's just get one thing working one time.&nbsp;
I find proof of existence to be an incredibly&nbsp; powerful proof, rather than proof by theory or&nbsp;&nbsp;
proof by debate. It's like, "Look, we did it one&nbsp; time. Hey, I'm holding the piece of paper." Pretty&nbsp;&nbsp;
motivating. If we just printed out the right&nbsp; information, we'd be done. You're like, "Okay,&nbsp;&nbsp;
actually there's a lot to do other than just&nbsp; that," but it really pushed us forward. Cutting&nbsp;&nbsp;
through a little bit of the red tape is about&nbsp; momentum and making each step not such a big&nbsp;&nbsp;
deal and asking for less permission. Then of&nbsp; course, once you have a little bit of that&nbsp;&nbsp;
under your belt, you're going to naturally be&nbsp; trusted with taking more of those kinds of bets.&nbsp;
Paired with some of the things we talked about&nbsp; earlier of everyone's looking at the same place&nbsp;&nbsp;
about the metrics, everyone can watch the success.&nbsp; We don't need to do big, internal updates with&nbsp;&nbsp;
long-winded PowerPoint presentations and scrambles&nbsp; the night before. You can just go to the metrics&nbsp;&nbsp;
page and see how we're doing. That brings so much&nbsp; trust to the group that people start going from,&nbsp;&nbsp;
"Why do we have this Atlas thing that doesn't&nbsp; really produce so much money. It's charging&nbsp;&nbsp;
companies when they don't have money. We're a&nbsp; big payments business. How do you even compare&nbsp;&nbsp;
these things?" To "Wow, look at the progress&nbsp; that they're making against the mission,&nbsp;&nbsp;
and look at its impact on the curves."&nbsp; And you start to root for it more.&nbsp;
I think that's how we got it there. I will say&nbsp; one other thing, which is that making something&nbsp;&nbsp;
economically viable is extremely important.&nbsp; I am probably the fourth person to run Atlas,&nbsp;&nbsp;
and it's quite a pantheon of people prior&nbsp; to me, including the founder of Mozi,&nbsp;&nbsp;
which is a compliance startup, Watershed,&nbsp; which is this amazing climate reporting tool,&nbsp;&nbsp;
also led Atlas, Patrick McKenzie, patio11,&nbsp; for many folks who [inaudible 02:08:46]
Wow, what an alumni group, this collection.
We owe ourselves a dinner. We owe ourselves&nbsp; a dinner. Quite a group. And now we have a&nbsp;&nbsp;
new person. I technically no longer lead&nbsp; Atlas, so we've hired up a whole team,&nbsp;&nbsp;
which is really exciting. And Hayley Halvarsson,&nbsp; who's joined us about a year or two ago,&nbsp;&nbsp;
she leads Atlas now and you can find her&nbsp; on Twitter. She's fantastic. We swap jobs&nbsp;&nbsp;
over a course of a year, just one month at&nbsp; a time, the roles. And so she worked for me,&nbsp;&nbsp;
then I worked for her, and she's gone&nbsp; off to hire some amazing people to run&nbsp;&nbsp;
Atlas. So it's really quite a privilege&nbsp; to have these people lead it over time.&nbsp;
But it was really important for us to communicate&nbsp; why we were going to run this in an economically&nbsp;&nbsp;
viable way, and I think that applies to all&nbsp; products and all businesses. It's like, "Look,&nbsp;&nbsp;
if you're a customer acquisition-style&nbsp; product, showcase why this is the best&nbsp;&nbsp;
customer acquisition for the dollar for the&nbsp; company. If you are a margin-generating,&nbsp;&nbsp;
moat-creating, ecosystem-growing portion of the&nbsp; business, then your metrics have to show it." So&nbsp;&nbsp;
you can't just have half the story of just the&nbsp; product quality and the tweets. You have to have&nbsp;&nbsp;
the economics. Who else is going to put this much&nbsp; energy into this style of product and that gives&nbsp;&nbsp;
us confidence that we should invest it in the&nbsp; long term? Because alternatives can come and go,&nbsp;&nbsp;
and I super encourage there to be more Atlas&nbsp; alternatives. That'd be great for founders,&nbsp;&nbsp;
but I think over the long term, it'll be&nbsp; difficult to do so because of the business model.
There actually was an alternative at one&nbsp; point, AngelList, and then they're like,&nbsp;&nbsp;
"No, Stripe is killing it. Let's&nbsp; just send everyone to Atlas."
I had worked on Stripe payments for a while, and&nbsp; I had just started on Atlas, and I think that&nbsp;&nbsp;
same month AngelList announced that they were&nbsp; doing incorporation and banking and cap table&nbsp;&nbsp;
all together, which was exactly what I wanted to&nbsp; do. I was like, "Oh shoot, did I sign up for the&nbsp;&nbsp;
wrong thing? AngelList is such a smart group&nbsp; of people, so customer-oriented, great brand,&nbsp;&nbsp;
I love many of the people that work there, they&nbsp; work with some of the best legal minds, and they&nbsp;&nbsp;
have the RUV setup. There's so much awesomeness&nbsp; here." I was like, " Should we really compete?&nbsp;&nbsp;
What should we do here?" And we thought about it&nbsp; more and more like, "Look, in the very long term,&nbsp;&nbsp;
this company-starting process is going to become a&nbsp; efficiency cost problem, and there's so much long&nbsp;&nbsp;
tail complexity with dealing with multiple&nbsp; financial institutions, multiple government&nbsp;&nbsp;
processes, all of this legal complexity, and&nbsp; it's difficult to charge a lot of money for it&nbsp;&nbsp;
because it's hard to charge people money when&nbsp; they haven't even started the business yet."&nbsp;
We looked at it and said, "Look,&nbsp; we're going to keep this long-term,&nbsp;&nbsp;
compounding approach because we think that this&nbsp; is where it's going to go." And it was a zero&nbsp;&nbsp;
interest rate environment at the time. AngelList&nbsp; built a phenomenal product. I looked at it with&nbsp;&nbsp;
nothing but admiration and happiness, but it also&nbsp; smarted and hurt. We kept building, kept building,&nbsp;&nbsp;
kept building, and I got a phone call one&nbsp; night, on my wife's birthday before we sat&nbsp;&nbsp;
down for dinner, and it was Dan at AngelList,&nbsp; I hope he'd be comfortable telling the story,&nbsp;&nbsp;
who I love. Incredible product mind and he led&nbsp; product over AngelList for startups. He said,&nbsp;&nbsp;
"We're going to get out of incorporation.&nbsp; This is not going to be our focus&nbsp;&nbsp;
going forward. Do you want the business?" That was like a year and a half after they had&nbsp;&nbsp;
really gone out, or maybe two years after they'd&nbsp; gone out, or something like this. I was like,&nbsp;&nbsp;
"Wow." We had kept such an open relationship&nbsp; with them. We had paired with them on legal&nbsp;&nbsp;
constructs. We had discussed 83(b) election&nbsp; openly. A lot of people were like, "I can't&nbsp;&nbsp;
believe you're talking to the competitor."&nbsp; Look, we all share the same mission here. Yes,&nbsp;&nbsp;
we're competing, but are we really all better off&nbsp; from treating each other at arm's distance? We&nbsp;&nbsp;
had a shared Slack channel. We discussed when&nbsp; the Delaware was slow on incorporation. One&nbsp;&nbsp;
time is because they were playing softball and&nbsp; they had an afternoon off. That's a real story,&nbsp;&nbsp;
and we've discussed it. AngelList was incredible&nbsp; in how they evaluated it. We're evaluating&nbsp;&nbsp;
different partners, but because of our working&nbsp; relationship and the quality of your product,&nbsp;&nbsp;
and they saw we were going with 83(b) election&nbsp; and the intensity of that, they just put up a&nbsp;&nbsp;
webpage that said to get started with AngelList,&nbsp; if you need a company, go right over to Atlas.&nbsp;
That was a really amazing moment because I&nbsp; respected them so much and I looked up to them so&nbsp;&nbsp;
much that they would mutually beneficially choose&nbsp; to do that. And everybody was excited and happy,&nbsp;&nbsp;
and customers are happy, and it's been an&nbsp; incredible relationship since, in which you&nbsp;&nbsp;
can start on AngelList, go through Atlas, and then&nbsp; all of your information is automatically populated&nbsp;&nbsp;
into AngelList automatically. We've since rolled&nbsp; that out with several other partners, Mercury,&nbsp;&nbsp;
Carta, others, but AngelList really led the&nbsp; way there, and we maintain a great relationship&nbsp;&nbsp;
with the team. It took a while, but it really&nbsp; reproved to me that they're not competitors. It's&nbsp;&nbsp;
alternatives, and if you care about your customer,&nbsp; you care about their alternatives, and if you care&nbsp;&nbsp;
about the mission, you need to all work together.&nbsp; Look, there's some friendly competition, of&nbsp;&nbsp;
course. We all want to win, but in the long term,&nbsp; I think all parties are significantly better off.
Wow, that is an awesome story. I don't know&nbsp; if you've shared that anywhere else. There's&nbsp;&nbsp;
so many lessons there that I could spin off&nbsp; on and... Not worrying about competition,&nbsp;&nbsp;
staying heads down, just solving customer&nbsp; problems, staying close to your competition,&nbsp;&nbsp;
not being afraid to talk to them, sharing&nbsp; advice with each other, just building the best&nbsp;&nbsp;
possible product. I don't know, there's&nbsp; a ton there that's super interesting.
I couldn't really draw it up any better, and&nbsp; I think the world is better off with more&nbsp;&nbsp;
specialization, and it's a pain in the butt to&nbsp; do these incorporations. I think you want more&nbsp;&nbsp;
specialization and more partnership, and I think&nbsp; a lot of companies are starting to do that now.
Let me go back to the lessons you shared on&nbsp; how to build something new at a big company,&nbsp;&nbsp;
then we can wrap up. I took a bunch of notes here,&nbsp; and these are awesome and they actually resonate&nbsp;&nbsp;
a lot with Mihika, who came on the podcast,&nbsp; who's at Figma, been the person building a lot&nbsp;&nbsp;
of zero-to-one stuff. So it's nice that there's&nbsp; these trends that are coming up again and again.&nbsp;
One tip is storyboard the ideal. With a Sharpie,&nbsp; draw out, "Here's this exciting vision of what&nbsp;&nbsp;
this could be if we were to pull it off without&nbsp; constraints." Unconstrained, powerful vision. Two&nbsp;&nbsp;
is solve a burning use case. Make it clear&nbsp; this is a huge problem for a lot of people.&nbsp;&nbsp;
There's probably stories you share there. Show&nbsp; tangible forward progress like, "Look at this,&nbsp;&nbsp;
we made this progress, we made this progress. Sent&nbsp; ourselves a piece of blank paper. Look at this,&nbsp;&nbsp;
it's a huge milestone." And have momentum, and&nbsp; Mihika talked about this. Keep the fire alive.&nbsp;&nbsp;
Keep the fire alive, show momentum. We're making&nbsp; progress. This metrics moving up into the right.&nbsp;&nbsp;
Then there's a milestone... Felt like you&nbsp; had an early milestone of like, "Look, we&nbsp;&nbsp;
made progress," and then also, have the business&nbsp; case, basically. "Look how much we could make and&nbsp;&nbsp;
look what this could be if we were to succeed."&nbsp; Anything you'd add there? Anything you'd correct?
Bringing the earliest customers into the room with&nbsp; your team as soon as humanly possible. We would&nbsp;&nbsp;
just invite a founder to the team meeting. We&nbsp; would pipe all their feedback into a Slack channel&nbsp;&nbsp;
automatically. We have all the NPS scores going&nbsp; to a channel, and anytime it's not a 10 for 10,&nbsp;&nbsp;
we follow up directly. Constant engagement with&nbsp; a customer creates the momentum where it doesn't&nbsp;&nbsp;
need to be the product person or some other leader&nbsp; saying, "We need to do this. Follow me." It's,&nbsp;&nbsp;
"Oh my gosh, the world needs this. Let's&nbsp; figure out how to do it even faster."&nbsp;
And a tip that the team has tried, and this&nbsp; is well since I've been involved day-to-day,&nbsp;&nbsp;
is literally inviting customers in to design the&nbsp; product, which I'd actually never heard of. "Hey,&nbsp;&nbsp;
we're thinking about what happens after&nbsp; incorporation now and what can we do&nbsp;&nbsp;
to help founders after they've set up their&nbsp; company? What would be magical there?" We just&nbsp;&nbsp;
invite founders in, into a Whimsical, a piece&nbsp; of software I love. It's a really easy learning&nbsp;&nbsp;
curve to create visual diagrams. And rather than&nbsp; doing a UXR about it, we just say, "What would you&nbsp;&nbsp;
hope this dashboard would have?" And they'd grab&nbsp; a thing, and they start typing, and they start&nbsp;&nbsp;
drawing what they want their dashboard to be.&nbsp; Why were we guessing beforehand? I now scratch&nbsp;&nbsp;
my head. I'm several years into a decade-plus&nbsp; building things and I was like, "I doing this by&nbsp;&nbsp;
myself. Why didn't I just assign it to the people&nbsp; who are going to use it in the first place?"&nbsp;
Now look, that doesn't always work because not&nbsp; all of your customers are going to be product&nbsp;&nbsp;
designers at heart, but more of them than you&nbsp; think, and I think it's giving your customers&nbsp;&nbsp;
write access, and not just read access, to&nbsp; your company is incredibly powerful. I think&nbsp;&nbsp;
I had not quite seen it so directly where you&nbsp; just actually designed what they want, but I&nbsp;&nbsp;
saw a diagram of something we're working on right&nbsp; now. I was like, "Wow, we haven't even had design&nbsp;&nbsp;
look at it." They're like, "No, actually the&nbsp; customer drew it." Great. Why were we guessing?
I think you have an unfair advantage where&nbsp; your customers are founders and oftentimes&nbsp;&nbsp;
have product skills and design skills,&nbsp; but I love that [inaudible 02:18:43].
It's true, but I will really push,&nbsp;&nbsp;
because you don't need a hundred of them and&nbsp; you'll find somebody somewhere who knows.&nbsp;&nbsp;
You just got to sit in a little more&nbsp; silence. They'll raise their hand.
There's a quote you shared somewhere that relates&nbsp; to what you just said that your dad once said,&nbsp;&nbsp;
"You can screw up a sentence if&nbsp; it begins with 'The customer.'"
That's true. Yeah, my dad runs an IT business&nbsp; in Baltimore to help other businesses with&nbsp;&nbsp;
their computer systems. Growing up, I would&nbsp; literally, physically clean the keyboards&nbsp;&nbsp;
of his employees and dust the mice. But&nbsp; yeah, he's very, very customer-oriented,&nbsp;&nbsp;
where I get a lot of it from, and my mom's a&nbsp; painter, so I think there's some combination&nbsp;&nbsp;
of talents or interests there. He would take it&nbsp; one step further, and he sometimes physically&nbsp;&nbsp;
bring a chair over in a meeting and say, "The&nbsp; customer is sitting here," and you'd have to&nbsp;&nbsp;
pretend. Then he would fake talk to the invisible&nbsp; customer. "Based on what you've seen today at the&nbsp;&nbsp;
meeting..." I saw him do this one time. "Based&nbsp; on what you've seen today at the meeting, are&nbsp;&nbsp;
you more likely to pay your bill or less likely&nbsp; to pay your bill based on what you witnessed?"&nbsp;
That's a little intense on the pantomime, but&nbsp; I think the point gets across that... Again,&nbsp;&nbsp;
because it's so natural to think internal,&nbsp; if you begin the sentence physically with&nbsp;&nbsp;
"The customer" then start your sentence,&nbsp; you just have a much better shot at it.
That's an amazing story. Very a study&nbsp; group-ish, like an early prototype. Jeff,&nbsp;&nbsp;
we've covered so much ground. I have two&nbsp; hours more worth of questions, but we need to-
Let's lock.
We need to cut it off, I think. Is&nbsp; there anything else you wanted to&nbsp;&nbsp;
share or leave listeners with before we&nbsp; get to a very exciting lightning round?
Really excited about whatever you're building out&nbsp; there, thinking of building. My email address is&nbsp;&nbsp;
incredibly easy to find. My Twitter handle&nbsp; is incredibly easy to find. Do not hesitate&nbsp;&nbsp;
to send me cold emails. My love language is&nbsp; Loom videos of bugs, but feel free to send&nbsp;&nbsp;
anything you have off the top of your head. I&nbsp; respond to good cold emails. Don't hesitate.
What's the email, real quick, for people?
If finding my email address is your issue? It&nbsp; can't possibly be, but it is my first initial and&nbsp;&nbsp;
last name at basically everything in the world,&nbsp; though my handle on Twitter is jeff_weinstein,&nbsp;&nbsp;
but gosh, if you can't find my email&nbsp; address then you got a bigger problem.
Okay, we'll link to it in the&nbsp; show notes, as well. With that,&nbsp;&nbsp;
we've reached our very exciting&nbsp; lightning round. Are you ready?&nbsp;&nbsp;
Here we go. What are two or three books&nbsp; you've recommended most to other people?
I know a lot of people on this podcast recommend&nbsp; high-output management, but it should be swap the&nbsp;&nbsp;
Bible out for it at all the hotels in the world,&nbsp; in the little drawer. Put it everywhere. You can't&nbsp;&nbsp;
go wrong, though. It is an incredible clarity of&nbsp; how to spend your time as a leader, a manager of&nbsp;&nbsp;
other people, a very high bar for how evaluating&nbsp; your work as the sum everyone around you. That was&nbsp;&nbsp;
very clarifying to me that it's not an individual&nbsp; effort, it is the sum of everything I'm involved&nbsp;&nbsp;
in is how to measure it. So that's definitely up&nbsp; there. A nice pair to that book, as a amuse-bouche&nbsp;&nbsp;
afterwards, is Orbiting the Giant Hairball: A&nbsp; Corporate Fool's Guide to Surviving with Grace,&nbsp;&nbsp;
I think, is the full exact title by Gordon&nbsp; MacKenzie, which is the story of a illustrator at&nbsp;&nbsp;
Hallmark, the greeting card company, and it turns&nbsp; out to be a, again, bureaucratic, slow-moving&nbsp;&nbsp;
organization that, over time, added rules and&nbsp; policies and rules and policies and quelled&nbsp;&nbsp;
creativity and innovation, which is surprising&nbsp; at a greeting card company, but it existed. So&nbsp;&nbsp;
this is his incredibly well-drawn book, as you'd&nbsp; imagine, with beautiful illustrations about how&nbsp;&nbsp;
he orbited the hairball of the organization&nbsp; to inspire others, keep himself engaged, and&nbsp;&nbsp;
to bring creativity and excitement and trying to&nbsp; pull people off the hairball as he orbited it. So&nbsp;&nbsp;
I think it's a fun afternoon read with beautiful&nbsp; illustrations about how to stay sane at big&nbsp;&nbsp;
companies and where to be a little goofy and take&nbsp; the advantage and gravity of the hairball, but not&nbsp;&nbsp;
be succumbed by it and to be able to orbit it. Those two are really fun. I will say one other&nbsp;&nbsp;
one I like... Because we haven't talked about&nbsp; strategy here, there's been more getting&nbsp;&nbsp;
stuff done and some other tactical things, but 7&nbsp; Powers, and I know you had the author recently on,&nbsp;&nbsp;
which was awesome. I won't explain the book,&nbsp; you just watch the podcast of it, but it walks&nbsp;&nbsp;
through many of the business powers and moats&nbsp; a company can have. I ran into the author...
Hamilton Helmer.
Hamilton Helmer, yes, thank you.
What a cool name.
Very cool name. Alliterative. At the Box&nbsp; lunchroom one time, where I worked at Box,&nbsp;&nbsp;
they acquired one of our companies, and I was&nbsp; like, "Any luck finding the eighth power?" He&nbsp;&nbsp;
was like, "I'm looking, I'm looking," as he&nbsp; ran off with his sandwich. One other funny,&nbsp;&nbsp;
somewhat embarrassing moment about that book&nbsp; is when I was applying to work at Stripe, I was&nbsp;&nbsp;
in some email conversation with our CEO, Patrick&nbsp; Collison, who is quite well-read and enjoys books,&nbsp;&nbsp;
and I was trying to showcase, " I like books a&nbsp; little bit," though not at any level of him. And&nbsp;&nbsp;
I had mentioned I just finished reading&nbsp; 7 Powers, and I recommended it to him,&nbsp;&nbsp;
but it joke's on me because he's quoted in&nbsp; the foreword that I had skipped. So he was&nbsp;&nbsp;
very kind to let me know that he had read&nbsp; it and he is quoted in it, so I was like,&nbsp;&nbsp;
"Oh shoot, maybe I won't get the job." But I got&nbsp; through that part, at least. So those books have&nbsp;&nbsp;
spoken to me. Do you have a favorite power, by&nbsp; the way, Lenny? Do you have a favorite power?
His favorite power is counter-positioning.&nbsp; I also like that power a lot because I think&nbsp;&nbsp;
it's the one you can that really changes&nbsp; everything about how you build your company,&nbsp;&nbsp;
so that's the one that always&nbsp; stands out to me. How about you?
I like counter-positioning also,&nbsp; and Atlas with going cheap and&nbsp;&nbsp;
that audience is counter-positioning, but&nbsp; I really enjoy process, the process power,&nbsp;&nbsp;
because it is very difficult to, as&nbsp; an organization, get good at anything,&nbsp;&nbsp;
and if you could do that over a long period of&nbsp; time in a sustainable way, you have a power.
This is the nerdiest chat I've ever had. Which&nbsp; is your favorite 7th Power? I love it. But on&nbsp;&nbsp;
that power, I asked him about it. He makes a&nbsp; really strong point there, that rarely is it&nbsp;&nbsp;
actually a power for people. They think the&nbsp; way we execute is going to be our advantage&nbsp;&nbsp;
and rarely is it actually a power. Usually&nbsp; people can copy it, but when you nail it...
That's even better, because then if&nbsp; your competition thinks they have it-
Yeah, exactly.
They won't invest than the other one.&nbsp; So I like it even more, for that reason.
I love it. But I was going to say with&nbsp; Patrick Collison being quoted in the book,&nbsp;&nbsp;
not only was he wrote part&nbsp; of the forward or was quoted,&nbsp;&nbsp;
he basically credited 7 Powers of&nbsp; helping build Stripe. No big deal.
Totally.
This lightning around is going great.&nbsp; This is a very microcosm of our whole&nbsp;&nbsp;
chat so far. Second question, do you&nbsp; have a favorite recent movie or TV show?
How To with John Wilson. It's on&nbsp; HBO. For those who haven't seen it,&nbsp;&nbsp;
not really giving away anything because it's&nbsp; just wild when you watch it. You can't give&nbsp;&nbsp;
it away. This videographer has found footage&nbsp; where he's just walking through Manhattan,&nbsp;&nbsp;
and other parts of the country, but mostly New&nbsp; York, with a camera for 10 years, just filming&nbsp;&nbsp;
intensely weird things. And if you've spent&nbsp; any time in New York, there's plenty to film.&nbsp;&nbsp;
Then has put together this narrative afterwards&nbsp; about certain topics like how to make risotto&nbsp;&nbsp;
or how to take out the trash or how to... It's a way of seeing life through the eyes&nbsp;&nbsp;
of these vignettes, diving down and really&nbsp; understanding people, and he does it through&nbsp;&nbsp;
this incredibly dry humor of stitching together&nbsp; this video footage to tell a different narrative.&nbsp;&nbsp;
And I think some of it is that we used to live&nbsp; in New York, and I love living in California,&nbsp;&nbsp;
but I miss that frequency of strangeness, and&nbsp; you can see that through that TV show. Fantastic.&nbsp;
Movie? I recently watched The Quiet Girl,&nbsp; which is a film about a young Irish girl&nbsp;&nbsp;
who is from a dysfunctional home and has&nbsp; this opportunity to live with a family&nbsp;&nbsp;
friend who have more opportunity for her, more&nbsp; empathetic to her, and it showcases, again,&nbsp;&nbsp;
how fragile things are. It's a very intense&nbsp; film, but there's something beautiful in how&nbsp;&nbsp;
much opportunity was in front of this young&nbsp; girl. It is a tearjerker, but a great one.
Do you have a favorite product you&nbsp; have recently discovered that you love?
I love my computer. I'm fast at my computer.&nbsp; Being fast at my computer helps me just go from&nbsp;&nbsp;
intention to just out in the world. I've fallen&nbsp; back in love with Raycast, which is an automation&nbsp;&nbsp;
tool for those who have watched the journey of&nbsp; Spotlight and Quicksilver and Alfred and all&nbsp;&nbsp;
these automator services. Raycast seems to have&nbsp; cracked the nut on automation, nerd complexity,&nbsp;&nbsp;
but also UI ease and some nice touches and loads&nbsp; quickly, does the basics. It's fully programmable,&nbsp;&nbsp;
extensible, just a huge fan of Raycast.&nbsp; And then I think for product people,&nbsp;&nbsp;
if you don't have CleanShot installed for&nbsp; screenshots, you're behind the curve. Being&nbsp;&nbsp;
able to take a screenshot and blur particular&nbsp; things or point at stuff or have arrows and&nbsp;&nbsp;
lines and have that be second nature, fast,&nbsp; instantaneous is so useful to be able to&nbsp;&nbsp;
communicate what you're seeing. When I get a new&nbsp; laptop, it's Raycast first and CleanShot second.
Wow, I am going to download CleanShot immediately.
Yes, it's extremely-
I've not heard of it. I've been&nbsp; using Skitch as my blurrings.
As much as I appreciate the Skitch folks,&nbsp; CleanShot is an incredible piece of software.
Amazing. I'm going to do that. All right, two more&nbsp; questions. Do you have a favorite life motto that&nbsp;&nbsp;
you often come back to, share with friends&nbsp; or family, find useful in work or in life?
I don't even realize I say "Go Go Go" a lot,&nbsp; but I do. I actually say it and write it so&nbsp;&nbsp;
people I hear that they'll later say, "Go Go&nbsp; Go" back to me. I'm like, "Huh? Don't I say&nbsp;&nbsp;
that sometimes?" "Yes, you say it a lot." So&nbsp; apparently, "Go Go Go" is one of them. I also-
I love that.
Say, "Let's make some mistakes," when we're&nbsp; brainstorming something or sitting at a sushi&nbsp;&nbsp;
restaurant and talk sushi guy or gal, to showcase,&nbsp; "Let's be creative. Do whatever you want. No&nbsp;&nbsp;
pretense. I'm not evaluating anything. Let's&nbsp; make some mistakes." It's just a weird thing.
They're so good. I'm going to use&nbsp; that for my podcast guests. "Let's&nbsp;&nbsp;
just make some mistakes. Don't worry about it."
At that point, everyone's like,&nbsp; "What? Okay, fine. Sure. Cool."
I like the combo of those two, "Go go go, let's&nbsp; just make some mistakes while we're going."
You have to use it in certain circumstances and&nbsp;&nbsp;
not for the five nines of reliability&nbsp; on our API, but it does have its place.
Final question. You worked with Patrick Collison&nbsp; and John Collison for many years. I'm curious&nbsp;&nbsp;
what the most useful feedback or advice you&nbsp; have heard from them or learned from them?
On my first month working here, which&nbsp; I guess is six, seven years ago now,&nbsp;&nbsp;
they had put me in charge of our&nbsp; payments infrastructure services.&nbsp;&nbsp;
That's all the backend systems that communicate&nbsp; with the financial system and all the internal&nbsp;&nbsp;
APIs where we build the external APIs and products&nbsp; on top of, so quite a lot of stuff. I knew nothing&nbsp;&nbsp;
about finance. I knew nothing about the scale&nbsp; that we're talking about. They entrusted me,&nbsp;&nbsp;
somewhat insanely, with that responsibility. On&nbsp; the first month we had our quarterly business&nbsp;&nbsp;
review where... The normal quarterly process,&nbsp; and I was like, "Okay, cool. I'll do the next&nbsp;&nbsp;
one. I'll write the next one." I've been here&nbsp; one month. They're like, "No, you write it. It'll&nbsp;&nbsp;
be even better that you write it." It's like,&nbsp; oh my God. It's forcing me to have to, in the&nbsp;&nbsp;
fourth week, have that catalyst to understand&nbsp; the whole business and with the permission,&nbsp;&nbsp;
because I was going to have to write this doc&nbsp; about how we're doing. The company had been in&nbsp;&nbsp;
existence for seven years before I got here.&nbsp; It was already at some reasonable scale.&nbsp;
It was an intense operation, and I remember&nbsp; writing the first draft and sending it to him&nbsp;&nbsp;
because it was... I didn't want to send... He had&nbsp; pushed me to do it a bit, and I figured I'd give&nbsp;&nbsp;
him an early draft and he wrote back, "This&nbsp; doesn't sound like you yet." The willingness&nbsp;&nbsp;
to entrust a new person to provide their own&nbsp; perspective and bring it into a very formalized&nbsp;&nbsp;
document like that was an impressive... That&nbsp; really spoke to me, and I rewrote it completely,&nbsp;&nbsp;
and I made it sound like me, and I've&nbsp; tried to make things sound like me since.&nbsp;
John's is more of a gut punch,&nbsp; I'll say. I reported to John,&nbsp;&nbsp;
the co-founder. Maybe nine months into reporting&nbsp; to him, I would run around with a clipboard.&nbsp;&nbsp;
I was a little bit manic of getting a lot&nbsp; done. A lot going on at Stripe at the time.&nbsp;&nbsp;
We'd have a one-hour one-on-one, I'd&nbsp; be listing all of the things that we&nbsp;&nbsp;
had accomplished and the problems we have and&nbsp; where we need escalation help and where we're&nbsp;&nbsp;
stuck and all this that and the other. Lots&nbsp; of stuff. I had checklists and physical paper,&nbsp;&nbsp;
flipping it over a little bit frantically. And he&nbsp; said, "You are one of the best people I've ever&nbsp;&nbsp;
worked with at solving problems three through 100,&nbsp; but I need you stuck on problems one and two."&nbsp;
Oh man, that hurt. I was like, "Oh, shoot." I am&nbsp; productive on the non-hardest problems and I was&nbsp;&nbsp;
trying to mask, not on purpose mask, but who wants&nbsp; to be stuck on something so hard when there's so&nbsp;&nbsp;
much else to do? From then on, I would show up&nbsp; to him with problems one and two and not talk&nbsp;&nbsp;
about problems three through 100. Even if we were&nbsp; working on them, we would just not talk about them&nbsp;&nbsp;
and we would get stuck on problems one and two.&nbsp; That was phenomenal advice, which I was like,&nbsp;&nbsp;
"Oh, shoot, I'm going to be fired." But&nbsp; it was really a deeply impactful sentence.
Wow, what a powerful, great, helpful... That's&nbsp; great advice [inaudible 02:34:10] right there.
He really looked my soul and-
Yeah, I love this.
Like a street fighter style or something.
But to your point, very impactful and helpful.
Yeah.
Jeff, we did it. The archeology is complete.
I appreciate the time, Lenny. It was&nbsp; fun. I don't do too many of these,&nbsp;&nbsp;
so I'm curious to people's feedback&nbsp; and really appreciate the questions.
Amazing. Jeff, thank you so much for being here.
Appreciate it, Lenny.
Bye everyone. Thank you so much&nbsp;&nbsp;
for listening. If you found this valuable, you can&nbsp; subscribe to the show on Apple Podcasts, Spotify,&nbsp;&nbsp;
or your favorite podcast app. Also, please&nbsp; consider giving us a rating or leaving a review,&nbsp;&nbsp;
as that really helps other listeners&nbsp; find the podcast. You can find all&nbsp;&nbsp;
past episodes or learn more about the show at&nbsp; LennysPodcast.com. See you in the next episode.

