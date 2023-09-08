#Beliver01:-youtube

#Database:-Db is an organized collection of structured information, or data, typically stored electronically in a computer system.
#to make the data preserved db is used.the output will be stored in DB.

#Data stored in 2types:-
#1)File handling :-this is previously used this is slowly      platforms
#2)Database:-this is new & this is fast 1)RDBMS:-Relational DB tools(mssql,mysql,oracle,postgresql,sqlite) 2)NOSQL:-Non Relational DB tools(DynomaDB,DocumentDB,MangoDB) tools used for create,read,update,delete the data in DB

#RDBMS(Relational DataBase Management srvc)- SQL(structured query language)this is programming language used to interact with DB.this works on tables(mssql,mysql,oracle,postgresql) {mysql is easy to use}
#install mysql workbench = with password we have to give.

#sql is used in database,table,data for accessing(reading) and manipulating(add/remove) the data 
#Sub languages in SQL Server:-sql commands
#1)Data Definition language(DDL):-Creation of DB,Creation of Tables,alter a table,drop of Tables,Trancate,rename. (DDL)
#2)Data Manipulation language:(DML)-INSERT,SELECT,DELETE,UPDATE (DML)
#3)Data control (or) query language(DCL):-grant,revoke.SELECT Query (USED TO ACCESING THE DATA) (DCL)
#4)Transaction control language(TCL):-SAVE,COMMIT,ROLLBACK,UNDO (TCL)
#5)Data Query language(DQL):SELECT
#contstrains:-primary key,foreign key,check,unique,default,not null. 

#Creation of DB:- 1st create a file and save it,CREATE DATABASE First;#DB created, USE First;#DB activited, DROP DATABASE First;#removes DB

#sql commands:-create database,create table,alter database,alter table,reading data,update data,delete database,delete tables,delete data(by using sql commands)

#DATA types in SQL:-   
#1)exact:-INT,TINYINT,SMALLINT,BIGINT
#2)DECIMAL(10.2) .right ki 10digits, left ki 2digits.
#3)STRINGS(Char(20)fixed length)(nchar(20)unicode values ni can store)(varchar(20)variable length)(nvarchar(20)unicode values ni can store),TEXT.
#4)TIME(HR:MIN:SEC) (3)give 3 millisec    (this can store time)
#5)DATE(YEAR:MONTH:DAY)
#6)binary:-(images)                                     #common data types that can support in every DB tools(float,int,char,varcahr,date,time,datetime)

#Creation of Table in sql:-                --comments in sql
#CREATE DATABASE FIRST;                                  #creates DB
#USE FIRST;                                              #using that DB
#CREATE TABLE student table(                             #creating a table
#student_id int,
#student_name varchar(40),
#student_age int,
#student_avg decimal(10,2)    
#);                                                      #student table created
#select * from student table;                            #(checking about data in table) this will show 4 created fields
#show databases;                                         #this shows the all databases.
#show tables;                                            #this shows the tables in DB.
#desc student;                                           #this show the all attribute names and constrains.

#creating a new column in a table:-
#use FIRST;                                              #entering into DB(or)using DB.
#ALTER TABLE student table
#ADD Stud_parent VARCHAR(40);                            #here new column is added in table (Stud_parent)

#change a column in a table:-
#use FIRST;
#ALTER TABLE student table
#CHANGE COLUMN Stud_parent parent_name varchar(60);        #now the name of column and we can change data type and size will be increased by using alter commands 

#alter table table_name
#modify column perc float;                      #this will modify the datatype in column

#alter table table_name
#modify perc float not null;                    #this will modify not null in datatype

#alter table table_name
#add constraint unique(email)                       #this will add new constraint 

#alter table table_name
#add constaint primary key(id)                   #this add primary key

#alter table student
#add constraint check (age>18);                  #this will check the constraint is 18 or not

#alter table student
#drop index email;                               #this will drop the column in a table

#alter table student
#drop primary key;                               #this will drop the primary key from table

##How to remove column in a table and remove table in Database:-
#use FIRST;                                                 
#alter table student
#rename column tudent_age to student_age;                    #this will rename the column name

#ALTER TABLE student                                        
#DROP COLUMN parent_name;                                   #DROP:If we drop the table all the data and structure of table will be deleted. 
                                                            #the column will be removed from a table data and structure is dlted
#TRUNCATE TABLE student;                                    #TRUNCATE:only data will be deleted(structure will not be deleted)
                                                              
                                                            #here only data will be deleted(rows data will not be deleted)

#DROP TABLE student table;                                   #this will remove the table from Database

#ALTER COMMAND:-(add column,delete column,modify datatype of existing column,set constraints like not null2,primary key,unique key,remove constraints etc..)

