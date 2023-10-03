#Logical representation for flow of Data:-
#                               (job runs)    storess only2days data  (1,3,5,10,30,60min)    (updated data)          jobs running twice/day
#Info pro system(Source system)--------------------->Landing zone-------------------------->Operational database(ODS)------------------------->PS/STG Environment
#                               (continously)            |              frequent jobs                      |             8pm & 1am AZ                 |
#                                                        |                                                 |                                          |
#                                                        |                          part of jobs processing|                     jobs running once/day|
#                                      Daily running job |10.11pm.AZ           data directly to core tables|                    -----------------------                               
#                                                        |                                                  -----------------> | 1am AZ(ETL Load)
#                                                        |                                                                     |
#                                                    LZ Archival                                                  Core Tables Dimensions & Facts         
#                                    (data will be processed continously from LZ to LZ 
#                                               archival,as it stories allthe data)                                                                
#


#Modern data Architecture(MDR):- in this we have 2 Architecture v1(here we using 2 Lambdas) and in v2(we eliminated 1 lambda and carrying forword with one lambda)
#
#MDR (V1):-
#Data from info pro---->Getting data from informatica---->(raw data)S3----->SNS--->SQS---->Lambda---->(formated data)s3---->SQS------>lambda---->snowflake(staging area) snowflake(ODS schema) snowflake(core schema) 
#MDR (v2):-
#Data from info pro---->Getting data from informatica---->(raw data)S3----->SNS--->SQS---->Lambda(s3 to snowflake)---->(formated data)s3---->snow pipeline---->snowflake
#


#Winscp
#putty
#CDH

#AWS                                (IDMC:-intelligent data management cloud)
#informatica power center(youtube) (IICs:-informatica intelligent cloud service):-Informatica PowerCenter is an ETL tool that is used to enterprise extract, transform, and load the data from the sources. We can build enterprise data warehouses with the help of the Informatica PowerCenter. The Informatica PowerCenter produces the Informatica Crop. The Informatica PowerCenter is extracting data from its source, transforming this data according to requirements, and loading this data into a target data warehouse.The main components  are client tools,server,repository,and repo server. designer,workflow,monitor. 
#informatica cloud(youtube):- Intelligent Data Management Cloud, designed to help businesses innovate with their data on any platform, any cloud, multi-cloud, and multi-hybrid.
#Terraform:-Is an infrastructure as code tool that lets you define both cloud and on-prem resources in human-readable configuration files that you can version, reuse, and share. You can then use a consistent workflow to provision and manage all of your infrastructure throughout its lifecycle. Terraform can manage low-level components like compute, storage, and networking resources, as well as high-level components like DNS entries and SaaS features.
#MS SQL(Youtube):-SQL is a standard language for storing, manipulating and retrieving data in databases.
#snow flake:-Snowflake is a cloud-based data warehousing platform that is built on top of AWS and is a true SaaS offering. In contrast with traditional data warehouse solutions, Snowflake provides a data warehouse which is faster, easy to set up, and far more flexible. With its unique features, it soon became a leader in data management solutions for analytics.
#Denodo (Sai following some KT sessions I have to follow him):-The Denodo Platform, powered by data virtualization, is a logical data integration, data management, and data delivery solution that provides a centralized data access layer that enables all users to find, query, integrate, and securely share datasets, in real time, with breakthrough cost-effectiveness. This enables organizations to acquire timely, trusted, integrated datasets for faster analytics and informed business decisions. 
#A part from that I have to attend the meeting with Dillip for AWS
#And From Santhosh I have to follow what is the working process.






#serviceNow Tool:-This is one cloud based service management tool.(used for giving access,Ticketing Tool or incident management(is a integral part of every (CRM Customer relationship management))(got any query that request is forwording to organization throught email notification if i.e, valid reason organization approve & respond(ex:1)forgetten password,2)customer service productivity)))

#In infrormatica we have 4 client tools inter connected with each other: 1)Repo manager(R),2)Designer(D),3)Work flow(W) & 4)Monitor(M)).
#1)Repository Manager(R):-Admin Realated task.(Folder creation/deletion.access/priveledges.Code migration(xml import/export). Historical run status)
#2)Designer(D):-Developer(Source Definition. Target DefinItion. Mapping(Business Logic))
#3)Workflow Manager(W):-Is used to create a session,connections & work flow in work flow manager.  
#4)Workflow Monitor(M):-Run status(running/succeeded/failed/aborated/stopped). Run count(source/target). Throughtput(record/sec). session log-imp.  (we can see the work folw in gantt chart or Task view). get session log we can see ERROR.  

#5 component of Designer:-
#1)Source Analyzer:-Source Definition(Relational DB table.Flat files(txt/csv).Cobol.Xml files).
#2)Target Designer:-Target Definition(Relational DB table.Flat files(txt/csv)Xml files)
#3)Transformation Developer:-(if the single transformation can be used in multiple mapping is called reusable transformation)(Filter Transformation,Update strtegy transformation,Expression transformation,Aggregator transformation,Lookup transformation,Joiner transformation,Mapplet input,Ranker Transformation,)
#4)Mapplet Designer:-Is also used to create reusable component(Reusable Transformation,Set of transformation - to create a reusable logic,can be re-used in multiple mapping). 
#5)Mapping Designer:-(we create Business logic:Mapping)(here we can see source & target).    Source defination--->source qualifier(converts source Datatype into informatica day to day data type)--->target Defination. 

#3 components in workflow manager:-used to create sessions,connection, & work flows. 
#Task Developer:-session(reusable session). connections definition. single reuseable session. 
#Worklet designer:-Re-usable component. session lvl. set of sessions.
#Workflow designer:-session (non-reusable session). workflow
 
