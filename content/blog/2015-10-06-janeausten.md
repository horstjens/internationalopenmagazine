Title: Jane Austen on Python: The intersection of literature and tech
Date:  2015-11-04 00:00   
Modfied: 2015-11-05 07:17 
Tags: python, coding, art
Status: published 
Slug:   2015-10-06-janeausten 
Authors: WILLIAMS HENSCHEL Lacey 
ICBM: 30.267153, -97.743061
GeoPosition: 30.267153;-97.743061
GeoPlacename: Austin
GeoRegion:  US-TX
Summarytext: Lacey Williams Henschel draws fascinating parallels between coding python and writing novels, and explores the connection of style guides for for both.
Summary: <div style="float: left; margin:5px"><img src="/images/2015-10-06-janeausten/jane_austen.jpg" alt="Jane Austen" height="100"><img src="/images/2015-10-06-janeausten/LaceyWilliamsHenschel.jpg" height="100" alt="Lacey Williams Henschel"></div>Lacey Williams Henschel draws fascinating parallels between coding python and writing novels, and explores the connection of style guides for for both.<div style="clear:both;"></div>

<div style="float:right; width:260px; padding: 5px; margin: 5px; background-color: #bbbbbb;"> 
<b>Name</b>: <a href="https://www.linkedin.com/profile/in/laceynwilliams">Lacey WILLIAMS HENSCHEL</a><br>
<b>Contact</b>: <a href="@laceynwilliams">@laceynwilliams</a><br>
<b>Shorturl</b>: <a href="http://goo.gl/XK6j8X">http://goo.gl/XK6j8X</a><br> 
<b>Hashtag</b>: <tt>&#35;python</tt><br>
<b>Fork / improve</b>: <a href="https://github.com/horstjens/internationalopenmagazine/blob/master/content/blog/2015-10-06-janeausten.md">on Github</a><br>
<b>Extras</b>: <a href="https://youtu.be/55gXwFviOuQ">Video of DjangoCon talk</a><br> 
<a href="https://creativecommons.org/licenses/by-sa/4.0/"><img src="http://internationalopenmagazine.org/images/ccbysa88x31.png" align="right" alt="cc-by-sa"></a><b>License</b> for text and photos in this article, unless indicated otherwise (e.g. <i>Image rights</i> notice below pictures): <a href="https://creativecommons.org/licenses/by-sa/4.0/">creative commons attribute share-alike 4.0</a> <br>
<b>Location</b>: <a href="http://www.openstreetmap.org/?mlat=30.2813&amp;mlon=-97.7401#map=13/30.2812/-97.7400">30.281,-97.7401</a><br>
<iframe width="250" height="250" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="http://www.openstreetmap.org/export/embed.html?bbox=-97.85333633422852%2C30.218580196726734%2C-97.62674331665039%2C30.34384300675069&amp;layer=mapnik&amp;marker=30.281254000012744%2C-97.74005299999999" style="border: 1px solid black"></iframe><br>
<img src="/images/2015-10-06-janeausten/LaceyWilliamsHenschel.jpg" alt="Lacey Williams Henschel" width="100" align="right">
<b>about the author</b>: I'm a developer for the University of Texas at Austin, but I live in Portland, OR. I'm an organizer for DjangoCon US 2015 and 2016, and on the Django Girls Support Team. I've also organized a few Django Girls workshops to teach women to build websites. In my spare time, I bake and craft.<br>
<b>Donate the author</b>: No donation address given yet<br>
</div>

