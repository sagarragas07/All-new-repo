#NS Skill:-youtube      https://www.terraform.io (for decmentation)     Developed by Hashicrop     used Hashicrop lang(mostly Declaretive lang(this wont follow your given order it creates own order))   this is cross cloud platform
#Terraform:-is a writ,plan & create Infrastructure as code(IAC)(open source)(Hashicorp Terraform enables you to safety & predictably create,change, & improve infrastructure. it is an open source tool that codifies APIS into declarative configuration files that can be shared amongest team members treated as code,edited,reviewed & versioned.)
#in powershell give this command:-Get-command terraform(for checking path),terraform version. 
#AWS CLI Setup:-Download AWS Cli (windows for browser),accept & install,in powershell get command aws,aws help,create a user & take access key & secreat access key.#to create a profile:-aws configure --profile msagar-terraform ,give access & secreat key,aws iam list-users --profile msagar-terraform(for checking about user)
#Terraform file:create a folder,create a new file with .tf,terraform init,terraform plan,terraform validata,terraform apply,yes,terraform destroy,
#in sublime:-provider "aws"{      always choose a profile over giving access & secreat keys(bcz it is good method)
"""               region = "eu-west-1" """
#                profile = "msagar-terraform"
#            }
#Terraform variables:-string(a sentence),maps(key-value paris),lists(sg1,sg2,sg3),booleans(true(1) or false(0))    outputs are neceesry to view  to use variable "${var.vpcid}"
#Input & Output Variables:-
#AWS components:-s3 bucket uploading a file init,create ec2 key pair & sg,
#
#terraform Modules(seperate into small segments):-in this we have to import or call (we have to always terraform init)
#inputs to Terraform Modules:-
#Reuse Terraform Modules:-
#Multiple Environments Problem:-(by using workspaces)1st create the ws by terraform workspace new stagging,terraform production)   terraform workspace select production
#ENV Specific Local Variable:-using local function
#Shared Environment Variables across modules:-
#project 3tier architecture:-networking,as,alb&tg,launch config with userdata,asg,relaunch in diff Environment
#
#Terraform:-(IAC)    Terraform_config -->Terraform  -->cloud    -->cloud env (vpc,sub,ec2)
#infra as a code     Terraform_tfvars -->     |     <--provider -->
#                                          terraform.tfstate
#                                             |
#                                 stored in Terraform cloud
#Tf version,tf init,tf plan(dry run),tf apply,tf destroy,tf apply -target,tf providers,       tf code made of blocks,arguments,expressions
#Variables order:-ENV variable,tf.tf vars,tf.tf vars.json,auto.tf vars,CLI option(used by tf apply-var=var_name)
#input variables,output variables,local variables
#Modules:-contains for multiple resources.consists of collection of .tf & .tf json
#Types of moudules:-Root(need atleaste one root module),child(called by root module),published(loaded from pub or pre registor),
#state CLI:-Tf state list;tf state show;state move;state remove;state pull;
#Terrafrom workspace:-tf workspace list;workspace new;workspace show;workspace select;workspace delete,
#
#Terraform version:-display the version of TF
#Terraform -install-autocomplete:-set up tab auto-completion,reqires logging back in
#Terraform fmt:-rewrites all terraform configuration file to a canonical format (.tf)(.tfvars) are updated.
#3)terraform validate:-validates the configuration files for errors.
#terraform provider:-cloud provider
#1)Terraform init:-initializes a new or existing Terraform working directory by creating intial files
#2)Terraform plan:-generates an execution plan,showing that actions will Terraform take to apply the current configuration.
#4)Terraform apply:-creates or updates infra according to TF configuration files in the current directory.abs
#Terrafrom destroy:-destroy tf-managed infra & is an alias for tf apply-destroy
#Terraform refresh:-updates the state file of your infra with metadata that matches the physical resources they are tracking.
#Tf workspace:-dlt,list,new,select,show
#Terraform state:-this does advanced state management. the state is stored by default in a local file named "terraform.tfstate",but it can also be stored remotely,which works better in a team environment(list,show,mv,rm,pull)
#Terraform output:-reads an output variable from a terrafotm state file & prints the value. with no additional arguments,output will display all the output for the root module
#Terraform graph:-produces a reprsentation of the dependency graph b/t diff objects in the current configuration & state. 
#Terraform import:-import existing infra into your tf state. 
#Terraform login:-Retrives an authentication token for the given hostname,it supports automatic login,& saves credentials file in your host directory. 
#Terraform logout:-removes locally-stored credentials for the specified host name
#
#terraform apply -auto-approve       (used for withouting giving yes while applying)
#
#cloud junction(Terraform(go lang Hasicorp lang)):-IAC.(open source)           (total 150 providers)        altermnate tools(Terraform,Vault,Consul) 
#Imperative approach:-step by step creating infra(CLI,BASH SCRIPT)
#Declarative approach:-we create directly final step(TERRAFORM,CF,ARM(Azure resource management),Deploymaent manager). used for developing ,changing infra safely. 
#2)video installing tf in windows & linux        click terrafoem -v     terraform(see commands)
#3)provider "aws" {                           (sample script to create ec2 ins)       (scripts found on terraform document(https://registry.terraform.io))
# #   region     = "ap-south-1"
#    access_key = ""
#    secret_key = ""
#    }
#resource "aws_indtsnce" "int1" {
#ami            =  ""
#instance type  =  ""
#tags = {
#   Name  = ""
# }
#}
#4)video creating vpc
#terraform.tfstate (file):this will save all we created script in json format.(dont try to dlt this bcz it will update when we are updating the script. if we dlt & run agian it create resources again)
#terraform.tfstate.backup:(bup of tfstate file)
#5)video creating EC2 ins
#6)video terraform variables(vars.tf)(we used write scrits in diff files)    (input variable:with in the directory we placed & performing called as)(output variable)(by using count fun we can create no.of ins)
#7)video terraform modules:-combination of multiple resources or group of tf files 1)root module:terraform file calling another file that is rm 2)child module:calling the inside file that is cm 3)published module:calling the remote module
#
#
#embedded(pondhuparchadam):-implanted,fixed,inherent,intrinsic,
#encompasses(kalupukune):-surrounds,encircles,embraces,encloses
#NBFCs:-non-banking financial companies

