#Aws sol architech notes:-#150USD, 2hrs, 65questions, 52need, to come 72%Pass outoff 100%                                                     AKIAWRFJHTO6DDJOC2O2
#syllabus:-                                                                                                                                   5eBWwVngSqPMpl7cWTYptzmUBqwwEICnIlkOdLup
#1)Design Resilient Architectures -30%
#2)Design High-Performing Architecture -28%
#3)Design Secure Applications and Architecture -24%
#4)Design Cost-Optimized Architecture -18%


#stephan maarek:- 30Aws services  SAA-C03
#AWS:-Amazon web Services is a cloud provider
#They provide you with servers and services that you can use on demand and scale easily
#AWS:-powers some of the biggest websites in the world :-
#1)Amazon.com
#2)Netflix              :-They dont have single server they rent from the aws cloud(pay as you go) 
#AWS Services:-
#EC2:-
#ECR:-
#ECS:-
#AWS Elastic Beanstalk:-
#AWS Lambda:-
#Auto Scaling:-
#IAM:-
#KMS:-
#S3:-
#SES:-
#RDS:-
#Aurora:-
#DynamoDB:-
#ElasticCache:-
#SQS:-
#SNS:-
#Step Functions:-
#CloudWatch:-
#CloudFormation:-
#CloudTrail:-
#APIGateway:-
#Elastic Load Balancing:-
#Cloud Front:-
#Amazon Kinesis
#Route 53:-
#
#AWS use cases:-
#scalable application, application to diverse set of industries
#backup, big data analytics,website hosting,mobile,and social apps,gaming.
#
#AWS Global infrastructure:-
#AWS regions:-is a cluster of data centers
#AWS availability zones:-each region has many az (3min ,3max is 6) there are seperated from each other isolated (they are connected with high bandwidth)
#AWS data centers:-each az is consist of (1 or more data centers) (they are connected with high bandwidth)
#AWS edge locations/points of presence:-216 points of presence (205 edge locations)(84 cities and across 42 cities)
#
#choosing a AWS region:-
#compliance:-standard,rules following
#proximity:-near,close
#availabe services:-new services aren't available in every region
#pricing:different pricing in every region
#
#global services:-
#IAM(identity and access management) 
#Route 53 (DNS service)
#Cloud front (Content delivery network)(edge locations)
#WAF(web application firewall)
#Region services:-
#EC2(infrastructure as a sevice)-                             AWA3231F5E68
#Elastic beanstalk(platform as a service)
#Lambda(function as a service)
#Rekognition(software as a service)
#
#i am policies structure:-json document that outlines permissions for users or groups  (RAPES)       (siv)
#version:- 2012-10-17,
#id:-an identifier for the policy
#statement:-1 or more individual statements
#statement consists:-
#sid:- an identifier for the statement
#effect:- whether the statement allows or denies access
#principal:-account/user/role tp which this policy applied
#action:- list of actions this policy allows or denies
#resource:- list of resources to which the actions applied to
#condition:- conditions for when this policy is in effect
# 
#To access AWS 3types:- 
#1)AWS management console:-password + MFA 
#2)AWS command line interface(cli):-access keys
#3)AWS software developer kit(SDK):-access keys
# 
# 
#e2:- chmod 400 .pem(to change the permissions),   whoami, ping google.com,   control(to exit)
#ssh -i .\EC2Tutorial.pem ec2-user@public ip (then it will be connected) 
# 
#
#cloud shell:- give aws access and secreat keys, aws --version, aws iam list-users(this will show the list of users)
#{
#    "Users": [
#        {
#            "Path": "/",
#            "UserName": "solution",
#           "UserId": "AIDAWRFJHTO6ONG67A7YV",
#            "Arn": "arn:aws:iam::449178999740:user/solution",
#            "CreateDate": "2023-02-01T06:25:28+00:00",
#            "PasswordLastUsed": "2023-02-01T06:26:41+00:00"
#        }
#    ]
#}
#echo "text" > demo.txt (creating demo.txt and writting a code init)
#cat demo.txt (read demo.txt)
#ls (shows list)
#pwd (shows present working directory)
#
#
#Important ports:-
#FTP:- 21
#SSH:- 22
#SFTP:- 22(same as SSH)
#HTTP:- 80
#HTTPS:- 443
#NFS:-2049
#RDS DATABASES:PORTS:
#POSTGRESQL:-5432
#MYSQL:- 3306
#ORACLE RDS:- 1521
#MSSQL SERVER:- 1433
#MARIA DB:- 3306(same as MYSQL)
#AURORA:- 5432(if POSTGRESQL compatiable)or 3306(if MYSQL COMPATIABLE) 

