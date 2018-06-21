# Log Analysis Project

## Introduction

This project deals with analyzing over 1 million rows of a news website
database using ```PostgreSQL``` and ```Python```, answering three questions:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Requirements
For running this project, you'll need to install the following software
to avoid cross-platform errors.
1. [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
2. [Vagrant](https://www.vagrantup.com/downloads.html)
3. [VM Configuration](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip)
4. [The Database ```newsdata.sql``` ](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) 

> ###### _Note: The versions of softwares used during the making of the project are as follows:_
> + _Python_: 3.6.3
> + _PostgreSQL_: 10.1
> + _VirtualBox_: 5.2.6
> + _Vagrant_: 2.0.2

## Setting it up
1. Install the files above from their respective links.
2. After installing, unzip the VM Configuration files, which will create the **FSND-Virtual-Machine** folder.
3. Unzip the ```newsdata.sql``` file from above and copy it to the folder **FSND-Virtual-Machine\vagrant**.
4. Navigate to the folder **FSND-Virtual-Machine\vagrant** from your terminal (_Git Bash on Windows and default terminal in Mac and Linux_), run ```vagrant up```.
5. Once the initialization is done, run ```vagrant ssh ``` to login into your virtual machine.
6. Run the command ```psql -d news -f newsdata.sql``` to populate the news database with the required data.
7. Now execute the file ```log_analysis.py```.
8. If you did everything correctly, the raw output should match the contents in the file [output.txt](output.txt).