#Data models:-is the modeling of the data description, data semantics, & consistency constraints of the data. it provides the conceptual tools for describing the design of a DB at each lvl of Data abstraction. 
#1)Relational Data Model:-is a type of model designs the data in the form of Rows & columns within the table.Tables are also called as relations.
#2)Semistructured Data Model:-ER model is the logical representation of data as objs & relationships among them.
#3)Entity Relationship Data Model:-an extenstion of the ER model with notions of function,encapsulation, & obj identity, as well.
#4)Obj Based Data model:-this is different from the other 3data models. The semistructured data model allows the data specifications at places where the individual data items of the same type may different attributes sets. 
#
#Data modeling:-Is the simplification of complex software designs by breaking up into simple desings. 
#design schemas:-star schema(main table to dimension table in star stucture) snowflake schema(fact table to dimension table to sub table).    
#  
#aws official youtube:-
#AWS GLUE Studio-part 1/3(visually author ETL jobs):is a fully managed extract,transform, & load (ETL)SRVC that makes it easy to prepare & load your data for analytics. 
#Catalog:-
#AWS Data Catalog:-stores metadata from variety of data sources, maintains key information about data such as partitions,schema changes
#AWS Glue Crawlers:-connects to data stores,progresses through a prioritized list of classifiers to determine the schema for the data, & then creates metadata in your Aws glue Datacatlog. 
#Process:-
#serverless spark:-fully managed cost efficient ETL engine for Big Data proceesing with 1min billing & super fast startup times
#Dynamic Frames:-extends Spark to handle dynamically changing structures
#Aws glue streaming:-process real time data streams from IOT devices
#Devops:-
#Aws Glue Studio:-allows authoring of highly scalable ETL jobs for distributed processing without becoming an Apache spark export
#Aws glue development Endpoints:-provides notebook styled intractive ETL development so that developers can easily develop ETL code step by step
#Glue workflows:-Orchestrates Glue jobs based on schedule. on demand or an event allowing customers to build complex ETL pipelines. 
#ML powered cleansing:-
#enables data engineers handle complex data quailty problems such as matching inconsistent patient names,customer names. 
#
#AWS Glue Studio(is an easy-to-use graphical interface for creating,running,& monitoring AWS Glue extract,transform,& load(ETL)jobs.)Benefits(visual ETL for Hybrid Development):-Rapid development,Job Monitoring,streaming & batch ETL,complex Transformations,structured data handling. 
#
#glue is data integration srvc:-it is process of combining & preparing data for data analytics,m/c l, & etc., ETL-automated script1)user interface,codeing interface. 
#glue benefits:-faster data integration,automate your data integration at scale,no server to manage. 
#data catalog:- this contains the metadata information of data in source s3
#crawler:- this craws the data form source & stores the data in glue catalog
#classifier:-give the automated schema for your data. 
#
#source:-s3,kinesis,kafka,RDS,JDBC
#Transform:-applymapping,join,filter,custom
#Traget:-s3,glue catalog(redshift,RDS,or JDBC)
#
#AWS GLUE studio-part2/3(learn how to author complex ETL jobs):
#some of the complexities in ETL:-Extract data from various sources,UDF's,string Operations,Multi-way joins,Hash operations,case statements,Aggregations/Metric calcualtions,sub-queries,many more....
#
#AWS GLUE Studio-part3/3(Learn how build stream data processing job):AWS Glue studio benefits for stream processing jobs:-
#Seamlessly integrate with Stream Sources without writting code. 1)AWS Kinesis Data Streams,2)Managed Streaming for Kafka,3)Self-managed Kafka 
#Hassle-free connectors management
#No checkpoint management overhead
#integrate with any glue supported sources for lookup data without writting any code
#Hybrid development allowing hand-written code where necessary
#Easy job monitoring & Serverless