#steps to create a workflow:- 
#1)Source Defination -Source Designer -Designer D 
#2)Target Defination -Target Designer -Desinger D 
#3)Mapping -Mapping Designer -Desinger D                 #this 3 things we have to do in designer
#4)session(reusable) -Task Developer -Workflow Manager W 
#5)ConnectionsB -Task Developer -Workflow Manger W
#6)Workflow -workflow Designer -workflow Manger W 
#7)Monitoring -working Monitor M
 
#Naming conventions:- 
#Mapping:-m_Table_name   ex:m_Employees_Details 
#Session:-s_mapping_name ex:s_m_Employees_Details 
#WorkFlow:-WKF (or) WF_session_name ex:wf_Eployees_Details 
#Mapplet:-mplt (or) ml 
#worklet:-Wklt (or) wl
#Demension table:-dim_ (or) d_ 
#Fact Table:-fact_ (or) f_ 
#view:-table_name_v 
#Materialized views:-table_name_mv      (this naming conventions is different from project to project but this are standard one). 

#Informatica Full course(infromatica powercenter transformations(Nic IT Academy)):-informatic power center is ETL tool this handle huge volume of data support,and failover mechanism is also high(falut tolerance is high).
#Informatica powercenter 10.4 installation steps:-we have 9 steps
#System reqirements - for informatica installation:-50GB space,Windows 8/10/11 -64 bit OS,6GB RAM/8GB RAM. 
#oracle 11g xe(is a sowfware or Database)(on top of it):-1)in built user called(system) is a schema) 2)we create schema (infa(for informatic repo) 3)in built user called(HR)is a schema)                 4)we create schema(core(for target)      we can aslo move data from hr to other DB. 
#                                                             un:system,pw:admin |                 un:infa,pw:infa         |               un:hr,pw:hr                  |B/w HR & core we use informatica for transfering data| un:core,pw:core                                        
#                                                                      oracle metadata tables          informatica metadata tables(repo)                         source(employees,locations,deps)                     Target(t_employees,customer,prods)
#for querying oracle 11g xe(DB)we have to use (SQL Developer(GUl)) This is connected by connections
#Extract the folders by using winrar or winzip.  
#Install Oracle 11g(as informatica repo)
#configure SQL developer(GUI tool,source & Target DB) give the connection b/w SQL developer to Oracle Database.  + ADMIN,system,admin(user) connect.we need hr schema unlock from ADMIN schema(alter user hr identified by hr account unlock;).+ HR,hr,hr,connect(for source). from admin(create user core identified by core; grant dba to core;) +CORE,core,core,connect(target). in admin(create user infa identified by infa; grant dba to infa;)+INFA,infa,infa,connect(infa repo).    in infa & core dont have any tables. 
#Now we are creating a table in core from ADMIN (create table core.t_employees as select * from hr.employee where 1=2;)by this we create a table in core(select * from T_employees;)(consist sm schema HR CORE) that which is used to transfer the data from HR(select * from T_employees;)we can see data here & moved to CORE. 
#Now install informatica powercenter server. In this enter DB information for the domain configuration repo. connection will be created. Informatica pinging the oracle DB for repo creation. After we can go to informatica Adminisatrator access. user:Administrator,pw:Administrator,log in.  #goto services & notes we can see IS(integration srvc),REP(repo srvc)
#Now instaall informatica client(hvaing 1of2)
#Now configure source & target connection.  for moving of Data hr to core. Now open powercenter Repo manager(in this we have 4 client tools inter connected with each other: (1)repo manager,2)designer,3)work flow & 4)monitor). Goto repository and add repo(REP),configure domains,dname:domain,localhost,port:6005.ok.click,connect,informatica un:Administrator,pd:Administrator,connect. create a floder Training,ok.goto designer. Now clients are inter connected. click training,open. 1st define sources,import from DB. give to connections ODBC 1)Oracle_Src & 2)oracle_Tgt,choose the source connection hr,HR,hr,connect. Take the employees table,ok. now goto the targets,import from DB,Oracle_Tgt,core,CORE,core,connect,go inside,ok. (target table is imported here)
#Now create mapping:m_Test_mapping,ok. Drag and drop (Oracle source,Employees source,T_employees Target(on right-hand side)).After goto Work flow.goto connection relational connection, new,source Oracle,ok,hr,xe,ok. now target new,Oracle,ok,core,core,ok,xe(we created both connections). Now goto the workflow designer create a work flow name,ok. click on session icon,choose test mapping ok, click on link task(link it),Double click on mapping goto mapping choose the target pointing to the Oracle_Tgt,go down Tick Truncket & target table option,ok,apply. control+f (for testing).write click on white space(start work flow). Now Monitor automatically opened. goto task view,click session,get run properties,goto source & targets. Now goto core and(select * from T_Employees;)we get the data in Target(core schema)from HR schema to core schema data is loaded.
# 
#Different types of Data Load:-  converting
#1)Table to table (load the data from Table to Table)
#2)Flat file to Table(load the data from FF to Table) 
#3)Table to flat file(load the data from Table to FF) 

#3)Table to falt file:- (Table to FF)2:48time         (ctrl+s(is used to validity the mapping))

#How to genrate file with dynamic file name:-2:48time     'T_FF_Employees_' ||To_CHAR(SYSTIMESTAMP(),'MMDDYYYYHH24MISS')||'.csv'            (|| concatanation ||)

#2)Flat file to table:-(load the data from FF to Table) 3:07time  (Extrans Expression)