<div style="float: left; margin: 5px; background-color: #cccccc"><a href="https://opensource.com/business/15/10/jane-austen-on-python"><img src="/images/opensourcecom.png" width="220" alt="opensource.com logo"></a><br><small>Logo & image rights: <a href="http://opensource.com">opensource.com</a></small></div>
*This article was originally published 2015-oct-06 under a [creative-commons share-alike 4.0 license](https://creativecommons.org/licenses/by-sa/4.0/) at [opensource.com](https://opensource.com/business/15/10/jane-austen-on-python)*
<div style="clear:left;"></div>

<p>This article is for the English majors, the bookworms, the lovers of literature, and the people with humanities backgrounds who sometimes struggle with the question, "So do you ever use your English degree?" It's also for the people who've asked that question of their colleagues with non-STEM backgrounds, who've been confused about how someone could start in psychology and end up in Python.</p>
<!--break--></p>
<p>The truth is that technology and humanities aren't so far apart; in fact, a lot of concepts we English majors perfected over our thesis papers get used in our daily lives as developers. This article isn't about what coders can learn from humanities majors or vice versa. It's a demonstration of the overlap between the two disciplines; a study in their compatibility and how they complement one another.</p>
<p>Before I became a developer for the University of Texas at Austin, I wanted to become an English professor. I got my bachelor's in English from Auburn University in 2007, and while I was there I did a lot of tech things. I was the webmaster for a professor's professional website, which was maintained in Dreamweaver and stored on a Zip drive. I also worked in the Technology Center, where I screencasted videos to teach professors how to use <a href="http://www.blackboard.com/" target="_blank">Blackboard</a>, and helped them integrate tech into their classrooms in ways I thought were cool.</p>
<p>When I started working on my Master's in English from Texas A&amp;M University, I still wanted to become Professor Lacey and write scholarly articles about literature. But again, I steered myself into tech roles. I worked in the English Technology Center instead of being a teaching assistant, and I helped faculty screencast, make videos, use <a href="http://opensource.com/education/14/10/open-access-learning-moodle" target="_blank">Moodle</a> (an open-source version of Blackboard), and find ways to integrate Google Docs into their classrooms. I also worked for the <a href="http://www.worldshakesbib.org/" target="_blank">World Shakespeare Bibliography</a>, where I researched scholarly articles on Shakespeare and then wrote summaries on them. I had to use some <a href="http://opensource.com/life/15/8/markup-lowdown" target="_blank">markup</a> so that the admin could copy and paste my summaries into the site, but what I didn't know was that I was sort of coding.</p>
<p>In 2009, I took a workshop on <a href="http://www.tei-c.org/index.xml" target="_blank">TEI: The Text Encoding Initiative</a>. TEI is an XML markup language that's specific to manuscripts. It has lots of awesome, specific tags for publishers and other information about books, but it also provides ways to talk about handwritten manuscripts that are being transcribed for the web; for example, you can represent in markup that some text was scratched through and replaced with different phrasing. I wanted to make a site, using TEI, to talk about Jane Austen fan fiction.</p>
<p>But I felt like I didn't know how. I was really tech-inclined and tech-interested, but not very tech-savvy. I didn't know how to register a URL, I didn't understand what CSS was, and if there were tutorials available to me, I didn't know how to find them. I also thought it was <i>too hard</i>. I had <a href="http://opensource.com/business/15/9/tips-avoiding-impostor-syndrome" target="_blank">impostor syndrome</a> before I even started. So I wrote a paper on Jane Austen fan fiction instead.</p>
</p>
<h2>Guess the source</h2>
<p>So let's play a game called <i>Guess the Source</i>. I'll put up a quote from a style guide, and you can guess where it comes from:</p>
<blockquote><p>You should use two spaces after a sentence-ending period.</p></blockquote>
<p>Is this from <a href="https://www.python.org/dev/peps/pep-0008/" target="_blank">PEP8</a>, or Strunk &amp; White?</p>
<p>I hate this particular line from PEP8, because in your regular writing, you should never ever, ever put two spaces after a period. Don't do it. This is from the days of monospace fonts and typesetting, and we don't use monospace fonts on the Internet or in printed materials anymore.</p>
<p>Except in code. So follow this rule for writing code, but break it everywhere else. The first clue that writing code has anything to do with writing a research paper or an essay is right there in PEP8, the style guide for Python code: "When writing English, follow Strunk &amp; White." PEP8 doesn't even cite Strunk &amp; White. It assumes you know what that means. (For those who don't, <i>Strunk &amp; White</i> refers to the <a href="https://en.wikipedia.org/wiki/The_Elements_of_Style" target="_blank">The Elements of Style</a>, an American English style guide first published in 1959.)</p>
<p>The broader point about Strunk &amp; White is that this is a guide written to help people write clearer, more concise, more consistent, more readable English. PEP8 is also a guide for helping people write clearer, more concise, more consistent, and more readable code.</p>
</p>
<h2>Plot-driven development</h2>

<div style="float:right; margin: 20px; width=405; background-color: #bbbbbb;">
<a data-flickr-embed="true" data-header="true"  href="https://www.flickr.com/photos/internetarchivebookimages/14774185771/in/photolist-ovMZPE-ovN3K9-oejR8Q-ovxACg-ovxyGT-ovxE8x-ovPNMP-ovN5mf-oejVe5/" title="Image from page 9 of &quot;The novels and letters of Jane Austen&quot; (1906)"><img src="https://farm4.staticflickr.com/3891/14774185771_75e08e83ea_z.jpg" width="405" height="640" alt="Image from page 9 of &quot;The novels and letters of Jane Austen&quot; (1906)"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script><br><small>Image from page 9 of "The novels and letters of Jane Austen" (1906).<br><a href="https://www.flickr.com/commons/usage/">No known copyright restrictions</a></small>
</div>

