#AWS,Python,SQL,Terraform






#Darshil pramar youtube data engineering projects:-end to end
#goals & success creteria:- Data ingestion(data coming from multiple sources),ETL design(Extract,transform,load data),Data Lake(to orgainze the data & build pipeline around it),Scalability(scale efficiently),AWS Cloud(cloud),Reporting(dash board). 
#big data:-massive data sets,with varied & complex structure(structured data csv files)(unstructured data audio,video)
#data lake:-Relation DB,Non-relational DB,big data processing,log analytics,data warehousing,ML.
#Glue data catalog:-is the information of data & what it contains.  
#Data stores:-redshift,s3,RDS,DB on Ec2----->Glue ETL(Glue data catalog)---->Athena,Redshift spectrum,EMR------>BI Tools 
#when we get json format data we cant queary it on athena then we have to change the formate by using the lambda & store that changed parquet formate to another s3 bucket & create glue crawler & do queary by Athena(this is the correct path(of data cleaning  semi-structured data to structured pipeline)) 
# 
# 
# 
# 
#Data eng:-data warehousing,DB,management & design data modelling, sql,nosql,distributed system,programming,(lang like:py,java,scala) 
#Data scientist:-Advanced statistics,M/L,lang:-py,& R
#data Analyst:-Business Analytics,Sql,statistics,visuailization & Dashboarding 
#
# 
#Data Engineer road map:-
#part1(fresher lvl):-sql,python,java,dbs
#part2(intermidate lvl 2-3yrs):-big data,apache airflow,hadoop,apache spark,data warehouse.
#part3(adavance lvl 3-4yrs):-aws,vpc,docker,kubernetes, 
# 
#Data Structure:-is a particular way of organizing data in a computer so that it can be used effectively. this basic fundmentals we have to know (Arrays,Linked list,stack,queue,graphs,trees,sorting & searching algorithms) 
#
#Databases:Relational databases(create,read,update,& delete table,insert data in table,join tables,sub queries,group by & having case statement,window function,(aggregate function(max,min,avg,sum,etc)),Type casting):sql statement:-(data defination lang(DDL),data manipulation lang(DML),data control lang(DCL),transaction control lang(TCL)). we need to know (Database Schema,Indexes,ACID Properties,Creating Views,Stored Procedure,Normalization,Data Models & ER Diagrams). 
#
#2video:-Big Data Fundamantals:-volume(huge amount of data),variety(diff formats of data from various sources),value(extract useful data),velocity(high speed of accumulation of data),veracity(inconsistencies & uncertainty in data))
#data processing:-batch processing(large quantity data),stream processing(in real-time or near real time),hybrid processing(both batch & streming)  
#Data warehouse:-A data warehouse is a large collection of business data used to helpan organization make decisions.       (redshift,apache hive,snowflake,big querys)
#OLTP(online transaction processing)this is used for system that need quick insert,updtae,dlt.
#OLAP(online analytical processing)used for analysing the data & extracting value out of it. 
#python librires:-pandas,numpy,matplotlib
#SQL DB:relational,OLAP    NoSQL DB:-column-family,graph,document,key-value. (apache hbase,casndra,mongoDB,DynamoDB)
#streaming srvcs:-Apache Kafka,cloud pub/sub,amz Kinesis.
#
#3video:-aws
#
#4video:-python,data structure & algorithms,sql,big data fundamentals,librires,data orchestration airflow,nosql,