##3)How to use select query:-(Data Query language)
#select student_id,student_name,student_age 
#from student table;                                           #this shows the Data of students id,name & age.
#
#select * from student table;                                  #this will shows the total data in the table.

##2)How to Insert Data to the Table in a Database:-(Data Manipulation language)
#USE FIRST;
#CREATE TABLE student table(
#student_id int,
#student_name varchar(40),
#student_age int,
#student_avg decimal(10,2)
#);                                                           #the table is created in database
#
#INSERT INTO                                                  #1st method of inserting. if we need insert bata for specific colomuns then we have to mention their names
#student table (student_id,student_name)
#values (1,'student1'),(2,'student2'),
#(3,'student3'),(4,'student4'),(5,'student5');               #this will create 5rows in table
#
#select * from student table;                                 #this will show the output created 3rows in table
#
#INSERT INTO                                                 #2nd method of inserting. if we are inserting the data in all columns than we dont need to mention thier names. 
#Student table
#values (5,'student5',25,89),(4,'student4',22,98),
#(3,'student3',23,78),(2,'student2',21,89),
#(1,'student1',78,99);                                       #this will add 5 data rows to the table
#  
#select * from student table;                                #this will show the output data created 5rows in table


#How to update Data in a table in a Database:-  by using where clause
#select * from student table;                             #checking purpose 
#  
#UPDATE student table                                     #(this is used at first in updating process bcz of security reasons)
#set student_age = 18
#Where                                                    #without using condition we dont have to update
#student_age is NULL;                                     #the age will be updated in null places with 18 in the table. 
#   
#select * from student table;                             #checking purpose weather is created or not   
#
#UPDATE student table
#set student_avg = 70
#Where
#student_avg is NULL;                                        #the avg will be updated in null places in a table.
# 
#select * from student table;                               #checking purpose weather is created or not  

#update student set grade="pass" where perc>35 and perc<60;            #this will add pass to >35 and <60 in table
#update student set grade="first class" where perc>60 and perc<70;     #this will add first cls to >60 and <70 in table
#update student set grade="distinction" where perc>70;                 #this will add distinction to >70;

##How to delete Data in the table in a Database:- 
#SET SQL_SAFE_UPDATES = 0                                   #(this is used at first in dlting process bcz of security reasons) 
#select * from student table;
  
#DELETE FROM student table
#WHERE student_avg<75                                        #(avg less than 75 will be dlted form table)  
# 
#select * from student table;                             #checking purpose weather is dlted or not 3members data dlted

#delete from student where grade="pass";                   #this will delete the pass members data
#delete from student where grade="first cls";              #this will delete the first cls members data
#delete from student;                                      #this will delete rows

#primary key in SQL:-(we will create over a column)(non duplicate - unique)(no null values)is unique i.e,(id)by using this can easily axis.
#create  database university;
#use university; 
#create table student
#(
# id int,                                                #(Here we can use (#auto_increment) id values1,2,3,4,automatically) by using this we can reduce one step of adding id values by us
# name varchar(30),
# gmail varchar(30),
# primary key(id)
# );                                                      #this will create student table in a Database
#
#create table certificate
#(
# id int,                                                ##(Here we can use (auto_increment) id values1,2,3,4,automatically) by using this we can reduce one step of adding id values by us
# year int,
# sem int,
# primary key (id)                                      
# );                                                     #this will create certificate table 
#                                                 
#select * from student ;                              #before adding values checking  
# 
#INSERT into student 
#values 
#(1,'student1',mail1@gmail.com),
#(2,'student2',mail2@gmail.com),
#(3,'student3',mail3@gmail.com);                    #this data will be inserted in table 
# 
#select * from student table;                      #checking weather the data is inserted or not 
#
#insert into certificate
#values
#(101,1990,1),
#(102,1991,2),
#(103,1992,3);                                   #the data will be inserted in certifiacte table
#
#select * from certificate;                      #checking weather the data is inserted or not
#
##Foreign key:-this refrence the primary key (is mixed added with 2 primary keys by that we can axis the primary key)(only primary key values and null values accepted)
#ex:-(student_id is foreign key for primary key id and certificate_id is foreign key for primary key.)
#create table certificate_log                                          #certificate_log table is created
#(
# student_id int,
# certificate_id int,
# received_date date,
# foreign key(student_id) references student(id),
# foreign key(certificate_id) reference certificate(id)               #3rd table created with the 2foreign key is generated with student(id),certificate(id)
# ); 
# 
#insert into certificate_log
#values  
#(1,101,'2020-10-28'), 
#(1,102,'2020-10-29'), 
#(1,103,'2020-10-30');                                                #the data will be inserted in certificate_log table
#
#select * from certificate_log                                        #checking the data