#Transformation:-Is used transform the data from one format to another format. 
#Active Transformation:-A transformation does change the no.of records passed throgh it. (also changes the Row no.of the reccord)  10(source)-50(destination like that)
#Passive Transformation:-A transformation does not change the no.of records passed through it.  
#Connected:- The Transformation will be in pipeline  
#Unconnected:- The Transformation will not there in pipeline. (stored proceduree,Lookups) this is stand alone. 

#Source Qualifier Transformation(this is the very 1st transformation):-An Active,connected (It converts Source Datatype into Informatica native data type).     Source Defination(numbr,date)-->Source Qualifer(decimal,Date & time)-->Extenstion. 
#properties of source Qualifier Transformation:-
#select all_columns from table_name:
#1)SQL query:-Sql override,-->by writting sql query, we can filter/restrict the data from source itself. 
#2)User defined join:-Hemogeneous join - tables from same type of data base 
#3)source filter:-filter condition (salary is not null)
#4)select distinct:-enable/disable  (full row duplicate)
#5)pre-sql:-SQL,before data fetch (ex:-index creation in source)
#6)post-sql:-SQL,before data fetch (ex:-index drop in source)
#7)No.of sorted port:2 (1,2)
#8)Tracing lvl
#9)output id depremistic
#10)output is repeactive 
 
#if the source is flat file then all the above properties are disabled.  
#session log(analysis):-In this we can see 3Threads 1)Reader(read the data)(source side),2)Transformation(transform the data from one format to another),3)Writer(write the data into target table)(target side).  
# 
#SQL query:-
#we can write the query in source qulifer properties level to filter the data & only that data is transfered to target lvl. in mappping (session lvl properties if can get that query & we can edit it again in to filter out more). informatica give the prefrence to session lvl queries will be excuted. (3:30) 
#Select Employees Employee_id,Employees First_name,Employees Last_name,Employees Email,Employees Phone_number,Employees Hire_date,Employees Job_id,Employees Salary,Employees Commission_pct,Employees Manager_id,Employees Department_id from Employees where Commission_pct is not and salary>9000         (this query will improve the performance DB)     This query is mentioned source qulifer level(mapping lvl). 
#Select Employees Employee_id,Employees First_name,Employees Last_name,Employees Email,Employees Phone_number,Employees Hire_date,Employees Job_id,Employees Salary,Employees Commission_pct,Employees Manager_id,Employees Department_id from Employees where Commission_pct is not and salary>10000         (this query will improve the performance DB)    This query is mentioned session level properties.(session lvl) (if we mention both the queries the session level will be excuted)  
#if we remove session lvl query it gng to show the total data. like (select * from employees)

#source filter:- 
#If we excuted of source qualifier then informatica gng write the session lvl properties for what we have mensioned in source qualifier.   this is source filter.   (Employee job_ID='SA_REP')   
#we use properties of source Qualifier Transformation in this.  

#No.of sorted port:-
#This will written order by cluse(1,2,3) like that. 
#If we excuted of source qualifier then informatica gng write the session lvl properties for what we have mensioned in source qualifier. 

#User defined join:-
#oracle employees:employee_id,department_id 
#                                                             source qualifier:join condition(employees.department_id = departments.department_id),filter condition(department_name='finance')            t_employees_dept (target table):employee_id,department_id,department_name,location_id
#oracle department:department_id,department_name,location_id


#Filter Transformation(appear as 'funnel'):-An Active, connected.  (same like SQL) we can use any were in the pipeline.  
#SQ Filter: This Filter Source itself  
#Filter Transformation: is used to filter out record any where in the pipeline. 
#properties:
#Filter condition:
#True-- It will pass all the record
#False--It will block all the record
#Condition--Passes-->Satisified record
#If it is a flat file we cant use source qulifer filter.(for ff The source qulifier properties are disabled)
#we can use filter transformation and we bring out data(s+SQ+filter(lower(country)='india' AND salary>50000))

#Expression Transformation(it will not filter out any record)f[x]:-Passive, connected (Business logic)
#
#               Input(port)   Output(port)   Variable(port)       expression(not a port)
#Salary             10000       10000                           (if we enable both we cant change any write the expression)
#New_Salary                     11000                           (Salary+(Salary*0.1)) (here we used for salary increment like that)
#Variable:Intermediate calculation -- you can't take variable port as output.  
#V_c=a+b;       (v= variable)
#o_c=v_c        (o= output) 
#e=d+v_c;       (e= intermediate calculation)
#order of excution:-1)Input,2)Variable,3)Output       (cant filter record in expression transformation --passive)(we will do some logic & expression we get idea)
#
#select employee_id,salary from core.t_employees
#minus
#select employees_id,salary+(salary*0.1)from hr.employees;       query used in Admin table for accessing data from core table. 

#If conditions in informatica:IIF(condition,true,false)
#expression logic:
#IIF(salary<=10000,salary+(salary*0.2),salary+(salary*0.1))    (by using we can add 0.1 and 0.2% to employees)
#select employee_id,salary from core.t_employees    (this shows the data in core table)
#Testing:Minus query
#select employee_id,salary from core.t_employee
#minus 
#select employee_id 
#case when salary <=10000 then salary+(salary*0.2) 
#else salary+(salary*0.1) end salary from hr.employees;             (when ever opening the case we have to close with end)
# 
#expression logic:-
#IIF(salary<=5000,salary+(salary*03),IIF(salary>5000 and salary <=10000,salary+(salary*0.2),salary+(salary*0.1))) 
#Testing:Minus query
#select employee_id,salary from core.t_employees 
#minus 
#select employee_id 
#case when salary <=5000 then salary+(salary*0.3)   
#when salary > 5000 and salary <= 10000 then salary+(salary*0.2) 
#else salary+(salary*0.1) end salary from hr.employees;
 