#interview questios:-
#DE:-conversion of raw data into useful information. 
#Data modeling:-is the simplification  of complex software designs by breaking by breaking them up into simple designs.(provides simple visual representation among numerous other advantages). 
#Design schemas are used when performing data modeling:-1)star schema(main,dimension in star shape), 2)snowflake schema(fact,demensional,sub in snowflake shape).
#hadoop streaming is one of the widelyused utilities provided by hadoop for users to easily create maps & perform reduction operations.  
# 
# 
#ER model:-Entity-Relationalship mosdel introduced by peter chinn in 1976. E-R model is a visual representation at data that descride how data is related to each other. (or) the E-R model defines the conceptual(logical) view of a database.   
#ER model is a graphical represented in an entity,attributes & relationships.   
#ER model are represented in an entity-relationship diagram.  
#components of ER model:-
#Entity:-is a thing or object in the real world. which consists of either places,persons,animal & soon. 
#attribute:-is nothing but charactersistics or properties of an entity. an attribute is represnted by an ellipse. each entity is described by a set of attributes 
#relationship:-relationship describe associate among data. relationship is represented by a diamond
#Advantages:-visual representation,conceptual simplicity,integrated with the relational data model. 
#Disadvantages:-limited relationship representation,it doesn't supper DML.   
# 
#
#
#
#
#Serverless(Not required to maintain servers or Operating systems,No need to bother about the security, Its completely managed by the service provider(fully managed srvc)). AWS provides DynamoDB as a srvc.No installations required and pay only for what you used. No schema restrictions,vary fast while retrieving the data. rows=items, cells=attributes.  
#fast(provides very fast throughput with low latency)Throughput(the amount of data moved successfukky from one place to another in the given time period). latency(is a measure of delay in a network,latency measures the time it takes for some data to get to its destination across the network)
#Flexible(there is no schema restrictions. so,you can maintain different types of data in the same column & the attributes count could be different in each row.)
#fault Tolerant(It automatically replicates data to multiple availability zones(AZs). In case any failure happen at one AZ,automatically the data will be fetched from another AZ, DynamoDB supports cross region repliaction. which provide more safety to the data.)
#Security(It's a highly secured NoSQL DB). 
#Partition:-is simply logical separation or group of m/cs that hosting your data. (used to find the location in which the row is located)
#
#(Cloud computing in telugu)AWS Dynamo Db part1:-To over come the limitations of Relational Databases the non-relational Db comes into the picture.
#A Relational DB(we have give the values according to the schema)(if we have to update anything in table 1st we have to update schema) is a collection of data items with pre-defined relationships b/w them. these items are organized as a set of tables with columns & rows. Tables are used to hold information about the objects to be represented in the DB.(strong DB,DB Normalization & data must be maintain organized way) (if develop a software for certain level we havn't gone back to basics again for corrections)(to overcome this problem no-sql will be used)(MySQL,PostgreSQL,Microsoft SQL server,MariaDB,ORACLE).
#NoSQL DBs(json or xml format)(we dont need to update the schema we can add values directly) concept was emerged to overcome the limitations of traditional DBs. When compared to relational DBs like SQL server,MYSQL,Oracle etc..,NoSQL DBs are highly scalable flexible & faster. Schemaless & non relational structure.(Enable Easy Updates to Schema & fields,store unstructured,semi-structured,or structured data,Handle large volumes of Data at high speed with a scale-out architecture,Developer-friendly,Take full advantage of the cloud to Deliver Zero Downtime.) (we dont know how the data will come to us to store we use this NoSQl)(Amazon DynamoDB,MongoDB,cassandra,Apache HBASE,Azure CosmosDB,CouchDB).
#NoSQL DB Models:-1)Document-Based DB,2)Graph-Based DB,3)Wide Column Based DB,4)Key-Value DB.    In AWS DynamoDB(Key-value) used. 
#Amazon DynamoDB part2:-is a serverless cloud based NoSQL DB.this is Fast,Cost Effective,Flexible,fault Tolerant,security.    
#Core components of Amazon DynamoDB:-In DynamoDB,tables,items,& attributes. (tables:-similar to other DB systems, DynamoDB stores data in tables.A table is collection of data)(Items:-Each table contains 0 or more items.An item is a group of attributes i.e., uniquely identifiable among all the other items.)(attributes:-Each item is composed of one or more attributes. An attribute is a fundamental data element,somethinng that does not need to be broken down any futher). 
#A table is a collection of items, & each item is a collection of attributes. DynamoDB uses primary keys to uniquely identify each item in a table & secondary indexes to provide more querying flexibility.
#You can use DynamoDB Streams to capture data modification events in DynamoDB tables.       
#Primary Key:-when you create a table,in addition to the table name,you must specify the primary key of the table. The Primary Key uniquely identifies each item in the table, so that no two items can have the sm key. 
#DynamoDB supports 2different kinds of primary keys:-1)Partition Key(maintaing only one single column as primary key(without having duplicates)) 2)Partition key & sort Key(if we want the combination 2 columns as primary key. this abserve in b/w 2columns contains duplicates or not).   
#Hands-on:-goto AWS DynamoDB-Tables-create table-table name-country,string-default setting-create.   go inside-explore table item-create item-(we get 2 formats form & json)
#
#
#
#DynamoDB is a fully managed, key-value, and document database that delivers single-digit-millisecond performance at any scale..DynamoDB is a fast and flexible NoSQL database service for all applications that need consistent, single-digit-millisecond latency at any scale. Its flexible data model and reliable performance make DynamoDB a great fit for mobile, web, gaming, advertising technology, Internet of Things, and other applications.
#
#DynamoDB(jyothi IT Solutions):-is a fast & flexible NoSQL DB srvc for apps that need consistent,single-digit millisecond latency at any scale.Its flexible data model & reliable performance make it a great fit for mobile,web,gaming,ad-tech,IOT,& many other apps.   Is a full(AWS)managed NoSQL Key-value & Document DB. Is aligned with the values of server-less apps:- automatic scaling according to your app load, pay-per-what-you-use pricing, easy to get started with,& no servers to manage. High availability & Durability(deployed 3AZ). PIT recovery:- you can restore a table to any point in time during the last 35days. 
#Hands on:-create a table,table name(musicnotes),add partition key(Artist),add sort key(song title),uncheck defalut setting(to add secondry index),add index,add primary key add attribute as sort key,all,tick the check box add index(LSI created),provisined,create.Now adding global index values(GSI)Go to indexes,create indexe,add primary key new added,add sort key as attribute key,all,create.(GSI created)
#
#DynamoDB(Code Practice):Tables,items,Attributes,primary key(mandatory),Local Secondary Indexes(LSI),Global Secondary Indexes(GSI).
#SQL:Tables,Rows,columns,primary krys(optional),Indexes,views. 
#DynamoDB Provides 3types of consistency:-1)Strong consistency,2)Eventual consistency,3)Transactional consistency.  
#LSI(Local Secondary Index):-will have sm partition/Hash key attribute as the primary index of the table. Will have different sort/range key than the primary key of the index table.Provides an alternative sort key to use for scans & queries.Must be created at table creation time. should always define a sot=rt/range key. Only 5LSIs can be defines per table. 
#GSI(Global Secondary Index):-when your app needs same or different partition key as the table. Provides consistent index reads only. 
#GSI is an additional data structure that you can create on a DynamoDB. It provides an alternative partition key & optional sort key for querying the table's data in a different way than the primary key. A GSI allows you to define different attributes as the primary key or sort key for the index. They allow you to perform queries that are not possible or efficient using the primary key or sort key alone. AWS DynamoDB only supports 20 indexes per table.   
#
#DynamoDB(JOYATRES TECHNOLOGY):-NoSQlDB,Fully Managed DB,Supports both Document(JSON,XML)&key-value store models,TTL Features,No Fixed Schema,Designed to scale out using Distributed cluster of the hardware.(read time is high compared to SQL DBs)(In this DynamoDB there is no specific columns it has multiple columns it defined on rows).
#Benefits:-cost effective,provisions,AWS set of srvcs support. 
#Tables:-DynamoDB stores the data in tables. A table is a collection of data.
#Items:-Each table contains 0 or more items. An item is a group of attributes that is uniquely identifiable among all of the other items.In DynamoDB there is no limit to the no.of items you can store in a table.
#primary Key:-Each item in a table is uniquely identified by a primary key.This key definition must be defined at the creation of the table,& the primary key must be provided when inserting a new item.
#There is 2types of primary key:-1)A simple primary key(made up of partitiomn key) 2)A composite primary key(made up of partition key & a sort key)
#CRUD Operations:-(Create,Read,update,Delete) operations using AWS DynamoDB with a focus on a table that has a Global Secondart index(GSI). These are the four basic functions of persistent storage.Also,each letter in the acronym can refer to all functions excuted in relational DB apps & mapped to a standard HTTP method,SQL statement, or DDS operation. CRUD is data-oriented & the standardized use of HTTP action verbs. 
#Drabacks of DynamoDB:-Limited query capabilities,Provisiones throughput management,maximum item size limit(400kb),Eventual Consistency,Lack of Multi-table transaction.
#Benefits of CRUD:-Instead of using ad-hoc SQL statements, many programmers prefer to use CRUD bcz of its performance. 
#Reads & writes:-Strongly Consistent Reads & Eventually Consistent Reads.Transactional Reads.Read Capacity Units(RCUs).Write capacity Units(WCUs).Throttling-Provisioned Throughput ExceededException.Can be Dynamically adjusted. 
#DynamoDB-Partitions:-10GB per Partition,3000 RCUs per Partition,1000 WCUs per partition,Intitial partitions = round(RCU/3000+WCUs/1000),Assume RCUs  = 3000 & WCUs =1000,then initial noof partitions = 3000/3000 + 1000/1000 = 1 + 1 =2.   
#Primary Key index(Partition key PK1 + Sort key SK1).
#Local Secondary index(LSI)(Partition Key PK1 + Sort Key SK2).
#Global Secondary index(GSI)(Partiition key PK2 + Sort Key sk1)
#
#
#
#(Be A Better Dev)AWS Dynamo DB(A fast & flexible NO-SQL DB Srvc for any scale)(is a fully managed key-value & document DB that delivers single Digit-millisec performance at any scale):Managed No-SQL DB optimized for performance at scale. High Availability99.9999% & Durability(multi AZ),ideal for applications with known access patterns,Access DynamoDB through APIs/ORMs & authorized through IAM,Integrates well with other AWS srvcs,cost effective usage based payment model.   
#Core concepts:-Tables,Items,Attributes,Indexes.            DynamoDB is a Region specific.        only a single partition key per DynamoDB Table. You Can create Global Indexes that have a different partition key than the table itself.This is useful if you want to query your data in a different way than the primary table. 
#Tables are a collection of items. Items are collections of Attributes or key/value pairs. Primary key = Partition key, Partition key Sort key(or)range key,Global Secondary index, Attribute.  
#Hands-on:-create table-name-partition key orderid string-sort key creationdate string-customize settings-provisioned-on 5 off 5-crete table.  
# 
#Are you always doing quick lookups of as known key,& is if globally unique:-use partition key  
#Is your key non-unique, or do you want to do range-like queries based off some other value:-use partition key + sort key 
#Other strategsies:-Prefixes/suffixes,composed partition keys DynamoDB Accelerator(DAX).  
# 
#DynamoDB GSI(Global Secondary Index):-Naive Approach:-Scan + FilterExpression("OriginCountry=="Germany")   Efficient Approach:-OriginCountry GSI,fetch "Germany" with one lookup.  
#you as a user define a GSI index- This involves selecting a new Partition Key. 
#creating a GSI clones your Primary Table using your new Partition Key,but keeps these 2 tables in SYNC.
#GSI works:-your GSI table plays by the same rules as a normal DynamoDB table:-1)GSI partition Key requiers uniform data distribution,2)Define RCU/WCU capacity separately on the index,Throttling. 
# 
#DynamoDB(Local Secondary index(LSI)):-
#Limitations of LSI:-Can only define a LSI at table creation time,Limited To 5LSIs,No Extra Cost.
# 
#DynamoDB Autoscaling:-(RCU:-Red capacity units)(WCU:-Write capacity units)
#Consumed Capacity & Provisioned Capacity.  By using Target Utilization we can configure the autoscaling in DynamoDB. 
# 
#DynamoDB Streams:-Feature that emits events when record modifications occur on a DynamoDB table. Events can be of types INSERT,UPDATE,& REMOVE. Events can carry the content of the row(s) being modified.Events are guaranteed to be in the same order the modifications took place. Unlock powerful use cases.   
#USe Cases:-Real Time Dashboards.Data Replication for Fuzzy Searches.             By using Lambda & It has shards to store the real time stream. 
#Features:-Guaranted,in order events,Customizable events - Keys only,New Image,Old Image,New & old Images,Batch Processing,No performance impact on source table,Super easy integration with AWS Lambda Functions. 
# 
#DynamoDB streams to Lambda Trigger:-Hands on 
#GO to DynamoDB-->Give table name-->Give partition key-->sort key-->create. 
#Goto IAM & create a role for lambda.
#Goto lambda and create a function py3.6.
#
#AWS EVEnts(jason hunter):-DynamoDB came on 2004(DB Scalability challenges),2007(published on paper),2012(DynamoDb Availability)
#Characteristics:-users-1million,Data volume:-TB PB EB,Locality:-Global,Performance:-Microsecond latency,Request rate:-Millions/sec,Access:-mobile IOT devices,scale:-Up & down,Economics:-Pay as you go,Developer access:-instant API success. 
#DynamoDB:-Fast & flexible NoSQL DB srvc for any scale(performance at scale),(No servers to manage),(Enterprise ready).
#DynamoDB Acceletor(DAX)Adds read cache(Performance at scale):-your apps(fully managed highly available cache for DynamoDB),DAX(Even faster-microsecond latency,scales to million of read request/sec),DynamoDB(API compatible).
#Global Table provide apps with multi-region replication(performance at scale):-builds high performance,globally distributed apps, low latency reads & writes to locally available tables,multi active writes from any region. 
#If we migrate  from oracle to DynamoDB:-Improve customer experience,Reduced cost,Reduced complexity risk. 
#No srvers to manage,On-demand capacity mode:rapid,flexible,scaling(pay per request pricing),Provisioned capacity mode:auto scaling,maintains performance(provision capacity as needed)
#Native,server-side support for ACID(Atomic,Consistent,isloated & Durable) transactions(Enterprise ready).
#Security-Access controls & Encryption at rest(Enterprise ready). All tables encrypted in transit,at rest by default. (DEfault,KMS-C,KMS-AWS)
#Security-Audit Logging with AWS CloudTrail(Enterprise ready)
#Backup & restore(Enter prise ready):-on-demand bup for long-term data archiving & compliance,(PITR),0 performance impact.
#Export DynamoDB data to s3 for analysis & insights:-DynamoDB used for transional workloads(OLTP) Not used analytics prupose(OLAP)
#PartiQL now supported for easier queries(enterprise ready):-this is used in dynamoDB for easier queries(query,insert,update,& dlt table data),Improved productivity:-(this supports all data plane operations,developers can use a familiar,structured query lang to perform these operations),consistent performance:-(by this dynamoDB continues to provide consistent,single-digit-milisecond latency at any scale).use partiQL (a sql-compatiable query lang). PartiQL Operations:-Executestatement:-supports single/multiple item SELECT & single item INSERT,UPDATE,& DELETE. Batchstatement:supports a batch of single item SELECT batch of single item of upto 25 items. ExecuteTransaction:-supports all-or-nothing changes to multiple items bith within & across tables. 
#SQL(used scale up & down):-Normalized/relational,Ad hoc queries,Scale Vertically,Good for OLTP/OLAP  NoSQL(used scale in & scale out):-Denormalized/hierachical,Instantiated views,scale horizontally,built for OLTP* at scale.
#Table,Items,partition key(Mandatory),sort key(optional),Attribute. 
#How to read data from DynamoDB:-
#Getitem:-Specify exact value of primary key (pk & sk).will consume read capacity units(RCUs)based on the size of the item.if you need to get onerecord with a specific partition key & sort key.
#Query:-Specify exact value of PK & optionally a SK condition.Optionally add filter conditions on non-key attributes.shows matching items.get most matched items.If you need to get 1 ir more records with the same partition key. If you need to get many records with the sm partition key & want to narrow down results with a key condition(=><exists)
#Scan:-Don't spacify  any keys! optionally specify filter conditions on non-key attributes. shows all  matched items. Almost never use    
#DynamoDB Type:-string,number,number or string,binary,bool,null,list,set of string,number,or binary,map.
#Operational types:-Getitem,query,scan,batchgetitem,putitem,updateitem,deleteitem,batchwriteitem,transgetitems,transwriteitems.
#Global Secondary index(GSI):-Alternate partition &/or sort key index is across all partition keys.  (create at any time,wcu/rcu independent of table,no size limits,limit=20,Eventual Consistency).  is a like of secondary table. with different structure.automatically propageted from the base table into GSI. maintained by the DynamoDB system. with a log propagator that knows how to move data from the base table into the GSI table. 
#Local Secondary index(LSI):-the partition key has to be the same. LSI(create at table creation,share WCU/RCU with table,Collection size<=10GB,limit =5,strong consistency).  is a kind of like data sitting right there next to base table inthe same partition. 
#Part2:-DynamoDB will carry the 2working copies in different AZs. Its resilient to the failures. 
#Provisioned mode:-steady workloads,Grasual ramps,Events with known traffic.
#use on-demend mode:-Unpredictable workloads,Frequently idle workloads,Events with unknown traffic,set it & forget it. 
#DynamoDB Accelerator(DAX):-Fully managed highly available: handle all software management,fault tolerance,replication across multi-AZs within a region. write-through:DAX handles caching for writes. flexiable:configure DAX for one table or many. Scalable:scales-out to any workload with upto 10 read replicas. Manageability:-fully integrated AWS srvc:CW, tagging for DB,AWS Console.  Security:- Amz VPC,AWS IAM,AWS Cloud Trail,AWS Organization.  
#DynamoDB API compatible:-seamless caches DynamoDB API calls, no app re-writes required.
#DynamoDB Scans:-Operation to retrieve all items in your table. Equivalent to select * from table in SQL. FIlter down results with FilterExpressions*. Can be very expensive & should be avoided in production apps. supports parallel scans using multi-threading. Can only return 1MB worth of data per call, extra data needs pragination. 
#DynamoDB Queries:-Queries allow you to retrive data with partition key+range key. use Rangekey's conditionExpressions to further narrow result,you can also query on global secondary indexes(GSIs),Much better performance than scans, as lookup is o(1).cost effective,but may require careful through of your schema
#DynamoDb  class(in customize settings we can see this):-DynamoDB standard,DynamoDB Standard-IA. 
#
#LoveTocode(DynamoDB with pyton):-Hands-on with python. 
#index in dynamoDB helps to accelerate app access and data retrivel.
#primary key partition key sort key (pk+sk(composite key)).
#scan cost is high because it need to read the all data to filter our needy data(it calculates read capacity unit). so use query or getitem to filter our needy item. 
#Query uses indexses. current table will have only one partition key & sort key. we have to create LSG while creating the table only after we can't create. but GSI we can create at any time. 
#GSI:-with pk & sk that can different from those in the base table. (this create the seprate table by taking our input pk & sk)  (we need to specify the different rcu & wcu from base table)
#LSI:-pk is sm as base table but sort we can add attribute as sort key. in lsg.  (this cant create a seprate table this should be down on base table)   (this uses existing rcu & wcu of the base table). (in customizes we able to create LSI) (by using this we increase the performance & decrease the cost)
#projrctions:-we can create GSI with projections when we query with GSI we can able to see only that projection attributes. (all,only keys,include)
#
#
#
#
#
#
#
#
#  
#Python data types such as Number(Integer, Float, Complex), String(""''), Boolean(True or False), (sequencial or array DT) List, Tuple, Set and Dictionary.

