
<h2>Purpose </h2>
My friend wanted me to build a script so that another friend of his could win this vote competition thing. I wasn't entirely sure on the details however I thought it would be fun to play around with some cool web script using python.

<h2> Procedure </h2>
<p>The first step was to find some python module that could allow me to control my keyboard and mouse despite the fact I was going to literally use it to only click a button. In retrospect I could have used some sort of JS code to manipulate the website's GET method (the site is poorly designed and susceptible to script kiddies such as myself) or somehow use their POST method. Its whatever though, the module I used could be useful in the future, specifically non malicious key logging (you know, with the user's consent and knowledge).</p>
<p>The module I used was pynput. It was pretty much what my first idea to solving this problem was, seeing as how short my brainstorming period was and how quick I was able to produce a result I figured there was no need for further research. I basically copied the documentation with minor amendments. I might come back and add some more original code but for the purposes of the project it works, and why mess with something that works.</p>

<h2> Update Log </h2>
<p>03/10/2019</p>
<p> Rewatching Full Metal Alchemist so I am not expecting a lot of work today done today, however I might look into the documentation for the pynput module.</p>
<p>Update, didn't do much aside from glance at documentation for module and maybe test some code, mainly decided to watch anime. Good decisions as always</p>
<p>03/11/2019</p>
<p>I was testing my script from the previous day using one of their vulnerabilities however they have seemed to patched it. The exploit that I was using was the fact that one could just refresh and vote again for n amount of times, with n being a whole number. I had initially thought that the script would be easy due to this but its proving to be more difficult than otherwise initially thought; that is now I have to actually code something that does something clever rather than brain dead copy pasta code.</p>
<p>Update part II, turns out you can just wait for like 2 minutes and resume voting; turns out I can revert back to brain dead code instead.</p>
<p>Update part III, just realized the way I coded the mouse positioning stuff only applies to 1080p monitors so either I change it whenever I use the code or figure out a way that doesn't rely on resolution. To be honest, the former sounds like less work so I am most likely going to do that. Also, I plan to run this script on public PCs using several VMs and possible even proxy through an onion server. Overkill I know, its mostly just a flex but the proxy thing is probably the last thing I'm gonna do. The VMs however I am going to use as it expedites the process by a considerable amount. </p>

<h2> Results <h2>
<p>It kinda worked. I mean the actual code itself, aside from being bad code, worked for the most part. I ran a few VMs and let the code run for an hour and considering the voting timer being 2 minutes and my bot working for every minutes, I got pretty much exactly the number of votes that could be calculated for. I used 2 VMs (slax linux) with each one running the script. In terms of goals that I set out I accomplished them however I think in a very poor and rudimentary fashion; nonetheless considering the amount of time I put in for writing the code I am content.<p>

<p>I spent more time on writing the README than the actual code, but considering the banality of the task I needed to compensate elsewhere. Some sort of diary/log also felt cool to write. I hope that this serves of some purpose later on in life.</p>