#Joiner Transformation:-  (more used in real time project)  here we are using 2 different tables 
#oracle employee:-emp_id,department_id
#                                                  source qulifier         Target table: Detail,join type,join condition(employees.department_id=departments.department_id)                                                  source qulifier         Master
#FF department:-department_id,department_name,location_id
#
#1 table is detail table and 2 table is master table.
#1)Normal join:-inner join(matching record from the both table)
#2)Master outer:-left join(all the record from detail & matching record)
#3)Detail outer:-right join(all the record from master & matching record)
#4)Full outer:-full join(matching and non matching records)
#
#small table==>Master table==>bcz informatica takes cache(less sapce occupied (increas the proformance))
#n sources==>n-1 joiner
#
#Sorter Transformation:-An Active,connected
#IN SQL: Order by (either by ascending or desending)
#select * from employees order by salary;          (this shows ascending order)
#select * from employeea order by salary desc;     (this shows descending order)
#select * from emloyees order by salary desc, hire_date;      (this shows descending order)
#select * from employees order by commission_pct desc;             (Null treated as highest value by default so it displayed on top)
#
#IN Informatica :Sorter(indicated by A to Z)
#           input      output        key    direction
#salary      *           *            *      (desceding)
#hire_date   *           *            *      (ascending)     
#Here we can select more then one key port in sorter
#Properties:
#distinct:-To remove duplicate record from sorter        (we have distinct option in source qulifer(select from source itself) & sorter(pipeline lvl))
#source ff(duplicate) + SQ cant use sq distinct + sorter (use distinct)
#This works on Case sensitive.     Null treated as low:enable 

#Aggregator Transformation(Appear as 'M' from side):- An Active,connected        adding:- (aggregate function(sum) is used for colum(|) lvl total marks in maths).  (if row((-) lvl we have to add go with expression (select(maths+phy+chem+bio+)total_marks,(maths+phy+chem+bio)/4 Avg_marks from students))
#min(),max(),sum(),avg(),count()                   
#irrespective of no.of record -->you will get only one record in output           (in expression we dont have folder but in aggregate we have a folder)
#                             -->last record will get aggregate value. 
#Group by:- sum(salary)   group by department_id
#properties:-sorted input(if we are using group by port then we have to use this):enable     (Aggregator==>sorted input+aggregation)
#performance:sorted input,incremental aggregation. 
#select department_id,sum(salary) from employees group by department_id having sum(salary) > 50000 order by1;
#
#Exercise:- At 5:58 (hands on)

#Router Transformation(it appears like this(->=):-An Active,connected. (Router transformation used)single source pipeline to multiple pipeline. default grroup. multple filter in single transformation.   Upper(country='INDIA')
#Employee_country(table)-->Router Transformation(Input|'india'|'UK'|'USA'|Default)-->India|UK|USA|Default target table. 

#Exercise:-At 6:22(hands on)

#Rank Transformation(appreas like bar graph):-An Activity, Connected  (Rank on only one column)
#           input      output       rank       group by
#Salary      *           *            *
#Department_id                                   *
#
#In SQL Rank: rank() over(order by salary desc)rnk          (in sql we write the query to get data but in informatica we just enable the port that write the queary for us).
#
#properties: Top/Bottom: Top     No.of Ranks:5   (we cant do dense rank by using Rank transformation,instead we can do by using expression transformation). 
  
#Sequence Generator(appears 1 2 3):-Passive, connected. Auto increment number.
#                   Nextval       1 2 3 4 5 6 7 8 9 10  (in this start value:1. increment by:1. end value:4. cycle:enable. reset:enable). 
#Sequence Generator:-
#                   Curval    nextval+1
#Properties:
#Start value:100000000. Increment by:1. End value:921423423353544454. current value:10000000. cycle: enable/disable. reset: enable/disable. Number cached values: 100. 
#To Generate surogatr key,unique key--->Sequence Generator. 
#select * from employees_hist   (shows the history data)

#Union Transformation(opposite to router (many to single))(appered as 'u'):-Active ,connected. (Same structured table. Heterogrneous source).
#In Informati-> Union acts as union All-->it will not remove duplicate.   Union-->union + sortter(distinct)
#Exactly opposite to router. Multiple pipeline input-->single pipeline output.             (2 different tables we can do join.  same structure table we can use union)  if we to remove duplicate from the table use soter & distinct. 

#Lookup transformation(An Active)(appears as 'mignifer in doc'):-Lookup transformation is used to retrieve data based on a specified lookup condition. For ex, you can use a lookup transformation to retrieve values from a DB table for codes used in source data.    7:00       (To do Lookup as Active Transformation we have to enable Lookup policy return all values on multiple match) that is avaliable in propeties 
#Types of Lookup transformation:1)connected Lookup(It will be in the pipeline)(has input port,output,lookup,return)  2)Unconnected Lookup(it will not be in pipeline). 
#IN Joiner Transformation will do the joining but joiner need to have the joining column in the sourcce side. 
#IN Lookup Transformation we can have the lookup table either in source or target or we can import newly. 
#
#Connected Lookup:                                                      LKPTRANS:Departments(department_id,department_name,location_id,in_department_id) 
#Eployees_table(source)(Employee_id,department_id)--->Source qualifier |                   ------>                                                      | T_Employees_dept(target)(Employee_id,department_id,department_name,location_id)            
#we can change lookup as inner join by using (lookup and filter we can change)   Here we have to provide connection Lookup table. 