#Function:-is block of code designed to perform a particular task.
#OPPs concept intro in python:object orinted programming system. by using oops concept nmbr of values printed by one function name (by using this concept 1)security 2)duplicate remove 3)re usability of the existing code 4)gives good structure 5)we can hide our data by that only cls lo vunna vale access chestharu
#OPPs concepts:-class,object,inheritance,polymorphism,encapsulation,abstraction.
#class:-is a user-defined layout or blue print of an obj that describes what a specific kind obj will look like.
#object:-An obj is an instance of a cls which has properties and behaviour attached to it. 
#inheritance:-one class acquires the properties (or) attributes and methods of another class. The class whose properties and methods are inherited is known as the parent cls. and the cls that inherits the properties from the parent cls is the child cls.(single(1parent-1child),multi lvl(No.ofparent-1child,multiple(grand-parent-child),hierarchical(1parent-no.of child),hybrid(mix of multi- multiple),)
#polymorphism:-many forms and it occurs when we have many classes that are releated to each other by inheritance.(poly:many)(morphism:forms)same entity used in different forms. one has many forms. 
#Encapsulation:-is a process of wrapping code and data together into a single unit.(member variable,function,class)
#Abstraction:-is the process of only showing the necessary details to the user and hiding the other details in the background.


#palindrome:-A str is said to be palindrome if the reverse of the str is the sm as the str.
#las = "asdsa"
#w = ""
#for i in las:
#    w = i + w   
#if las == w:
#    print("this is a palindrome")         #asdsa Palindrome
#else:
#    print("this is not a palindrome")     #sagar         
#print(w)                                   #asdsa


