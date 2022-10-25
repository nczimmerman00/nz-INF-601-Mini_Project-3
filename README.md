INF601 - Advanced Programming in Python <br />
Nicholas Zimmerman <br />
Mini Project 3<br />

<h1 align="center"> Nick's Quiz Website</h1>
<br>
This project starts a website which you can take a quiz over various 
things about Nick, and compare your results with other people who
have taken the quiz!

### Installation

Start by cloning this repository using: <br><br>
`https://github.com/nczimmerman00/nz-INF-601-Mini_Project-3.git`


### Prerequisites
To install the packages needed to run the website, open a terminal 
(such as command prompt) in the folder where you cloned this repository 
and enter the following command:
<br> <br>
`pip install -r 'requirements.txt`

### Usage

For the first time starting the website, you need to initialize the
SQLite database. To do this, use the terminal opened for the cloned
repository and run the command: <br><br>
`flask --app quiz init-db`

To start the website, use the terminal you opened in the directory 
where this repository was cloned and run the command: <br><br>
`flask --app quiz run` <br>

A message should pop up giving a link to the website and the port.
<br><br>
To change the questions on the quiz, you'll have to open the schema.sql
file and change the questions on the INSERT INTO statements, following
the format used. After adding or removing any questions, you'll need to
reinitialize the database using `flask --app quiz init-db`