#Unconnected Lookup:-(it will not be in pipeline). In this expression transformation is manditory
#LKptrans:departments(department_id,department_name,im_department_id)1 & 3join and 2is return port.   LKTRANS:departments(department_id,location_id,in_department_id)1 & 3join and 2is return port. 
#Employees(Employee_id,department_id)-->source qualifer-->Expression transformation(employees_id,department_id.(lkp.lkptrans(department_id),o_department_name,(:lkp.lkptrans1(department_id),o_location_id)-->T_Employees_dept(employee_id,department_id,department_name,location_id)-->T_employees_dept(employee_id,department_id,department_name,location_id)

#How to return multiple columns from unconnected lookup?
#This query used in SQL: select department_id as department_id,Department_name||'~'||location_id as Department_name_Loc from department;
#We have to use this in Lookup  (convert the query into upper case)   in properties Lookup Sql Override(paste the query) ok 

#Lookup policy on multiple match:-
#Source:(20)-->Lookup Table:(10 HR,20 Admin,30 Insurance,40 Finance,20 Sales) 
#Use any value(default),use first value,use last value,report error - sessin failed.  lookup import_____ return all values on multiple match(20 Admin 20 Sales).

#11)Joiner                                                                                                                 Lookup
#A joiner is used to join data from heterogeneous sources.                                                 #Lookup is used to get related values from another table or check for updates etc in the target table. 
#Joiner has inner,left,right,full outer joins.                                                             #Lookup is left outer join
#Joiner joins source table only                                                                            #Look up used to source as well as the target and source qualifer. 
#It may used only the "=" operator.                                                                        #It may used =,<,>,<=<>= operatoes
#In joiner may be not present in Lookup override.                                                          #It may be present in the lookup override option.
#Data cache & index is used in joiner.                                                                     #Different caches(like presistent,dynamic)are possible in lookup transformation which improves performance.
#Joiner is used for joining 2 homogeneous or heterogeneous sources residing at different locations.        #Lookup is used to look-up the data.
#Joiner is an Active Transformation                                                                        #Lookup transformation is a Passive,Active transformation. (if we enable)
#joiner is always connected                                                                                #Lookup has both connected as well as unconnected. 

#in real time we cannot do w(Truncat) for all tables. Only staging table we can do truncat & load.  

#12)Update strategy Transformation(appers as 'note pad with pencil') with SCD(slowly changing dimension)-type-1 implementation: An Active, connected    
#(dd-data driven) dd_insert 0, dd_update 1, dd_delete 2(instead of delete, we will soft dlt --inactive), dd_reject 3.   #note:2 & 3 we use very rare case mostly we use 0 & 1. 
#To use update strategy we need to have (Target-->Primary key). 
#Inset_flag:-IIF(ISNULL(lkp_cust_id),true,false)
#update_flag:-IIF(cust_id=lkp_cust_id1 AND(cust_name!=lkp_cust_name OR email_id!=lkp_email_id1 or mobile_no!=lkp_mobile_no1 or city!=lkp_city1 or country!=lkp_country1),tue,false)

#13)Normalizer(appers 'hook'):-An Active,connected Transformation. it  converts row--->column.        (this transformation we you very rarely)
#Transpose the data(SQL:pivot unpivot)
#cobol source==>VSAM file==>Instead of SQ. Normalizer will be used. 
#GK:-generated key value        (this are automatically created)
#GC ID:-generated column value  (this are automatically created)    
#In Normalization we can not copy the column to this transformation. instead of copying we need to create that column.  In this we have 3 data types(number,string,nstring)

#14)Transaction control Transformation(appers like 'pepsi' symbol):-An Active,connected. Dynamic file in target.  (instead of Router transformation we will use Transaction control Transformation)
#SQL:TCL:  commit,rollback
#Informatica:-TC_COMMIT_BEFORE,TC_COMMIT_AFTER,TC_ROLLBACK_BEFORE,TC_ROLLBACK_AFTER,TC_CONTINUE_TRANSACTION-DEFAULT.
#Dynamic file in target. 
#Employees_country(names)-->Source Qualifer-->Sorter(1,0,1)-->Expression transformation(1,0)-->Transaction control transformation(1-commit before,0-continue txn-->Target table(names are segrated)

#15)Java Transformations(appear like 'tea cup'):-This provides a simple,native programming interface to define transformation functionality with the java programming lang. 
#If Activ, the transformation can generate more than one output row for eachinput row.
#If passive, the transformation generates one output row for each input row. 
#string str = mobile_number;
#string [] temp;
#string delimiter = "~"
#temp = str.split(delimiter);
#for(int i=0;i<temp.length;i++)
#{
#o_cust_id=cut_id;
#o_cust_name=cust_name; 
#o_dob=dob; 
#o_mobile=temp[i]; 
#grnerateRow();             (then compile it ava at down)   and fullcode we can see. Java transformation will import all the packages.   apply.    Here we can mention encryption and decryption logics.        
#}

#15)SQL Transformation (appers like 'SQL'):-An Active, Connected   (Instead of Joiner, Lookup(takes lot of memory bcz it take cache memory))     in this transformation we have Query mode & Script mode 
#SQL Transformation is used to process SQL queries in the midstream of a pipeline. 
#we can insert,update,delete & retrieve rows from the DB at run time using the SQL transformation. 
#1)Data definition statements:-(create,alter,drop,truncate,rename)
#2)Data manipulation statements:-(insert,update,delete,merge) 
#3)Data retrieval statement:-(select)
#4)Data control lang statement(grant,revoke)
#5)Transaction control statements(commit,rollback)

#Debugger:-step by step execution of the transformation flow.  (in mapping we will find this term debugging). use an existing session instance. (ins = transformation). in this we can see current ins and target ins.  we have to debugger (f10)next instance then it move one ins to other.  in this we have break point concept (instead of sending one by one to target by using this we can select one other than that every thing is moved to target tabel. after we can send one). 
#session is failed - session log
#session is succeeded -
#                   expected output-1000
#                   actual output-null