#1)Srce cde:- youtube:-  Glue is the fully managed,serverless ETL(Extract,Transform,Load) srvc.  
#Extraction is the process of fetching/retrieving data from various data sources & load it into a staging area for furture use
#Transformation is the process of performing operations like cleansing,aggregating,mapping,re-formatting & more on the extracted data. The objective is to prepare & optimize the data which can be easily consumed by the end processes like data analytics,ML,etc
#Loading is the process of inserting the transformed data into the target DB,Data warehouse,data store from where the users & various processes can consume it
#Aws glue:-is the fully mangaged,serverless ETL tool. used to discover the Data,transform it & prepare it for analytics. Glue provides all the capabilities for data integration via visual & code based interfaces. it consists of central Metadata repo Known as Glue Data Catalog. Apache Spark ETL engine. Flexiable scheduler
#Components of AWS Glue:-
#AWS Glue console:-Orchestrate ETL Workflow
#AWS Glue Data Catalog:-Persistent metadata store
#AWS Glue Crawlers & classifiers:-Detect & infer schemas to store it in Data Catalog
#AWS Glue Operations:-Automatic ETL code generation in Python or Scala
#Streaming ETL in AWS Glue:-ETL operations on streaming Data
#AWS Glue Jobs system:-Enable to orchestrate the ETL workflow which can be scheduled or triggered based on events
#Work Flow AWS Glue:- 
#Define crawler to populate the Data Catalog
#Create the ETL job
#AWS Glue generate script for the ETL job or you can also provide/write one                  
#Run the job on-demand or define the Scheduler or Trigger
#Extract data from DS(data source),transforms it & load it into the Data Target.
#benefits(pros) of AWS Glue:- 
#Serverless,pay as you go,Automated schema recognition(by using crawlers),code Autogeneration(code in py & scala for ETL jobs),interface(visual+code based interfaces,provides unified view of data via AWS Data Catalog),Scalability(based on-demand)
#Limitations(cons):-limmited to pay & Scala programming Lang,Tightly Coupled with AWS eco-system,Dependency on Spark,Little or no information about what's going on under the hood
#Pricing:-ETL jobs,development endpoints & crawlers:$0.44 per DPU-hour. Data CAtalog:-free for 1st milloin objs,$1.00 per 100,000 objs stored above 1M,per month,Requests:-free for 1million per month,$1.00 per million requests above 1M in a month. 
# 
#2)AWS Glue Basic end to end transformation:-(Hands-on) csv to parquet by using(i am role for glue,s3bucket source & target folders,creating database,crawler,datacatalog,to data target in parquet formate)
#Terminologies:- 
#Data Catalog:-Persistent Metadata store in Glue
#Database:-Logical group of table definitions 
#Table:-Schema of you data
#Crawler:-Program that connects to the data store, which will determine the schema of the data using the classifiers & writes the Metadata in the AWS Glue Data Catalog
#job:Definition of ETL work 
#DATA:Data store(Repo where the data is store permanently),Data source(A data store that is used as input to any process or Transformaton),Data Target(A Data store where the transformed data is witten)
#Stats.govt.nz/large-datasets/csv-files-for-download/       (for downloading the csv files)
#
#3)AWS Glue:-Data Catalog & Crawler
#AWS Glue Data Catalog:-Persistent Central Metadata Repo. Each AWS acc can have one AWS Glue Data Catalog Per Region. Metadata Repo is the DB of descriptive information about data(i.e Metadata). Descriptive information of data includes structure of data(schema),its location,data types,business relevant info, of how data has changed over time. Heart of AWS Glue.  
#what makes AWS Glue Data Catalog:DB(a logical of tables)Tables(Matadata Definition that represents your)Crawlers & Classifiers(Detect & infer schemas to store it in data catalog)Connections(an obj that contains the properties to connect to a particular data store)AWS Glue Schema Registry(schema & registry for streaming data)
#Populate metadata|Data catalog:-1)first & manual way(manually creating the table definition & adding the metadata info manually like schema structure,location data types,owner of data & soon)2)second & Automatic way(using AWS Crawlers to populate metadata into AWS Glue Data Catalog)
#AWS Glue Crawlers & Calssifiers:-create &update data catalog tables. use custom/built-in classifiers to infer & determine the structure of data. can crawl file based & table based data stores. can detect changes to existing data,strucure & update the table definition. crawler will not determine the relationship. can run on schedule,trigger & on-demand.AWS glue does not support Crawlers for data streams.  
#When to use AWS Glue Data Catalog:-need of unified view of data from data silos. keep track of data in data silos. Data Transformation(ETL job). Query,Analyze data(Athena). Control access to underlying data via lake formation permissions
#Access AWS Glue components through:-Via console,via cloud formation,via CDK,via CLI,via SDK,via third party srvcs like Tf. 
#Hands-on:-Crawl CSV in S3 &populate metadata to Data Catalog:-(create IAm Role)(create folder in s3)(create DB)(create & run crawler to create table definition) 
#
#4)AWS ETL(Extraction transformation loading):-(is a set of process to move data from source to destination (or) point x to point y with some transformaation)(AWS Glue ETL is a tool available under Glue studio which is a part of the AWS Glue ecosystem to move data from source to destination)
#AWS Glue ETL:-suitable for ad-hoc data processing jobs like daily. jobs take min or hours to complete. No burden of infra management. supports only G.2X as largest worker type. 
#AWS EMR:-suitable for long term,large scale data processing jobs. job takes longer time to complete. we can choose any type on insts. if fixed infra then EMR is used. 
#Access Glue ETL:-via console,write the ETL script loacally & upload it as zip file,via development Endpoints(advanced option)
#Hands-on:-create the ETL job(TO transform the data & store it into Apache Parquet format), create crawler to populate the table for target data(Parquet data)
#
#5)Query data in s3 using Athena via AWS Glue Data Catalog:-
# 
#6)AWS Glue Custom Classifiers:-Role of the classifier is to read the data & identitying its structure & help to catalog the data correctly.(is the configuration, that is used along with the crawler to inferthe data & determine its structure or schema.)
#How crawler choose the classifier:-uses custom classifiers(one or more to match the data store). match with each classifier generates the certainty score. if certainty score = 1.0 means the crawler can create the correct schema with 100% confidence
#Types of classifiers:-(grok,JSON,XML,CSV)Apache Avro,Apache ORC,XML,JSON,Amaon lon,csv,mysql,redshift,dynamoDB,etc...
#when to use custom classifier:-when the built-in classifier is unable to create the table as you need, then you should consider creating the custom classifier. 
#Custom classifier(grok):-Grok is a tool to parse textual data using a grok pattern. Grok pattern is the named set of regular expression(regex). AWS Glue uses grok patters to dettermine the schema of the data. 
#Custom classifier grok:-grok patterns can process only one line at a time. line breaks with in a pattern are not supported. any changes in the custom classifier will not re-classify the previously crawled data. create a new crawler if any changes is made in the custom classifier.
#Hands-on:-create the crawler & try to determine the structure using built-in classifier, create the gork custom classifiers, create the crawler with custom classifiers, Query the data via Athena. 
#
#7)AWS Glue:-CSV Custom Classifier:- create Database. create crawler & populate catalog with buil-in classifier. modify the CSV file. create crewler & re-populate data catalog. can we also use Grok classifier as well?
#
#glue databrew:-s3(extract raw data)-->glue databrew(receipe (write prepared data)-->amz redshift(data warehouse)
#create a s3 bucket & uplode a file to the s3 biucket. create floder & store the data init. 
#create a redshift cluster save user name & password. & create 2 endpoints1)glue ep interface 2)s3 gateway
#goto databrew-create a dataset, name,s3,source s3,choose folder,csv,comma(,) ,trate 1st row as header,create. goto projects,demo project name,select dataset,add a role to this,create project.Now create a recipe add step,column delete,product-id-timestamp-transaction-id,apply(this create a set of recipes).filter,by condition,greater than,sc=amount,0,apply(this is recipe 2). sort,asscending,sc statename,*newyork*,texas,california,*new jersy* apply (3recipes applyed). now  create a job name,output jdbc,create a connection name enter jdbc url user password vpc sub sg create connection & run, ceate new table public orderdemo ac,use browse role,create & run job. now the table seen in redshift editor(we get refined data in redshift by glue databrew).
#
#


