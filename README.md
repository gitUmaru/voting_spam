Hey,

<h2>Purpose </h2>
My friend wanted me to build a script so that another friend of his could win this vote competition thing. I wasn't entirely sure on the details however I thought it would be fun to play around with some cool web script using python.

<h2> Procedure </h2>
<p>The first step was to find some python module that could allow me to control my keyboard and mouse despite the fact I was going to literally use it to only click a button. In retrospect I could have used some sort of JS code to manipulate the website's GET method (the site is poorly designed and susceptible to script kiddies such as myself) or somehow use their POST method. Its whatever though, the module I used could be useful in the future, specifically non malicious key logging (you know, with the user's consent and knowledge).</p>
<p>The module I used was pynput. It was pretty much what my first idea to solving this problem was, seeing as how short my brainstorming period was and how quick I was able to produce a result I figured there was no need for further research. I basically copied the documentation with minor amendments. I might come back and add some more original code but for the purposes of the project it works, and why mess with something that works.</p>

<h2> Update Log <h2>
03/11/2019
I was testing my script the previous day using one of their vulnerabilities however they have seemed to patched it. They exploit that I was using was the fact that one could just refresh and vote again for n amount of times, with n being a whole number. I had initially thought that the script would be easy due to this but its proving to be more difficult than otherwise initially thought; that is now I have to actually code something that does something clever rather than brain dead copy pasta code.



Thanks,
Umar Ali