#a = input("enter a value: ")
#c = a[::-1]
#if c == a:
#    print("this is palindrome")       #asdsa  this is a palindrome
#else:
#    print("this is not a palindrome")   #sagar  this is not a palindrome
 
#def ispalindrome(s):     #function #parameter(s)
#    return s == s[::-1]        #return
#s = "malayalam"                #assigning valu to variable
#ans = ispalindrome(s)
#if ans:
#    print("yes it is a palindrome")
#else:
#    print("no it is a palidrome")    


#finding the duplicate values from a list:-
#ay = [1,2,3,4,4,4,5,6]
#sy = []
#dup = []
#for i in ay:
#    if i not in sy:
#        sy.append(i)
#    else:
#        if i not in dup:
#            dup.append(i)
#print(sy)         #[1, 2, 3, 4, 5, 6]
#print(dup)        #[4]
"""

#finding the missing terms
lk = [1,3,7,9]
for i in range(1,11):
    if i not in lk:
        print(i,end=" ")      #2 4 5 6 8 10 
    else:
        pass   

     
#problems
#no = float(input("enter a value: "))
#if no>0:
#    print("this is a positive number")                  #1      this is a positive number
#elif no==0:
#    print("this is 0")                                  #0      this is 0
#else:
#    print("this is a negitive number")                  #-5     this is a negitive number


#nmb = int(input("enter a value : "))
#if nmb % 2 == 0:
#    print("this even")                     #20  20 this is even
#else:
#    print("this is odd")                    #5   5 this is odd

#leap year problem:-366 feb 29 4years difference.
#def checkyear(year):
#    return(((year % 4 == 0) and (year % 100 != 0 )) or (year % 400 == 0))
#year = 2004
#if (checkyear(year)):                                 
#    print("leap year")                                #2004   leap year
#else:
#    print("this is not a leap year")                  #1999    this is not a leap yeaar

#find the largest number among 3 input number:-
#l = [44,56,78,45]
#print(max(l))                   #78
#k = sorted(l)
#print(k[-1])                     #78
#l.sort()                        #decending to ascending
#print(l[-1])                         #78
#l.sort(reverse=True)              #ascending to decending (finding lowest number).
#print(l[-1])                       #44
             

#num1 = float(input("enter a value: "))
#num2 = float(input("enter a value: "))
#num3 = float(input("enter a value: "))
#if num1>=num2 and num1>=num3:
#   print("largest num is num1")           #12 8 9   #largest num is num1     12.0
#   largest = num1
#elif num2>=num3 and num2>=num3:
#   print("largest num is num2")           #12 15 8  #largest num is num2   15.0
#   largest = num2
#else:
#   print("largest num is num3")           #8 9 15   #largest num is num3    15.0
#   largest = num3
#print ("largest number is::", largest )     #largest number is:: 16.0


a,b,c = ['hello','python','family']
print(a,"sagar",b,"your",c,"welcoming you")           #hello sagar python your family welcoming you
print(f'%s sagar %s your %s welcoming you'%(a,b,c))   #hello sagar python your family welcoming you
"""
#a=4
#b=6 
#print(a+b)         #10
#k = a + b
#print(k)           #10
#y = (1,2,6,8,10)
#s = 0
#x =(4,5,6,8,9,4)
#print(sum(y+x))    #63
#haa =sum(y+x) 
#print(haa)         #63 
#m = sum(y)
#print(m)           #27
#he = x+y            #cancatation
#print(he)        #(4, 5, 6, 8, 9, 4, 1, 2, 6, 8, 10)
#for i in y:
#    s = i + s 
#print(s)