#                                                                                                                           Amz cw
#(s3,glue,redshift,cw,lambda) 1st project migrate incoming source data from s3 to redshift:-(cloud quick labs)ETL(Extract Transfer Load) with GLUE    s3 ---|-->glue  ----->Redshift
#                                                                                                                           lambda        
#
#At 1st when ever the crawler operation get suceeded that trigger event in the cw rule. that rule invoke the lambda. lambda inturn the aws glue job & glue job is targeted to load the data present in s3 bucket to redshift srvc.(this is done end to end automation)
#Redshift is warehouse where you can load size of tbs,pbs of data(olap srvc)
#Glue:-(ETL Tool)is a bridge b/w source(s3)&destination(redshift)
#1method steps:-1method (Cloud Quick Labs. youtube ETL | AWS Glue | AWS S3 | Load Data from AWS S3 to Amazon Redshift. 
#1st create a Redshift cluster dc2.large awsuser Awsuser123 & create a table & 3 columns  
#create a bucket & upload a CSV file. that CSV file must match the Redshift cluster columns. Take this file as a source.  
#Now check the cluster properties(vpc,subnet,route table,sg)create a end point,AWS srvc s3,select Gateway,create. add route table to end point. Go to sg & Edit inbound rules(ALL TCP add sm sg)(ALL traffic add 0.0.0.0/0),save rules. 
#Now goto IAM create a Role lambda admin access & add trust relationship for Glue & Lambda
#Now goto the Glue srvc 1st create a connection TestETL,Redshift,Next,cluster,DB,username(all poped),give password,finish,testconnection.(now the connection point is created b/t Glue to Redshift).test the connections
#Now goto CW & create a rule(rule in quick labs S3TORedShiftETL.json) (name as s3toredshift)event pattern. & add the target as lambda funtion to the rule (this pattern will watch the crawler state & invoke lambda)(when state succeeded it invoke lambda)
#create a lambda function with py 3.8. & use a handler code in cloud quick labs. we have to mention the job name
#add the event bridge as trigger as we created on top to the lambda
#Now we have to create 2dbs & 2 crawlers(for s3 & Redshift).add the sm name as we given in CW Rule to the cloud watch(Datasource s3),Next,Next,add s3path,select,next,next,add iam role existing,next,run-on-demand,add DB(s3gluedb),create,next,finish,select & run crawler(now we are loading the s3 data to crawler DB we get metadata in glue data catalog)
#Now create the other crawler for redshift RedshiftDB,Next,JDBC,TestETL,dev/public/sagartble,next,noselect next,add i am role existing,next,run-on-demand,add DB(redshiftDB),create,next,finish, & run crawler
#Now goto tables & check the 2tables are created(s3DB & RedshiftDB)
#Now goto redshift & query it (select * from tablename(copocsredshiftdemo)),Run,DB name,user name,(connected),Run,(it shows empty table & returns only coloums)
#Now goto ETL job & create visual with a blank canvas,create, s3,data catalog,s3db,tablebuctnm,+ change schema,+ data destination redshift direct data conn,conn,public,sagartble,job details job add role. run the job. (python or pyspark script created automatcally)
#(manually running)Now Run the job(after completion goto redshift & Run select * from tablename(cqpocsredshiftdemo)). we get all the data to redshift from s3
#2)Now run the datasources3 crawler after getting succeeded(the job get invoked(we can see 2nd ins))(this is fully automation by using s3,lam,cw,glue,redshift) (after completion goto redshift & Run select * from tablename(copocsredshiftdemo) we can see the rows or data doubled. pushed the data from s3 to redshift.  

#2methods
#s3 bucket load sm files to it,goto redshift & create a table with sm columns as s3 file,now goto glue create a DB,create a crawler to s3_craw & run the crawler(this will create the table in db catalog),create another crawler with the glue redshift connection then create(Redshift_crawler & run crawler)(this create the table in dc)now create a glue job(gluewill create the py code)save & run the job. now check the redshift we get the data from s3(select * from tablle)
#Now create a lam fun & trigger s3 bucket with the code(now auto matically when the data came to s3 it automatlly moved to redshift cluster with the help of lambda) 
#

