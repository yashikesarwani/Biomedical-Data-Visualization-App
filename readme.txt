numpy==1.16.4
psutil==5.6.2
pytz==2019.1
flask
forms
neo4jrestclient
selenium
py2neo

#all these modules should be imported in your virtual environment

#Procedure for the setup of virtual environment

pip install virtualenv
mkdir Environments              #let say you make a folder named Environments
cd Environments                 #(to go to the folder you made)
ls                              #to check your folder has been created
project_1\Scripts\activate      #check if there is another command for linux like it may be (source project_1/bin/activate)

then import all the modules mentioned above using command "pip install modulename"

#make sure your neo4j server is open and the knowledge graph is running on that and before that change the neo4jusername and password according to your setup.

#for running knowledge graph make sure you provide the required dataset and empty csv files as per the coding requirement and neo4j server setup is done properly.

then run the python file "python flaskblog.py"