<p>Let's talk about testing, because testing is a perfect example of where some concepts from your literature class might come in handy. Perhaps you remember the basics of <a href="https://en.wikipedia.org/wiki/Story_arc" target="_blank">story arc</a>:</p>
<ul>
<li>The exposition is where you learn who the characters are, where they are, and the basics of what is happening.</li>
<li>The rising action is where the problem gets introduced and we start experiencing the events that will lead us to the climax.</li>
<li>The climax is the most exciting part of the plot. This is where the thing that changes the main character's fate happens. In <a href="https://www.gutenberg.org/files/1342/1342-h/1342-h.htm" target="_blank">Pride and Prejudice</a>, this is would be the scene where Mr. Darcy finally proposes to Elizabeth, and then she tells him she wouldn't marry him if he were the last man on earth, and then she starts questioning herself.</li>
<li>The falling action is where things begin to unravel and fall into place.</li>
<li>The denouement ties up everything in a neat little bow. The end.</li>
</ul>
<p>We can make use of this arc, which is called <a href="https://en.wikipedia.org/wiki/Dramatic_structure" target="_blank">Freytag's pyramid</a>, in testing as well. In fact, that was what first gave me the idea for a talk I gave at <a href="https://2015.djangocon.us/speaker/profile/8/" target="_blank">DjangoCon Austin</a>, on which this article is based. I was in Harry Percival's <a href="https://us.pycon.org/2015/schedule/presentation/300/" target="_blank">testing workshop at PyCon</a>, and realized that the example of a functional test he gave was a perfect example of Freytag's pyramid applied to testing. The functional test had:</p>
<ul>
<li>Exposition: Harry introduces us to Edith, who's heard about a to-do app.</li>
<li>Rising action: Edith goes to the app, finds her way around, and decides to enter an item on her to-do list.</li>
<li>Climax: Edith's fate is forever changed. She performs the crucial, pivotal action of adding an item to her to-do list.</li>
<li>Falling action: She's entered her item, she sees that it's been entered and saved for her.</li>
<li>Denouement: Edith is happy and is going back to sleep.</li>
</ul>
<p>Before Harry ever writes a single functional test, he writes out this user story that follows Freytag's pyramid exactly. This way, he knows what path the user needs to take through his site, what they will encounter, what they will do, and how it will all resolve. He can write tests to test that these steps all happen, and then he can write the code to pass those tests.</p>
<p>The path that Edith takes through the app is her user story; Edith herself is a persona. In another world, Edith might be the protagonist in a novel, and this particular journey might be a chapter in what I hope is an otherwise more thrilling story. The ability to write a complete and convincing user story is helped by having studied character development and plot development before. A programmer needs to be confident in what their code is supposed to do, and in what order that's supposed to happen, in order to effectively test it.</p>
<p>And user stories and functional tests aren't the end of it. How do we want Edith to react when the app breaks? Do we want her to tear her hair and rend her garments like she's in a Greek tragedy? I hope not. We probably want to provide her with the tools she needs to correct the error, if possible, or reassure her that we know something went wrong and we're already on it. Which of these is the more reassuring error message?</p>
<p>Creative thinking is required to determine where our code might break, to build in checks, and to return useful data. Any programmer can return the error message, but to compose an error message that is helpful—rather than intimidating—requires a programmer who is also a creative thinker and possesses excellent written and verbal communication skills.</p>
<p>When you're writing good tests, you're doing world building: Accessibility requires empathy, and empathy requires imagination. You can leverage that awesome feeling you get when you get lost in a book and identify with the main character by putting yourself in the shoes of the people using your code. Imagine their struggles and frustrations. Create a persona for them. Fix the things that hinder or annoy them about your app.</p>
<p>But back to the functional test. You know what else this looks like? An outline.</p>
<p>You know what else looks like an outline? Basically, all Python code. Python loves whitespace and indenting and pretty formatting, even more than an English major does.</p>
<p>Python code actually uses a lot of the same formatting as many other written works, such as news stories, blog posts, novels, research papers, and even <a href="http://www.npr.org/sections/thesalt/2011/10/20/141554113/a-coconut-cake-from-emily-dickinson-reclusive-poet-passionate-baker" target="_blank">Emily Dickinson's handwritten coconut cake recipe</a>. Your function definition is like the title. And your <a href="https://www.python.org/dev/peps/pep-0257/" target="_blank">docstring</a> is like the abstract to a research paper, or the forward to a new edition of a favorite novel. The docstring tells you a little bit about what's coming, and it gives you a peek into the author's or programmer's mind. Then there's everything in the middle: the meat of the function, the paragraphs of the article or story. And finally, you conclude. You return something, and your journey through this particular function is over.</p>
</p>