#(Not)3rdmethod (Cloud Quick Labs. ETL from S3 to Amazon Redshift with AWS Redshift withAWs Lambda Dynaically) (s3,lambda,vpc endpoint,redshift)(ETL from s3  to Redshift with Lambda)
#s3 bucket loaded with some files. that files trigger the lambda.that lambda load the data to Redshift.this 2 are connected with VPC connection.Here we use lambda layer,tigger,Env variables,vpc,code (after send to visulization tools)
#
#create s3 bucket,create a lambda function with (py3.7),add the trigger as s3 bucket to lambda,create a cluster(dc.large),go to query editor & create a table with sm colummns as s3 file,go  & edit sg inbounnd rules,add a layer to the lambda(cloud quilk labs layer zip file)after creaing attach the layer,paste the code in function & goto env variables add the key-value as secrets(access secrete,access key,daname,host,password,tablename,user),now upload a file in s3 then automatically event created that trigger the lambda & invoked now goto redshit & check(select * form table) the data will present here.

#
#4rd method(sumit Kumar. Load data from S3 to Redshift using AWS Glue|| AWS Glue Tutorial for begginer)(s3,glue,redshift)(load data from s3 to Redshift using glue)
#s3 bucket load sm files to it,goto redshift & create a table with sm columns as s3 file,now goto glue create a DB,create a crawler to s3_craw & run the crawler(this will create the table in db catalog),create another crawler with the glue redshift connection then create(Redshift_crawler & run crawler)(this create the table in dc)now create a glue job(gluewill create the py code)save & run the job. now check the redshift we get the data from s3(select * from tablle)
#
#
#5method:-cloud quick labs:-(by using AWS Glue databrew)s3(data source)--->AWS DataBrew-(ETL)-->AMZ Redshift(destination)    By using VPC endpoint. 
#create a bucket & add a sub folder upload the files init
#create a Redshift cluster free,dc2large,user name,password,create. 
#create a dataset in glue data brew,name,source as s3,browse,give folder,csv comma(,),treat 1st row as header,,create dataset.
#Now create a projecct,name,select data set,add role,create a project.(this creats a connection between s3 to glue databrew(for extract raw data)).
#goto redshift & goto vpcendpoints(create ep with glueep with interface,create ep with s3 with gateway)(our vpc should enable the vpc to this eps)
#Now preparing the recipe columns,delete,col name,apply(this create the recipe),filter,sort(we created 3 recipes)
#Now create job name,output jdbc,create a connection paste jdbc ep,user password,vpc,sub,create a connection,createnew table,public_oredserdemo,acc,browse,give the role to it,create & run job. (the rewind data is transfered to Redshift)check with the sql commands. 
#
#


#create table copocsredshiftdemo (
#    sid    int    ,
#    sname  varchar(30) ,
#    marks  int    
#);