##constrains for Data in SQL:- 1)primary key(by default takes null) 2)Foreign key
#3)not null:-(one particular column should accept the not null values(no duplicate values))this constrains will say
#4)unique:-(one particular column that does not accept the duplicate values(this accept null values)) this will be used 
#5)check:-(by conditioning the age will be accepting or not)
#6)Default:-(it takes the value our given)
#use first;
#create tabel student1
#(
#  id int auto_increment,                         (here we used auto_increment to increase numbers1,2,3,4,5)
#  name varchar(30) not null,
#  gmail varchar(30) not null,
#  age int,
#  primary key(id), 
#  unique(gmail),
#  check(age>12)                                 #the table will be created            
# );
# 
#insert into student1
# (name,gmail,age)
# values
# ('student1','mail@gmail.com',18),
# ('student2','mail2@gmail.com',19),
# ('student3','mail3@gmail.com',20); 
# 
#select * from student1;                              #this data will stored in the student1 table by using constrains

#Where clause Explanation:- equailty,greater than,less than,between
#select query:-this shows the data in the table
#where clause:-by using this we can delete(we dlt our needy) and update    
#filtering the table: 
#By using where clause:- used for filter in table in database
#create table student2
#(
#	id int auto_increment,
#    name varchar(30),
#    age int,
#    marks int,
#    gender varchar(10),
#    primary key (id)                         #the new student2 table is created
# ); 
#  
#insert into student2
#(name,age, marks,gender)
#values
#('stu_1',23,89,'male'),
#('stu_2',25,90,'male'),
#('stu_3',19,78,'male'),
#('stu_5',25,80,'female'),
#('stu_6',25,90,'male'),
#('stu_7',25,78,'female'),
#('stu_8',25,90,'male'),
#('stu_9',25,90,'male'),
#('stu_10',25,70,'female'),
#('stu_11',25,90,'male'),
#('stu_12',25,80,'male'),
#('stu_13',25,79,'female'),
#('stu_14',25,90,'male'),
#('stu_15',25,90,'male'),
#('stu_16',25,90,'female'),
#('stu_17',25,90,'male'),
#('stu_18',25,70,'female'),
#('stu_19',25,90,'male'),
#('stu_20',25,80,'male'),
#('stu_21',25,99,'female'),    
#('stu_22',25,90,'male');                        #the data will be added into the student2 table


#select query is used for filtering purpose:-
#select * from student2;                              #this will shows the data in the table
#desc student2;                                       #this will show the pattern of table
#select distinct sname from student2;                 #this show the different terms in table(repeated values removed)
#select * from student2 where perc>85                 #this shows the less then 85% in table
#select * from student where perc<70 and id>103;      #this will show the less 70% and id above 103
#select * from student where perc>70 or id>103;       #this will show the grt 70% or id>103;
#select * from student where not perc<90;             #this will show the less 90%  data
#select * from student order by perc;                 #this show the order lower to higher
#select * from student order by perc desc;            #this show the order higher to lower
#select * from student where perc>80 limit 3;         #this will show the above 80 3people data
#select * from student order by perc desc limit 3;    #this will show the top3 perc in table
#select * from student order by perc limit 3;         #this will show the last3 perc in table
#select * from student where sname like 's%';         #this show the starting s letter from the table
#select * from student where sname like '%ee%';       #this show the middle ee letter from the table
#select * from student where sname like '%I';         #this show the starting I ending from the table
#select * from student where perc in (90,99,88,75);   #this show the perc in from the table
#select * from student where perc between 85 and 95;  #this show the perc in between the values 85 to 95
#select name,age,gender from student2;                #this will print only 3columns data
#select * from student2
#where
#id = 15;                                #this will show the id 15th data in table (by using where clause equailty check)
#select * from student2
#where
#age > 18;                                #this will show the age above 18 (greater than)
#select * from student2
#where
#age < 18;                               #this will show the age less 18 (less than)
#select * from student2
#where
#age between 20 and 25;                  #this will show the age between (20-25)
#select * from student2
#where
#age >=17 and age <25;                   #this will show between 
#select * from student2
#where
#age in (20,23,25);                     #this will show the age of 20,23,25
#select * from student2
#where
#name like '%1';                        #this will show the name of (last ending with1) 
#select * from student2
#where
#name like '%1%';                      #this will show the name of (middle with1)
#select * from student2
#where
#name like '1%';                       #this will show the name of (starting with1) 
#select * from student2
#where
#age<>23;                              #this will show the data by escaping 23age.