"""
import math
r = float(input("enter a value:"))    #30
area_of_circle = math.pi*r*r
circumfrence_of_circle = 2*math.pi*r
print(area_of_circle)                #2827.4333882308138
print(circumfrence_of_circle)        #188.49555921538757 """

#base = int(input("enter a value: "))        #20
#height = int(input("enter a value: "))      #10
#area_of_triangle = 0.5*base*height
#print(area_of_triangle)                   #100.0

#va = 100*365             #36500
#da = 36500*24            #876000
#hr = 87600*60*60         
#print(hr)                #315360000

#for i in range(5):
#   for j in range(i,5):
#        print("#",end=" ")
#   for  j in range(i+1):
#        print("$",end=" ")
#   print()

#a = ['Thirty', 'Days', 'Of', 'Python'] 
#r = ' '.join(a)            #list to str     (lsj)
#print(r)                   #Thirty Days Of Python  

#a = "Thirty Days Of Python" 
#k = a.split(" ")                    (sls)
#print(k)                           #['Thirty', 'Days', 'Of', 'Python']
"""

marks = [90,89,78,89,98,89]       
def get_avg(arr):         #fun with parameter
    n = len(arr)
    sum = 0
    for i in range(0,n):
        sum = sum + arr[i]
        return sum/n           
print(sum)
print('marks avg : ', get_avg(marks))

k = sum (marks)
print(k)                           #533
print(533/6)


l = [1,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,3,3,3,2,1,1,1]
ct = l.count(5)
print(ct)            #5 count in given list.


"""