#DATA Format:-()Different data file formats in big data:-json,csv,Avro(This all are Row based formats (is used to sales data)),parquet,ORC(this are coloumn based format(used to analysis for a particular product based)))
#CDC:-change data capature. (CDC for continuous data replication. Tracks data changes by reading transaction logs,continuously streammms changes for downstream apps to consume.)
#Data models(Relational,Document,Graph-like models):-SQL(Relational),NoSQL(key-value),column-family,Analytical(OLAP),Graph,Document. 
#Application Discovery Srvc:-Reliable,engage with experts,encryption,integration(Discover,identify,Measure,Explore)
#AWS Database Migration Srvc(AWS DMS is not free we have to by the srvc)can enable near zero downtime migrations (DMS will load data & keep it in sync an on ongoing basis & once your DB is in full sync you can switch your app user to use DB in aws):-simple,reliable,lowcost,range of support(migrate DBs quickly & securly)high ava,(easily & securely migrates &/or replicates your DB & Data warehouses to AWS)(secure,assess,validate,snowball integration,monitor,stream data,low cost,multiple options)
#DMS Architecture:-Data Source(s)--->Replication ins--->Data Target(s)
#Snowball & Snowmobile:-high speed,Tamper resistant,Scalable,Lowcost          DMS + Snowball:-Migrate large DBs(over 5TB),Migrate many DBS at once,migrate over slow network. 
#AWS Schema Conversion Tool(AWS SCT):-converts your commerical DB & Data warehouse schemas to open-source engines or AWS-native srvcs, such as Amazon Aurora & Amazon Redshift
#AWS SCT create assessment Reports for homogeneous/heterogeneous migrations,secure connections to your DB with SSl,convert DB schema,Data warehouse schema,optimize schemas in AMZ Redshift,AWS SCT is also shaped with data extractors
#Driver for migration:-Infrastructure(hardware end of life),scalability(change insts sizes as required),cost optimization(pay for what you use),innovation(modernize your DB tier)
#AWS Database migration srvc(DMS):-easily & securely migrates &/or repliacates your DB & data warehouses to AWS. (Homogeneous or Heterogeneous:-oracle-->DMS-->oracle,sql srvr-->DMS-->Aurora,oracle-->DMS-->s3)
#Features of SCT(AWS SCT helps automate many DB schema & Code conversion tasks when migrating from source to target DB engines):-convert DB schema,convert data warehouse schema,convert embdded application code,secure connections to your DB with SSL,ETL modernization to AWS Glue,Migrate Data to data warehouses using AWS SCT Data extractors,optimize schemas in AMZ redshift. 
#AWS SCT product highlights:-Assess,Plan,convert schema & code,optimize,Migrate Data warehouses. DB Migration assessment:-connect AWS SCT to source & target DBs,Run assessment report,
#AWS SCT data extractors:-Extract data through local migration agent. Data is optimized for AMz Redshift & saved in local files. files are loaded to an AMZ s3 bucket & then to AMZ Redshift. Source Data warehouse--->AWS SCT---->s3 Bucket---->AMZ Redshift
#Data migration process:-(on-premises data center)start a replication ins,connect to source & target DBs,Select tables,schemas,or DBs,       (AWS DMS)let AWS DMS load  data & keep them in sync. switch apps over to the target after they are in sync at your convenience,AWS DMS captures ongoing changes after initial migration using CDC.               
#AWS DMS(is a HIPAA certified srvc):-Newer generation of compute-optimized(C5),general-purpose(T3),& Memory-optimized(R5)insts. ava in AWS classic & China Regions. 
#AWS SCT:-Snowflake,Azure Synapse,MariaDB 10.5(target),Babelfish(target).         DMS supports for:-PostgreSQL,ORACLE,AURORA,SQL Server,MYSQL,Maria DB. (Migrate(business-critical apps)Migrate(from Classic to VPC)Migrate(data warehouse to AMZ Redshift)Upgrade(to a minor version)Consolidate(Shards into Aurora)Migrate from NOSQL to SQL,SQL to NoSQL or NoSQL to NoSQl)
#when to use SCT:-Modernize your DB tier(oracle-Aurora,(commerical to open-source)). Modernize & Migrate your Data Warehouse to Redshift. (co,mmerical to Redshift)
#SCT helps with converting tables,views & code,sequence,user-defined types,synonyms,packages,stored procedures,funs,triggers,schemas,indexes,sort & distribution keys. 
#When to use DMS:-(Replicate)Create cross-region Read Replicas,Run your analytics in the cloud,Keep your dev/test & production env sync. 
#Databases:-DMS,SCT(for ingestion, Transfer,migration,API,client Tools)
#When to use AWS DMS & AWS SCT:-1)Modernise(modenise your DB tier & Data Warehouse)    2)Migrate(Migrate Bussiness-critical apps..)  3)Replicate(create Cross-region Read Replicas)
#
#
#
#Migrating Large Data stores using AWS Database Migration srvc & AWS Snowball Edge.(AMZ S3 is an AWS storage & retrieval srvc. To store an obj in AMZ s3,You uploadthe file you want to store to a bucket.when you upload a file,you can set permission for the obj & also for more info.)steps:-
#you use the AWS schema Conversion Tool(AWS SCT)to extract the Data locally & move it to an edge device.
#you ship the edge device or devices back to AWS.
#AWS DMS takes the files & migrates the data to data store. If you are using (CDC), those update are written to the Amazon s3 bucket & then applied to the target data store. 

#project from youtube(mycloud uni)AWS DMS srvc to migrate data:-Create DMS data source & targets(Aurora Mysql RDS,S3&DynamoDB)                                                           s3
#Create DMS Replication ins(you cant start/stop this ins,cant ssh/rdp into this ins),endpoints & tasks                                                            Aurora---->DMS
#Perform Data migration including CDC(change data capture)                                                                                                                             dynamoDB
#work flow:-Aurora(Data source Endpoint)--->Replication ins(Replication Tasks)---->S3,DynamoDB(Taget Endpoints)
#create a Replication instance in a DMS:namet,t3.micro,single AZ,uncheck,sg default,create.
#Now create a RDS DB,Aurora,dev/test,name,password,create.
#create a s3 bucket,create a im role(DMS role for s3 as source take the ARN),
#Now create a Endpoint:Target ep,name,s3,paste ARN,bucket name,dms,Run test,create ep.
#Now take RDS EP,Now create another ep in DMS,source ep,ins pop,private access,RDS name & password,Run test,create ep.
#Now create a role for dynamoDB(dynamoDb as DMS target)copy the ARN,
#Now Create a Endpoint:Target ep,name,Dynamo DB,ARN,Run test, 
#Now create a bastion srvr (one ins),sg new MYip,launch. create a SG bastionRDS SG,ALlow TCP 3306 traffic from bastion host to RDS,inbound MYSQL/Auroracustom,custom,add pvt ip of ins,create a sg,Goto RDS & modify,Add Bastion SG,continue,apply.goto parameter groups in RDS create a PG,DB cluster parameter group,name create,go inside it search binlog edit properties,binlog format row,binlog checks none,save. & add this PG to RDS ins,modify,additional add PG,apply,  
#Now goto ins & connect. SQL electron, give RDS name & ep password,connect RDS ins. Run:call mysql.rds_set_configuration("binlog retention hours",24);(we have to on bcz of change data capture),Reboot the RDS ins,show variables like"log_bin";,Now create DB(schema) table & insert the data in it,
#Now goto DMS Database migration tasks,name mysql to s3,ins pop,source pop,target s3 ep,migrate existing data & replicate ongng changes,schema nametable,create task. 
#Now create another task name,repins,sourcerds,target dynamo DB ep,cdc,table maping,schema,table name,create task, 
#Now go & check the data is migrated to s3 or not the data will come in s3. & check the dynamo DB the data is migrated. now when you change the RDS data the data will replicaated to s3 & DynamoDB  
#


