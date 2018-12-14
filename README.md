# darkspear



File Hierarchy:
All files need to be installed relative to main.py. Unzipping files should put everything where it needs to be but if not, make sure the narwhal image is in a file called images in the same directory as main.py. All other files need to by in a folder called pages, located in the same directory as main.py. 

MySQL Server installation instructions:
Current iteration of Darkspear requires a local server in order to run. You can download the MySQL installer from https://dev.mysql.com/downloads/installer/, it is also included in the downloads in the Darkspear file path. Before you start this make sure you have Python 3.7.1 installed on your system. Once started you must accept the License agreement, after that you need to select full install, you may install in any file location you want. After that it will show you what is being installed, click execute to begin installation. Then you must select standalone MySQL server and click next, then select use legacy authentication method, then click next. then type in the password 'trolldevelopers' without the quotes, click check, then click next. After installation, open up MySQL Workbench. You should be able to connect to a localhost server.  

Running and populating the database: 
Within your MYSQL localhost server, you will go to file -> Run SQL script. You will select the file (located within the folder within Darkspear labeled MySQL) and select the file ds_design.sql. After this has successfully be ran, you will again go to file -> Run SQL script. From the same folder within the Darkspear folder, you will choose the script darkspear_populate.sql. Run this script. 

Opening up the program: 
Once you've connected with your server and ran the database, it is time to run the program. Open up main.py and run the file. You should be brought to the login page, where you can enter 'Zuroke' as the username and 'poophead' as the password in order to access the other pages of the program! 

© 2018 GitHub, Inc.