"""
class student:

    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        self.age = age

    def print_id_name(self):
        print(self.id,self.name)    

v1 = student(1,'user1',20)
v2 = student(2,'user2',21)
v3 = student(3,'user3',21)

print(v1.id,v1.name,v1.age)         #1 user1 20
print(v2.id,v2.name,v2.age)         #2 user2 21
print(v3.id,v3.name,v3.age)         #3 user3 21

v1.print_id_name()                  #1 user1
v2.print_id_name()                  #2 user2
v3.print_id_name()                  #3 user3


class student:
    def __init__(self,no,first,last,age):
        self.id = no
        self.first = first
        self.last =last
        self.age = age

    def print_id_age(self):
        print(self.id,self.age)
    
    def print_full_name(self):
        print(self.first,self.last)

v1 = student(1,'user1','s1',21)
v2 = student(2,'user2','s2',22)
v3 = student(3,'user2','s3',23)

v1.print_id_age()               #1 21
v2.print_id_age()               #2 22
v3.print_id_age()               #3 23

v1.print_full_name()            #user1 s1
v2.print_full_name()            #user2 s2
v3.print_full_name()            #user3 s3


class student:    #if we need to create a obj for a cls we need to create a constructor at first.
    school_name = 'xyz school'          #static variables(used for all over the cls)
    def __init__(self,id,name):         #init function, self cls key, id,name(parameteres,arguments)
        self.id = id                    #constructor
        self.name = name

    def show_data(self):                #cls method by using this we can work with cls variables.
        print(self.id,self.name) 

student1 = student(1,'user1')          #assigning values to variables. object creation
student2 = student(2,'user2')    

print(student1.school_name)      #xyz school
print(student2.school_name)      #xyz school
student1.show_data()             #1 user1      #calling cls by obj.
student2.show_data()             #2 user2
student.show_data(student1)      #1 user1      #calling the cls by using cls name.to do that we have to  pass the obj name to it. 
student.show_data(student2)      #2 user2


class Amazon:
    overall_discount = 5                     #static variable

    def __init__(self,p_id,p_name,p_price,p_discount):
        self.id = p_id
        self.name = p_name
        self.price = p_price
        self.discount = p_discount
    
    def get_actual_price(self):
        final_price = self.price - self.price*self.discount/100 - Amazon.overall_discount*self.price/100
        return final_price

p1 = Amazon(1,'user1',100,10)
p2 = Amazon(2,'user1',100,12)
p3 = Amazon(3,'user1',100,15)

print(p1.get_actual_price())        #85.0
print(p2.get_actual_price())        #83.0
print(p3.get_actual_price())        #80.0
"""


#17)OOPs(object oriented programming system) concepts by vamshi bhavani:-                   in oops we use both (variables and functions)
#        properties                          color,age,no.of legs               color,capacity,wheels      (variables)
#Entity:-                       #(class)Parrot:-                 #(class)car:-                                              #object:-swift,swift dizer,nano,etc.,       
#        Functionalities                      fly,sing                         start,stop                   (functions())

#classes:-user defined data type(is a blue print). in this cls we create both variables and functions. object is the implementation of class. 
#class(is a key word) class name:   #(this is just syntax).
#   variables data properties
#   functions - functionalityes
#swift = car()                      #methods & functions are same in OOPs. 
"""

class person:                             #cls name 
    def SetValue(self,name,age):          #(taking values) (mathod 1)   (self is reference) (name and age is function variables (or) function methods)
        self.name = name
        self.age = age

    def GetValue(self):                 #(printing values)   (method 2)
        print("The name of the person is",self.name,"and the age is",self.age,".",sep="")
    
p = person()                           (giving input)
name = input("enter your name: ")
age = int(input("enter your age: "))

p.SetValue(name,age)      #assigning the values
p.GetValue()              #object calling         #The name of the person is sagar and the age is 24.


#18)constructors:while creating a object(or) initalization. At the sametime,if you are setting properties is known as constructors. (without creating separate function) we use constructor method.

class person:                             #cls name 
    def __init__(self,name,age):          #(taking values) (mathod 1)   (self is reference) (name and age is function variables (or) function methods)
        self.name = name
        self.age = age

    def GetValue(self):                 #(printing values)   (method 2)
        print("The name of the person is", self.name,"and the age is",self.age,".",sep=" ")
    

name = input("enter your name: ")
age = int(input("enter your age: "))
p = person(name,age)
p.GetValue()                 #The name of the person is sagar and the age is 24.


class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def student_details(self):
        print(self.name,end=" ")
        print(self.age)

s = student("Sagar",60)
s.student_details()            #sagar 60



#19)Constructors:- are 2 types 1)default __init__(self):  2)Parameterized __init__(self,name,age):   __   __(dunder methods)
#types of attributes:-      variables(data members,properties,attributes)
#                    #class
#                           function
#2types of attributes:-1)instance(object attributes) attributes.(different for every object) 2)class attributes(same for all objects of a class)
1)
class person:                    #this name and age are instance(or)object attribute.(because this is different for every object).
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def getvalue(self):
        print("The name of the person is", self.name,"and the age is",self.age,".",sep=" ")

p1 = person("sagar", 24)
p1.getvalue()                        #The name of the person is sagar and the age is 24.

p2 = person("ragas", 24)            #here we calling by objects
p2.getvalue()                       #The name of the person is ragas and the age is 24.

2)
class person:                 #this is class attribute(because this is same for all objects in the same class)
    city = "Hyderbad"          #city is same
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def getvalue(self):
        print("The name of the person is", self.name,"and the age is",self.age, "and he is from",person.city,".",sep=" ")

p1 = person("sagar", 24)
p1.getvalue()            #The name of the person is sagar and the age is 24 and he is from Hyderbad .

p2 = person("ragas", 25)
p2.getvalue()            #The name of the person is ragas and the age is 25 and he is from Hyderbad .


#20)Types of methods (or) functions in python:-1)class(static methods)(this is same for all the objects). 2)instance(this will particulaly corresponding to particular obj)(this behavior will be changed by according to the object which is calling to this function)
class person:
    city = "Hyderbad"
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @staticmethod               #this is decorator
    def Hello():
        print("Hello")

    def getvalue(self):
        print("The name of the person is", self.name,"and the age is",self.age, "and he is from",person.city,".",sep=" ")
p1 = person("sagar", 24)
p1.getvalue()            #The name of the person is sagar and the age is 24 and he is from Hyderbad .
person.Hello()           #Hello

p2 = person("ragas", 25)
p2.getvalue()            #The name of the person is ragas and the age is 25 and he is from Hyderbad .
person.Hello()           #Hello          #p2.Hello()  Hello


#21)Access Modifiers in python:- This is used to apply the restrictions. 1)public(no restrictions), 2)private(full restrictions), 3)protected(partial restrictions)
#varibles and methods used:-               __name, _name,  name (the sytax of this modifiers)                     
#with in the same class:-                private,protected,public
#with in the derived class(inheritance):-protected,public
#outside the class:-                    public

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def getvalue (self):
        print(self.name)

p1 = person("sagar",24)
#this is 1st method for accessing. (we written a function and that will print the variable)
p1.getvalue()                      #sagar
#this is 2nd method for accessing.  (we bought the variable outside the cls and printing)
print(p1.name)                     #sagar
#this is 3rd method for accessing. by using inheritance


#22)Inheritance & types in python:-  #Person(parent)-----Inheritance------>Student(child) taking the required data from the parent and re-using the code.
class person:
    age = 20
    def walk(self):
        print("I am walking")
class student(person):
    rollno = 15 
    def read(self):
        print("I am reading")       
s1 = student()
s1.read()                 #I am reading
s1.walk()                 #I am walking          #child cls can call the data from parent & student
p1 = person()     
p1.walk()                 #I am walking          #but parent cls only cl the parent data.
p1.read()                 #It wont produce the data of child.
"""
#types of inheritance:-
#1)single inheritance:-  x ---> y
#2)Multiple inheritance:-   x--        father
#                              -->z        child
#                           y--        mother
#3)Multi level inheritence:- x(grand parent cls) --> y(parent cls) -->z(child cls)
#4)Hierarchial inheritence:-
#                            -->y                      square   1
#                      x---  -->z   shape(parent cls)  triangle(2child cls) #this are siblings.
#                            -->u                      circle   3
#5)Hybrid inheritance:-the mix of multiple & multi is knowns as hybrid inheritance.
#            x-->
#                 z-->u -->v
#            y-->

