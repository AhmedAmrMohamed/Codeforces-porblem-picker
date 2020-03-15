# Codeforce porblem picker
<h2>Diclmair</h2>
<p>I deveolped this program as a way to help the community I take the most pirde of being part of ACM chapter Shoubra.</p>
</p>The whole idea was to automate the process of choosing codeforces problems for online contests held for the chapter members.
  However anyone is welcomed to use/edit it the way he/she sees fit.
  Till now it's still in development but this is a simple running version for how I hope this thing turn into. <h5>All suggestions opinions and offers of help are most welcomed</5> 
<h2>To run...</h2>
<ul>
  <li>You're gonna need python 3.6+ installed.</li>
  <li>install the tkinter library -usually gets installed automaticly with python-</li>
  <li>navigate to the program folder and run <h5>python gui.py</li> 
 </ul>
 make sure to click update data base when first used and every few days or so.
 <h2>Fatures so far</h2>
  <li>update the base to the lateset codeforces problems with a push of a button</li>
  <li>Add the handles of participants</li>
  <li>Choose the tags you want</li>
  <li>specify how the tags are filtered</li>
  <li>problems gets saved to 'problems.txt'</li>
  <li>Also the ability to launch the last used handles and /or tags</li>
  </ul>
<h2>Atonmy</h2>
<ul>
  <li><code>connection.py</code> : responisble for threading the http requests to the codeforces api</li>
  <li><code>contestant.py</code> : represetnt each contestant once intialized make an http request to get the wanted info of the given handle
      </li>
  <li><code>gui.py</code>        : guess what! responsible for the gui in the program.</li>
  <li><code>inter.py</code>      : I tried my best to make this classs responisble for all communication between classes and that is the case for
    the most part.</li>
  </ul>
  