#aggregate functions:-
#count():-count of values of on attribute
#sum():-numerical values(sum of all values of an attribute)
#avg():-average of all values
#min():-min value of an attribute
#max():-max value of an attribute

#aggregate function:-count,max,min,sum,avg,distinct
#select * from student2;
#select count(*)
#from student2;                          #this will give the total count in table.
#select count(*) as no_of_students
#from student2;                          #this will give the total count in table by duplicate name.
#select count(*) as no_of_students
#from student2
#where age =23;                          #this will show the age 23 people in table
#select avg(marks) as marks_avg
#from student2;                          #this will show the marks avg
#select avg(age) as age_avg
#from student2   
#where 
#age = 23;                              #this will show the avg age of 23 in table
#select sum(marks) as total_marks
#from student2   
#where 
#age = 25;                              #this will show the 25 age canditates total marks  
#select max(marks) as max_marks
#from student2   
#where 
#age = 25;                              #this will show the max marks of age 25  
#select min(marks) as min_marks
#from student2   
#where 
#age = 25;                             #this will show the min marks of age 25 
#select distinct age from student2;    #this will show the distinct ages in table(this avoid the duplicate values) 

 
#joins in sql:- used for joining the data between mulitiple tables(joins).
#1)inner join:-common data between two tables is displayed
#2)left join:-common data + left side data is displayed
#3)right join:-common data + right side data is displayed
#4)full outer join(not supporting in mysql):-all data in tables is considered 
#5)self joins 

#1)inner join:- 
#creating 4 tables stu_joins,mar_joins,sports_join,ncc_nssjoins  
#create table stu_join                   
#(
#	id int auto_increment,
#    name varchar(30),
#    age int,
#    primary key (id)                             #db created
#); 
#insert into stu_join                            #data inserted
#(name,age)
#values
#('stu_1',18),
#('stu_2',18),
#('stu_3',18),
#('stu_4',17),
#('stu_5',18),
#('stu_6',17),
#('stu_7',17),
#('stu_8',18),
#('stu_9',18),
#('stu_10',17);
#select * from stu_join;                         #checking weither inserted or not

#create table mar_join
#(
#	id int auto_increment,
#    marks int,
#    ranks int,
#    primary key (id) 
#);                                             #db created
#insert into mar_join                            #data inserted
#(marks,ranks)
#values
#(89,6),
#(90,3),
#(94,9),
#(80,8),
#(92,4),
#(69,10),
#(90,5),
#(82,7),
#(97,2),
#(9,1);
#select * from mar_join;                         #checking weither inserted or not

#create table sports_join
#(
#	id int auto_increment,
#    sports varchar(30),
#    primary key (id) 
#);                                       #db created
#insert into sports_join                  #data inserted
#(sports)
#values
#('cricket'),
#('basket ball'),
#('cricket'),
#('basket ball'),
#('basket ball'),
#('cricket'),
#('vollyball'),
#('cricket'),
#('vollyball'),
#('basket ball');
#select * from sports_join;                         #checking weither inserted or not

#create table nccnss_join
#(
#	id int auto_increment,
#    ncc_nss varchar(30),
#    primary key (id) 
#);                                   #db created
#insert into nccnss_join              #data inserted
#(ncc_nss)
#values
#('ncc'),
#('nss'),
#('ncc'),
#('nss'),
#('ncc'),
#('nss'),
#('ncc'),
#('ncc'),
#('nss'),
#('nss'); 
#select * from sports_join;                         #checking weither inserted or not

#1)inner join:-stu_join and mar_join  combining (only common data joined data displayed)
#select * from 
#stu_join as t1
#inner join
#mar_join as t2
#on 
#t1.id = t2.id;                   #the data will be joined t1 and t2(stu_join and mar_join) now 2 tables joined and shown

#select t1.id,t1.name,t2.marks,t2.ranks from 
#stu_join as t1
#inner join
#mar_join as t2
#on 
#t1.id = t2.id;                       #this will show the t1 and t2 mixed result (id,name,marks,ranks)