#



#23)Polmorphism:-poly(many) , morphism(forms).  In this a single entity is working in many forms is knowns as polymorphism.
#a = 3
#b = 4
#c = "sagar"    
#d = "ragas"
#print(a+b)        #7   + is work as addition
#print(c+d)        #sagarragas  + is works as concatanation.
#            (here + is single entity but it took multiple entities)(this is polymorphism)

#print(len("sagar"))           #5  #each character is counted in string.
#print(len([1,2,3,4,"sagar"])) #5  #this calculte as just a element in a list.
#             (here len is a single entity but has multiple forms)(polymorphism)

#def mul(a,b,c=1,d=1):
#    print(a*b*c*d)
#mul(2,3)
#print(mul)      #6
#mul(2,3,4)
#print(mul)      #24
#mul(2,3,4,5)
#print(mul)      #120 #here we done polymorphism in functions. mul function single entity but multiple forms.

#24)Exception Handling:-
#           -->compile time error(if we have done syntax mistakes then it shows)(before running the code)
#in program    
#           -->run-time error(syntax is correct but after running the code we get any errors is known as run time errors)(after running the code)
#a =2
#b = 2
#if a == b:        #by not adding : we get compli error syntax error
#    print("it is perfect for complie error")

#l = [1,2,3,4,5]
#print("Provide the index to print")
#i = int(input())
#print(l[i])            #1 2  #6- this through error while running. and bye was not printed. after getting error the code wont perform.(this is runtime error)
#print("bye")

#handling runtime errors is known as exception 

#l = [1,2,3,4,5]
#print("provide the index to print")
#i = (int(input()))
#try:
#    print(l[i])             #by this the whole code is printed by using try & exception. 
#except Exception as e:      #6 -  list index out of range
#    print("there is a runtime error")         #there is a runtime error
#finally:
#   print("i am inside finally")    #i am inside finally
#print("bye")                       #bye (after code is also printed)

#try:-placed critical code
#except:-if exception comes what it have to do will be mentioned here
#finally:-if exception comes or not what it have to do will be said.

#25)Packages & Modules:-python files is known as modules.(example.py = example as module). Packages are folders that hold python files (or) other folders in this py files (or) folders.
# we import module by doing import function. (import example)calling(example .login())
# built-in modules:-
# math    import math as m    #print(math.pi)  #print(m.pi) 
#pip (python package manager).
#python has huge support committe.(pip install package name)  by using pip i can install module and packages. wihth the help of djungo and flask this are python development frameworks by using this we can use the code we can do backend develop.

#26)Abstraction:- is (hiding unnecessary details).(ex:-wts up,coffee m/c). Python wont support abstract clses and abstract methods directly. we bring it in python by using modules.
#1)Abstact classes method:-    (here vehicle is Abstact classes)
#2)Abstract method method:-    (here no.of wheels,def start,def stop is Abstract method)
"""
from abc import ABC, abstractmethod

class vehicle(ABC):        #vehicle is abstract class.
    @abstractmethod
    def start(self):
        pass

class car(vehicle):        #car will be inheritance from vehicle.
    def horn(self):        #horn is a method
        print("Horning..")
    def start(self):
        print("Starting..")
c = car()                 #creating a object to a car      starting printed.
c.start()                 #Starting
c.horn()                  #Horning 
""" 

#27)File handling:- modes(r-read,a-append,w-write,x-create)file(t= text file,b= binary file). 
#we can call from one file to another file(bcz file has modes r-read,a-append,w-write,x-create). 
#f = open ("example.txt","rt")                 #this code is written in day27 file and calling this file in terminal and this open the example.txt file according we given mode.
#print(f.read())
#f.close()

#28)Python module index &pypi
#modules:-1)built-in(direct import ex:-data time,regular expersion)(python module index(we get the bulit-in module))    2)published(django)(pypi.org)(when py developers do something new if that is use for another ressources then they will publish there module))

