# Udacity-Logs-Analysis-Project

The Logs Analysis project uses PSQL and Python to query a large database and output the data to answer three questions:
1. What are the most popular three articles of all time? Which articles have been accessed the most?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

### How To Download ###
To download using Git click on the clone button and copy the clone address. Create a new repository and run git clone along with the address.

To download a zipped file of the project, hit the Clone or download button and then click the Download Zip button. Then unzip the file.

### Prerequisites ###
* [Python 2.7 or higher](https://www.python.org/)
* [Vagrant](https://www.vagrantup.com/)
* [VirtualBox](https://www.virtualbox.org/)
* PostgreSQL
* psycopg2

### Installation ###
1. Install Vagrant and VirtualBox
2. Download or clone [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository
3. Download or clone the project file within the vagrant folder and then move the newsdata.sql file within the project file

### Operation ###
1. Launch Vagrant Virtual Machine by running $ vagrant up. __If you're on a Windows machine you'll something like Git Bash to run these commands__
2. Run the $ vagrant ssh command to enter the Linux virtual machine
3. Create PSQL views by entering PSQL by running PSQL -d news and then running:
* CREATE VIEW newsHits as select articles.title, count(*) as num from articles, log where articles.slug = substring (path from 10 for 45)
group by substring (path from 10 for 45), articles.title order by num DESC limit 3;
* CREATE VIEW authorHits AS select authors.name, count(*) as num from articles, log, authors where articles.author = authors.id AND articles.slug = substring (path from 10 for 45) AND log.status!='404 NOT FOUND' group by authors.id order by num DESC;
* CREATE VIEW totalHits AS select date(time), count(*) as results from log group by date(time);
* CREATE VIEW errorHits AS select date(time), count(*) as errors from log where status!='404 NOT FOUND' group by date(time);
4. Exit PSQL and then run the application by running python /vagrant/Udacity-Logs-Analysis-Project/newsdata.py