#prameter & variables:-parameter filreover view & significance in powercenter. parameter file structure. configuring the parameter files in workflow & session. use mapping parameter & variable to make mapping more flexiable. mapping parameters & variables represent values in mappings & mapplets. use mapping parameter & variables in a mapping to incrementally extract data. 
#$$:-Mapping lvl parameter
#$:-Session lvl parameter
#$PMSourcefileDir\ = cd drive informatica. 
#Parameter:-It will not change the value during run time.  $$salary=10000 
#Variable:-It may change the value during run time         $$count=$$count+1
#Global:-Any session any parameter can read that.      (All integration srvcs,integration srvc processes,workflows,worklets,& sessions)   [folder name. WF:workflow name.ST:session name]
#Local:-particular to the perfect session. (foldername,sessionname).   

#!/usr/bin/bash
#sample pmcmd script
#Assigning workflow variables:
#PM HOME=<INFA PATH>
#INF_server=<INFA SERVER NAME-DEV/UAT/PRD>
#INF_domain=<INFA DOMAIN>
#Wf_folder=<PERSONAL_PROMO>
#inf_user=<CSV_PAVANI>
#inf_PWD=<password>
#wf_name=<wf_promo_1839>
#start the workflow
 #$PM_HOME/pmcmd startworkflow -sv <$inf_server>-d <$inf_domain> -u <$inf_user> -p <$inf_pwd>-f <$wf_folder> -wait <$wf_name>
#Fetching workflow status
#$wf_name.status=$?
#Echo status message as per workflow status
#if[$wf_name.status -eq 0] then echo "workflow Execution Succrssful"
#elif echo "workflow Execution failed"

#SCD:-Slowly Changing Dimensions:- we will extract the data from source table and we load it into the target table.  we maintain it in a data warehouse  (customer,product,account,user,employee,region,location,time,store,mercant). 
#Dimension table:(Primary Key + Attributes)
#To maintain the table as target used SCD:we have 3types
#Type 1:-No history will be maintained simple update.       (when change happend in oltp side it updated in olap side also)
#Type 2:-History will be maintained Row level history. (method1-falg,method2-version,method3-date(end date null,9999,2999))      ()
#Type 3:-Recent history will be maintained Column level history. 
#Surrogate key:-In addition to the natural key column(primary k column). in order to maintain the history we will maintain this column(this is unique column)
#Version:-maintaining the previous version and present changes.

#select column_names from T_customer_version where (cust_id,veraion) in (select cust_id,max(version) from T_customer_version group by cust_id);  To take the current records.  
#Merchant:-
#Type1:-No history will be maintained simple update. 
#Type2:-History will be maintained Row lvl history.  (Method-1-Flag,Method-2-Version,Method-3-date).  (used most of the times)
#Type3:-Recent history will be maintained. 

#Workflow task:-we have different task here (session,command,Email,)this are re-useable(green mark visable(in this we cant modifiy in session lvl)) and non-reusabke tasks (decision task,assignment task,Timer task,control task,event wait,task,event raise,worklet,link tasks,session config,scheduler)
#windows command:-echo >c: \informatica \touch.txt
#linux command:-touch touch.txt
#
#
#
#
#
#
#
#