#29)py project problem statements:-
"""
from random import randint
def random():
    while True:
        n = str(randint(100,999))
        if not(n[0] == n[1] or n[1] == n[2] or n[0] == n[2]):
            return n

name = input("welcome to the cow and bull game\nplease enter your name.")
print("Hi name")
chances = 5
cows = 0
bulls = 0
num = str(random())

while chances>0:
    print("you have",chances,"chances left.")
    n = str(input("enter your guess"))
    if num == n:
        print("great! you git it right.") 
        break
    else:
        for i in range(0,3):
            if n[i] == num[i]:
                bulls = bulls +1
            elif n[i] in num:
                cows = cows +1
            print("keep going.you have",bulls,"bulls and",cows,"cows.")
            bulls = 0
            cows = 0
            chances = chances -1
print("the correct answer is",num) 


#print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")         Basic ryme

k = '''Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are'''

print(k)


#def print_pattern(rows):                                      #1 1 1 1 1
#    for i in range(1, rows + 1):                              #2 1 2 4 8
#        print(f"{i} {1} {i} {i**2} {i**3}")                   #3 1 3 9 27
                                                               #4 1 4 16 64
                                                               #5 1 5 25 125 
#print_pattern(5)
"""
"""
a = (10)
b = (20)
print(a+b)        #30

c =(1,2,3,4,5,6)
d =(1,2,3,4,5)       
print(sum(c+d))   #36

e = (1,2,3,4,5,6)
f = (1,2,3,4,5)
print(e+f)      #(1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5) concatnation

i =[1,2,3,4,5]
print(sum(i))

la = [10,20,30,40,50]
s = 0
for i in la:                        
       s = s + i
print('answer : ',s)                     #150 sum of all

name = input("enter a value: ")
print("greeting massage with",name)

import math
p = math.pi
print(p)

is_raining =(input("enter a value: "))
if is_raining == True:
       print("The data type of the converted boolean")
else:
       print("The data type of the converted boolean")

sk=[1,2,3,4,5,6,1,2,6]
sn =[]
du =[]
for i in sk:
    if i not in sn:
        sn.append(i)
    else:
        if i not in du:
            du.append(i)
    

print(sn)                 #[1, 2, 3, 4, 5, 6]
print(du)                 #[1, 2, 6]

sentence = (input("enter a value: "))
k = sentence.split()
n=int(k)
o = []
x = []
for i in n:
    if i not in o:
        o.append(i)
    else:
        if i not in x: 
            x.append(i)
print(o)
print(x)

value=123
value=input("enter a value: ")
print(value)

k=(8+4)*3/2+12-12  #this is followed by BODMAS:-
s=10+3*2-8/9
print(s)  #15.11111111111111
print(k)  #18.0
    
a = "sagar loves" + " python" #string concatanation. 
print(a)                      #sagar loves python
b = "sagar" + " " + "ragas"   #sagar ragas
print(b)

str1 ="Hello"
str2="world"
s = str1+str2         #concatanation.
print(s)      #Helloworld

name=input("enter a value: ")
print("Hi",name)                   #Hi python

word ="python"
print(word * 5)            #pythonpythonpythonpythonpython

k = input("enter a value: ")       
w =int(input("enter a value: "))    #python 3
print(k*w)                    #pythonpythonpython

k = "this is sample sentence"             #23
s = ["this is sample sentence"]           #1
print(len(k))
print(len(s))

s = 42
print(type(s))           #int
k = str(s)
print(type(k))           #str

n = "123"
print(type(n))           #str
m = int(n)
print(type(m))           #int

k ="The sun is shining"
print(k[0])      #T
print(k[0:7])    #The sun
print(k[-1])     #g
print(k[:-1])    #The sun is shinin
print(k[-1::])   #g
print(k[2])      #e
print(k[-2])     #n
print(k[4:7])    #sun
print(k[-7:-3])  #shin
print(k[::-1])   #gninihs si nus ehT                    #arthematic(+-), conditional(==,!=), logical(and,or,not), bitwise(& | xor) 

a = 10
b = 20
if a < b and a >= b:
    print("True")
else:
    print("False")           #and (False)  #or (True)

a = 10
b = 5
c="apple"
d ="APPLE"
if a>b or c==d:
    print("True")        #True (!=)       #True (!=)
else:                        #and            #or
    print("False")       #False(==)       #True(==)


a= 10
b= 20
print(not(a>=b))   #True

k = int(input("enter a value: "))
if k % 2 ==0:
    print("even")          #52
else:
    print("odd")           #53


k = int(input("enter a value: "))
v = int(input("enter a value: "))
if k > v:
    print(k,"if")               #21,12   21 if
else:
    print(v,"els")              #12,21    21 els


#nested if condition:-
x = 10
if x > 0:
    print("this is a positive number")    #10 0     this is a positive number    this is even
    if x % 2 ==0:
        print("this is even")
    else:
        print("this is odd")
else:
    print("x is not positive")          #13 20   #x is not positive


l = 10
if l > 0:
    print("positive")
    if l % 2 == 0:
        print("even")                #10 positive  even
    else:
        print("odd")                 #19 positive odd
else:
    print("negitive")


#card = (input("enter a value: "))
#if len(card) == 16:
    #print(12*'#'+card[-1:-5:-1],end=" ")      #1method        ############4444
    #print(12*'#',end="")    
    #print(card[12:])                          #2nd method     ############4444
    #print(12*'#'+card[12:])                   #3rd method     ############4444
#else:
#    print("Invalid")

from random import*
for i in range(10):
    print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep="")


#chat Bot:-creating a chat bot by using Amazon Lex.
#Chatbots are among the most popular uses of artificial intelligence. 
#They allow companies to enhance customer experience and reduce costs. 
#There are many types of chatbots present, and they all perform different tasks. 
#A chatbot is an application that conducts a conversation with someone else in the place of a person. 


#mon wed fri 1hour zoom link sended.

#1)#Prime nmbr(1 to 200)
for num in range(1,200):
    if all(num%i != 0 for i in range(2,num)):
        print(num)              #this prints 1 to 200 prime numbers

n = int(input("enter a value: "))
for i in range(2,n):
    if n % i == 0: 
        print("not prime")                #22 not prime
        break
else:
    print("prime")                             #7 primme

#2)l = [64,25,12,11,1,2,44,122,23,34]
s = sorted(l)
print(s)            #[1, 2, 11, 12, 23, 25, 34, 44, 64, 122]
l.sort()
print(l)           #[1, 2, 11, 12, 23, 25, 34, 44, 64, 122]
l.sort(reverse=True)
print(l)           #[122, 64, 44, 34, 25, 23, 12, 11, 2, 1]

#3)data = [24,55,78,64,25,12,11,1,2,44,3,122,23,34]      #without using sort functionalite
new = []
while data:
    minimum= data[0]
    for x in data:
        if x > minimum:
            minimum = x
    new.append(minimum)
    data.remove(minimum)
print(new)                 #[122, 78, 64, 55, 44, 34, 25, 24, 23, 12, 11, 3, 2, 1]

def F(n):                              #fibonacci series:- is the meaning of adding 1 & 2 we get 3nmbr. 3 & 4 we get 5nmbr. 
    if n == 0: return 0                  
    elif n == 1:return 1
    else: return F(n-1)+F(n-2)
for i in range(0,12):
    print(F(i))                    


fruits =  ['banana', 'orange', 'mango', 'lemon']
k = fruits.sort
print(k)                      #['lemon', 'mango', 'orange', 'banana']
#fruits.sort(reverse=True)
#print(fruits)                #['orange', 'mango', 'lemon', 'banana']
s = fruits[::-1]
print(s)                     #['lemon', 'mango', 'orange', 'banana']
a =[]
for i in fruits:
    a.append(i)
print(a[::-1])              #['lemon', 'mango', 'orange', 'banana']
"""