#select * from
#stu_join as t1
#inner join
#sports_join as t2
#on 
#t1.id = t2.id;                     #the data of stu_join and sports_join is shown with inner join
#
#2)left join:-(this will show the combined and left data displayed)
#select * from
#stu_join as t1
#left join
#nccnss_join as t2
#on t1.id = t2.id;                         #this will shown the left side table data and combined data in table
#  
#3)right join:-(this will shown the right side table data and combined data in table) 
#select * from
#sports_join as t1
#right join
#nccnss_join as t2
#on 
#t1.id = t2.id;                  #this will show the right table and combined data in both the tables
# 
#4)full outer join:-(this wont support in mysql)(this supports in mssql) (this show common data and 2 tables full data will be shown )
#select * from 
#sports_join as t1 
#full outer join
#nccnss_join as t2
#on 
#t1.id = t2.id; 
# 
#5)self join:-(this will done on 2same tables if marks more than oneself ) 
#select * from
#mar_join as t1
#inner join 
#mar_join as t2
#on
#t1.marks < t2.marks;              #(this will show the marks more than table2 then joined and shown)
#select t1.id,count(t1.id) as no_of_student_above
#from
#mar_join as t1
#inner join 
#mar_join as t2
#on
#t1.marks < t2.marks
#group by
#t1.id                     
#order by
#t1.id;                 (this will show the data of t1 less than t2 marks table with index is shown)(ex of marks move then one self) 
 
#order by clause in sql:-(this gives order ascending or decending arranging the data in table) 
#use first;
#create table ordr_byc
#(
#	id int auto_increment,
#    name varchar(30),
#    age int,
#    marks int,
#    sports varchar(30),
#    primary key (id) 
#);                                #the table is created
#insert into ordr_byc
#(name,age,marks,sports)
#values
#('stu_1',18,89,'cricket'),
#('stu_2',17,78,'football'),
#('stu_3',18,90,'basketball'),
#('stu_4',17,90,'cricket'),
#('stu_5',19,56,'basketball'),
#('stu_6',18,76,'football'),
#('stu_7',17,45,'cricket'),
#('stu_8',18,90,'cricket'),
#('stu_9',18,65,'football'),
#('stu_10',17,97,'cricket');            #the data is inserted
#select * from ordr_byc                 #we get the data what we inserted 
#select name,age,marks
#from ordr_byc
#order by marks;                        #this will show the marks in ascending order by defalut 
#select name,age,marks
#from ordr_byc
#order by marks desc;                  #this will show the marks in descnding order
#select name,age,marks
#from ordr_byc
#order by marks desc,age desc;         #here it will show marks and age cretieria  
#select name,age,marks
#from ordr_byc
#order by marks desc,age desc,name desc;    #here it will show marks,age,name in desc.
 
#groupby clause:-
#create table group_by
#(
#	id int auto_increment,
#    name varchar(30),
#    age int,
#    marks int,
#    sports varchar(30),
#    primary key (id)
# );                                                  #the group_by table is created
#insert into group_by
#(name,age,marks,sports)
#values 
#('stu_1',18,89,'cricket'),
#('stu_2',17,78,'football'),
#('stu_3',18,90,'basketball'),
#('stu_4',17,90,'cricket'),
#('stu_5',19,56,'basketball'),
#('stu_6',18,76,'basketball'),
#('stu_7',17,45,'cricket'),
#('stu_8',18,90,'cricket'),
#('stu_9',18,65,'football'),
#('stu_10',18,89,'cricket');                               #the data is inserted in table
#select * from group_by                                    #checking the table
#select sports
#from group_by
#group by
#sports;                                             #this will show the no.of sports
#select sports,count(name) no_of_students
#from group_by
#group by
#sports;                                      #thiswill show the no_of_students in sports(by using count(agrigade functions))
#select sports,count(name) no_of_students,avg(marks) avg_marks
#from group_by
#group by
#sports;                                #this will show the avgmarks,no_of players,sport. 
#select sports,age
#from group_by
#group by
#sports,age;                          #this will show the sports and age in table 

 
#having in sql:-(condition) while using group by we use having clause. 
#select sports,count(name) no_of_students,
#avg(marks) avg_marks
#from group_by
#group by 
#sports
#having 
#no_of_students >=3;                     #this will show the greater than or equal 3 no_of_students 
#select sports,count(name) no_of_students,
#avg(marks) avg_marks
#from group_by
#group by 
#sports
#having 
#no_of_students >=3 and avg_marks>80;                #this will show the no_of_students having morethan 3,and avg_marks grt 80 
  

#ranks in mysql:-3types of functions auto generted
#1)rank() :-duplicate rank is counted here(it counts nmbrs and give after rank)
#2)row_number() :-different rank
#3)dense_rank() :-duplicate ranks not counted(dont count nmbrs)
#1)
#select 
#name,marks,rank() over(order by marks desc) as student_rank
#from group_by;
#2)                                                    #this will show the ranks of students (this will give duplicate ranks)
#select 
#name,marks,row_numbers() over(order by marks desc) as student_rank
#from group_by;                                         #this is show the ranks of students (this is give differnt nmbrs by sequenc)
#3)
#select 
#name,marks,dense_rank() over(order by marks desc) as student_rank
#from group_by;                                           #this gives the (duplicate invloved but give the next nmbr after that nmbr)