#Business intelligence:-(good decisions by effectivly managing data)enables the business to make intelligent,fact-based decisions(Aggregate Data(DB,Data mart,DW,ETL Tools)-->Present Data(Reporting tools,Dashboards,static reports)-->Enrich Data(add context to create information)-->Inform a decision(Decision are fact-based & data driven)) 
#ETL:-process that extracts data from source systems,transforms the data into a consistent data type,applies business logic then loads the data into a single repo. 
#ETL:Extract-->Transfrom-->Load        :-(OLTP(Heterogeneous source):-online transaction Processing(DB)here we have replication server(which stores last 10days data)-->ETL(informatic powercenter)(Batch processing)-->(OLTP:-online analytics processing(DW,DL-->DM(is a subset of DW))))-->from here we transform data for reports(Tableau,MS powerBI,Qlikview,looker,quick sight)          generaly we use 1)Batch processing here(i.e.,scheduling at proper time to transfrom data from source to target). 2)Live processing(near real time data)(i.e.,IOT devices,sensors Kafka(read data & holds logs)-->spark engine-->sending to data lake)
#ELT:-Extract-->Load-->Transform       :-(extract data from(DB)-->Load data to (Data lake)-->procees it(extraction-ingestion-processing it))
#Data Analyst/Business Analyst:-Creates data requirements(source to target map or mapping doc) 
#Data Architect/Data modler:-Models & builds data store(Big DL(Raw data),DW(structured),DM(sub set DW),etc.) 
#ETL Developer:-Transforms & load data from sources to target data stores 
#ETL Tester:-Validates the data,based on mappings,as it moves & transform form sources to targets.  
#Data Warehouse Architecture:-source layer(ERP,Other Data source,social media)-->(Real time,batch)-->Data integration layer(data cleaning,data validation,data auditing)-->Data warehouse layer(staging operation data start (EDW))-->DM-->Presentaion layer(BI Apps,mobile,on-demand)
#DW:is a subject oriented integreated,time-variant & nonvolatile(never over written or dlted) collection of data to support managements decision making process.(integrated,architected & periodic copying data from various heterogeneous sources,boy=th inside & outide the enterorise into a centralised repo optimised for reporting & analytical processing)   
#
#Top Dwon Approach(inmon):-(Data marts are created only after the complete DW has ben created)Database(OLTP)-->Data warehouse(OLAP)-->Data marts        (time consuming,easy,high intial cost,longer start up)
#Bottom up approach(kimball):-(Enterprise DW is created by combining the data marts together)source(OLTP-->Data marts-->Data warehouse).                (takes lesser time,low intial cost,shorter time)
#Hybrid approach:-is aims to harness the speed of the bottom up approach & user orientation of the top down approach(sourceOLTP)-->Data marts-->Data warehouse-->Data mart-->user).    #Data modling team will do this.   
# 
#In informatica we have 2 tables:-Dimensions & Fact Table(in enterprise DW):- 
#1)Dimension Table(the tables surrounds the fact table(consists tranctional data) and make link by primary key)this has primary key:-1)Non measurable,2)Primary keys 
#2)Fact Table(consists all transational Data taken key values from dimension tables).this table contains normalized data .this has forigen key:-1)Measurable,2)Foreign keys 
#
#STAR Schema:-Fact Table(Forigen key) is surronded by Dimensions Tables(primary key).  In STAR Schema we have to load Dimension table at 1st then Fact table.(like a star shape)(slowly changing dimension)
#Snow Flake Schema:-this has one-dimensional table that can be splited into multiple Dimensional tables.A Deenrmalized dimension table is splited into 1 or more tables,which results in normalization of dimensions. (one dimensional table refers to the other dimension table based on normalization)normalization to avoid data tenancy,duplicate. OLAP tables(De-normalized) in OLTP tables(normalized) 
#Galaxy schema:-
#
#Data warehouse:-structured,processed.schema-on-write.expensive for large data vols.users business professionals.is a relational DB which is specifically design for business transactional processing. this supports for decession making process. Business managers need a data warehouse for analysis the summaries of business.  Hence it is also called Decession Supporting System(DSC). 
#1)Time Varient(supports the business managers in analysing business & comparing the business with different time periods),
#2)Non-volatile(once data entered into the DWH it does not reflects to the change. Hence the data is static),
#3)Integrated(wich stores the data in an integrated format,which is collected from multiple,operational DBs),
#4)Subject oriented DB(which supports the business needs of middle manager(or)dept specific users.(this is defined as a collection of department specific business data)). 
#Operational (OLTP DB):-It is designed to support business transactional processing. volatile data. current data. detailed data. less history(3-6months). supports normalization.defined with more no.of joints. designed for running the business. few indexeses. Entity relationship. 
#Data warehouse(OLAP):-It is design to support decession making process. Non-volatile data. Historical data. summary data. supports denormalization. History data(5-10years). define with fewer joints. more indexes. dimenssional modeling.    
#Enterprise dataware house stores the entire dept of data. Data mart s a subject oriented DB. Data mart is a subject of EDW.It stores the DEpt specific data .  
#Data mart:-is a subset of an Enterprice DWH.is also a high performancequery structures. 
#1)Dependent DM:-In a Top Down approach a data mart develop depends on enterprice DWH such DM are knowns a Dependent DM.
#2)Independent DM:-In a bottom up approach a DM development is independent of DWH. 
#Operational Data store(ODS):-An ODS is a integreated view of multiple operational DBS designed for business transactional process.  
#Data Lake:-structured/semi-structured/unstructures,raw. schema-on-read. designed for low-cost storage. users data scientist. 
#Data Acquisition:-It is a process of extracting  the relvant business information,transformation the data into a required business format & loading into the target system. (data extracting ,transforming, loading). 
#
#ETL Tools:-2 types 1)code based ETL(this can be developed using some programming lang(SQL/PL/SQL)).  2)GUI(can be design with a simple GUI,point & click drag & drop)ex(informatica,data srvcs,Oracle data integration,data stage,data manager,SSIS(SQL server integration srvc)). 
#Data Extraction:-Its aprocess of reading the data from various types of sources. a)Relational sources(oracle,SQL srvr,DB2,Sybase) b)File sources(Flat file(test file),xml file) c)ERP sources(Sap,people soft,t.d-edwards) d)Legacy sources(main frames,AS 400,cobol files) 
#Data transformation:-process of converting the data & integration the data into the required  business  format. A staging area is a temporary memory (or) buffer where data transformation activities takes place. 
#a)data merging(process of integratingthe data from multiple sources into single output pipeline)horizontal(joints)source are having a diff data defination with the common field ,vertical(union)have similar data defination then such sources can be merge vertical using union.  
#b)data cleansing(process of removing unwanted data,which is also known as filtering). process of changing inconsistent data into a consistent format. (removing duplicates,removing records which contains nulls).  
#c)data scrubbing(process of deriving new attributes from existing source data defination)
#d)data aggrigation(process of calculating the summaries from the detailed data). (sum)
#Data Loading:-process of inserting the data into a target system. 2types:-1)Initial load(or) full load (process of loading data into an empty target tables.data from source inserts into the target tabel) 2)Incrementtal load(process of loading only new records after an intial load) 
#ETL Plan:-An ETL Plan logicaly definers extraction transformation & loading. Types 1)source data defination,2)Target data definition,3)Transformation logic
#ETL Repository:-is a brain of an ETL development system where you store the metadata such as source definition,Target defiition transformation logic,ETL plan etc.,
#ETL server:it is a ETL engine which erforms extraction,transformation & loading according to ETL plan given.
#Data moduler:-builds or design Data Bases process of designing DB is known as data modeling. the proscess of designing the DBs is known as data modeling. A Data modeler (or) DB Architec design the DBs using a GUI based DB desinging tool called ER win.  
#Data warehouse designing types:-1)star schema 2)snowflake schema 3)galaxy schema(complex star schema,integrated schema,hybrid schema)
#Normalization:-eliminating  duplicates. 
#session:- A session is a task that runs mapping. 
#work flow:-is start task that runs one or more sessions. the sessions can be run either in sequence or parallel. 
#Sheduling:-is an adminstrative task that specifies the date & time to run the workflow
#session log:-is created by integration srvc & stores in the repostery through repositery srvc. 
#
#ETl Tools:-Informatica,IBM-websphere Datastage,Microsoft-(SSLS(SQL server integrated srvcs)),SAP(BODS(Business objs Data srvcs)),oracle-(ODI(data integrator)),Talend Open Studio,Apache Nifi.
#Data visualization Tools:-Tableau,Microsoft power BI,SAP BO,Quilck sight,Tibco Spotfire,google locker.  
#
#Conceptual Model Design:-Includes the imp entities(tables) & the relationships among them. No attribute is specified. No primary key is specified.(Highly abstract,easily understood,only tables visiable,no software tool is required to define a conceptual Data Model).   
#Logical Model Design:-Includes all entities(tables) & relationships among them. all tables for each entity is specified. The primary key for each table is specified. Foreign keys are specified,Normalization occurs at this lvl.  
#Physical Model Design:-Specification all tables & columns.foreign keys are used to identity relationships b/w tables.Denormalization may occur based on user requirements. physical data model will be diff for diff RDBMS. ex:-Data type for a column may be diff b/w oracle,DB2 etc.   
#By using ERWin tool we can create forigen key first then we can create primary key.Actually we cant create like that. 
#
#OLAP Cube:-Is based on the Multidimensional Data model.OLAP enables a user to easily & selectively extract & view the data from diff point of views.Helps in decision making business process.   
#OLAP Operations:-4 types of analytical operations in OLAP:- 
#1)Roll-up:-Summarize the data (suming up)   (consolidation or aggregation) this operation can be performed by 2ways:1)Reducing Dimensions,2)climbing up concept hierarchy. 
#2)Drill-down:-Reverse of Roll up(data is fragmented into smaller parts. it is the opposite of the rollup process.) 
#3)Slice and dice-Project & Select:-one dimension is selected, & a new sub-cube is created.  
#4)Pivot(rotate)-Re-orient the cube:-converting Rows into column.(Rotate the data axes to provide a substiute presentation of data).  
# 
#Demensional modeling:-is a design methodolgy for designing data warehouses & data mart.this consists 3 phases to build the data model. 
#1)conseptual modeling:-understanding the business requirement,identifying the lowest lvl grains,identifying attributes & entities.
#2)logical modeling:-Design the table with required attributes using on rwin tool create relationships b/w the tables. 
#3)physical modeling:-Define the tables in the DB to physically store the data
#
#ETL Development:-Design ETL plans using GUI based ETL tool such as informatica,Datastage etc.,
#ETL Testing phase:-1)unit test,2)system testing,3)performance testing,4)UAT
#Report Development phase:-Design the reports by fulfiling report requirement specifications use the following tools to design reports.(cognos,bussiness objs micro strategy)
#Deployment:-Its a process of migrating the metadata from development environment to production environment. 
#
#Types of OLAP systems:-         (data modeling team will take care of it)
#1)ROLAP:-Relational OLAP:-Is extended RDBMS along with multidimensional data mapping to perform the standard relational operation.
#2)MOLAP:-Multidemensional OLAP:-Implements operations in multidimensional data.
#3)HOLAP:-This approach the aggregated totals are stored in a multidimensional DB while the detailed data is stored in the RDB. this offers(ROLAP & MOLAP)
#4)Others:-

