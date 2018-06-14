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

### Installation ###
1. Install Vagrant and VirtualBox
2. Download or clone [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository
3. Download or clone the project file within the vagrant folder and then move the newsdata.sql file within the project file

### Operation ###
1. Launch Vagrant Virtual Machine by running $ vagrant up. __If you're on a Windows machine you'll something like Git Bash to run these commands__
2. Run the $ vagrant ssh command to enter the Linux virtual machine
3. Run the application by running python /vagrant/Udacity-Logs-Analysis-Project/newsdata.py
