<h1>Tools used</h1>
The software is implemented using <b>Python</b>. I imported <b>tkinter</b> for GUI and <b>re</b> for handling regular expressions.

<h1>GUI and software's utility</h1>
The GUI consists of 3 buttons and 3 input boxes. 

The input box underneath <b>"Pattern:"</b> is used in order to
enter the needed regular expression; if pressed the button "Print Pattern", it will output either the introduced
pattern or an error if the pattern does or does not follow the general rules (in the case of incompatibility, it
throws an error - line 20).

The input box underneath <b>"Text1"</b> is used in order to enter a single match for the pattern. Whether or not the
pattern matches the text, it will show a message in regards to this by pressing "Check Text1".

The input box underneath <b>"Text2"</b> is used for finding multiple matches for a pattern. There, you can write anything,
and the program will show the matches if "Find Matches" is pressed.

<h1>Code</h1>
In the code, the buttons enlisted above's functionalities are written in:
Print Pattern - printPattern
Check Text1 - printText
Find Matches - printText2

<h1>Examples for testing</h1>
<h2>Example 1 - email address</h2>
<b>Pattern: </b> ([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})<br>
<b>Text1: </b> soup@yahoo.com<br>
<b>Text2: </b> cristinatom2002@gmail.com cristinatom2002@gmail.com 17382748274192 hiafhjsajhfa jhgsafdahsdfacristinatom2002@gmail.com<br>

<h2>Example 2 - phone number</h2>
<b>Pattern: </b> [\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}<br>
<b>Text1: </b> +919367788755 <br>
<b>Text2: </b> 
+919367788755 <br>
8989829304 <br>
+16308520397 <br>
786-307-3615 <br>
789 <br>
123765 <br>
1-1-1 <br>
+982 <br>

<h2>Examples 3 and 4 - errors in the pattern</h2>
<b>Pattern: </b>[a-z <br>
<b>Pattern: </b>a{2,1} <br>