#Steps involving developing an ETL process:-
#step1:-creation of source definition.
#step2:-creation of Target definition.
#step3:-Designing a mapping with or without transformation(implemented by designer)
#step4:-create session for each mapping
#step5:-create workflow to start sessions 
#step6:-Excute workflow. 

#Power center Repo:-is a relational DB which contains metadata required to perform extraction,transformation & loading
#Local repo:-is the repo which alows you to share the metadata with in the repo across multiple users.
#Global repo:-Meta data can be shared across multiple repos.
#Repo srvc:-Is a multi threaded process which allows you to insert,update,dlt, & retrive metadata from repo. 
#Integration srvc:-Reads mapping & session information from repo through repo srvc. This extracts the data from mappping sources, stores the data in a temp memory (or) buffer called stagging. where it applies the transformation rules that you configured in the mapping. 
#Integration srvc have components like:-1)Reader(responsible for extracting data from mapping sources)a)Relational reader,b)File reader,c)XML reader.  
#2)Data Transformation Manager(DTM):-This process the data according to the transformation logic given in the mapping. 
#3)Writter:-It inserts the data in to the mapping targets. 





#rep(repository srvc) & Is(integration srvc)
#                                    (Integration srvc (data Movement))
#                                      |              |              |
#                                    Reader      Transformation    Writer
#
#                                         Read                                 write
#Heterogenous source(DB(schema1,schema2))------->informatica server(unix/linux)-------->Tera Data(DB1,DB2) 
#                                        select              |               insect/Update
#                                                               Repository srvc                                         1st install repo and next informatic srvr next client. 
#    (informatic srvr will run on top of repo srvr)Repository(DB)this stores the metadata.  ex:Oracle
#                                                       |                                 
# 
#                                                  Informatic Client:          ETL Developer will operate. 
#                                                     R  D  W  M        :Repository manager,Designer,Workflow manager,Monitor. 
 
#Before starting informatica we have to strt the informatica srvc. client caannot read the data from source. only the informatica srvr will read the data it has integration srvc that intiat the integration srvc. that read the data from source and load to destination. 
# 
# 
# 
# 
#    