#union and intersection:-(it will combine total rows in two select quries(sm no.of columns must be presnet))(mysql) (it will display common rows between two select quries)(not there in mysql)
#select * from group_by where sports = 'cricket';                 #this will show the no_of_student playing cricket
#select * from group_by 
#where sports = 'cricket'
#union
#select * from group_by
#where sports = 'football';               #(union will remove the duplicate data)by using this union we get both cricket and football data from the table
#select * from group_by 
#intersect
#select * from group_by
#where sports = 'cricket';         #this will done in mssql(intersect)


#sub queries in sql:-if in one sql querie then inside that writting no of queries is known as sub queries
#1)normal sub queries:-at first 1 sub querie excuted and that value is used excute next main querie  
#2)co-related subqueries:-for every row the subquery will execute.(all rows scaned no.of times)
#create table sub_queries
#(
#	id int auto_increment,
#    name varchar(10),
#    age int,
#    marks int,
#    gender varchar(10),
#    primary key (id)
#);                                    #creating a table
#insert into sub_queries
#(name,age,marks,gender)
#values
#('stu_1',18,95.00,'Male'),
#('stu_2',19,90.00,'Male'),
#('stu_3',17,84.50,'female'),
#('stu_4',18,75.00,'Male'),
#('stu_5',18,75.00,'Male'),
#('stu_6',18,75.00,'Male'),
#('stu_7',18,69.00,'feMale'),
#('stu_8',17,79.00,'Male'),
#('stu_9',18,87.00,'feMale'),
#('stu_10',19,98.00,'Male'),
#('stu_11',18,91.00,'Male'),
#('stu_12',18,65.00,'Male'),
#('stu_13',19,93.00,'Male'),
#('stu_14',18,45.00,'feMale'),
#('stu_15',18,49.00,'feMale'),
#('stu_16',17,70.00,'feMale'),
#('stu_17',18,65.00,'feMale');               #the data is inserted into the table
#1)now i want to find the no_of male stu who have marks more than avg marks of female stu
#select avg(marks) from sub_queries where gender = 'female';                   #we get avg marks of female stu
#select count(*) 
#from sub_queries
#where
#gender = 'male'
#and 
#marks > (select avg(marks)avg_marks from sub_queries where gender = 'female');          #this will show the grter count male avg marks>avg marks girls
#select * 
#from sub_queries
#where
#gender = 'male'
#and 
#marks > (select avg(marks) avg_marks from sub_queries where gender = 'female');      #this will show grter the no_of_stu male with name.1st female avg counted the sub querie runned.
#select * 
#from sub_queries
#where
#gender = 'male'
#and 
#marks < (select avg(marks) avg_marks  from sub_queries where gender = 'female');     #this will show less marks data of male 

#2)create a table  
#create table co_related_sq
#(
#	id int auto_increment,
#    name varchar(10),
#    age int,
#    salary int,
#    gender varchar(10),
#    primary key (id)
#);                                        #table created
#insert into co_related_sq
#(name,age,salary,gender)
#values
#('emp_1',18,9543,'male'),
#('emp_2',19,9054,'male'),
#('emp_3',17,8654,'female'),
#('emp_4',18,7235,'male'),
#('emp_5',18,12395,'male'),
#('emp_6',18,5545,'male'),
#('emp_7',18,6569,'female'),
#('emp_8',17,7569,'male'),
#('emp_9',18,8877,'female'),
#('emp_10',19,2398,'male'),
#('emp_11',18,12191,'male'),
#('emp_12',18,4565,'female'),
#('emp_13',19,6793,'male'),
#'emp_14',18,9845,'female'),
#('emp_15',18,9849,'female'),
#('emp_16',17,9770,'female'),
#('emp_17',18,3665,'female');               #the data is inserted
#select * from co_releted_sq                 #checking
#2)now find the nth highest salary of the employee table.(using co_releted subqueries):-
#select salary as nth_highest_salary
#from 
#co_related_sq as t1
#where
#0 = (
#select count(*) from co_related_sq as t2
#where
#t1.salary < t2.salary                                   #the highest salary will be displayed 0,1,2,3,4 we get index we see
#);                                                           


#practice problem-1:- (in hacker ranker)
#name of any student in students who scored higher than 75 marks order your output by the last 3 char of each name if 2 or more students both have names ending inthe same last 3 char secondary sort them by ascending id.
#create a table and insert the data inside the table.and check select * from parctice_1
#select name from parctice_1
#where
#marks > 75
#order by 
#substring(name,length(name)-2,3)asc,
#id asc;                                           #here we get names of students who got above 75marks.but they have to be ordered in base on last 3 char if that also equal then use id to display.