#
#1method(KVR Tech Labs. AWS RDS - Database Migration from on premises to AWs RDS)
#2nd project migration of on-premises mysql RDS to AWS mysql RDS (using Dms) our aim is migrate datebase from on-premises to AWS
#create a RDS DB,standard,mysql,freetier,name,password(admin1234),burstable Classes,db.t2.micro,public access yes,Choose existing,create Db.
#(on-premises)create a linux server,(install a DB(&that DB need to migrate to AWS))STEPS:- 
#wget https://dev.mysql.com/get/mysql80-community-release-el9-1.noarch.rpm  (this will install DB)
#ls -rlt,   dnf install mysql80-community-release-el9-1.noarch.rpm,  dnf repolist enabled | grep "mysql.*-community.*",  dnf install mysql-community-server,  y,  mysql -Version,  
#systemctl start mysqld
#systemctl enable mysqld
#systemctl status mysqld
#netstat -plntu
#mysql -u root
#grep 'temporary password' /var/log/mysqld.log   (if we get password worng we have to use this temp p)
#mysql_secure_installation copy the pass & paste, enter new pass and y give again,y,y,y,y,y
#mysql -u root -p   (this gives login)
#'W3lcome@123'       *(seting password)
#CREATE DATABASE employee;
#SHOW DATABASES;
#use employee;
#create table salary(emp_no INT,name VARCHAR(100),salary INT);
#Show tables;        desc salary;   insert into salary(emp_no,name,salary) values(01, "Mike", 8000);     insert into salary(emp_no,name,salary) values(02, "kevin", 7000);     select * from salary;
#(remote(AWS))create a lightsail server(centos) connect it with lightsail shell.(now connect RDS DB) root,give password,  mysql -h aappsbd.c9glqfkeqb2o.us-east-1.rds.amazonaws(endpoint(app   -p)).,password,show databases;,create database employee;,use employee;,create table salary(emp_no,INT,name,VARCHAR(100),salary INT);,show tables,desc salary;select * from salary;
#Now goto to linux server.mysqldump --databases employee -r backup.sql -u root -p,password,ls(this will create a bup file),more backup.sql,ll,mysql -h endpoint(app .com) -u admin -p employe <backup.sql,password         now go & check the RDS DB ins the records(data will be present)(select * from salary;)
#if you want some more rows in linux. mysqp -u root -p,password,use employee,insert into salary(emp_no,name,salary)  values (03,"khan",7000);select * from salary;,mysqldump --databases employe -r backup.sql -u root -p,password,mysql -h appsdb.c9glqfqb2o.us-east-1.rds.amazonaws.com -u admin -p employe < backup.sql,password.
#now got RDS db ins and check select *from salary;  (now we can see the updated row in the DB)       (here data will be migrated on-premises to aws)        #we need to create the sm schema for two table only the data will be migrated by this concepts. 


#2nd method(E-Multiskills Database Tutorials(Migrate Mysql on-premises to AWS RDS @MYSQL))
#create a linux a ins & connect. sudo su,sestatus,systemctl status firewalld,wget https://dev.mysql.com/get/mysql80-community-release-el9-1.noarch.rpm  (this will install DB),yum local install mysql80-community-release-el7-3.noarch.rpm,y,yum repolist enabled| grep "mysql.*-community.*",yum install mysql-community-client,yum install mysql-community-server,y,systemctl status mysqld,systemctl start mysqld,systemctl,grep 'temporary password' /var/log/mysqld.log(this give temp pwd),mysql_secure_installation,cp & pst pwd,new pswd Sagar@1234,y,y,y,y,y,create a DB,create a table,instert data into it.Now this will create some data in on-premises Db.1)  ,vi /etc/my.cnf,add this line (bind-address = 172.31.88.86),systemctl restart mysqld,systemctl status mysqld,mysql -u root -p, give password,show databases,exit(this is source db).2)    (now we are connecting the target system)mysql -u admin -h endpoint (rds-.com) -p, give db password,show databases,create database employee;,use employee;,create table salary(emp_no,INT,name,VARCHAR(100),salary INT);,show tables,desc salary;select * from salary;, 3)Now goto to linux server.mysqldump --databases employee -r backup.sql -u root -p,password,ls(this will create a bup file),more backup.sql,ll,mysql -h endpoint(app .com) -u admin -p employe <backup.sql,password.  (now we can see our employees table in target RDS DB)
#Now create a RDS instance.standard,mysql,MySQL8.0.25,freetier,rdsmysql name,Admin,Sagar1234,assword,burstable,dbt2.micro,yes public,create DB.Now connect to workbench by Rds Endpoint.1)   Now we are connecting RDS to Mysql Workbench. copy the ENDPoint of RDS,goto mysql wb & database,connect to Database,host name as endpoint,admin,pwd,ok(we connected with RDS instance Now)

#
#3)Method:-(Annalytics Excellence)To use schema conversion tool we have to install the SCT in our lap. & create a RDS mysql DB becz we beed the Endpoint of RDS. & we need a driver bcz tool needs a driver we need to install Driver we need to add Driver path(this will connect the DB ins).it will load the metadata
#crete a Redshift cluster(port 5439)(we need endpoint)   source as sql server & destination as redshift
#aginity workbench for reshift is used to connect the redshift endpoint. (it is used as workbench)
#

#4)Method:-migrate a mysql on-prem db to aws rds:- 
#create a Rds DB, public yes,sg 3306mysql/aurora 0.0.0.0/0,connect to workbench with endpoint,connect DB,endpoind nm password,there is no schemas now in this. Now export fro local workbench. Go to adminstration,Data Export,select schema,export self contained file link,start export. now goto Rds DB.admin,import,select file link,start import. Now the DB & tables moved to Rds DB.(on preme data to aws moved)
#



