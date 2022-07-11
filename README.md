# django_my_projects_websites
<img src="https://github.com/wsvincent/awesome-django/raw/main/assets/django-logo.svg">
<hr>
<ul>
<h2>Contents</h2>
<li><a href="#kinomania"><h3>KINOMANIA</h3></a>Website for booking screenings at the cinema</li>
<li><a href="#dictionary"><h3>DICTIONARY</h3></a>Website for looking translation of words and create your self vocabulary and train your knowledge in a card game</li>
<li><a href="#clone_project"><h3>Clone and Run a Django Project</h3></a>how run projects in your computer</li>
</ul>
<hr>

<center><h1 id='kinomania'>KINOMANIA<span style='font-size:70px;'>&#127916;</span></h1></center>
<h4>Website for booking screenings at the cinema</h4>
  <p>On the home page you can see a random movie what is playing in the cinema right now and read about it on Wikipedia, 
<p align="center">
<img src="https://user-images.githubusercontent.com/97242088/172056532-b8eefde9-a160-4999-a410-c48e3b667fe9.png" width="350" alt="Home page" title="Home page"> </p> <center>Home page</center>
<p>Also you can go and see all movies, and you can click and see all the rooms in the cinema</p>
<p align="center"> 
  <img src="https://user-images.githubusercontent.com/97242088/172056473-7826d7b6-6506-4d03-baea-d796a150f443.png" width="350" alt="all rooms" title="all rooms"> <center>all rooms</center>
</p>
<p>and what is playing in them right now</p>
<p align="center">
    <img src="https://user-images.githubusercontent.com/97242088/172056429-018d3a58-d9f7-4a46-a0c8-a07d3a3712e6.png" width="350" alt="screenings" title="screenings"> <center>screenings</center>
<p>when you click on a room you will see the screenings at different times, and when you click on the time you will see the free and occupied seats, if you choose an empty seat (occupied is displayed in red) you will see your ticket.</p>

<p align="center">
    <img src="https://user-images.githubusercontent.com/97242088/172056344-68350dce-9425-4102-b5ae-2609639040d3.png" width="350" alt="cinema hall"><center>cinema hall</center>  
</p>
  <p>User to book tickets should be registered and only then he can book screening and see all his tickets.
After the date on which the tickets were booked they will be deleted from the database <span style='font-size:20px;'>&#128197;</span>. Also, if the room was not booked by the administrator and it is free on that date, the user can book the whole room by himself. </p>
  <p align="center">
<img src="https://user-images.githubusercontent.com/97242088/172056602-402ec3a7-c60b-4e58-a041-9f58727eaf80.png" width="350" alt="user tickets"><center>user tickets</center> 
  </p>
  <hr>
<center><h1 id="dictionary">DICTIONARY<span style='font-size:70px;'>📖</span></h1></center>
<h3>Website for looking translation of words and create your self vocabulary and train your knowledge in a card game</h3>

<p>On the main page you can see the word of the day which will automatically change at 00:01 <span style='font-size:20px;'>&#128197;</span>. 
You can translate the words and dynamically receiving the result you can add to the dictionary this translation if you need.</p>
  <p align="center">


  <img src="https://user-images.githubusercontent.com/97242088/177044720-702e2ca3-4e55-4ea3-b3bf-16eff5530954.png" width="500" alt="Home page">
</p>
<center>Home page</center>


<p>On the page we have two dictionaries - one general and the other personal for each user. In a personal dictionary there will be words that user
added personally, on the home page when you click on descriptions which you need this word and description will be on your own dictionary (you can add words only when you are logged in). You can change or delete your own words. </p>
  <p align="center">
  <img src="https://user-images.githubusercontent.com/97242088/172055161-d490e908-52e8-4cba-92b5-04752da1f604.png" width="350" alt="add word" title="add word"> add word 
  <img src="https://user-images.githubusercontent.com/97242088/172055231-feb0add4-37ef-4edb-87d6-edef2eeab00c.png" width="350" alt="global dictionary" title="global dictionary"> global dictionary

</p>
  <p align="center">
  <img src="https://user-images.githubusercontent.com/97242088/172055425-bb42165f-c3b1-48f0-b5fd-94850db73acc.png" width="350" alt="user own dictionary" title="user own dictionary">
  </p>
<center>user own dictionary </center>

<p>Also we have two options card game, you can play with all the words, or you can  play with the words of a specific user (but when you have in the 
dictionary more than 16 words). The game is that on one side of the card you have a word, and on the back you have definitions, when you click on the card it turns and you can preview the translation
  <p align="center">
  <img src="https://user-images.githubusercontent.com/97242088/172049037-f39daae3-32ca-401e-9029-2b2410f36376.png" width="500" alt="Card game" title="Card game">
</p>
<center>Card game</center>
<p>And that's not all, you can practice in inventing  sentences to words (it should be at least 25 letters)  and if you are satisfied with your creativity, you can share it with other users
</p>
  </p>
  <hr>
<h3 id="clone_project">Clone and Run a Django Project</h3>

Before diving let’s look at the things we are required to install in our system.

To run Django prefer to use the Virtual Environment

`pip install virtualenv`

Making and Activating the Virtual Environment:-

`virtualenv “name as you like”`

`source env/bin/activate`

Installing Django:-

`pip install django`

Now, we need to clone project from Github:-
<p>Above the list of files, click Code.</p>
<img src="https://docs.github.com/assets/cb-20363/images/help/repository/code-button.png">

Copy the URL for the repository.
<ul>
<li>To clone the repository using HTTPS, under "HTTPS", click</li>
<li>To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click SSH, then click</li>
<li>To clone a repository using GitHub CLI, click GitHub CLI, then click</li>
</ul>
<img src="https://docs.github.com/assets/cb-33207/images/help/repository/https-url-clone-cli.png">

Open Terminal.

Change the current working directory to the location where you want the cloned directory.

Type git clone, and then paste the URL you copied earlier.

`$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY`

Press Enter to create your local clone.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `Spoon-Knife`...<br>
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Install the project dependencies:

`pip install -r requirements.txt`

Now go to the setting.py and change the SECRET_KEY.
from
`SECRET_KEY = os.environ.get('SECRET_KEY')`
to
`SECRET_KEY = 'your own secret key'`

create admin account (**remember you must be at the main application folder with file manage.py, and do this steps for
each application in this repository!!!!**)

`python manage.py createsuperuser`

then

`python manage.py makemigrations`

then again run

`python manage.py migrate`

run this command to start periodic tasks in application(in Kinomania it is checking data in tickets and deleting not
active, in Dictionary it is changing the word of day)

`python manage.py crontab add`

to start the development server

`python manage.py runserver`

and open localhost:8000 on your browser to view the app.

Have fun
<p style="font-size:100px">&#129409;</p>