#practice problem-2:-(we use group by and order by in this problem)(hacker ranker)
#in this an employee total earning to be their monthly salary * months worked. and the max total earnings to be the x earning for employee in the parctice_2 table. write a query to find the max total earning for all employees as well as total no.of employees who have max total earnins. then print these values as 2 space separated integers.   
#create a table and insert the data inside the table.and check select * from parctice_2
#select months*salary as earning,count(*)
#from parctice_2
#group by 
#earnings 
#order by  
#earnings desc
#limit 1                                #by this we find months * salary and find max value that max salary how many members got should be displayed. 1,2,3,4,5 we get no.of employees details

 
#practice problem-3:-(joins concept)(hacker ranker)
#given the city and country tables query the names of all the continents(country,continent) rounded down to the nearest interger 
#create 2tables(city and country) and insert the data inside the table.and check select * from parctice_3
#select t2.continent,floor(avg(t1.population)) from
#city as t1
#inner join
#country as t2
#on
#t1.countrycode = t2.code
#group by 
#t2.continent                #using country code we joined city and country table. by using continent based we did group by inside continent cities population avg found continent space avg printed 


#practice problem:-4(joins concept)(hacker ranker)
#given the city and country tables,query the names of all cities where the continent is 'africa' 
#create 2tables(city and country) and insert the data inside the table.and check select * from parctice_4  
#select t1.name from
#city t1 
#inner join
#country t2
#on 
#t1.countrycode = t2.code 
#where 
#t2.continent='Africa'           #city and country table joined with citycode and countrycodes tables. then we filtered cites names 
 
 
#practice problem:-5(joins concept)(hacker ranker)
#ketty gives eve a task to generate a report containing 3columns: Name,grade,marks. ketty doesn't want the names of those students who received a grade lower than 8.it must be in desc order by grade if same grade then same with alpha order if less then 8 then say null  
#create 2tables(students and grades) and insert the data inside the table.and check select * from parctice_5
#select if (t2.grade>=8,t1.name,NULL) as name,t2.grade,t1.marks
#from
#students t1
#inner join
#grades t2 
#on 
#t1.marks >= t2.min_marks and t1.marks <=t2.max_mark             
#order by
#t2.grade desc,t1.name asc,t1.marks asc                    #student and grads table joined. after used if condition  >8,name,null. order by t2.grade desc,t1 asc,t1.marks asc. printed

 
#normalization in DBMS:-(by using this we can avoid duplicate data in table) (this save the storage by spliting one table to 3different tables by this the NULL values will be removed from table)(data dupplicate and errors removing and data will be worked efficient and structuredway in table)
#main normal forms
#1)1nf:-1st normal form
#To Remove Insertion Anomolies (in one cell you have to store only 1 name or value and you cant store multiple names or values)
#To Remove Deletion Anomolies (just remove the particular student data)
#To Remove Updation Anomolies (just update the particcular student data)
#2)2nf:-2nd normal form (it should follow 1 nf no partial dependencies)(dependencies:-a table contains prime attributes(student id) and non prime attributes(age,gender)) 
#functional dependencies(non prime attribute depend on prime attribute)
#partial dependencies(if 2 columns acting as prime attributes then that columns no need depend on partially it should depend on completely then it allows 2nd normal form)
#transitive dependencies(if in a table one non-prime attribute depend on another non-prime attribute)1 table splited as 2 tables
#3)3nf:-(table should follow 2nf)(it should not have transitive dependencies)
#4)BCNF(boyce codd normal form):-it should follow 3nf (prime attribute should not depend on non-prime attribute)

 
#views in sql:-virtual table(it is used to make secure access of the data. simple way of accessing the data)(this is used for security purpose)(by creating view the data which need access to outside by this we can access the data by view) 
#creat a emp_view table,insert the data into it 
#create table emp_view 
#(	
#	id int auto_increment,
#   name varchar(10),
#   age int, 
#   salary int,
#   gender varchar(10),
#   primary key(id)
#);                        #table created
#insert into emp_view
#(name,age,salary,gender)
#values
#('emp_1',18,9543,'male'),
#('emp_2',19,9054,'male'),
#('emp_3',17,8654,'female'),
#('emp_4',18,7225,'male'),
#('emp_5',18,122395,'male'),
#('emp_6',18,5545,'male'),
#('emp_7',18,6569,'female'),
#('emp_8',17,7569,'male'),
#('emp_9',18,8677,'female'),
#('emp_10',19,2398,'male'),
#('emp_11',18,12191,'male'),
#('emp_12',18,4565,'male'),
#('emp_13',18,4793,'male'),
#('emp_14',18,9533,'male'),
#('emp_15',18,9893,'female'),
#('emp_16',18,9153,'male'),
#('emp_17',18,9343,'female');    #data inserted
#select * from emp_view;        #checking
#create view male_data_view as        #create a view 
#select id,name,age from emp_view
#where gender = 'male';               #created
#select * from male_data_view;          #checking
 
 
#stored procedures in sql:-(if complex queries we need to use no.of times then we create that complex querie as stored procedure by creating the querie is stored)(by using that querie name we can refernce to another) (by using call statements)
#(to refrence complex query) 
#delimiter //
#create procedure emp_procedure()
#begin
#select id,name,age from emp_view
#where 
#gender = 'male' and age < 19 ;
#end //                              #the storage procedure is created
#call emp_procedure();               #this will show the emp_procedure 
# 
#delimiter //
#create procedure parameter_procedure(
#	p_gender varchar(10),
#    p_age int
#)
#begin
#select id,name,age from emp_view
#where 
#gender = p_gender and age < p_age ;
#end //                                  #the parameter_procedure is created
#call parameter_procedure('male',20);        this show the data above 20 and male data shown 
 
 
#indexes in sql:-  
#create index <index name> on table (<column name>) if we want employee data whose salary is more than 8000
#create index salary_index on 
#emp_view (salary asc);                          #the index is created in emp_view table
#select * from emp_view
#where
#salary > 8000;                            #by this we can access that table
# 
# 
#select * 
#FROM 
#   order_table 
#WHERE
#   order_date = current_date()-1;               #we get the information yesterday orders. 
# 
#OLTP(Transactional app):(online transfer process)high vol of transactions,fast processing,Normalized data,many tables,
#OLAP(Analytics reporting):(online analytic process)high vol of data,slow queries,denomalized data,fewer tables.  
# 
#Relational(sql DB): relational(column & rows)analtics(OLAP),      Non-relational(Nosql DB):Key-value,column-fammily,graph,Document. 
#structure:DB management system,DB,schema(is a named collection of tables),Tables(is a collection of data which is organized in terms of rows & columns). 
# 
#select * from teachers
#order by salary DESC;                                 #this shows the salary from high to low in table.
# 
#select * from teachers
#order by school ASC, salary DESC;                     #this shows school names with alaphbet order & salary high to low. 
# 
#select * from teachers 
#WHERE school = "st mathew's";                    #only the mathews school data filtered out.  
#
#select * from teachers
#WHERE first_name ='Janet';                       #here we get the first name data from table.
#
#selet * from teachers
#WHERE hire_date > '2000-01-01';                  #here we get the data which teacher hired date. 
#
#select * from teachers
#where salary between '40000' and '65000';          #this query will show the salary data b/w 40 to 65
#
#select * from teachers
#where salary > '60000'                         #this will show above 60k list
#
#create table data_time_types(
#   timestamp_column timestamp with time zone,
#   interval_column interval
#);                       #this create a table
#INSERT INTO data_time_types values
#('2018-12-31 01:00 EST ','2days')
#
#
#problems:-
#select max(salary) from employee;          #50000  #this shows the max salary from the table. (max is aggregate function)
#select employee_name from employee
#   where salary=(select max(salary)from employee);             #this show person name and salary highest. 
#select max (salary) from
#   employee where salary <>(select max(salary)from employee);            #this shows the 2nd max salary from the table
#select empolyee_name from employee
#   where salary =(select max(salary)from 
#   employee where salary <>(select max(salary)from employee);            #this shows the 2nd highest salary person name. 
#
#select dept,count(*) employee group by depatment;                        #this shows the department count of members.
#
#select depertment from employee group by depeartment having count(*)<2;       #this shows the employee count lessthan 2 compared with other groups. 
#select emplyee name from employee where department  in
#   (selecct department from employee group by department having count(*)<2);          #this shows the employe name 
#
#select min(salary) from employe;       #min 
#select max(salary) from employe;       #max
#select count(*)from employe;           #shows no.of 
#select sum(salary) from employe;       #this show some of table values.
#select distinct (sum(salary)) from employe;       #this show some of table values.(removes the distinct values)
#select avg(salary) from employe;           #shows avg
#
#select employe name from          #use nested query 
#   employe where Eid in (select distinct(Eid)from project);        #this name of emp.
#
#delete from student
#   where id=1;                #this dlt the row 1 data
#
#select name,max(salary) as salary from employee
#   where salary<>(select max(salary)from employee);                            #shows the 2nd highest nmbr. 
#

