#Athena:-serverless,interactive query platform,works on the data stored in s3,uses standard SQL & ANIS for quering data,supports variety of formats(CSV,Json,Avro,ORC(columnar),Parquet(columnar)),only pay for querying the data
#Athena quickly query Unstructured,semi-structured & structured data. uses Presto(a distributed  SQL engine for Big Data),Athena accessed by AWS console,Athena API,Athena CLI,JDBC connection. Integrated with Glue Data Catalog,integrates with Quicksight(BI Tool) for data visualization. 
#Athena populared due to:-Used by Data Analysts to Query large S3 data sets,No need to spin up servers or Hadoop Cluster. 
#Athena Use cases:-Analyzing cloudTrail/cloudfront/vpc/elb logs.integration through ODBC/JDBC with other visualization Tool. As-hoc logs analysis
#s3--->AWS Glue Crawlers--->AWS Glue Data Catalog--->AMZ Athena--->AMZ Quuicksight
#                                         |
#                                 AMZ Redshift Spectrum     
#Athena Creating Tables using:-DDL commands,AWS Glue Crawler,JDBC driver,Create table Wizard. 
#query results & metadata information is stored in s3(you have to provide storing output)
#Hands-on:-create a bucket and folder & upload a object init,Goto glue &create a crawler with source data as s3path,add the i am role for glue, crawler created run it,DB is created in glue,goto Athena we can see the DB & table,here we need set up a result location in s3 athena output folder in bucket create,take the path and paste it athena output,now run the query in Athena we get details of data in datacatalog.& the history will be saved in athena. 
#

#Projects:-3years
#
#awsuser
#Awsuser123
#s3 to redshift yashwanth
#create table sagar(
#    sid int,sname varchar(30)
#);
#
#copy public.sagar from 's3://s3toredshiftbuck/sag.csv'
#iam_role 'arn:aws:iam::290987992570:role/s3toredshift_lam'
#IGNOREHEADER as 1
#delimiter ','
#
#select * from sagar;
#
#
#redshift-cluster-2.ceggssx0vvgf.us-east-1.redshift.amazonaws.com:5439/dev
#
# 
#
#Experience terms to learn:-
#KT:-Knowledge Transform(explaning about product full details to new employee by a experienced employee)
#Standup meeting:-(conducted at mrng discussing about yesterday work & sharing today plan)(every indivudal have to respond here)
#offshore team:-we are offshore team because we working for us client
#onshore team:-sm employees will go there & work there. they called as onshore team
#Build & Deploy:-developer written code has to be complied & excute that will created as package file(var file or rar file)zip file created is known as Build. That build file copied to servers or excuting in server is known as Deployment  
#Sprint:-is a particular period time (the given task has to be completed in the given time is known as Sprint(this comes under Agile Dev process))
#Bug:-mistake while preparing the code by Dev
#
#
#
#
#Data Engineering:-is the primary process of converting a raw entity of data into useful info.
#Data Modeling:-It is process of simplifying complex software designs by breaking them down into simple diagrams that are easy to understand.  
#Features of Hadoop:-Free & simple to use,highly scalable,data is replicated across multiple DataNodes,Extremely Versatile,Faster data processing. 
#Big Data:-Vol,variety,velocity,veracity. 
#Star Schema:-A Star Schema in a Data Warehouse can have one fact table & a no.of associated dimension tables in the centre. 
#Snowfalke Schema:-It is a logical arrangement of tables in a multidimensional DB that corresponds to the shape of a snowflake. 
#COSHH:-It provides scheduling at both the cluster & app levels to have a direct positive impact on ob completion time. 
#XML configuration files present in Hadoop:-Core-site,Mapred-site,Yarn-site,HDFS-site. 
#Spark:-processes & store data in memory for subsequent steps.100 faster speed then MR
#MapReduce:-processes data on disc.
#Replication Factor:-is the no.of times each Data Block is replicated by the Hadoop framework. 
#Intermediate quetions:-
#security ensured in Hadoop:-Secure the authentic channel,use recevied stamp to request a srvc ticket,Authenticate the connection. 
#Data Engineer do:-Handling data inflow & pipeline processing,Maintaining data staging areas,Performing data cleaning,Ad hoc query construction operations. 
#Data stored in the Namenode:-FSimage(stores the entire state of the file system namespace since NameNode's inception), Editlogs(It contains all of the most recent changes made to the file system in relation to the most recent Fsilmage)
#Hive in the Hadoop ecosystem:-Hive is used to provide a user interface for managing all of Hadoop's stored data. 
#Table creation functions in Hive:-Explode(array),Explode(map),Json_tuple(),Stack().
#unstructured data to structured data:-for proper analysis,unstructured data must be transformed into structured data,& the methodes for transformation can be discussed.
#validate a data migration from one DB to another:-you should be able to discuss approprite validation types in various scenarios. 
#What happens when block scanner detects a corrupted data block:-DataNode informs NameNode of the corrupted block,NameNode creates a replica based on an existing model.
#
#
#Aws glue:-is the fully mangaged,serverless ETL tool. used to discover the Data,transform it & prepare it for analytics. Glue provides all the capabilities for data integration via visual & code based interfaces. it consists of central Metadata repo Known as Glue Data Catalog. Apache Spark ETL engine. Flexiable scheduler
#S3 is simple storage srvc as (source data)
#Redshift is a data warehouse (destination)
#cloud watch:motintoring tool       event bridge rule:used to monitor glue crawler
#Lambda:-this used to triggere to rule & run glue job when the source data got suceess. 
#Data Engineer do:-Handling data inflow & pipeline processing,Maintaining data staging areas,Performing data cleaning,Ad hoc query construction operations. 
# 
# 
# 
# 
# 
# 
# 
# 
# 
#  