#sudo yum install -y bind-utils(this will install dig(mac) and nslookup(windows) in cloudshell for using route 53)
#dig(domain name)      (this shows the record type)
#
#
#Aws Machine learning:-
#Amazon Rekognition:-used to find objects,peoples,text,scenes in images and videos by using ML(A2l)
#Amazon Transcribe:-automatically convert speech to text(ASR).Automatically remove peronally identifiable information(PII) using Redaction 
#Amazon polly:-this turns into lifelike speech using deep learning (convert text to speech)(lexicon & SSML)
#Amazon Translate:-natural and accurate Language translation (easily translate large volumes of text efficiently)
#Amazon Lex:-(alexa)helps to build chatbots,call center bots
#Amazon connect:-receive calls,create contact flows,cloud-based virtual contact center and can integreated with CRM systems or AWS
#Amazon comprehend:-(this is regional srvc)fully managed (it uses SSL protocol is secured)(natural language processing(NLP))(fully managed and serverless)(understands how positive and negative the test is)srvc that uses M/L to uncover valuable insights & connections in text.finds sentiment of customer
#Amazon comperhend Medical:-this detects and returns useful information in unstructured clinical text(uses NLP)
#AMZ Translate:-is a Neural M/c Translation(MT) srvc for translating text b/w supported lang
#Amazon Sagemaker:-fully managed service for developers/data scientists to build,train & deploy ML model for any use case (difficult to do all the processes in one place + provision servers)(prediction by seeing past results)
#Amazon forecast:-fully managed service that uses ML to deliver highly accurate forecasts(predict)
#Amazon Kendra(intelligent search srvc by ML):-fully managed document search service (extract answers from with in a document(text,pdf,html,power point,ms word,faqs....))(it supoorts semi-structured & unstructured & audio video)data search through s3,sharepoint,salesforce,srvcnow,RDSDB,One drive (it wont support for ans require cross document passage aggregation or calculation)
#Amazon personalize:-fully managed ML-service to build apps with real-time personalized recommendations (used in retail stores, media and entertainment)
#Amazon Textract:-automatically extracts text, handwritting, and data from a scanned documents using AI and ML
#AMAZON Neptune(produce graph DB)(Billions of relationships)(milisec latency):-fully managed build & run graph apps with highly connected datasets(recommendation engines)Fraud Detection (acid:-atomicity,consistency,isolation & durability:-immediate consistency)15 RR
#AWS Outposts:-run aws infra & srvc on premises for a truly consistent hybrid experience(aws people comes to us and install & go.(outpost rack:-it provide AWS infra srvc to virtually any DC)(outpost srvrs:-have limited space or smaller capacity requirements such as shops. this provide localcompute & network) gives true hybrid expirence
#REDACT:-Automate the extraction of insights form packets of legal briefs such as contracts & court records. further secure your docs by identifying & redacting personally identfiable informaton(PII)
#
#Amazon Timestream is the most sutiable serverless time series DB for IOT operational srvcs. it can store trillions of events from these sources
#
#Serverless in AWS:-AWS Lambda,Dynamo DB,AWS Cognito,AWS API GW,AMZ s3,AWS SNS & SQS,AWS Kinesis Data Firehose,Aurora Serverless,Step Functions,Fargate
#
#Appsync:-is used to collect the data and querie by using GraphQL languages on multiplle Databases,Apis,&micro services
#Recovery point obj less then 1sec:-must enable Multi-az deployment for the DB ins
#AWS Cost explorer:-visualize,understand,and manaage your AWS costs & usage overtime
#
#AWS Secrets Managar will store the secrets can be DB Credentials,passwords,&3rd partyAPI keys (can rotate keys automatically) (doesnot support dynamo db)
#Systems Manager parameter store:-you can store passwords,DB strings,AMZ AMI IDs,&license codes as parameter values (but it doesn't rotate its parameters by default)
#
#Glue:- fully managedd extract,transform,and load(ETL) srvc That makes customers to prepare and load their data for analytics
#DMS:-data migration srvc helps you migrate DBS to aws quickly and securely
#RDS Proxy:-is a fully-managed highly ava and easy-to-use DB proxy feature of amz RDS that enables your apps to:1)improve scalability by pooling & sharing DB connection 2)improve ava by reducing DB failover 66% 3)improve security
#
#s3 inventory:-used to get obj list & s3 select to filter your objs
#AWS Transfer Family:-fully managed srvc for file transfer into & out of AMZ s3 or AMZ EFS using the FTP protocol(supports:-FTP,FTPS,SFTP)(used for sharing files,public datasets,CRM,ERP..)
#AWS Datasync:-move large amount of data to and from (Schedule data sync)(on-premises/other cloud or AWS-needs Agent)(AWS to AWS-no agent needed)file permission & metadata are preserved
#AWS App Runner:-fully managed srvc that makes it easy to deploy web apps and APIs at scale(no infra experience required)(used:-web apps,APIS,Microsrvcs,rapid production deployments)
#
#Cloudfront function & Lambda@Edge:-some of the logic at the edge (the code is attached to cloudfront runs close to your users to minimize latency) 
#1)cloudfront functions:-lightweight funs written in JAVASCRIPT (scales millions of request /sec)<1m/s
#2)Lambda@Edge:-written in NODEJS or PYTHON(scales 1000s of requests/sec)5-10sec
#AWS Control Tower:-easy way to set up & govern a secure & compliant (multi-acc AWS environment) used in AWS Organizations to create accs (Preventive=using SCPs)(Detective=AWS Config)
#
#By default:Lambda fun is launched outside VPC. for that you must define vpc id,sub,sg. Lambda will create ENI in your sub. RDS proxy is never publicly accessible only accessed by VPC
#
#TOP 50 Aws Exam Tips for aws sol architech:-(global srvs:-IAM,ROUTE53,CLOUD FRONT,WAF)(Regional srvs:-EC2,ELASTIC BEANSTALK(PAAS),LAMBDA(FAAS),REKOGNITION(SAAS))
#High Availability = Load balancer + Asg + Multi AZ
#NAT gw:-aws managed        #NAT ins:-you need to managed
#Athena will works on ad-hoc sql queries to find sentimental words in a statement and quicksight is used to create intelligent dashboards
#
#Millions of Transactions per second = Network Load balancer             transaction loss to prevent=sqs,kinesis
#TCP/UDP Traffic = Network load balancer (layer4) millions of reqs/sec (high throughput & low latencies)
#HTTP/HTTPS/TCP/SSL protocal = classic lb (layer 4&7)
#Intelligent load balancer = Application load balancer(layer7) http/https and websockets(web layer)
#gateway load balancer=(layer3) ip packets
#
#SSH protocol uses TCP & port 22
#High ava:-multi AZ     Elastic beanstalk environment:-with least changes to the application        fargate wont support for AMZ fSX for Luster file share    REST API:-use AMZ API GW with AWS Lambda 
#Website running worldwide Content without violation distribution rights:-on figure AMZ Route53 with a Gelocation policy
#burst of traffic within sec:-set up an API gw & use AWS Lambda function
#serverless:-scaliable for infinte capacity & highly performance
#Rds bups 35 days & aurora 35days  supports CRR & Rds
#SSL(secure socket layer) Termination = Application load balancer
#HTTP/HTTPS = Application load balancer (layer7)(having health check options)
#gateway lb- = layer3 ip packets
#High Availability = Think about only high availability
#Cost optimization = Think about only cost optimization
#sticky sessions:works for clb & alb always gng to sm webserver
#SNI:-Server name indication (multiple SSl certificates onto one web server) ALB & NLB,cloudfront. does not work for CLB
#
#A-maps a hostname to IPV4   AAAA-maps a hostname to IPV6   CNAME:-maps a hostname to another hostname(to change zone apex)
#CNAME RECORDS:-points a hostname to anyother hostname only for non root domain 
#ALIAS RECORDS:-points a hostname to an aws resource works for root domain & non root domain (you cant set the TTL)(you cannot set an ALIAS record for an ec2 DNS name)(to change )
#
#For movement + Replication = Data Sync (full securied)
#HPC(high  performance computer) = Amazon luster / Aws instance store 
#Big Data/Hadoop = FSX luster
#Rest Apl = Amazon Api Gateway          
#Api Gateway = Answer is more related to lambda  
#Windows file server share service = SMB / FXS
#Linux file server share service 1  = NFS
#Restrict S3 bucket access = Most likely bucket policies
#Unware of file movement in S3 = S3 intelligent-tiering
#S3 Replication = S3versioning is must enable
#Encrpty RDS instance = Automatically Encrypts backups and snapshots
#Real time streams = Kinesis streams
#Near real time streams = Kinesis Firehose
#S3 Encryption = SSE-s3/SSE-KMS/SSE-C/Client-side-encryption/AWS Encryption(server side encryption/client side encryption/aws side encryption)
#Recovering deleted file from S3 = S3 versioning must be enabled              kms=key managment srvc     cmk=customer management keys
#NAT Gateway(network address translation,managed by aws,paid price per GB) vs NAT Instance(managed by youself,like a bastion host)
#Security Group = Stateless; only inbound rules only allow
#Network ACLS = Statefull; both inbound and outbound rules allow and deny
#Common Web exploiting, sql injections = WAF(web application firewall)
#Advanced DDOS support = AWS Shield Advanced
#AWS Cloud Watch = Metrics for every AWS Service
#AWS Cloud Trail = API calls tracking
#AWS Config = Compliance of resources / Auditing & Recording compliances of AWS
#RPO = Recovery point objective
#RTO = Recovery time objective
#If more load on RDS = Then create read replica and change connection strings in the application (improve read performance) (transfer reports for analtics)
#Big Data = Elastic Map Reduce
#cross AWS Account Access = Through secure token service(sts)
#For web identification = AWS cognito
#VPC peering is not transitive
#Use transit gate ways = Hub & Spoke model
#Decouple / first in first out = SQS queue /sqs fifo
#push /pub-sub Mechanism /fan out = SNS
#Detailed Monitoring =for every 1 minute interval we can do          basic monitoring =srvc send data points to cw every 5min
#RDS for MYSQL in multi az:- High ava & ensure (acid)compliance in the data tier 
#AWS Site-to-Site vpn:aws side(virtual private gw),customer gw on on-premises side (enable route propagation for the virtual pvt gw in route table)(in sg ICMP Protocol)
#
#Snowcone (small portable transfer) = 8TB upto 24TB      (can be sent back to aws offline or connect it to internet & use AWS datadync to send data)
#snow ball edge storage optimized:- (max 80TB transfer TBs and PBs)     snowball edge compute optimized:-42TB   
#snowmobile =Peta bytes movement = (data transfering exabytes of data on-premises to aws 1EB=1000tbs)
#AWS OpsHub used to order the snowball           snowball can not import to glacier directly for that you have to use s3 life cycle policy       but for glacier deep archive it sends directly
#
#RAID 0:-Multi EBS ins attaching to work properly(high performance)
#RAID 1:-Imatitat or mirroring each other volums(fault tolerance) 
#RAID 5,6:-Not AWS recommended bcz it consumes high iops
#
#Daynamo Db  max(20million request/sec)  Dyanamo Dax supports encryption but not supports TLS
#At max 1 IGA(interet gateway access) per vpc
#Globally /Content distribution /Worldwide /Caching = Think about CloudFront
###gateway endpoint = Only for S3 and Dynamo DB         for access ec2
#Disaster recovery = Multi AZ RDS
#for performance = Read replicas
#No SQL = DYNAMO DB (key-value pairs) stores large amount data (millions of request/sec & milli sec response time) store session data,high ava,and stored durably  
#Best for mobile/web/gaming/IOT = DYNAMO DB
#Unsure of Database schema = Dynamo DB /Mango DB
#Business intelligence /Data warehousing /peta bytes of data storage = REDShIFT(OLAP)
#Big data processing = EMR(elastic map reducer)
#Rediscache is more advanced than memcache But memcache supports for multi-threading
#Spikes on holidays = Scheduled scaling
#increasing the cpu while touches the limit = target scaling
###Hybrid workload data processing = Storage gateway
#Low latency with less cost = Cloud front
#Media / news = Cloud front @edge location
####No Data transfer charge b/w ec2 and S3 in same region
#durable = S3 bucket                   S3+Dynamo DB:-only this 2srvcs used Vpc endpoints(to give access to ec2)
#s3 multi part upload= obj size more than 100MB should consider this.5gb more use this,speed up the uploads to s3.
#EFS for linux and FSX for windows(supports DFS Namespaces and DFS replication)
#
#VPC peering connection(there is no single point failure for communication or a bandwidth bottleneck) to allow other vpc's to access resources you have in one of your vpcs(connected through gatway or vpn connection)
#high avaiability:-migrate sql to RDS for sql server in a multi-az deployment
#
#The ELB need to high ava & fault-tolerant the app need  path-based url.host based routing & bi-directional streaming using remote procedure call(gRPC):-configure an ALB in front of ASG. select gRPC as protocol version (NLB wont support gRPC)(GWLB supports layer 3 7 layer4 not support for layer7 gRPC)
#prerequistites when routing traffic by route53:-1)A registered domain name 2)the s3 bucket name must be the sm as the domain name
#use alias with a type "A" record set,use alias with a type "AAAA" record set :-will be used to point the DNS name of ALB as it is using ipv4 & ipv6 for communiction
#set up AWS control Tower Landing zone.Enable pre-packaged guardrails to enforce polices or detect violations:-this will create the new accounts in organzation with configurations
#For EBS vol bup automatically :-use AMZ Data lifecycle manager (AMZ DLM) to automate the creations of EBS Snapshots (if dlt it. it can restored recycle bin)
#Budgets only allow you to be alerted & run custom actions if you budgets threshold are exceeded
#cost allocation tags:-used to tag resources with the depertment name and enable we get vallues
#cost explorer:(visualize,understand & manage your AWS cost & usage over a time) this shows the cost of 12months suggestions
#cost & usage report for AWS srvcs that each department is using.the report must contain a breakdown of cost incurred by each department based on tags
#
#lam fun and api gw getting highest peak load error preventing the users from access:-create RDS Proxy b/w the lambda fun & RDS DB instance
#If RDS with multi-AZ deploments primary DB fails then:-The canonical name record(CNAME) is switched from the primary to standby ins
#
#create a custom endpoint for the workload:-the 6 aurora replica 3are using with one depertment & another rest of the DB cluster in items of computation & memory
#Elasticache is a in-memory cache that(unlock microsec latency)
#scale with in-memory but for only read performance) improve the performance of DB the customer get satisified
#
#multi az=decreaces the failover concept (high ava)
#readreplica:-helps the performance of DB (used for read queries) this will decrease the pressure on DB read traffic id diverted aurora(15RR) & RDS(5RR)
#
#variable workloads = spot fleet(calls spot ins & on-demand ins)    spot block:-(1hour - 6 hours without interuption)
#Less than 1sec replication done = Aurora 
#Failover at globle DNS level = Global accelerator
#Infra as a code = cloud formation
#Critical = Fault tolerance
#gaming leader board = elasticache,dynamo db dax(accleration)(srvrless app repositories=for alex +IOT)
#
#percentage = Traget tracking scaling
#time or date = schedule scaling
#we want this many units cw is used for alarm for thresold= simple scaling    multiple threeshold for cw scaling:-step scaling
#forcasting the needy of instances= predective scaling
#
#posix= efs (linux used) efs provides a file system interface.it supports millions of files as requested    efs(supports concurrency) and ebs(does not support concurrency) (network attached)
#piops= ebs (persist data)                                               #network attachment
#instance store= emphermal storage once you stop you loss your data      #Hardware                                             instance store (hardware appliance)
#Nitro-based amz ec2 ins with EBS Provisioned IOPs SSD(i01)Vol attached.provisioned 64,000ipos for the vol
#EBS gp3,gp2(general purpose ssd)=3000iops to 16000iops         (3iops for one GiB)  need 40GiB storage & 1000iops  for RDS (cost less)=(provison 334GiB of GP SSD storage for RDS instances)
#EBS io2Block express=256,000
#io2,io3=64000+       Nitro
#EBS throughput optimized HDD(st1):-500 iops
#EBS cold HDD(sc1):- 250 iops
#
#drag and drop= cloud formation
#Elasticache(supports for static content)(this shows identical or similar datasets from DB bcz that may cause performance slowdowns)(supports encryption & is HIPAA eligible & PCI DSS compliant)and Dynamo Db Dax used to store running leader board 
#
#Multi threading,engine upgrading:-supported Elasticache with memchached
#Elasticache redis cluster mode:-fully managed in memory data store that provide sub millisec latency performance with high throughput
#Redies cluster mode disabled:engine upgrading,high ava & replication for caching layer
#
#Maximum expiry of s3 pre-signed URL is:-7days  (most secured way to give access to specifed obj)
#
#AWS WAF(web app firewall):-protect web apps from common web exploits(layer7 is HTTP) and cyber attacks & SQL injection(handles incoming request to app)(for DDOS protection).(this doesnot support Network LB) can block ip address and countries too. integreated with cloud front,ALB,API gw,Appsync(to protect from cross site scripting)(create a rate-based rule in AWS Waf & associate the web ACL to ALB)
#AWS Shield standard:-maximze app ava & responsiviveness with managed DDOS(distributed denial of srvc) protection safegaurds the app(fake traffic)(SYN/UDP floods,reflection attacks &other layer3/layer4 attacks)
#AWS Shield advanced:-has a lot more power & protection on offer than the shield advance.(24*7)access to AWS DDOS Response team
#AWS firewall manager:-protect resources across accounts in AWS Organization
#AWS Network firewall manager:-protect your vpc layer3 to layer7 protection
#ssm store:-secrete storage for configuration & secrets
#AWS secrets manager:-ment for storing secrets rotation of secrets every x days
#ACM:-AWS certificate manager easily create manage & deploy(TLS certificate)(integreated with aws API,ELB,& cloudfront)
#AWS Inspector:-automated vulnerability management srvc that continually scans AWS workloads for software vulnerabilities and unintended network exposure(on ec2 instance,container imgs,Lambda functions)(Reporting &integration with AWS Security Hub)
#AWS Maice:-dectect & protect your sensitive data in AWS at scale (credit card no.,documents no.) (s3)
####AWS gaurd duty:-Intelligent threat detection & gives remidetions(continously monitor your AWS acc,ins,container,users,DB.protect Malicious attacks)(inputs are vpc flowlogs,cloudtrail logs,Dns logs,EKS Audit logs)
#AWS Trusted advisor:provides recommanding to Reduce cost,improve performance,improve security(cost optimization,performance,security,fault tolerance,service limit)
#
#AWS Secrets Manager(integreated with RDS,REDSHIFT,DOCUMENT DB this rotates DB credentials automatically):-Easily rotate,manage & retrieve DB credentials, API Keys, & other secrets through their lifecycle
#AWS System Manager Parameter store:-provides secure,hierarchical storage(you can store passwords,DB strings,license,SSM documents, & configuration & automation workflow by unique name)
#KMS is used for managing encryption keys & not passwords
#
#AWS Amplify:-Build full-stack web and mobile apps in hours,easy to start easy to scale.
#
#AWS certificate manager:-for Encryption in Transit you use Certificate manager
#EBS & RDS:-the data is encrypted at rest with kms(keys to ins & database vols)
#for encryption in transit we use:- SSL 
#
#simple/step scaling:- just creating by cloud watch alaram threshold according to our traffic give alarm and we have to create the instance (you need to wait for cooldown period before initiating additional scaling activities) deregestriation
#target scaling:- % scaling giving threeshold and when it touches it increases and decreases(this wont wait for cool down period)
#schedule scaling:- certain time or day correctly mainting our servers to customer traffic
#predective scaling:- forecasting the future scaling
#
#AWS Snow family:-secure portable device collect and process data at the edge & migrate data into & out of AWS(offline devices to perform dat migrations)
#Snow cone: 8tb of data transfered
#Snow ball(80TB):migrate large quantities (TB/PB) of data into aws    (one time transfering or moving(snowball used) #the data to cloud 50tb in secure connection &constant throughput b/w dc and app:snowball for intial transfer & AWS dc for on gng connectivity           SNB EDGE COMPUTE:-42TB   this cannot send to glacier directly for that use lifecycle policy
#Snow mobile:migrate ex-bytes of data to the cloud (1EB=1000PBS=1000,000TBS)
#
#cluster placement = low lantency,high throughput one zone 1 rack
#spread placement =to over come faliover max 7 high avaliability    
#partation placement = upto 7 partation multi az 100s of ec2 instance
#
#Disaster Recovery:-Any event that has a negative impact on a  companys business continuity or finances is a disaster (RPO:Recovery point objective,RTO:Recovery time objective)
#backup and restore = high rpo(recover point obj).takes more time        #rto =recovery time obj
#pilot light = a small version is always running in cloud (useful for critical core)
#warm standby = full system is up and running but at minimum size (upon disater we can scale to production load)(5min)
#Hot site /multi site = very low rto,very expensive production scale is running on aws and on-premise. minimal downtime & data loss (active-active) configuration
#
#DMS:-Database Migration srvc:-quickly & securely migrate DBs to AWS. (continuous Data Replication using CDC)
#AWS Schema Conversion Tool(SCT):-convert DBS schema from one engine to another.(you do not need use SCT if you are migrating the sm DB engine)
#AWS Bup:-fully managed srvc(centrally manage & automate bup across aws srvcs)supports cross-region bup & cross-acc bups (support PITR)
#AWS Bup Vault Lock:-(Worm)protect for dlt, even root user cant dlt bup
#AWS Application Discovery srvc:-Plan migration projects by gathering info about on-premises data center (data can be viewed within AWS Migration hub)
#AWS server migration srvc(MGN):-Lift-&-shift solution which simplify migrating apps to AWS (minimal downtime,reduced costs)
#for on-gng replication/transfers:site-to-site VPN or DX with DMS or Datasync
#
#Routing of route traffic:
#simple:- mul values are returned a random one is choosen by the client (no health check)(used anycast ips)
#weighted:- control the % of the requests that go to each resource (health check)
#latency:- redirect to least latency close to users (health check)
#Failover:-(active-passive)one fail another one come(disaster recovery)(health check) 
#Geoloaction:-routing based on user location of your users(health check)(lang)
#Geo proximity:-shift more traffic to resources based on the defined Bais geographic location of user & resource (you must use route 53 traffic flow to use this feature)
#Multivalue:-(the DNS based routing is done using Multi Value routing policy)use when routing traffic to mul resources(health check) #7ec2 instances the organization needs the DNS queries provide the IP address all healthy ec2 insts
#
#S3 storage lifecycle policies:-                     max obj size:-5TB (5000gb)   100mb used 5gb use multi-part upload(parallel upload)
#s3 transfer accelration:-increase transfer speed by transferring file to AWS edgelocation which will forward the data to s3 bucket in target region      (byte ranges)
#s3 inventory to get obj list & use s3 select to fillter your objs
#cors:cross-origin resource sharing:-allow requests to other origins while visting the main origin
#s3-MFA Delete    enable versioning      preventing accedential deletion
#s3 pre-signed urls:-users download a premium video from your s3 bucket(downloading purpose) with highly securly
#s3 glacier vault lock:-(worm)for future edits(helpfull for compliance & data retentaion)     #s3 object lock(versioning must be enabled)(worm)(retention mode compliance:-(no one can dlt or change retention period or shortened))(retention mode goverance:only some users have spcl permissions to change the retention or dlt of obj)
#s3 Access points:each access points gets its own DNS & policy to limit who can access it(easier to manage than complex bucket policies)
####s3 standard:-(used frequently need fast retrive of objs)
#s3 standard-infrequent access(IA):-(used infrequently but need fast retrived of objs in millisec)
#s3 intelligent tiering:-(we dont know when the accessing periode is gng to happen so this is used to automatic life cycle of objs according to use)
#s3 one zone(IA):-(used to save in only in one zone. when the az gone the data will goes)
#s3 glacier instant retrieval:-(long lived archive data accessed once a quater with instant retrival in millisec)
#s3 glacier flexiable retrival:-(long term bups & archives. with retrival option 1 to 12 hours) 1)expedited retriveals(1-5min),2)standard retrival(3-5hrs),3)bulk(5-12hrs)
#s3 glacier deep archive(long term data archiving not accesing frequently & can be retrived within 12hours. used for auditing purpose)
#
#s3 analytics:-decide when to transition objs to the right storage cls(used standard & standard IA)
#SSE-S3:-no automatic key rotation (server side encryption with amz s3-manged keys (keys manged and owned by aws)(objs are encrypted server-side))(enabled by default for new objs stored in AWS)))(AES-256)(x-amz-server-side encryption)(unencrypted objs & objs encrypted with SSE-S3 are replicated by default)
#SSE-KMS(keys handled & managed by aws kms):-automatic keys rotation is possiable(objs are encrypted server-side)(x_amz-side-encryption)(aws:kms)(for objs encrypted with SSE_KMS,you need to enable the position)
#SSE-C:-server-side encryption. keys fully managed by customer. s3 doesnot store encryption keys.(HTTP must be used)(objs encrypted with SSE-C(customer provided)are never replicated)
#CLIENT-side-encryption:-clients must encrypt & decrypt the data themselves before & after sending to s3(customer fully manages the keys & encryption cycle)
#
#If a client makes a cross-origin request on our s3 bucket,we need to enable the correct CORS Header        (do not set the logging buckets to be the monitoring bucket bcz it creates a loop & increase the size)
#
#Decouple:-SQS(queue model)SNS(pub/sub model)KINESIS(real-time streaming model)(this srvcs can scale independently from our app)
#standard queue:- provide at-least-once delivery which means that each msg is delivered at least once (unlimited transactions/sec)(Default msgs retention:-4days max 14days)(can have duplicate msgs at least once delivery,occasionally) 
#SQS-Producing msgs:-The msgs is Persisted in SQS until a consumer dlts it(4 to 14 days)
#SQS-consuming msgs:-poll SQS for msgs(receive upto 10 msgs at a time)
#FIFO queue:-(first-in-first-out)(ordering of msgs in the queue) queue to perserve the exact order in which msgs are sent and recevied (300 msg/sec when you batch 10 msgs/operation supports 3000msgs/sec)(exactly once send capability)(by removing duplicat)
#long polling(wait for a minute) reduces the no.of empty responses by allowing the sqs to wait until a msg is ava before sending a reponse to receive msg request
#short pooling(every 3secs) is a defalut in sqs  3sec proccess the data (this polling checks a subnet of servers and may not return all msgs)(eliminate empty responses by reducing the length of time a connection request remains open)
#change msg visibility(prevent dulication)(this will increase the time of visibilty & the duplicate msg entered less):-change the visibility time out on the sqs queue is set to new value(10min) but in defalut(30sec). if msg is not processed in this time it will appear again max12hours
#dead-letter queue to collect the requests that failed to process                      SQS fully managed msg queue for microservices,distributed systems and serverless apps= asynchronous(decouple) missed Transactions think of message queueing app.
#The web app is not deleting the msgs in the SQS queue after it has processed them          sqs & swf(workflow srvc) used to decouple for apps which make use of both resources
#
#AMZ SNS:-send one msg to many users(the event producer only sends msg to one SNS topic)(create a topic--> create a subscription -->publish to the topic) upto 12,500,000sub/topic &100,000 topic limits
#SNS+SQS:Fan out:-push once in SNS,receive in all SQS queues that are subscribers(fully decoupled,no data loss)(if you want to send the sm s3 event to many SQS sqeues,use fan-out)
#SNS FIFO + SQS FIFO:Fan out:-In case to need fan out + ordering + deduplication
#SNS-msg Filtering:-JSon policy used to filter msgs sent to SNS Topics subscriptions
#
#Kinesis:-makes it easy to collect,process & analyze streaming data in Real-time(ingest real-time data:-app logs,metrics,website clickstreams,IOT telemetry data..)
#Kinesis Data Streams(streaming srvc for ingest at scale):-capture,process & store data streams(retention b/w 1 to 365days)(once data inserted it cant be dlted)(data sm partition goes to sm shard)
#Kinesis Data Firehose(load streaming data into s3/redshift/EfS/3rd party/custom HTTP):-load Data streams into AWS data stores(NEAR Real Time)(supports many data formats,conversions,transformations using AWS Lambda)(easiest way to load streaming data into data stores & analytics tools)capture,transform,& load streaming data into s3,redshift,elasticsearch
#Kinesis Data Analytics:-analyze data streams with SQL or apache flink
#kinesis Video streams:-capture,process & store video streams
#AMZ MQ:-when migrating to the cloud, instead of re-engineering the app to use SQS & SNS we use AMZ MQ (this is a managed msg broker service for) 
#
#AWS STS:- is used to short-lived access token that acts as a temporary security credentials to allow access to you aws resources
#1)EBS volumes support live configuration changes while in production 1)which means that you can modify the vol type,vol size,&iops capacity without srvc interruptions,2)An EBS vol is off-ins storage that can persist independently from the life of an ins
#VPN connection:-used to create a connection b/w the on-premiese & AWS Resources
#
#FSx:-3rd party high-performance file system on AWS
#FSx for Lustre:-is a type of parallel distributed file system for large scale computing (HPC)(can be used from on-premises srvrs (VPN or direct connect))(scratch file system:temp storage)(persistent file system:long-term storage)
#FSx for Windows(file srvr):-fully managed windows file system(supports SMB,NTFS)can be mounted on Linux insts(supports Microsofts Distributed file system (DFS)Namespaces)scales up 10s of gbs,millions of IOPS,100s PB of data. data is backup daily to s3(microsoft active directory)
#FSx for Netapp ONTAP:-file system compatible with NFS,SMB,ISCSL protocol(point-in-time instantaneous cloning(helpful for testing new workloads))
#FSx for OpenZFS:-file system compatible with NFS. move workloads running on ZFS to AWS (upto 1,000,000iops with <0.5 latency)(point-in-time instantaneous clonning(helpful for testing new workloads))
#
#AWS STORAGE GW:-s3file gw,fsx file gw,vol gw,tape gw
#
#deploy an aws storage gw vol gw configured in cached vol mode
#
#storage gw :-bridge b/t on-premises data and cloud data(disater recovery,bup and restore,tiered storage,on premises cache and low latency file access)
#AMZ s3file gw:-s3 buckets accessible using NFS and SMB protocol.recently used data is cached in file gw(supports s3 standard,s3 stansard IA,s3 one zone A,s3 intelligent tiering)(transition to s3 glacier using lifecycle policy)
#AMZ fsx file gw:-native access to fsx for windows file server (smb,ntfs,active directory) local cache for frequently accessed data(usefull for group file shares & home directories)
#vol gw:-block storage using iscsi protocol backed by s3 and ebs snapshots
#tape gw:-bup by physical tapes(virtual tape library(vtl)) bup by s3 and glacier.(bup data using existing tape-based processes & iscsl interface)
#
####consistent iops gp ssd(gp2) root vol and provisioned iops ssd(io1) data vol
#Nat instance:-when a packet traverse outside the local(inside) network, then Nat converts the local pvt ip address to a global pub ip addres. when a packet enters the local network, the global pub ip address converted to local pvt ip address
#
#Aws step function:-build serverless visual workflow to orchestrat your Lambda function
#Aws Iot core:-connect cloud application and other devices easily and securly (supports billions of devices and trillions of msgs)
#
#installation initated by using scripts: user data (1)shell scripts and 2)cloud-init directives 3)script is limited only 16kb 
#Metadata :- host name,events,sgs of ins,
#Run command:- used to manage and configure of existing instances by using remotely executed commands (installing software,running ad hoc scripts)
#Aws config:- used to manage and configure Aws resources (governance & compliance)
#
#Lambda:-excution time 900sec 15min & memory 3008Mb Cost is less (lets you run code without provisioning or managing srvc)
#AWS Fargate with ECS to proceed the data (used when the timing is more then 15min performed to finish)      ecs,ecr,fargate,eks
#Least expensive Ebs vol:-cold HDD(sc1)(IA data sequential data access) < Throughput optimized HDD(st1)(intensive wd,FA) < General purpose SSd(gp2)(balances the price and performance) < Provisioned iop(io1)(16000iops)(high performance & low latency)
#
#Map Reduce process & high throughput large datasets cost less:-use EBS Through optimized HDD
#Aws Batch:-Manages provisioning,managing,monitoring and scaling  your compute jobs
#serverless app model(SAM) is an extension of cloudformation used to package,test deploy serverless apps
#
#Sg:statefull,ec2 level,allow rules
#Nacl:stateless,block ip address,sub lvl,allow rules & deny rules
#
#patterns for elasticache:-
#Lazy loading:-all the read data can become stale in caache
#write through:adds or update data in the cacahe when written to a DB (no stale data)
#session store:-store temporary session data in cache(using TTL features)
#
#instantiating apps quickly:-use a golden AMI(os),Bootstrap using USER DATA(dynamic content),Hybrid(golden AMI & user data(Elastic beanstalk))
#Elastic beanstalk:deploying an app in AWS(automatically handles capacity provisoning,LB,scaling,app health monitoring,increase configuration..)
#s3 hosting website URL:-http://bucket-name.s3-website.aws-region.amzonaws.com or http://bucket-name.s3-website-aws-region.amazonaws.com 
#for getting new objs for replication use s3 batch replication
#we can retrive the IAM Role name from the metadata,but you cannot retrieve the IAM policy    metadata=info about EC2 ins & userdata=launch script of the EC2 ins
#Dynamo DB supported by:-Scalar Types,Document Types,Set Types. therfore, in dynamo DB you can rapidly evolve schemas     Dynamo DB accelerator(DAX):-help solve read congestion by caching (microsecs latency for cached data) dynamo DB streams 24hrs retention  (dynamo DB global tables:-accessiable with low latency in mul-regions (active-active replication))
#
#zonal redundancy is split across mul AZs 2pubsub 2pvtsub total 4 subs 
#in ec2 High packets/sec- and performance of app stack to improve performance:-use enhanced networking
#Waf:block ip address,malicious web attacks,protect against SQL injections & cross-site scripting attacks 
#Hihg performance & ephemeral storage:instance store
#block device mapping:-EBS and instance store
#default Nacl of Vpc = all inbound & outbound traffic is allowed and a custom Nacl all inbound & outbound traffic is denied
#MetaData is data about ins that you can use to configure or mannage the running ins.(host name,events,sgs)
#constantly on an going basis cannot be interrupted or restarted:- Reserved instance selected
#opswork:is a configuration management srvc that provides managed instances of chef & puppet
#In cloud front:field level encryption adds a additional layer of security that lets you protect specific data throughput system processing 
#cloud front:grt for static content that must be ava everywhere        s3 cross region replication:grt for dynamic content that must be ava low latency in few regions
#unicast:-one srvr holds one ip address       anycast ip:-all servers hold the sm ip address & the client is routed to the nearest one        
#global accelerator:-tcp,udp,http(ALB,NLB)
#cloud front can cache the content closer and also reduce and also reduce the load on the webserver
#
#High performance computing(hpc) application this requires low latency and high performance:-use an Elastic fabric adapter(EFA)and deploy ins in cluster placement group
#install software,patches,updates in thousands of instances :-configure AWS systems Manager patch manager to apply the patch to all ec2 instances (windows and linux)
#High throughput and ability to brust (shared file system):-efs and mount the file using NFS
#a system manager Run commannd is designed to run commands across a large group of ins without having to SSH into all your insts and run the same command mul times(this to run a custom command that install the tool on all the ec2 insts)
#Aws config to track configuration changes and AWS cloud trail to record Api calls:team concerned about compliance,governance,auditing and security,Api calls history
#The MYSQL credentials are stored in systems manager Parameter store and update the function code and exection role.
#AWS Snowball edge devices to process the data locally(this can do local processing & edge computing workloads in addition to transfering data b/w local env & the cloud)
#provisioning & managing the resources with minimize operational overhead:- use AWS batch a multi-node parallel job
#
#launch the ec2 ins with amz ebs vol and configure RAID1: will improve the resilient that improve recovery time for the system
#RAID0:-I/O performance is more imp than falut tolerance(get throughput &iops)
#RAID1:-falut tolerance is more imp than i/o performance(safer from the standpoint)
#AWS license manager to manage the software license
#
#Data exchange:- allows gain access to 3rd party datasets across automotive,finance,gming,medical,marketing
#limited set of core srvc and part of infra is running on aws when the time comes for recovery, you can rapidly provision a full-scale prodection env (pilot light)
#High performance storge sol for temporary files (fastest storage option):-multiple instance store vols with software RAID0.
#burstable in efs:-max i/o
#
#AWS pvt 5G:-managed srvc .this makes easy to deploy,operate,&scale your own pvt cellular network
#AWS Wavelength:-embeds AWS compute & storage srvc within 5Gnetworks,providing mobile edge computing infra for developing,deploying and scaling ultra low-latency apps
#
#code effective sol to provide a bup for a dc connection:-implement an IPsec VPN connection and use the the sm BGP(boarder gw protocol) prefix
#
#AWS Appsync:-is a serverless GraphQL & pub/sub srvc
#AWS Lake formation:-is a centralized data repo to be used in m/c learning
#Cloudwatch agent(collects both system metrics & log files from ec2 & on-premises srvr) or   unified agent:- will show swaputilization  metrics in cw
#app expose static pub ip. sm users getting poor performance when accessing the app over the internet:-set up AWS acclelrator and add endpoints bcz GA improve ava and performance of app
#requests to large bursts of traffic:-set up API gw & use AWS lambda function
#ec2 ins & s3 bucket the secure connection b/t this two:-set up s3 bucket police to allow from a vpc endpoint
#Lambda@Edge is a feature of cloudfront that lets your code closer to user of your app. this improve performance & reduces latency
#mysql DB used only several times a week for short periods. The DB required to provide auto instantiation & scaling:-amz aurora serverles
#amz ebs gp ssd(gp2):-3000 iops
#interface endpoint:-Elastice network interface with a pvt ip,uses DNS entries to redirect traffic,APIgw,cloudformation,cw,etc,for security sg used
#AWS Data Exchange:this is just a data marketplace srvc
#ECS+Fargate=serverless & Ephemeral storage
#increase disk space in RDS without impacting the DB performance:-Modify the DB ins setting & enable storage autoscaling
#to decreas the instance loading time in restarting:-migrate the app to an ec2 ins with hibernation enabled
#stop the increase of bill by reserved ins:-Go to the AWS Reserved ins Marketplace & sell the reserved insts,2)Terminate the reserved insts as soon as posible to avoid getting billed at the on-demand price when it expires 
#Block the illegitimate requests with minimal impact on legitimate traffic:-create a rate-based rule in AWS Waf & associate the web ACL to an ALB
#Mysql RDS instance(accessed using profile credentials to your via authesntication token):-Enable the IAM DB Authentication
#for hibrid env(which store AD):-set up SAML 2.0-based Federation by using Microsoft AD Federation srvc(AD FS)
#API GW + Lambda lot of site vistors cming:-Enable Throttling limits & result caching in API GW          #use throttling limits in ApI gw:-protect backend systems & apps from traffic spikes
#
#HTTPS:-API GW    #(security for  acccess in a company):-create an HTTPS endpoint in amz api gw. configure the API GW endpoint to invoke an AWS lambda fun to process the msgs & save the result to an amz dyanamoDB table 
#gw endpoint:-a gw that is a target for a specific route,uses prefix lists in the route table to redirect traffic,s3&dynamo DB,security vpc endpoint polices used 
#
#(EFA)Elastic Fabric Adapter is an Elastic Network Adapter(ENA)this helps in scale,flexibility and elasticity of the cloud for(Hpc)app
#(ENI)Elastic Network Interface is a basic type of adapter. is a logical networking component in a vpc that represents a virtual network card (controls the inbound & outbound traffic for the ec2)
#(ENA)Elastic Network Adapter this provides Enhanced networking,does provide high bandwidth & low inter-instance latency but it does not support the features for a tightly-coupled app that the EFA does. 
#
#large amount of data on windows file shares in on-premise data center to s3 over their direct connection:- AWS Datasync
#(EKS)Elastic Kubernetes srvc: is a open-source &cloud agnostic to safe guard against future changes in cloud
#Athena:- is a srvc that enables data analysts to perform interactive queries in the web-based cloud from s3(used to query JSON in s3)
#the KMS keys used in 2 different buckets & in 2 regions to encrpty & decrpty with sm keys we use:-AWS KMS Multi-Region keys (kms client-side encryption)
#AWS System Manager is a collection of capabilities to help you manage your app and infra running in the AWS cloud.AWS Resources securely scale(newer srvc ment for storing secrets)(automatic rotation of secrets every x days)(ingreated with(sql DBs))
#AWS Systems manager parameter store:-collection to help you manage your apps & infr running in the aws cloud.(secure storage for configuration & secrets)(integration with cloud formation)
#AWS Certificate Manager(ACM):-Easily create,manage & deploy TLS Certificates (automate TLS certificate renewal)(cannot use ACM with EC2)(ACM Integration with API GW)     (ACM-Importing public certificates:No automatic renewal,ACM sends Daily expiration events,AWS Config(to check expiration certicates))
#cloud front(CDN)(static & dynamic content world wide)(edge locations):-(is used for caching & improving latency) decrease the latancy & increase the performance towards the customer      user -> edgelocation -> cloudfront ->app server
#AWS App flow:-is fully managed srvc that enables you to securely transfer data b/t saas & AWS Srvcs .(you can run data flows at a enterprise scale at the frequency on a schedule,business event or on_demand)
#Data sync over AWS Direct connect(most reliable data transfer):- used to secure transfer data from on-premises to aws  
#Kinesis data firehose:-Realiably load real-time streams into datalakes,warehouses,&analytics srvcs
#kinesis data streams:-to collect,process large streams of data records in real-time 
#Kinesis stream:-by default,the data records are only accessible for 24hours from the time they are added to a kinesis stream
#Dynamo Db to stored (rpo=15min) & (rto=1hr):-configure DynamoDb point-in-time recovery,restore to the desired point in time.      DYNAMODB Accelerator(DAX):-Help slove read congestion by caching
#Dynamo DB stream processing:-ordered stream of item-lvl modifications in a table(24 hours retention)
#DynamoDB Global Tables:-make DynamoDB Table accessiable with low latency in multiple regions(active-active replication)
#vpc gateway endpoint:- is used to decreases the cost of data transfering  on-premesis & aws sm region 
#
#when you stop & start the ins by lambda:1)the underlying host for the ins is possibly changed 2)all data on the attached ins-store devices will be lost
#Launcgh configuration is a template that an asg uses to launch ec2 instances           we cant modifi the launch configuration to over come that we have create new one               the old launch configuration is dlted
#EC2 Instance is Billed for:-you will be billed when your reserved ins is in terminated state,& billed when your on-demand ins is preparing to hibernate with a stoping state 
# 
#s3 obj lock governance mode(obj version can be over written):-(worm) this will help you protect the obj but you grant permissions to some users that to change settings or delete the obj 
#s3 obj lock compliance mode(obj version can not be over written):-(worm)here the retention period cant be changed the accout owner also dont have that changing permissions
#
#Dynamo DB global tables:-build on the global amz Dynamo DB footprint to provide you with a fully managed.(multi-region & multi-active DB that Delivers fast,local,r,& w performance for massively scaled,global apps)
#monolithic or decouple loosely couple:- sqs
#instance profile used to pass an I AM role to an EC2 instance for more information ,see I AM roles for amz ec2 in the amz ec2 user guide
#The oranganization want to limit access to this s3 bucket to only users of acc in organzation:-add the Aws PrincipalOrgID golabal condition key with refrence ID to the s3 bucket policy
#
#In Dynamo DB with mimimum feasiable operational overhead:- use create a Dynamo DB table 1)(on-demand capacity mode)              #Dynamo DB scales up & down according to the demand.used in falsh sale (there is no capacity planning and pay pre-request pricing)
#2)Dynamo DB provisioned mood is just like reaching the target with mannul scaling
#
#RDBMS=(SQL,OLTP):RDS ,AURORA-grt for joins security through IAM,sg,kms,ssl in transit
#NOSQL Database:-no joins,no sql:-Dynamo DB(json),elasticache(key/value pairs),Neptune(graphs),DocumentDB(for mongo Db),Keyspaces(for Apache cassandra)
#Data Warehouse:-SQL Analytics/BI:Redshift(OLAP),Athena,EMR
#opensearch:-(json)-free text,unstructued searches(is successor to AMZ Elasticsearch)(doesnt support SQL it has its own lang)
#Ledger:AMZ Quantum Ledger DB(QLDB)(recording financial transactions)(immutable)(no decentralization component)(used to review history of all the changes made to your app data(immutable))
#Time series DB:AMZ Timestream (store & analyze trillions of everts/day)(recent data kept in memory & historical data kept in a cost-optimized storage)(used IOT apps,operational apps,real-time analytics,..)
#Amz Aurora:-data stored in 6 replicas,across 3AZ autoscaling of rr
#Aurora serverless:-for unpredictable/intermittent workloads,no capacity planning needed
#Aurora Multi-master:-for continuous writes failover(high write ava)
#Aurora Global:-upto 16DB read insts in each region,<1sec storage replication
#Aurora M/c L:-perform ML using Sagemaker & comperhend on aurora 
#Aurora DB Cloning:-new cluster from existing one,faster than restoring a ss
#MongoDb:-used to store,query,& index json data.(sm deployment concepts as Aurora)(storage grows 10gb to 64tb)
#Neptune:-fully managed graph DB. graph dataset woulb be a social network(15rr)(fraud detection,recommendation engines,social networking)
#Apache Cassandra is an open-source nosql distributed DB (cassandra query language)(1000s/sec)(pont-in time-recovery up to35days)
#Elastcicache:-requries some app code changes to be used(key/value store,frequent reads,store session data for web,cannot use SQl)
#
#AMZ Athena:-serverless query srvc to analyze data stored in s3 (use standard SQL language to query the files) commonly used with AMZ quicksight for Reporting/Dashboards(use columnar data for cost-saving)
#AMZ Athena-Federated Query:-allows you to run sql queries across data stored relational,non-relational,obj,& custom data sources are connectors that run on AWS lambda to run Frederated queries & stored in s3
#Redshift:-(OLAP)column storage of data & parallel query engine(is based on postgresql,but its not used for OLTP)x performance then other data ware houses  (loading is amz kinesis firehose to redshift,s3 to rs,ec2 to rs)
#Redshift spectrum:-query data that is already in s3 without loading it(must have a redshift cluster ava to start the query then submitted to thousands of red shift spectrum)
#AMZ EMR:-(Elastic map reduce)helps creating Hadoop cluster(big data)to analyze & process vast amount of data (cluster is made of 100s of insts)used for data processing,m/c l,web indexing,big data
#AMZ Quicksight:-serverless m/c L- powered business intelligence srvc to create interactive dashboards (you can share the analsis or the dashboard with users & groups)
#AWS GLue:-(managed extract,transform,&load(ETL))useful to prepare & transform data for analytics(fully srvrless srvc)(convert data into parquet format)
#Kinesis Data Analytics(SQL APP)real-time analtics on kinesis data streams & firehose using SQL
#AMZ managed streaming for apache Kafka(Amz MSK):-Alternative Amz Kinesis (kafka topic with partitions)(TLS in-flight encryption)(KMS at-rest encryption)
#
#IAM Permission boundary:-used to restrict a user or role assiging undesired permission in a main account
#AWS Service control policies:-To enable or disable activity across all accs in organizations
#for push srvcs:-sms,message,email,aws sns              decouple:-sqs
#
#OLAP(online analtical processing):-Redshift is a warehouse and RDS. AWS Glue(ETL) is used to send athena,quicksight,sagemaker,to visualize data in(ML) 
#OLTP(online transactional system):-designed to have fast response time low data redundancy
#
#In Dynamo DB to delete the beyond 30days data :-use TTL attribute in Dynamo DB to delete old Data
#Amazon Lightsail is a virtual server provider & is the easiest way to get started with AWS for developers,small businesses,students,and users who need a sol to build & host their apps in cloud
#
#To monitor swaputilization metrics in cw we need install cw agent on the insts (this is a custom metrics) 1)Basic monitioring(every 5min)not charaged 2)Detailed monitoring(every1min)fee charged #Swap space:- is a space on a hard disk that is a substitute for physiacal memory.whenever our computer runs short of physical memory it uses its virtual memory & stores info in memory on disk. 
#busrtable performance instances provide a baseline level of cpu performance with the ability to burst above the baseline (enhances CPU performances)
#
#create a read replica(supports for dynamic content) of the DB to avoid Bottlenecks 
#create multi-master set-up to slove Bottleneck issues in Database(continues ava)
#
#Amazon Redshift spectrum to query the data in s3 directly & join that data with the existing data in same redshift.use quicksight to build the visualization
#Aws direct connect:-you can connect to all aws resources in an aws region data transferring to cloud
#In kinesis Data Streams:-a single shard is limited to 1Mb to 1000msgs/sec
#Transit gw:- connecting mul vpcs in same region 
#virtual private gw to aws & customer gw on-premises in site-to-site vpn connection
#API gw:-fully managed srvc that makes it easy for developers to create(create,maintain,&secure api's at any scale)(lambda(run code without thinking about srevers or clusters ))
#
#(remote to vpc comm)AWS Site-to-site VPN:-you can enable access to your remote network from your vpc by creating this connection and configuring routing to pass traffic through this connection
#(on premises to vpc comm):-AWS Transit gw:-connect vpcs and on-premises network through a central hub
#(vpc to vpc comm)(there is no single point failure):-vpc peering connection b/t vpcs.update the route tables of each vpc to use the direct connect connectionfor inter vpc communication
#
#storage gw using cached vols. use storage gw to store data in s3 while retaining copies frequently accessed data subnets locally (less cost and fast retrival in cloud space)
#configure DX connections at multiple DX loaction:-to connect aws and on-premises data center (this connection is durable)
#(PII) encrypted at rest to comply with compliance standards:-confgure AMZ Elastic Block Store(ebs)encryption and AMZ RDS encryption with key management srvc(AWS KMS)keys to encrypt instance & DB vols
#reading prbm:use readreplica & aurora serverless bcz auto change according to traffic
#The app poor response in lunch hours least amount of setting possible:-move app to elastic beanstalk. configure load-based auto scaling & time-based scaling to handle scaling during lunch hours
#use amz RDS for sql server with multi-az deployment & read replicas, & restore snapshots from RDS for the test database:-the dev need create a test DB for production. users will encounter delay during this time period
#AWS Datasync:-used to transfer the apps to aws 100tbs data shared file system  (must be capable of coping with brief gaps in internet access)used for continue data transfer b/t on-premises to s3
#migrate oracle-aws aurora app must transfered sequentially. throughput the entire migration process the data must be maintained in sync across both DBs:-use AWS schema conversion tool with aws database migration srvc(aws dms) using a memory optimizes ins. create a full load plus change data capture replication task & table mapping to select all tables   
#(HIGH ava & durability)RDS Multi AZ deployment:-synchronous replication-high durable. only DB engine on primary ins active. automated bups from standby. always 2 azs in region. automatic failover to standby when problem comes. 
#(improve read performance)(to split read & write workloads)RDS Read Reaplica:-Asynchronous replication-high scalable. all read replicas are accessiable & can be used read scaling. no bup by default. within AZ,cross-AZ,or cross-reg. can manually promoted
#
#App flow(saas integration):-AWS(redshift,s3,snowfalke) integrated with saas(software as a service)(salesforce,stack,) the appflow will be used. (alternate to Public API) use cases: data enrichment
#AWS Lakeformation(is a central place to have all your data for Analytics purpose)(enable self srvc analtics across your oraganization. (combine structured & unstructured data in data lake)secure & given your DL at scale):- used to build,manage, & secure Data lakes in days. import data from other external sources(using JDBC). transform data:AWS Glue used convert written in cloumanar format parquet&orc for better performance(s3,rds,non-relational DB)---->lakeformation----->(athena,redshift,EMR)
#Data warehose:-is primarly holding structured Datasets(pdf,docs,imgs,audio)
#AMAZON Wavelength:-(very low latency & high performance)for ex:gaming applications (is an infra offering optimized for mobile edge computing apps) this have wavelength zones (this gives EBS gp2 vol for persistent block storage) (supported by ec2,vpc,Ebs,auto scaling,Eks,Ecs,Ecs system manager,cw,cloud trail,cloudformation,Alb)(it wont use 5g network)
#AWS Data Excahange:-(data apis,data files,data tables) global app ----> api call -----> third party data
#
#AMZON Timestream(is always encrypted):-DATA is a sequence of data point recorded over a time interval for measuring events that change over time.(ex:stock price overtime,temp measurements overtimme). can store & analyze trillions of events/day (keeps recent data in memory)(serverless,cost effective)iot device ---->AWS iot core -----> AMZ timestream ------> dashboard srvcs(quicksight,amz sagemaker,grafana,JDBC) (nano sec granularity)(this has various level of certifications(HIPPA,PCI DS,FedRAMP))
#AWS Proton:-(is a deployment workflow tool for modern apps. it can be used to manage infra as a code(iac) templates build using tools like cloud formation or terraform)enables platform teams to connect &coordinate diff tools your development teams need for infra provisioning,code deployments,monitoring & updates(this is a centralized solution for platform & developer teams)dev can us e proton as a self-srvc interface to create infra & deploy thier project. this can do patch updates
#Amazon Amplify(forword & backword compatible):-build full-stack web & mobile apps in hours. Easy to start,easy to scale(is a complete sol that lets frontend web & mobile developers easily build,ship,&host full-stack apps on AWS,with the flexibility to use the breadth of AWS srvcs)(supports ios,android,web,flutter,& react apps for  web app react,angular,js). if a wb apps & static websites that can be accessed directly from console. hosted on amplifyapp.com subdomain. (free tier 1000 build min  & 15gb/month)
#
#ECS:-AMZ ELASTIC CONTAINER SRVC(AMZ's own container platform)(ECS TASK)(AWS takes care of starting & stopping)(supports for ALB,NLB)(fargate + ECS=serverless)(auto scaling uses target tracking,step scaling,scheduled scaling)
#EKS:-AMZ'S managed kubernetes srvc(open source)way to launch managed kubernetes cluster on AWS (alternative to AWS)(Kubernetes is cloud-agnostic(can be used in any cloud-AWS,AZURE,GCP))(supports on-demand &spot ins)(storage EBS,EFS,FSx for Luster,AMZ FSx for Netapp ONTAp)
#AWS Fargate:-AMZ's own serverless container platform (works with ECS & EKS)you jst create task definations that increase automatically
#AMZ ECR (Elastic container Registry):-Store continers imgs(public repo & pvt repo)fully integreated with ECS & bup by s3
#AMZ ECS LB:-(supported ALB)(NLB recommended for high throughput/high performance)(ELB supported but not recommended)
#ECS Data vols(EFS):-this works for both EC2 & Fargate (used for persistent multi AZ shared storage for your containers) (AMZ s3 cannot be mounted as a file system)
#
#Cloud watch metric using we get network packets out of an ec2ins,Disk Read activity of an ec2 ins,Cpu utilization of an ec2 ins.
#Cloud Watch custom metric (cw agent must be installed)to get this details:-Memory utilization,disk swap utillization,disk space utilization,page file utilization,log collection
#Enhanced Monitoring(need to install cw agent) metrics are stored for 30days in cw logs. it is used for detailed monitoring for every 1min (not supported for m1 small & gov cloud in us-east region)
#
#CIDR:-Classless inter-Domain Routing(a method for allocatng IP addresses)/32(1ip)(no octet changed)/0(all ips)(all octet changed)/26(64ips)/24(256ips)(last octet changed)
#private ip allow (10.0.0.0)big network. 172.16.0.0(AWS Default VPC inthe range).192.168.0.0(home networks)    rest of the ip addresses on the internet are public
#VPC:-Virtual private cloud(5vpcs in a region)(min size/28. 16ips)(max size/16. 65536ips)     5ip addresses are AWS reserved (1st 4 & last 1) 1vpc=1igw
#NAT=Network Address Translation (source & destination check)       Nat ins:manged by you (pre-configured Linux AMI is available)    NAT gw manged by AWS:is resilient with single AZ
#sg insts lvl,supports allow rules,stateful(applies to an EC2 ins)       NACL(netork access control list):subnet lvl,supports allow & deny rules,stateless,automatically applies to ec2 instances in subnet
#VPC endpoints:(interface endpoints(pvt link)(support site-to-site vpn or direct connect))(Gateway endpointw(supports s3 & dynamo db))
#vpc flowlogs:-capture information about IP traffic gng into your interfaces(FL stored in s3 & cw logs)
#AWS Site-to-Site vpn:aws side(virtual private gw),customer gw on on-premises side (enable route propagation for the virtual pvt gw in route table)(in sg ICMP Protocol)
#AWS vpn cloudhub:-provide secure connection b/w mul sites,if you have mul vpn connection (this connection goes over the internet)
##Direct connect(DX)(mvs GB of data to the cloud over pvt secure network):-provides a dedicated pvt connection from remote network to your vpc(supports ipv4,ipv6)  (Data in transit is not encrypted but is pvt)(AWS DC+VPN provide an IPsec-encrypted pvt connection)(for bup you can use a DC or site-to-site VPN connection)
#Transit Gw:-for having transit peering b/w thousands of Vpc & on-premises,hub-&-spoke(star)connection(supports IP Multicast)
#Vpc-traffic mirroring:allows you to capture & inspect network traffic in your vpc (used for content inspection,threat monitoring,trouble shooting)
#IPV4:provide 4.3billion addresses     IPV6 provide 3.4*10^38 unique ip addressess(IPV6 no pvt range)   (IPV4 cannot be disabled for your VPC & subnets)(Egress only internet GW used for IPV6 only)
#AWS Network firewall:-protect your entire AMZ vpc(layer3 to layer7 protection)(this use the AWS Gateway LB)(to protect against network threats)
#
##Elastic network Adapter(ENA):-EC2 Enhanced Networking(SR-lov)(higher bandwidth,higher PPS,low latency)
#ELAstic Fabric Adapter(EFA):-imroved ENA for HPC,only worlds for linux (tightly coupled workloads)used MPI standard
#
#AWS Batch:-supports Multi-node Parallel jobs, enables single jobs that span multiple EC2instances.fully managed batch processing at any scale(launch ec2 insts or spot ins)
#AWS Parallel Cluster:-Open-source cluster management tool to deploy HPC on AWS.(Automate creation of VPC,SUB<CLUSTER TYPE & INSTS TYPES). ABILITY TO enable EFA on the Cluster(improve network performance)
#AMZ SES:-Simple Email srvc (fully managed srvc to send emails securely,globally at scale)(used for transactional,marketing & bulk email communications)
#AMZ Pinpoint:-Scalable 2-way(outbound/inbound)marketing communications srvc (scales to billions of msgs/day). Ability to segment & personalize msgs with the right content to customers
#systems manager:-ssm session manager:-Allows you to start a secure shell on your EC2 & on-premises srvrs(supports linux,mac,&windows)
#system manager-Run command Execute a Document(=Script)or just run a command (Run command across multiple insts)
#system Manager-patch manager:-Automates the process of patching managed insts(os updates,apps update,security updates)
#Elastic Transcoder:-is used to convert mediafiles stored in s3 into media files in the formats required by consumer playback devices
#AMZ Appflow:-fully managed integration srvc that enables you to securely transfer data b/w software-as-a-srvc(saas) apps & AWS
#
#AMZ Cognito:-give users an identity to interact with our web or mobile app 1)cognito user pools:-sign in functionality for app users   2)cognito identity pools(federated identity):-provide AWS credentials to users to they can access AWS resources directly (they get temp credentials)(then users can access AWS srvc directly or api gw)
#cognito userpool:-create a serverless DB of user for your web & mobie apps
#AWS IAM identity center(successor to AWS single sign-on):-one login for all your AWS ACC in AWS organizations
#AWS CloudTrail:-provides governance,compliance & audit for your AWS acc.it is enabled by default(get an history of events/Api calls made with in your acc.)(90days retention after send to s3)
#
#instance metedata consists of data like ins-id,ami id,pub hostname,ipv4 address, etc which is ava from the running ec2 inss. meta-data
#
#API keys  user must provide the code for the lam fun that rotates the secrets
#Kinesis stream:-the default retention period of the data stream is set to 24hours only.& hence the failure
#To discover a queue lenth:-Approximate no.of msg visible 
#AWS Artifact:-To view the security reports as well as other AWS Compliance-realated information
#KMS:-only used for encryption    AWS systems manager parameter store(provide secure storage srvc):to keep DB credentials,passwords,license and encrypt with KMS.     #AWS Secrets manager srvc that helps you protect acess to your apps,srvc & IT resources.(enables you to easily rotate,manage,& retrive DB creditials,API keys)
#cw:-monitoring srvc.    cloud trail:-records all API calls & provides event history of your AWS acc activity.  AWS X-Ray:-helps you debug & analyze your microsrvcs apps with request tracking so we can find root cause of issues.  AMZ Redshift Spectrum:-enables you to query & analyze all of your data in s3
#identity frderation & role-based access control roles in corporate active-directory:-AWS Directory srvc AD Connector,& IAM Roles
#use throttling limits in API GW (1000request/sec REST API and Brust upto 2000r/s):- when they receive a 429HTTP response the API gw retry calls automatically.      #API gw:-integrated with (AWS Lambda,AMZ Kinesis,EC2,DYNAMO DB)
#IN cloud front:-signed URL and signed cookies:-allow you to control who can access your content         #blocking countries to apps should ideally be done at cloudfront level (by using goe-restriction)
#IN API gw how can you protect the backend systems of the platform from traffic spikes:- use Enable Throttling limits & Result Caching in API gateway   
#The Relaational DB with a Recovery point objective of 1sec & Recovery Time Objective <1min:-use Amz Aurora Global Database
#AMZ Quantum ledger DB:-is a fully managed ledger DB that provides a transparent,immutable,&cryptographically tranaction log
#1)The Convertible Reserved ins allow you to exchange for manager convertible reserved ins of a diff ins family
#2)unused Standard reserved ins can later be slod at the Reserved ins Marketplace
#create an AMZ SNS topic & configure 2 AMZ sqs queue to subscribe to the topic. grant Amz s3 permissions to send NOtification it SNS & update to use the new SNS topic.  
#The EC2 ins launched from the oldest launch configuration:-will deleted 1st in default termination policy
#(To minimize overhead & cost we consider this)AWS Lake formation is used to consolidate data from multiple accs into single acc.   
#THE data is stored in nfs vol & the bup of nfs vol are compliance requirements:-Install an AWS storage gw file gw hardware appliance on premises to replicate the data to AMZ s3(bcz hardware(is already loaded with storage gw software) can send data to s3 )
#Gateway endpoints:-this free and connectivity to s3 & Dyanamo DB (without requiring Internat gw or NAT gw) Ecs to s3 to uploaad photos
#create a read replica & connect the business reports to it(bcz it increase performance of app) only can read no write option in RR. 
#clone the production data into test environmenrt:-take EBS ss of the production EBS vol.Trun on the EBS fast ss restore feature on the EBS ss. Restore the ss into new EBS vols.Attach the new EBS vols to EC2 insts in the test environment
#on-premises to aws terabytes of data 1gb of internet & 72 hours deadline:-establish a VPN connection b/w vpc & the company DC 
#if the NAt gw not giving  internet access what has the problem:-1)the outbound rules on the sg Attached to the ec2 insts are configure incorrectly 2)the Route tabes in the vpc are configured incorrectly 
#
#RDS DB transit encryption is (SSL certificates).     in REST(KMS)
#
#AWS Batch(no charge):-workloads on spot ins & AWS Fargate           Lambda allows 5 layers in a function. layers are immutable. Lambda supports sources event:-DynamoDB,sqs,sns,cw event,API GW,AWS IOT,kinesis,cw logs
#sg rules can reference by IP or by SG     EC2 instance connect works only for AMZ linux2
#spot block:-1 to 6hrs with out interrptions (cancel the request and terminate insts)   #spot fleet:-set of spot + on-demand  #ipv4:-online(3.7billion diff address in pub space )  ipv6:-IOT(internet of things) 
#Lambda@Edge:-IT is the feature of Cloudfront which allows you to run your code closer to the location of users of your app.(improve performance & latency) 
#EKS:-is a srvc that enables users to manage kubernetes apps in the AWS or on-premises
#ECS:-is a regional container orchestration srvc like Docker that allows to excute,stop & manage containers on a cluster (task defination Json format) (ECS main uses microsrvcs(decouple),batch jobs(short-lived packages))
#ECR:is a managed srvc that allows users to store,manage,share & deploy container imgs & artifacts.mainly integrated ECS,EKS,Lambda & Fargate.  
#AWS Bup:-is a secure srvc that automates & governs data bup(protection) in the cloud & on-premises 
#AMZ Cognito:-used for authentication,authorization,& user managemnt for web or mobile apps
#cloud front origins:-enhanced security with cloud from(OAC)
#cloudd front:-(global edge network)great for static content must be ava for every where       s3 cross region replication:-great for dynamic content low-latnency in every region
#cloud front GEO Restraction:-(Allow list)  (Block list)  block or host in countries 
#cloud front invaldations:-get refreshed content after the TTL has expired
#AWS Global Accelerator:-2anycast ip send traffic directly to edge locations (EL sends traffic to your app)works with eip,ins,ALB,NLB, (TVCP,UDP)(gaming,iot)
#cloud front is used software update files they'r static(never changing)(easy way to make an existing app more scalable & cheaper)  
#CW logs can send logs to:-AMZ S3(exports),Kinesis Data Streams,Kinesis Data firehose,AWS Lambda,ElasticSearch
#CW Logs-S3 Export:-log data can take upto 12hours to become available for export
#CW agent on EC2 to push the log files 
#CW Logs Agent:-can only send to CW Logs
#CW Unified Agent:-collect additional system-level metrics such as RAM,Processes,etc(CPU,Disk Metrics,Ram Netstat,PRocesses,Swapspace)
#AMZ Eventbridge(formerly CloudWatch Events):-Schedule:cron jobs,Eventt pattern:Event rules to react to a srvc doing something
#AWS Cloud Trail:-Provide Governance,compliance & audit for your AWS Account.(An history of events/API calls made within your AWS Acc)(SDK<CLI<Console,IAm users & IAM roles)   (Cloud Trail Insights:-to Detect Unusual Activity in acc)  (cloud trail events stored for 90days in CT)
#AWS Organization:-Global srvc(allows to manage multiple AWS Accs)
#AMZ Cognito:-give users an identity to interact with our web or mobile app
#Cognito User pools:-sign in functionality for app users
#Cognito Identity pools(Federated Identity):-provide AWS credentials to users so they can access AWS Resources directly
#AWS IAM identity center(successor to AWS Single Sign-on):-one login for all AWS Acc in Organizations (SAML 2.0-enabled apps)(Windows ins)
#Microsoft Active Directory(AD):-(Windows srvr with AD Domain srvcs)(Centralized security mangement,create acc,assign permissions)tress(group) in forest (AWS Managed Microsoft AD,AD Connector,Simple AD)
#Encryption in flight(SSL):this certificates help with encryption(HTTPS)no man in the middle attack
#Server side Encryption at Rest:-the encryption/decryption keys must be managed somewhere & the server must have access to it
#Client side encryption:-data is encrypted by the client & never decrypted by the server
#Encryption for an AWS srvc:-KMS (never ever store your secrets in plaintext,especially in your code).1)AWS managed keys(keys automatically rotated every 1year),Customer managed keys(CMK)(must be enabled automatic every 1year),Customer manged keys imported(only manual rotation possible using alias)
#Cloudformation:-is a declarative way of outlining your AWS infra, for any resources 
#
#AWS Control Tower:-To launch a Landing zone to automatically provision & configure new accounts through an account factory.utilize the AWS CT dashboard to monitor provisioned accounts across your enterprise.
#
#AWS Personal Health Dashboard:-is the single place to learn about the ava and operations of AWS srvcs(gives you a personalized view into the performmance & ava of AMZ web srvcs)
#AWS service Health Dashboard:-you can overall status of AWS srvcs(about your particular AWS acc or organization)
#6 ec2 ins mean 3ec2 in 1az,3ec2 in 2az,3ec2 in 3az falut tolerance & high ava
#set the iops to 500 then maintain a low queue length:-the (HPC) with provisoned iops (process transaction-intensive,low latency workloads) the size of each vol is 10GiB
#create a new launch configuration with the new ins type & update the ASG:-(to change the ins type t2.micro to t2.2xlarge)
#inspector:-only for ec2 insts,container imgs,lambda functions (continuous scanning of the infra only when needed)                        one NACL = one subnet (newly created NACL will deny everything)(NACL are grt for blocking ip address at sub lvl)(100 for allow & 100 for deny)
#direct connect + VPN =provides an IPsec-encrypted pvt connection (site-to-site VPN connection is bup for direct connect fails)
#cloud formation is a declarative way of outlining your AWS infra, for any resources.(iAC)
#
#stephan maarek:- 30Aws services  SAA-C03
# 
#dynamicc websites or (PHP,Javascript)(server-side scripts) for adjust the capacity cost low and routed in sub domain:alb,asg              #sub domain:-alb
#static websit or (HTML,css,)client-side javascript code low:-create an Amz s3 bucket & host the websit there
#for storing of 10TB of storage high performance use (EBS) (s3)for durable data storage (s3 glacier)for archival storage         instance store can only 1.8TB of data only for that reason we using (EBS) 
# 
#EC2 Instance connect:-works only out-of-the-box with Amazon linux2.make sure that port 22 is opened
#spot block:instance during a specified time frame 1 to 6 hours without interruptions
#spot fleet:-set of spot ins + on-demand ins (this will allow us to automatically request spot ins with the lowest price)   ipv4(3.7 billion diff addresses) user online. ipv6(used iot)    pvt ip for internal network    pub ip for www
#ENI(elastic network interfaces):-logical component in a VPC that represents a virtua network card     EC2 hibernate:-then in-momery state is preserved (then the app starts get warmed up & that can take time)(the root EBS vol must be encrypted)(on-demand,reserved & spot ins)hibernated only 60days
#AMI will create EBS ss AMI is customization of  EC2 instance (built for specfic region & can copied across regions)(a pub AMI,your OWN AMI,An AWS Marketplace AMI)(we can launch instances from other AMIs)         EBS multi attach(1 ebs vol attach to multiple ec2 ins in same AZ)16instances at a time
#EFS(compatible with linux based)works with Multi AZ (encryption KMS)(posix)         GLB use(GENEVE protocol on port 6081)
#sticky sessions:-works on Clb,Alb         cross zone lb:enabled by defalut ALB, & disabled by default Nlb,Clb   ssl certificate (transit (in-flight encryption))
#SNI:-client can use sni to specify the hostname they reach(loading multiple ssl certifacte onto one web server)(works with ALB & NLB)(supports multiple listeners with multiple ssl certificates)
#connection draining:for CLB      Deregistration Delay:-for ALB & NLB
#for RDS RR within sm region you dont pay that is free
#RDS:entire DB & the os to be managed by AWS(no ssh)
#RDS Custom:-full admin access to the underlying OS & the DB
#Elasticache involves heavy app code changes-           redis cache security:-redis auth(supports ssl in flight encryption)  Memcached(supports SASL based authentication)
#DNS:-ip to human friendly hostnames        except for alias records,TTL is mandatory for each DNS record  (you cannot set an alias record for an EC2 Dns name)      DNS does not route traffic it only responds to the DNS queries
#
#bucket policy is used to give access:-user lvl,acc lvl.     i am polices:-user lvl        ACLS:-acc lvl
#user data:-by default runs only during boot cycle at first launch, by default scripts entered as user data are executed with root user privilleges              
#user data:-to customize the dynamic installation part at boot time,create golden AMI with static installation components already setup
#sg can be associated with a NAT ins,NAT ins supports port forwarding,NAT ins can be used as a bastion srvr
#copy data from source bucket to destination busting using the AWS s3 sync command,set up s3 batch replication to copy objs across s3 bucket in diff regions using s3 console
#network configuration for 2 tier app having pub web srvr & pvt database srv Not supported by the VPC console wizard:-vpc with a public sub only & AWS site-to-site vpn access
#improving performance for data delivery speed b/t producers & consumers:-use enhanced fanout feature of kinesis data streams
#vpcs to all departments using apps that need a high degree of interconnectivity:-use vpc sharing one or more subnets with other aws accs belonging to the sm parent organization from aws organizations
#the ebs volume was configured as the root vol of amz ec2 ins.on termination of the ins,the default behavior is to also terminate the attached root vol
#use global accelerator to distribute a portion of traffic to a particlar deployment:-2days left for annual thankings sale to commence
#s3 always returns the latest version of the obj
#SQS fifo :-make sure that the name of the FIFO queue ends with the .fifo suffix,dlt the existing standard queue and-recreate it as a fifo queue,make sure that the throughput for the target FIFO queue does not exceed 3000,msgs/sec
#throttles requests in case of sudden spikes handled by:-amz api gw,amz sqs,amz kinesis            company on various authentication/authorization mechanisms that aws offers to authorize api call built in user management:-use amz cognito user pools 
#can not be used for boot vols:-throughput optimizes HDD(st1),cold HDD(SC1)         general purpose SSD(gp2),provisioned SSD(1o1) instance used to boot volume
#s3 transfer acceleration:-need not to pay for using this
#cmk min waiting period is 7days after dlting that we can recover it with in 7days
#Set up an Aurora multi-master DB cluster:for cannot afford any downtime for DB wirte operation.            kinesis agent cannot write to a kinesis firehose for which the delivery stream source is already set a kinesis data streams 
#
#Well architect 6pillars:-operational excellence,cost optimzation,performancy efficiency,security,reliability,sustainability
#Trusted advisor:-cost optimization,performance,security,fault tolerance,service limit 
#
# 
#  
#More topics introduction by stephen maarak 
#•	Incident Response - with an overview of GuardDuty for threat detection, Detective, AWS Security Hub, Amazon EC2, and how to deal with compromised AWS credentials, and an AWS Abuse Report
#•	Logging and Monitoring - such as Amazon Inspector, AWS Systems Manager, CloudWatch, EventBridge, Athena, CloudTrail, Macie, and Virtual Private Clouds (VPCs)
#•	Infrastructure Security - such as Bastion, Endpoint, PrivateLink, NACL & Security Groups, CloudFront, WAF, Shield, API Gateway, Artifact, Network Firewall, and SES
#•	Identity and Access Management (IAM) - Overview of all the Policies, MFA, STS, Organizations, Cognito, Directory Services, and Control Tower
#•	Data Protection - CloudHSM, KMS, Secrets Manager, Elastic Load Balancing, Network Load Balancer, ELB SSL, and AWS Certificate Manager
#•	Other Services - Direct Connect, AWS Signer, CloudShell, RDS and Aurora Security, IoT Core Security, and Security services like ECR, Lambda, Glue, Workspaces, and Redshift
 
# IPADDRESSGUIDE:- to calculate the ip range by using a website
# 
#achieve that certification by step by step:-
#1)go to aws website and check syllabus and see sample questions
#2)pick a course (udemy) #stephen maarak  (23 sections will be there in course)
#3)FAQ'S and   White papers
#4)Re_compare with the syllabus
#5)go for practice exams  
# 