<div style="float:right; margin: 20px; width=405; background-color: #bbbbbb;">
<a data-flickr-embed="true" data-header="true"  href="https://www.flickr.com/photos/internetarchivebookimages/14777001832" title="Image from page 106 of &quot;The novels and letters of Jane Austen&quot; (1906)"><img src="https://farm4.staticflickr.com/3842/14777001832_dff08f63a7_z.jpg" width="403" height="640" alt="Image from page 106 of &quot;The novels and letters of Jane Austen&quot; (1906)"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script><br><small>Image from page 106 of "The novels and letters of Jane Austen" (1906).<br><a href="https://www.flickr.com/commons/usage/">No known copyright restrictions</a></small>
</div>

<h2>Readability counts</h2>
<p>A well-written piece of code will be readable, but what do we even mean by that? Machines don't need code to be readable, but in <a href="https://www.python.org/dev/peps/pep-0020/" target="_blank">PEP20: The Zen of Python</a>, Tim Peters is pretty clear that <i>readability counts</i>. The computer or compiler (or whatever) doesn't care at all if your code is a mess, as long as it works. But your colleagues care. The people who come after you care. The people who share in your work need your code to be readable.</p>
<p>Writing readable code requires empathy and means that you care about your fellow coder. Readable and conscientiously commented code also helps future programmers understand what you struggled with, or why you made decisions the way you did. Comments can even help you re-orient yourself in your own code. A friend of mine once said, "Comments are like love notes to yourself." A coworker likes to say that comments are what keep you sane at 3:00 AM when you get the phone call that something has gone catastrophically wrong.</p>
<p>There's a great example of this from <a href="http://www.dianagabaldon.com/books/outlander-series/" target="_blank">The Outlander Series</a>, which is basically a perfect book series. The Outlander Series is about a World War II nurse who accidentally time travels back to 18th-century Scotland. The story includes war and romance and wonderfulness (and it's now a pretty great TV series, too, but that's not the point). At the end of the fifth book, <a href="http://www.dianagabaldon.com/books/outlander-series/the-fiery-cross/" target="_blank">The Fiery Cross</a>—and I promise this is not a spoiler—our heroine Claire is in the 18th century and is the most knowledgeable medical professional for miles. She treats someone who winds up dying, and she's pretty sure it's because she gave this patient a medicine they were allergic to. She struggles with whether to write in her journal about what happened. In a previous book in the series, Claire is tried as a witch when townspeople mistake her medical badassery with magic, so she becomes hesitant to write down anything that might later get used against her.</p>
<p>Claire says, "Some future physician here would face the same dilemma; to undertake a possibly dangerous treatment, or to allow a patient to die who might have been saved. Who might that be? I wiped the pen, thinking ...." And then she thinks for a while about how isolated she is, how few doctors there are, how there aren't many medical schools, and she concludes, "I sat up straight and opened my book. I dipped my pen, and began to write the lines that must be there, for the sake of the unknown physician who would follow me."</p>
<p>This is why we write readable code: For the sake of the unknown coder who will follow us.</p>
</p>
<h2>Denouement</h2>
<p>When I was in college, I had a roommate who was a journalism major. Niki and I editted each other's papers, and I would try to get her to use more adjectives to make her writing more exciting. She would tell me to cut my flowery descriptions and get to the point. Most composition style guides and PEPs 8 and 20 agreed with Niki.</p>
<p>"Omit needless words." <br /> "Simple is better than complex." <br /> "Vigorous writing is concise." <br /> "Sparse is better than dense."</p>
<p>These are edicts from PEP20 and Strunk &amp; White. I won't specify which line is from which work, because it doesn't matter (and <i>The Zen of Python</i> devotees will be able to pick them out, anyway). But the point is that they are so similar. Good writing is concise and clear and simple and gets to its point, whether you're writing a piece of code or an article. I could take the lines from <i>The Zen of Python</i> that aren't code-specific and email them to my friends who are composition instructors, and they'd print them and hand them out to their classes immediately. <i>In fact, I should do that. </i></p>
<p>We're called <i>coders</i>, <i>programmers</i>, or <i>developers</i>. What do we do all day? We <i>write</i> code. We <i>read</i> pull requests. We <i>write</i> tests. We <i>read</i> other people's code. We <i>write</i> comments. We're <i>readers</i> and <i>writers</i>. The lessons learned in classes about reading and writing literature are exceedingly relevant to us as readers and writers of code.</p>
<p>"Do you ever get to use your English degree?" I'm often asked. Yes, I use my English degree every day.</p> 

<iframe width="640" height="360" src="https://www.youtube.com/embed/55gXwFviOuQ" frameborder="0" allowfullscreen></iframe>

# advertisement (google adsense) 

<hr style="height: 3px;">

<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- intopenmag-unten -->
<ins class="adsbygoogle"
     style="display:inline-block;width:728px;height:90px"
     data-ad-client="ca-pub-3535173094498375"
     data-ad-slot="7210184316"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
