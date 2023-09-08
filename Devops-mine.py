#python life:youtube.
#cloud computing:srvc model(saas)(paas)(iaas),deployment model(pvt cloud)(pub cloud)(hybrid cloud)(community cloud)           (pay as you go model)
#AWS advantages:-simple automated scheduling,pay as you go pricing,security,streamlined disaster recovery,automated multi region bups,speed & agility 
#water fall method:while creating a app we cant get back or update becz it is a continous flow (step by step)         Agile:by this we can modife easily. for this the devops came into picture
#
#Devops:-Dev:-plan,code(git,gitlab),build(maven,gradle),test(junit,selinium)   ops:-release(jenkines),deployi(docker,aws),operate(ansible,kubernetes),monitor(grafana,promethous)           server=instance=ec2   sudo su,sudo -i to got to root user
# 
#Git(coding):-is a version control system(vcs) or source code management(scm). & used for track the changes in files,free & open source,they can handle large projects efficiently.   
#git stages:-working directory,git add-->staging,git commit-->repository(local repo)(central repo)(remote repo)           work flow git:- local repo->working area->stagging or indexing->local repo->remote repo.
#git installation:-(in ec2)sudo -i,yum install git -y,git init .,clear to clear the desk,ll to check the long list,ls -al now we get hidden files also visable. 
#create a file:-touch filename,cat>filename,write somthing,enter control d. git status(files in untracking),git add filename(now file in track(staging)),git commit -m "filemsg" filename,git log  (this we have done in root user)
#(now we are configuring a user):-git config user.name "sagar",git config user.mail "sagar@gmail.com", touch f2,cat>f2,write something,enter control d,git add f2,git commit -m "file2" f2,git log (now we can see the root user & user commits (filename & f2))
#touch sagar{1..4}(now4 files created),git add .(now all files tracked),git restore --staged .(now all files will goto untracked state),git add sagar* (now all sagar files tracked). git commit -m "sagar commits" sagar* (now sagar files are commited)
#now ignoring content:-(useful when you dont want to track some specific files then we use a file called .gitignore) touch ragu{1..4},ll,ls -al,git status,vi .gitignore,i,ragu*,:wq!,
#Git branch:-represent a independent line of development. (the default name in git is MASTER)
#To see current branch:-git branch. To add a new branch:-git branch branch-name. To switch branches:-git checkout branch-name. to create & switch at a time:-git checkout -b branch-name. To rename a branch:-git branch -m old new. To delete a branch:-git branch -d <branch>    or -D=for force dlt
#For restoring Dlted files in git:-git restore disha* (now all disha files restored),ll    #moving back to untracked files:-git restore --staged shashi*,git status          (only from one branch we can dlt & rename another branch.we cant dlt current branch)
#  rm -rf .git                            when the dir have sm files then we have to
#  274  cat > file1                                     local reop--> stagging repo--> working repo--> remote repo
#  275  rm -rf file1                       remove the file
#  276  ls                                 list the files & directories
#  278  mkdir 123                          creating a director         rmdir name (for removing the dir)
#  279  cd 123                             for changing directory      cd .. (to go parent dir)
#  280  touch file123                      create a file (this are empty files) 2nd type
#  281  ls                                 cp f1 f100(for coping the file data to another file) 
#  282  vi file123                          vim file name create & write the data in file escp:wq! 3rd type
#  283  cat file123                         to read the file
#  284  cat > file456                       create a file & write the data   *cntl d  save & come out  1st type
#  285  ls                                  ls -l or ls -la(for long files with permissions) ls -a(shows hidden files)  ls -l f6(to know 1 specific file details)
#  286  cat file456                         touch .f6(this create hidden filles)
#       pwd                                 present working directory or print working directory   
#  287  git init                            ls -lt(for knowing the time stamp for created)
#  288  git status                          whoami(to know user)
# n289  git add*                            sudo su or sudo su root(super user do)
#  290  git add *                           cal(calender)    data(data)      (file permissions)--r(read4) --w(write2) --x(excute1)     total 7    ---(owner(u))---(group(g))---(others(o))    +-=
#  291  git status                          chmod 764 f6(for changing the permission of a file)
#  292  git commit -m 'single commit'       headd -3 f7(for seeing 3lines in file)  tail -4 f7(for seeing last 4 lines in file)  head -5 f7 | tail -1(we can see only line5 in file)
#  293  git status
#  294  git log --oneline
#  295  git remote add origin https://github.com/sagarragas07/testrepo.git
#  296  git push -u origin master
#  297  ls
#  298  git clone https://github.com/sagarragas07/testrepo.git
#  299  ls
#  300  cd testrepo/
#  301  ls
#  303  cd ..
#  304  ls
#  305  git fetch
#  306  ls
#  307  cat file123
#  308  git branch -a
#  309  git checkout  remotes/origin/master
#  310  ls
#  311  cat file123
#  312  git checkout master
#  313  ls
#  314  git branch -a
#  315  git merge  remotes/origin/master
#  316  ls
#  317  cat file123
#  318  git pull
#  319  ls
#  320  cat file456
# 321  history
#
#GitHub Actions is a continuous integration & continuous delivery(CI/CD)platform that allows you to automate your build,test,& deployment pipleine.you can create workflows that build & test every pull request to your repository, or deploy merged pull request to production. This goes beyond just DevOps & lets you run workflow when other events happen in your repository. 
#Actions:-is a custom application for the github actions platform that performs a complex but frequently repeated task. An action can pull your git repo from github,set up the correct tool chain for your build environment, or set up the authentication to your cloud provider.(you can write your own action or you can find actions to use in github marketplace.)(uses YAML syntax)(Each wf is stored in separate YAML file in your code repo.)
#
#Git Commands:-git add(add file content to the index),git archive(create an archive of fils from a named tree),git bisect(use binary search to find the commit that introdcued a bug),git branch(list,create,dlt branches),git checkout(switch branches or restore working tree files),git cherry pick(apply the changes introduced by some existing commits),git clean (remove untracked files from the working tree),git clone(clone a repo into a new directory),git commit(record changes to the repo),git describe(give a obj a human readable name based on an ava ref),git diff(show changes b/t commits,commit & working tree),git fetch(Download objs & refs from another repo),git grep(print lines matching a pattern),git init(create an empty git repo or reintialize an existing one),git log(show commit log),git merge(join 2 or more development histories together),git mv(move or rename a file),git pull(fetch from & integrate with another repo),git push(update remote refs along with associated objs),git rm(remove files from the working tree),git show(shows various types of objs),git status(show the w statsu),git stash(stash the changes in a dirty working directory away),git switch(switch branches),git config(get & set repo or global options),git remote(manage set of tracked repos),gti replace(replace objs),git help(display help info about git),gti version(shows version),git apply(apply a patch to file & or to the index),
#Git hub(central):- is a web-based platform used for version control. it simplifies the process of working with other people & makes it easy to collaborate on projects
#create a new repo in github,give name,create repo. take a copy of push an existing repo form the command line,paste,enter,git push origin master,enter,username,give,password,settings,developer settings,personal access tokens,token classic,generate a token,password,(generate) copy & paste. (now the files pushed to master to master(git hub))
#Git merge:-is using for mergeinng one branch file with other branch files in one branch.             we can upload files in 3ways:-1)git to git hub by push command,2)create a new file,3)upload file
#git clonning:- git hub to git by using the url. (we taking the everything from a repo)        git pull origin ritu (now we get all file of ritu branch)    get fork:taking the others repo y forking

#Maven(building)(manual):-is automation project management tool developed by apache software foundation. it is build tool & manages dependencies(java libraries that are need for project). it is based on POM(project obj model).it can build any no.of projects into desired output. such as jar(java archieve),war(combination of langs). it is mostly used for java projects. maven is written in java.
#Mvn build life cycle:-generate a resources-->compile code - mvn compile,-->Test - mvn test,-->package - mvn package,-->install - mvn install,-->Deploy(to servers) 
#install mvn in your ec2 instance,search in google https://dicdn.apache.org,maven,maven 3,3.86,binaries,copy the 1st link,   wget paste the link in instance.(now we get mvn repo),ll,(now we have to un tar that file)tar -zxvf apache-maven-3.8.6-bin.tar.gz,ll,,cd apache -maven-3.8.6/,ll,sudo amazon-linux-extras install java-openjdk11,y,yum install maven -y,java -version,   mvn archetype:generate(plugins of mvn all downloaded),enter,enter,batch2,devops,ent,ent,y,ll,cd devops,ls,ls src/,ls src/main/java,ls Src/main/java/batch,cd  src/main/java/batch/,cat app.java,   ,cd  ..,cd,cd apache-maven-3.8.6/,ll,mvn compile,clear,ll,ls target/classes/,ls target/classes/batch/,mvn test,   mvn package,mvn install, 
 
#Jenkins(ci/cd)(build automation):-continous integration(code-build-integration-ci)/continuous delivery(or)deployment(code-build-integration-QA or UAT-CD).
#pipeline:-version control-build-unti test-deploy-auto test-deploy to production-measure validate  
#                                                            feedback
#jenkins is a open source project written in java that runs on windows,linux,macos.consist of plugins.it is developed by sun microsystem.developers write code,we integrate all the code of all developers at any point of time & we build,test & delivery/deploy to client. this is called CI/CD.
#
#worlkflow:-we can attach git,maven,selenium,& artifactory plugins to the jenkins.once developer put code in github jenkins pull that code & send to maven for build. once build is done,jenkins pull that code & send to selenium for testing. once testing is done,jenkins pull that code & send to artifactory as per requirement. we can also deploy with jenkins.(jenkins will follow master-slave architecture)(master node assign works to slave nodes)
#launch a ins,port all traffic anywhere,launch,   sudo yum -y updatay,sudo -i,  jenkins.io(search) download,linux,copy the link & paste in ins(we get jenkins repo),copy & paste 2nd(to grt keys),sudo amazon-linux-extras install java-openjdk11(install java),yum install git maven jenkins -y,systemctl restart jenkins.service,systemctl status jenkins.service,(copy the pubip:8080 search in a browser),copy the path and cat paste it in ins we get password copy that & paste on browser,continue,install suggested plugins,add user password fullname mail,save & continue,save,
#master & slave concept(this 2 connected through SSH Key):-vim /etc/passwd,insert bin/false to bin/bash,:wq!,cat /etc/passwd,passwd jenkins,create password,visudo,(yyp or copy and paste of (root all=(all)all))insert,jenkins nopasswd:,:wq!,vim /etc/ssh/sshd_config, passwordauthetication no to yes,:wq!,systemctl restart sshd,systemctl status sshd,  
#login to slave:-take another ins launch,sudo yum -y update,sudo -i,useradd jenkins,passwd,use sm password,visudo,jenkins nopasswd:all,:wq!,vim /etc/ssh/sshd_config,pwdauto yes,:wq!,systemctl restart sshd,systemctl status sshd, now go back to master,su - jenkins,ssh-keygen,ent,ent,ssh-copy-id jenkins@localhost,yes,pswd,copy "ssh 'jenkins@localhost'"&paste,(now we connected localhost to localhost & master to master),hostname -i(we get pvtip for checking purpose),exit(now connection was closed) #(now connecting master to slave node)ssh-copy-id jenkins@copy &paste pubip of slave node,yes,pswd,copy and paste (now the connection is established master to slave),hostname -i(used to check the pvtip of slave node),exit
#
#jenkins pipeline:-is a combination of plugins that supports integration & implementation of continuous delivery pipeline(code-build-integrate-test-deploy). jenkinsfile:-jenkins pipeline can be defined using a text file called jenkinsfile. with jenkinsfile, you can write the steps,needed for running a jenkins pipeline.
#there are 2typees pf jenkins pipeline syntax for jenkinsfile:-1)Declarative:-offers an easyway to create pipelline.It gives you the ability of control all aspects of a pipeline excution in a simple,straight-forward manner. 2)Scripted:-it uses very few resources to translate the pipeline in to atomic commands.both declarative & scripted syntax are different from each other & are defined totally different. 

#Ansiable:-is configuration management tool. ansible is simple open-source IT engine which automates application deployment. Uses YAML scripting lang which works on KEY-PAIR. used PYTHON for back end & Git(C lang) Maven(Java) & Jenkins(Java).Michael Dehhan developed by Ansible & the Ansible [project began in feb 2012. Ansible was taken over by Red-hat. Ansible(push mechanisam).Cheif(pull mechanism)
#Ansible-server:-sudo -i,sudo amazon -linux-extras install ansible2 -y,yum install git python-pip python-level openssl -y,vi /etc/ansible/hosts,insert devpvt ips copy & paste & qapvt ips copy & paste,:wq!,vi /etc /ansible/ansible.cfg,insert uncomment the(inventory & sudo_user):wq!,useradd ansible,passwd ansible,visudo,insert ansible nopasswd:,:wq!,vim /etc/ssh/sshd_config insert yes,:wq!,systemctl restart sshd,systemctl status sshd,su -ansible,ssh-keygen,ssh-copy-id ansible@localhost,yes,s=passworfard,"ssh 'ansible@localhost'",hostname -i(we get ansible localhost pvt ip),exit,ssh -copy-id ansible@dev pub ip,yes,passwd,connecting top copy & paste,hostname -i,exit
#Dev1-server:-useradd ansible,passwd ansible,visudo,insert ansible nopasswd,:wq!,vim /etc/ssh/sshd_config,insert yes,:wq!,systemctl restart sshd,systemctl status sshd,su -ansible
#Dev2-server:-useradd ansible,passwd ansible,visudo,insert ansible nopasswd,:wq!,vim /etc/ssh/sshd_config,insert yes,:wq!,systemctl restart sshd,systemctl status sshd,su -ansible
#Ansible Inventory Pattern:-this shows which server in which group(used for checking). in ansible server. ansible all --list-hosts(we get pvt ips),ansible dev --list-hosts(now we can only see dev ips),ansible dev[0] --list-host(here we get ip by indexing )
#If we want to push the code from ansible server to nodes it can be done in 3ways:-1)Ad-Hoc Commands(simple linux commands(used for temp activties)),Modules(single command),Playbooks(more than one module(YAML lang))
#Ad-hoc commands:goto ansible server
# 
#Docker(is a set of paas products that uses os-level virtualization to deliver software in packages called containers):-is a software platform hat allows you to build,test, & deploy applications quilckly. docker packages software into standardized units called containers that have everything the software needs to run including librariees,system tools,code,& runtime. (container is a software code package containing an application's code,its libraraies,&other dependencies. containerization makes your apps portable so that the sm code can run on any device. A virtual is a digital copy of a physical m/c).(1)docker is a common container platform used for building & deploying containerized apps).  
#Docker Swarm is a container orchestration tool running the Docker app.It has been configured to join together in a cluster. The activities of the cluster are controlled by a swsarm manager,& m/cs that have joined the cluster are referred to as nodes.docker swarm does not manage any containers but instead is a cluster manager for docker containers.(provides native clustering functionality for Docker containers,which turns a group of docker engines into a single virtual docker engine). (1)if your company does not need to manage complex workloads. then docker swarm is the right choice). 
#Kubernetes is also know as K8s, is an open-source container orchestration system for automating software deployment,scaling,& management. originally designed by google, the project is now maintained by the cloud  native computing foundation.of containerized apps. (1)if your apps are critical & you are looking to include monitoring, security features, high availability, & flexibility,then Kubernetes is the right choice). 
#Docker is used for creating & running containers,while kuberbnetes is used for managing & automating the deployment, scaling, & operation of containers across cluster of hosts. 
# 
#Junit is a unit testing open-source framework for a java programming lang. Java Developers use thie framework to write & excute automated tests. in java,there are test cases that have to be re-executed every-time a new code is added. This is done to make sure that nothing in the code is broken. (java testing tool) 
# 
#Grafana is an open source interactive data-visualization platform,developed by grafana labs, which allows users to see their data via charts & graphs that are unified into one dashboard.  
#prometheus is an open source monitoring system for which grafana provides out-of-the-box support. This topic walks you through the steps to create a series of dashboards in grafana to display system metrics for a server monitored by prometheus.  
# 
#
#sonar Qude:- code quality checking software(code review) 
#nexus:-to store the back up artifact init. 
#
#Git hub(source code)->Jenkins(CICD)->Maven(build tool compile & package)->SonarQube(9000(for Code Review(code quality checking software))->nexus Repo(8081(for bup artifact is uploaded here)->Apache Tomcat Srvr(APP war file is uploaded)(used to run app)
#Git:-Version conroling system & source code management tool               working working repo----->stagging area---->local repo----->remote repo    
#Maven:-Is a Build tool used to build an artifact(Is a final file that which will given to the end users)
#Jenkins:-Deployment Tool(CICD(Continous Integration contious deliver(or)deployment)) 
#Docker & Kubernetes:-infra creating Tool also containerazation tool using this we can provide to dev team without waiting to operation team response. Kubernetes(k8s) is an open-source container orchestration system for automating software deploying,scaling,& managing containerized apps.   
#Ansible:-configuration management tool
#Nagios:-Monitoring Tool(we can monitor 100s of srvs at a time)
#Apache Tomcat:-is a wed server to host your website
#Terraform:-To manage your infra as a code enables the benefits of the CI/CD workflow for infrastructure deployments. since your infra is codified. your team can collaborate & review it & deploy it using automated pipeline instead of manual orchestration.
#CircleCI:-is a continuous integration & delivery(CI/CD)platform for automating software builds,tests, & deployments.The CI/CD pardign=m establishes versiom control repositories as the source of truth for your deployments. you can build deployment pipeline of varying complexity to satisfy your organization's requirements for production deployments.   
#
#SDLC:-software development lifecycle.
#Coding->testing->deployment->maintance->requirement analysis->defining->designing
#
#Devops lifecycle:-code(git)->build(mvn)->test(junit)->release(jenkins)->deploy(docker)->operate(ansiable)->monitoring(graffana)->planning(codeship
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
#
#  
# 
# 
#Ashok IT Videos Jenkins:- continues download,continues build,continues deploy,continues test,continues delivery.  
#DevOps. Build & Deployment process:-1)Take latest source code from git hub.2)Compile project source code. 3)Excute Unit Test  cases. 3)Perform code Review using sonarQube.5)Package the app(jar/war).6)upload Build Artifact in Nexus(for bup). 7)Deploy the app in srvr(by using url the client use).  
#Realtime app Env:-Dev-Developers will use to perform code integration testing. QA Env:-Testers will use to perform Functional testing. UAT env:-user acceptance testing(client side team eill perform app testing). Pilot env:-It is called pre-prod env(Performance testing). Prod:-Live Env(end user can access the app)
#Devlopment Team:-Responsible for project development(codeing). Testing Team:-Responsible for project functionality testing(verification & validation). Operations Team:-responsible for Build & Deployment process. 
#Developers(push the code)GitHub(store code)Jenkins(build & deployment)Maven(complie the code(packaged))SonarQube(perform the code review).Tomcat(deploy the code into srvr)
#If the application is stands alone app they package as jar file. If the project is web app they will package as war file.
#Jenkins is free & open source software. Jenkins developed using Java lang. Jenkins is used to automate Build & Deployment process. using jenkins we can implement CICD.   
#manuall deployment steps Download code using git. Excuted Maven Goal(Clean Package)-->WAr file created. Uploaded War file into into tomcat srvr(deploment). 
#Automate Deployment jenkins Steps:-1st Linux VM having tomcat srvr.2nd Linux VM having java,Jenkins, srvr(browse it &login now global tool configutaration maven & Deloy to container plugins(to deploy war to tomcat srvr)).create a job,freestyle,ok,git,Repo URL,*/master,Poll SCM *****,Delete workspace before build starts,Maven-3.86,clean packege,post build deploy war file to container target/*.war,maven-web-app,tomcat 9.x,creditals 2admin,tomcat URL,apply save,build now.Now access the URL it works. Code is ava in GitHub Repo. (#Buld Deployment process automated by jenkins)Download project from github.Package the project using maven.maven will create War file Deploy war file into tomcat.Access app using URL in browser. 
#

#2)video Devops project setuo with CICD Pipeline:-Git hub(source code)->Jenkins(CICD)->Maven(build tool compile & package)->SonarQube(9000(for Code Review(code quality checking software))->nexus Repo(8081(for bup artifact is uploaded here)->Apache Tomcat Srvr(APP war file is uploaded)(used to run app).
#In this Jenkins are connected with each & every tool as pipeline. 1)clone Repo(git),2)Maven Build(compile),3)code review(sonarqube),4)Upload Artifact(nexsus or jfrog),5)Deploy app. 
#API:-Application programming interface 
#

#1) video only DevOps youtube:-  developer team:-code     Operations team responsibilities:-installation of srvr hw & os,configuration of srvr,network,storage,monitoring of srvrs,respond to outages,IT security,Change Control,bup & disaster recovery planning.      joining this DevOps cames into picture
#SDLC Model-Software Development Life cycle         clint-.company
#1)Waterfall Model:-Requirments->Analysis->Design->Coding->Testing->Acceptance  (1)it takes lot of time(2years))(there is denpendecy other team members bcz stepp bby step)(2)not suitable for changing versions)
#2)Agile Model(or)incremental model:-is a type of evolutionary development. This results in small incremental releases with each release building on previous functionality.(it takes 8months) 
#DevOps:-is a Methodology that promotes collaboration b/w Development & Operations Team. This allow deploying code to production faster & in an automated way. It helps to enables rapid deploymant of products.  
#Linux:-All the DevOps tools used configurtions by Linux commands 
#Git:-Version conroling tool & source code management tool                working repo----->stagging area---->local repo----->remote repo    
#Maven:-Is a Build tool used to build an artifact 
#Jenkins:-Deployment Tool(CICD(Continous Integration contious deliver(or)deployment))
#Docker & Kubernetes:-infra creating Tool also containerazation tool using this we can provide to dev team without waiting to operation team response. Kubernetes container orchestration tool  
#Ansible:-configuration management tool
#Nagios:-Monitoring Tool(we can monitor 100s of srvs at a time)
# 
#2) video create a linux m/c & use linux commands  
# 
#3)video launching the ins &using the Linux commands
#4)video linux commands
#5)video Git:-is a version control system tool(that help a software team manage changes to source code cover time)is also known as(source code management tool)                                                                                                               untracked file->staging Area->(local repo)commited files     (only we can filter in untracked to staging to move local repo.we cant filter & send lr when it is staging area)
#Git is a Distributed version controlling.git commands(in gitbash)install git bash(Terminal),(folder)E:\bank--into-->Working Directory(convert using git init).git folder created,git config --global user.name "",git config --global user.email "",git config --gllobal --list,git status,git add filename(*)(.),git commit -m "first commit",git log(list commits)(or)git log --oneline,git restore --staged filename(to get back to stagging to untracked files)(if we dlt .git floder then it become untracked files again)
#6)video git branching:-git init(creates defalut master branch),touch f1,f2,f3,git status,,git add *,git commit -m "1a"git branch (test)branchname(creates 2nd branch),git branch,git checkout test,touch f4,f5,git status,git add *,git commit -m "2b",git log(the child b will show all commit logs),git checkout master,touch f6,git status,git add *,git commit -m "1c",git log --oneline(the master branch only show mb commits).(for merging you have to stay in masterb),git merge test,:q,git log --oneline(now we can see the all commits logs),
#7)video git Rebase:-is a fastforword merge.The commits from the child branch are added to the top of the master branch.This is helpful when we want code from a branch to be reflected as the latest working version on master. git init,touch f1 add .,git commit -m "a",touch f2,git add .,git commit -m "b",git branch test,git checkout test,touch t1,git add .,git commit -m "c",touch t2,git add .,git commit -m "d",touch t3,git add .,git commit -m "e",git checkout master,touch f3,git add .,git commit -m "f",git log --oneline,git checkout test,git rebase master,git checkout master,git merge test,git log --oneline(the child commits will be the latest commits we can see(byusing Rebase & merge)),
#8)video we need to rearrange the commit order(the 1st commit order is not changed):-create 5files & commit in a branch,git log --oneline,git rebase -i HEAD~4,copyd line insert mood paste on top of b,copy b & paste on d place,:wq!,git log --oneline(we can rearranged commit order)
#merging the commits(we can not remove 1st commit):-create 5files & commit in branch,git rebase -i HEAD~4,insert,pick to squash on commit(for removing commit),:wq!,git log --oneline(the squash said commits removed)tracking will be removed but files are present.
#picking up selective commits from child branch to master:-create 3files in master & 3files test & commit it,git log --oneline,git checkout master,git log --master,git cherry-pick eid & fid cp & paste,git log --oneline(we can see the child 2commits in master branch on)
#for ignoring some files to move stagging we use .git ignore file:-vim .git ignore,insert,add file name,:wq!,git status(now we cant see that file in untracked flist)(now only source code files is moved to stagging to repo)(this used for filtering)
#Git Stash:-is nothing but storing safely in a hidden place.This feature is usedd for leaving unfinishedd work,in such a way that Git cannot access it & continue work on some other files.(It works on Stagged area & hide that files).git init,touch f1 f2,git add .,git commit -m "a",touch f3 f4,git add.,touch f5 f6,git status(2stagged & 2untracked files),git stash,git status(we only see untracked filles now),git add .,git commit -m "b",git status(working tree clean),
#Git stash pop:for getting back files to staged area,git status(we see stagged files again)             #To stash the stagged files(git stash),To stash staged & untracked files(git stash -u),To see the list of stashes(git stash list),To get back the stashed files(git stash pop),To bring the older stash out(git stash pop stash@{stash_number})
#9) video git Ammed:-git init,git status,git add .,git commit -m "a"(moved into lr)(when the code updated it will come to untracked files again).git status,git log --oneline,git commit --amend -m "a",git status(this will move to lr by sm commit name).       #To role back the previous version:-create 5 files & commit,now 2more file create & 2files modify git status,commit it,git log --oneline,(for role back take the previous commit ID) git reset --hard ID(now it is role back pv).    #Remote Repo(Github):-create a repo in git hub &take the link & push commands from it(now the file uploaded from lr to rr)
#
#10)video Maven is Build Tool:-maven takes source code as input & converts into a Artifact(war/jar/exe).It can compile the programs & create a artifact. #Is a product of apache. All the open source communities like jenkins,tomcat,mysql etc upload their updated API's into Maven Global srvr(search.maven.org).  #source code in git hub we invoke the MVN. This take the source code & generate the Artifact.That Artifact is deployed in testing srvr.This will help in protecting the code from any threats/viruses that might be present in the API's     #Maven Globle srvr(API)search.maven.org---->Maven Local REPO---->Developer(code & api pushed)---->Github 
#For installing MVN:JDK 1.8 download,download with os config,download & install,download apache Maven,from the link to the m/c. extract & crete 2Env variables pointing to this 2.   #MVN  --version(checking)
#11) video Artifact:-Is a final file that which will given to the end users. #STEPS:-mvn archetype:generate(this will gen artifact),enter,com.icicitech,webappicicitech,enter,build sucess(mvn will create the project structure(src folder & pom.xml file)),src(source code) contain main &test folders.code created by the dev will be in main folder.for unit testing will be in test folder.POM stands for project obj model.It is xml file,stores all the external API info. now goto gitbash from webappicici,git init,git status,git add .,git commit -m "first commit"now pom.xml file contains dependcies now add the tags of API from MVN global repo to it and save. now install that API from global to localrepo by using mvn compile(command)in cmd.gitbash,git status,git add .,git commit -m "second commit",cmd mvn compile,mvn test,mvn package, 
#
#12)video(8080)(need java env)Jenkins:-Is a self contined, open source automation srvr which can be used to automate all tasks related to building,testing & delivery activities.(Is a CICD tool(continuous integration continuous delivery))(continuous download(in DEV.from github,git,mvn,jenkins),build,deployment(in QA tomcat(is a web srvr)),testing,delivery(in PROD. Tomcat going to live)). jenkins need java runtime env.continue download,continue testing,continue deployment, 
#Steps:-create 3ins in AWS (dev,qa,prod) connect dev m/c gitbash,sudo yum -y update or sudo apt update,sudo apt install openjdl-8--jdk -y,java -version,sudo apt-get install -y git maven,git --version,mvn --version,now jenkins download google it copy the link & wget url,ls,java -jar jenkins.war(for starting the jenkins),take the pub ip of dev & add 8080,copy the password from terminal &paste continue,install suggested plugins,all admin,save & continue,start, 
#13)video connect to dev m/c to gitbash java -jar jenkins.war,dev ip:8080 connect. Now connect to QA m/c to git bash,sudo apt-get update,sudo apt-get install -y tomcat8,sudo apt-get install -y tomcat8-admin,take the ip of QA srvr:8080 browse,cd /etc/tomcat8/,ls,sudo vim tomcat-users.xml,insert add users add a line13:43,:wq!,sudo service tomcat8 restart,Now connect the prod ins in GB & do sm 12 steps init,Now we can perform CICD configurations,take pub ip dev:8080 browse,2admin,goto github sunildevops77/maven copy the url,in jenkins new item,name frestyle ok,scm git url apply run(continus download is done),goto job & configure build invoke top lvl mvn targets package save run(artifate created),now install deploy to container plugin for that manage jenkins manage plugins search deploy to plugins install without restart,goto job configure post build deploy war to cotainer **/*war qaenv tomcat8.xRemote add jenkins add http://pvt ip of QA:8080 apply save run (for accessing this take pub ip QA srvr:8080/qaenv browse it),.Artifact is delpoyed in QA env
#14)video 4stage create new job for testing freestyle ok,git copy & paste testurl apply save run,job configure build excute shell echo "Testing passed" apply save run(continus testing done),#Now continus delivery deploy artifact to the prod goto 1st job post-b actions add psst-build action build other projects testing name trigger only if build is stable apply save, Now run the 1st job(automatically job 2 also ran). Now prod goto dev job configure add postbuild archive the artifact **/*.war apply save goto manage jenkins manage plugins search copy artifact install wr,goto testing job configure build add build setup copy artifact from another project development apply goto post build add pb deploy war to container **/war.*- prodenv tomcat8x add creditials of prod add pvt iip of prod:8080 apply save,Now run the devjob,copy the pvt ip:8080 and check app is hosted.
#15)video security option in jenkins:-start the 3srvrs. start jenkins in dev. java -jar jenkins.war,copy pudid:8080 dev & go jenkins dashboard, creating users in jenkins
#16)video Master slave configuration:-
#17)vidoe pipeline job:-
#18)multibranch pipline:-
#19)Docker:-is containerization tool(docker elimates the depency of os layer).In comparison the traditional virtualzation functionalities of hypervisors,Docker containers eliminate the need for a separate guest operation system for every new virtual m/c.Docker implement a high-lvl API to provide lightweight containers that run processes in isolation. This helps developers & operations team in rapid deployment of an  app.
#steps:-https://get.docker.com/,in ins sudo su,curl -fsSl https://get.docker.com -o get-docker.sh,sh get-docker.sh,docker --version,docker pull linux,docker pull jenkins,docker img ls,docker pull tomee, #docker run --name mytomcat -p   7070:8080 tomee(now take the pubip:7070 browse it),docker stop mytomcat(for stoping this goto another terminal & use this cmd),docker rm -f mytomcat(removing),dockr run --name mytomcat -p 7070:8080 -d tomee(to get #promt back this cmd used dettach mood),docker container ls,docker run --name myjenkins -p 9090:8080 -d jenkins,docker run --name myubuntu -it ubuntu,docker run --name appserver -p -d nginx,docker port appserver or docker cont ls,pubip:32768,docker run --name nydb -d -e MYSQL_ROOT_PASSWORD=sagar mysql:5,docker cont ls,docker exec -it mydb bash(open bash terminal of mysql),mysql -u root -p(connect to mysql db),give password,show databases;,create table,3exit,
#Docker images:-combinations of binaries / libraries which are necessary for one software app.
#Docker containers:-when image is installed & in comes into running condition,it is called container. 
#Docker Host:-m/c on which docker is installed,is called as Docker host.
#Docket Client:-Terminal used to run docker commands(git bash)
#Docker commands:-docker pull imgname(download img),docker image ls(or)docker images,docker rmi imagename/imageid(dlt img),docker push imgname(upload img to hub),docker tag imagename(tag an img),docker commit containername/containerid(build an img from customised container),docker build -t new img name(create img from docker file),docker search imagename,docker system prunr -a(to dlt all imgs that are not attached to containers),docker container ls,docker ps -a(list running & stopped containers),docker start containername/containerid,docker stop contnm/contid,docker restart contnm,contid,(to restart after 10sec)docker restart -t 10 contnm/contid,docker rm contnm/contid,docker rm -f contnm/contid,docker stop $(docker ps -aq)(stop all running cont),docker restart $(docker ps -aq),docker rm $(docker ps -aq),docker rm -f $(docker ps -aq),docker logs contnm/contid,docker port contnm/contid,docker inspect contnm/contidt,docker attach contnm/contid,docker exec -it contnm/contid (from command),docker run imgnm,
#20)video Docker:-top hands on 
#21)video creating multi-container architecture using link:-
#22)video docker compose:-
#23)video docker volumes:-
#24)video creating customized docker imgs using docker docker file:-
#25)video container orchestration (docker swarm):-
#26)video Ansible:-is a configuration  management tool. This is process of configuring remote servers from one point control. This cannot be used for installing os from the scratch.they can be used only for managing the apps on top of the os.    1controller & 4managed nodes
#Ansible is a open source configuration management tool,created using py. Main m/c in which anisble is installed,is called as controller. Remote srvrsthat ansible configures,are called as managed nodes. 
#steps:-launch 4 m/c name it as controller & srvr1,2,3,4,connect with srvr1,sudo apt-get update,sudo apt-get dist-upgrade,sudo apt-get install -y python2.7 python-pip,python --version,sudo passwd ubuntu,sudo vim /etc/ssh/sshd_config,insert notoyes,sudo service ssh restart,exit,Repeat sm configurating in srvr2,3. Now connect to controller srvr sudo apt-get update,sudo  apt-get dist-upgrade,suo apt-get install -y python2.7 python-pip,python --version,ssh-keygen,Now copy the pvtip of all 3srvrs and paste ssh-copy-id ubuntu@pvtidsrvr123 yes password,sudo apt-get install software-properties-common,sudo apt-add-repository ppa:ansible/ansible,sudo apt-get update,sudo apt-get install -y ansible,ansible --version,cd /etc/ansible,ls,sudo vim hosts,insert,cp &pst all the 3 pvtips of srvrs,:wq!,ls -la,ansible all -a 'ls -la'(we get all srvr ip address),  
#27)video in 2 ways ansible can perform operations:-1)ansible adhoc commands   2)playbooks                     all-all managed nodes    -i-inventory file.   -m-module    -a-arreguments   free-shows available space. 
#ansible adhoc commands:-(if we want write a command we have to use modules in ansible)in controller. ansible all -i /etc/ansible/hosts -m command -a 'free'(this cmd excuted in 3srvrs), ansible all -i /etc/ansible/hosts -m command -a 'touch file1'(this will create files in 3srvrs),(for checking)ssh pvtip 2ndsrvr,ls,(we can see file1)exit,get back to controller. now(to install docker in 3srvrs)(in controller)ansible all -i /etc/ansible/hosts -m shell -a 'curl -fsSL http://get.docker.com -o get-docker.sh',ansible all -i /etc/ansible/hosts -m shell -a 'sh get-docker.sh',(goto anysrvr3)ssh pvtip,docker --version,exit,   To check the inventroy file(how many ip address are added)sudo vim /etc/ansible/hosts.    Now we are creating own inventory file vim myinventory,insert,paste 2ips in this remove from default inventroy file & paste here:wq!,cat myinventory,  ansible all -i myinventory -m command -a 'free'(now this command are excuted on 2 m/cs only)  if didn't mention any inventory it takes default inventory file(ansible all -m command -a 'free')     
#Modules in Ansible(command,shell,ping,user,copy,fetch,file,stat,debug,apt,yum,git,replace,service,include,uri,docker_container,docker_image,docker_login,setup)By using this modules we write the commands & run the commands. 
#
#
#
#Gana Tech solution:-AWS(Amazon web srvcs)
#Cloud computing: srvcs/resources==>online==>ondemand==>through==>internet.
#Srvcs/resources==>srvrs,DB,Storage,Bup,..etc
#IAAS:-(Admins)     PAAS:-(Developers)     SAAS:-(End users). 
#Devops(it is a culture or Software development approach, which includes,continueosy combining the code,continueosly testing the code,continueosly integration the tools,continueosly deploying the apps,continueosly monitoring the apps,throughout its SDLC.)
#Dev(java code)-->testing team(test)-->ops(ci,cd,cm)-->client-->24/7-->EU. 
#Git:vcs--dev--code--push--github(repo)
#Maven:build tool--package--war / jar /ear
#Tomcat:webserver--deploy(copy war/jar/ear)
#jenkins:ci/cd tool
#sonarqube:codequality/review tool
#nexus:Artifactory--bup--war/jar/ear
#ansible:configuration management tool--ACm & target m/c-->yaml-->playbooks
#Docker:containeriation tool
#Kubernetes-->containerization orchastration tool.
#
#Devop project:-
#jenkins plugins installation ways are 3types
#1)managejenkins--manage plugins--available section--plugin name type--install. 
#2)we need to download the plugin in our local laptop--download & it is uploaded into the jenkins dash board managejenkins--manage plugins--advance section--plugin to upload. jenkins dashboard--restart.
#3)we need to download the plugin in our local laptop--& copy that plugin to jenkins instance--this path--/var/lib/jenkins/plugins--jenkins instances--restart. 
#jenkins pipeline:-pipeline as a code
#1)Declaritive pipeline (groovy script)  2)Scriptive pipeline
#In this pipline we will write Groovy script. Pipeline:-is a code & it has set of stages & stages contains steps, steps will excute entire pipeline. 
#Stages example:-git clone url(git checkout)--build--deploy.
#steps (git checkour)git clonr url--step (build) mvn clean package--step(deploy) war file copy(by using scp)
#pipeline--declarative
#pipeline--node--scriptive pipeline
#1)Declaritve pipeline:-(written in git hub)(pipeline)
#we will create jenkinsfile in github. 
#2)Scriptive pipeline:-(written in jenkins dash boar)(node)
#To upgrade the Jenkins instance:-
#1)Jenkins version 2 ins--> health checkup(bup)-->AMI/Image. 
#2)we need to create one ec2 ins-->login into that ins-->install jenkins version3
#3)Jenkins version2-->copy the contents of /var/lib/jenkins-->jenkins version3-->/var/lib/jenkins
#4)Plugins also copy from jenkins 2 to jenkins version 3. 
#installes plugins from jenkins 2 /var/lib/jekins/plugins-->jenkins version3-->/var/lib/jenkins/plugins
#5)Jenkins version3 ins-->reboot-->properly work-->jenkins version2 ins-->delete. 
#
#Master/slave concept in Jenkins:-
#master: jenkins install-->ins-->master.
#slaves/nodes-->another ins.-->we need to create a slaves/nodes. 
#The main purpose of Maste/slave is to distributing the builds. 
#By usig master/slave cocept-->we will create the obs in jenkins master & that jobs are builds in nodes. the communication b/w master & slave is SSH
#The communication b/w master & slave is SSH. Master & Slave has Tcp/Ip. 
#Key points:-1)we need to install jenkins in master only. 2)we don't need to install on slave/nodes. 3)Basic rule: Java installation is mandatory. master ins is only one ins. & nodes will be No.of insts. each node treated as one environment(Dev,QA,UAT,Prod). each node tomcat insts. The jobs are running b/w master & slave by using labels. 
#
#CICD with Jenkins(8080)(t2.medium),Git,Maven,Tomcat(8080)(t2.micro),SonarQube(9000)(t2.mideum) & Nexus(8081)(t2.medium):-    jenkins-1ins,tomcat-1ins,sonarqube-1ins,nexus-1ins.    4 insts will be available in sm AZ. 
#Dev--->Git Hub--->Maven       code push   build
#           |      |
#               |                         ci
#            Jenkins--->Tomcat            cd
#               |                         ci   
#           |        |
#     Sonarqube      Nexus
#
#7project:-end to end
#10project:-freestyle & pipeline
#
#11Docker:-Is a containersation platform which package your app & its all dependencies together in the form of containers. so as to ensure that you applicatiom works seamlessly un any environmentbe it Dev or test or prod.
#is a openplatform for developers & sysadmins to build,ship,& run distributed apps.
#Docker is available in 2editions:-community edition(CE) & Enterprise Edition(EE).
#Docker community Edition(CE) is ideal for developers & small teams lookinglooking to get started with Docker &experimenting  with container-based apps. Docker CE has 2 update channels,stable & edge: stable gives you reliable updates every quarter. Edge gives you new features every month.
#Docker Enterprise Edition (EE)is designed for enterprise development & IT teams who build,ship & run business critical apps in production at scale. 
#virtual m/cs:-infrastructures-host os-hypervisor-guest os-binaries/libraries-apps  (Each VM includes the app, the necessary binaries & libraies & an entire guest os) (heavy weight)(hardware level virtualization)
#containers:-infrastructure-os-Docker Enginge-Binaries/Libraries-apps      (Containers includes the app & all of its dependencies,but share the kernel with other containers)(Run as an isolated process in ruserspace on the host os)(Not tied to any specific infra-containers run on any computer,infra & cloud)(light weight)(os level virtualization)
#Docker components:-Docker image-->pull,Docker container:image-->container,Dockerhub/Docker registry:images-->bup,Docker file-->image create.
#Docker architecture:-Docker is a client/srvr architecture. Docker work flow:-Dev/QA/UAT/PROD. 
#client----->Docker Daemon
#             container1
#             container2
#              server
#     Docker Engine
#Docker has 3parts:-1 client:-Docker provides cli tools to client to interact with Docker Daemon. Client can build,run & stop application. client can also interact to docker_Host remotely.
#Docker_Host:It contains containers,images,& docker daemon. It provides complete environment to execute & run your app.
#DockerRegistry/Hub:-It is global repository of images. you can access & use these images to run your application i Docker environment. 
#
#
#
#
#
#
#

#Data Engineering is the process of collecting, analysing & transforming data from numerous sources. Data can be transient, or persisted to a repository. 
#Aws Data Streaming:-Amz kinesis(real-time)enables you to ingest,buffer & process streaming data in real-time, so you can derive insights in secs or min instead of hours or days. is fully managed & runs your streaming apps without requring you to manage any infra. this can handle any amount of streaming data & process data from hundreds of thousands of sources with very low latencies. 
#1)Kinesis video streams:-makes it easy to securely stream video from connected devices to AWS for analytics,M/c learning (ML) & other processing.
#2)Kinesis Data Streams:-is a scalable & durable  real-time data streaming srvc that can continuously capture gigabytes of data per sec from hundreds of thousands of sources. 
#3)Kinesis Data Firehosee:-is the easiest way to capture, transform, & load data streams into AWS data stores for near real-time analytics with existing business intelligence tools.
#4)Kinesis Data Analytics:-is the easiest way to process data streams in real-time with SQL or Apache flink without having to learn new programming langs or processing frameworks.  
#Producer will put records into Kinesis Data Streams. & the Retention Period is by default is 24hours & we can increase upto 365days. shard is a uniquely identified of data records in a stream. 
#Partition Key:-is used to group data by shard within a stream. sequence number:-each data record has a sequence no, that is unique per partition-key within its shard.  
#Destinations:-S3,Redshift,ElasticSearch,Splunk,Datadog,Dynatrace,LogicMonitor,MongoDB,New Relic,Sumo Logic.
# 
# 
# 
#Technology in telugu:-Big Data:-properties of big data:-1)High volume(petabytes,hexabytes of size),2)High velocity(speed or growth of data),3)High variety(structured,semi-structured,unstructured),4)veracity(quality & accuracy). 
#
#Big Data Applications & Technologies involved:-Data is new oil(raw data) we have to refine it make it petrol,disel(output data). refining(big data analytics used)big data methods or technics 1)Data mining, 2)Predective Analytics, 3)M/c learning, 4)natural language processing. 
#Fundamental rule in Big data analytics:-uncovering hidden patterns(super market milk,bread),identify correlations(Correlation is a measure of how things are related ex:-covid details)
#Big data leveraged by industries:-Healthcare,education,public sector,travelling,banking finance,insurance.    Advantages og BD:-cost Reduction(by using hadoop),Time reduction(map reduce),new product & srvcs(1,2fundamentals),smart business decisions(1,2fundamentals). 
#Big data technologies:-Apache hadoop(is a main frame work in big data)(Distributed storage & distributed processing using cluster of computers),spark,hive,Apache kafka,presto. 
#
#hadoop:-is one of the populr technology available to process the Big Data. Hadoop alternatives(google big query & apache spark)
#Apache Hadoop is a collection of open-source software utilities that facilitates using a network of many computers to slove problems involving massive amount of data & computation. it provides a software framework for distributed storage & processing of big data using the MapReduce programming model.
#Important components of Hadoop:-1)HDFS(Hadoop Distributed file system(we dived the data into small parts & making some duplicate copies of it sending that copies to different computers)1)we can store large amount of data2)falut tolare(data recovering),2)Mapreduce(distrubute the work to diffierent computers & making work to do parallel)map dividing small parts redusce colleting the result & making single result,3)YARN(yet another resource negotiator)(monitor the computer state in cluster)
#
#Big data processing:-1)Distributed computing,2)Distributed storage      3)Map-reduce.
#Map reduce(big data proceing task to dividing into small task & distributing the task to cluster of computer. this cluster of computers works on parallel on the work & give the work output):-Distributed computing
#MapReduce enables skilled programmers to write distributed apps without having to worry about the underlying distributed computing infrastucture. this is a very big deal.Hadoop & the mapreduce framework handle all sorts of complexity that app developers dont need to handle. 
#
#word count using python(pyspark(is a py libriries)) problem:
#pyspark is python API for apache spark,an open source,distributed computing frame work & set of libraries for real-time, large-scale data processing. 
#Apache spark is a general-purpose distributed data processing engine. or in other words: load big data do computations on it in a distributed way, & then store it. 
#Spark provides high-lvl APIs in java,scale,py & R, and an optimized angine that supports general execution graphs.                     (write a spark code and run the code with spark-submit wordcount.py) 
#
#Apache pyspark:-is a one of the big data technology(fast data processing(by using in memory computation),multiple packages(in built modules are available),supports multiple programming languages(this frame work supports multiple langs)). py spark is a python API for spark(py + spark= pyspark).
#pyspark setup process:-
#using public cloud provides:-take aws account
#using VM(virtual m/c):-cloud era,hotten works(heavy m/c it needs 32gb ran)
#using local m/c:-local m/c    steps for installing spark:- install python,python --version in cmd,install jdk(java development kit) 11(spark is depened on scala & scala is jvm(java virtual)),install apache spark(spark.apache.org/download.html),installing winutils,creating environment variables. (open cmd and pyspark(for checking the spark installed or not)).
#
#spark architecture & features:-spark is a fast & distributed data processing engine(big data). 
#Apache spark architecture:-master node driver program spark context)-->cluster manager(apache spark supports 4 main open source cluster managers mesos,YARN,standalone,& Kubernetes)-->worker node(task cache)worker node(task cache). The architecture is as sm as mapreduce but spark is 10X to 100X faster. 
#Apache spark Architecture- 1)RDD:-Resilient distributed datasets(in-memeory data structure)
#                           2)DAG(Directed Acyclic graph) this gives proper to to work on it (node=RDD,edge is explained as doing work on top of RDD)
#
#we are writting pyspark program running on movielens i.e., downloaded on grouplens,->datasets->ml-100l-zip files(download it & unzip it)
#pyspark code written  and runed by using vscode,&cmd the moive ratings as filitered by using pyspark. 
#
#Data Engineer is an IT worker whose primary job is to prepare data for analytical or operational uses. These software engineers are typically responsible for building data pipelines to bring together information from different source systems.  Roles & responsinilities of DE:-1)Builiding data pipelines,developing algorithms,developing data validation,data governance & compliance.        
#DE needed:-SQL(structured query language),programming knowledge(py/java/c#),ETL tools(informatica,ssis,Airflow etc.),big data(spark/hive/Hadoop etc.)
#
#Spark SQL & Dataframes:-RDD is the old concept. Dataframes simplified spark programming by provideing a data structure which is conceptually similar to a DB table.             (this is just like panads data frame) 
#Dataframes are extension of RDD.They contains Row objs,can run sql queries,can have schema(leading to more efficient storage),read & write to json,hive,paraquet,csv etc.,communicate with JDBC/ODBC,Tableau. 
#
#Databricks:-is a cloud-based data processing & analytics platform that allows users to collaborate on big data projects. it was created by the original developers of apache spark & offers a range of features such as data engineering,m/c learning,& business intelligence tool. 
#Databricks runtime is a data processing engine built on highly optimized version of apache spark & it provides upto 50x performance gains. 
#unified analytics platform:-Databricks provides a unified platform for data engineering,m/c learning & business intelligence workloads,which allows teams to collaborate on a single platform. (delta lake,apache spark,pytorch,miflow)
#Advantages of Azure Data bricks:-Integration with Azure srvcs:-Azure Databricks is tightly integrated with other Azure srvcs,such as Azure Datafactory,Azure data lake storage,Azure M/c learning & powerBI,which makes it easier to move data b/w srvcs & build end-to end data pipelines. 
#Azure Databricks gets several benefits from being integrated with microsoft's Azure cloud platform, including:-1)scalability & performance,2)enterprise-grade security,3)global reach. 
#
#Azure Databricks:-To use this we need to login in portal.Azure.com. before doing we need to have Azure subscription we get usd200* credits we can use for 1month. we have to create Azure databricks workspaces(to work Azure Databricks).  
#
#
#
#
#
#
#Hadoop:we need to hdfs(Hadoop Distributed file system) as source location.
#apache spark:do actual computation part
#Airflow:-basically orchestration or the work flow manager(time to time trigger for sheduleing job)
#Airflow is an open-source platform for developing,scheduling,& monitoring batch-oriented workflow (or) Data pipelines.Airflow's extensible Python framework enables you to build workflows connecting with virtually any technology. A web interface helps manage the state of your workflows. 
#Hive:-
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
#Snowflake cloud data warehouse(founded in 2012)(california)(built by 3 Data Warehouse Experts:-Benoit Dageville,Thierry Cruanes,Marcin Zukowski)(Refer Snowsflake Editions Documentation)(Has standard,Enterprise,Business Critical,Virtual Private Snowfalke(VPS)) cost different for different Regions.(Sf is SAAS everything taken care by the sf except your Roles security,your table design,db density)Alternate(AWS=Redshift,Google=BigQuery,Azure=Synapse,Databricks(AWS/Azure)) 
#Snow Flake(SAAS)software as a srvs,(DPCS)data Platform as a srvc,(DWaas)Data warehouse as a srvc:-is relatively new & fresh in the cloud data warehouse space. It is purposefully built only for the cloud platforms(AWS/AZURE/GCP). 
#Features of Snowflake:-Time Travel,Data Sharing,data cloning(Zero copy Clone),Readers Accounts,out of box security(RBAC/DAC)/Encryption/Column level Masking/Row Level Security,All popular connectors(JDBC/ODBC/Spark & many more),#Pay per second Billing Model(No upfront investment & only pay for actual usage). 
#Is named as Gartner Leader Quadrant as 2019.This supports all the standards connectors so adaption is easy.Supports(ODBC & JDBC connectors,py,go,.net NodeJS ,PHP,)& ANSI SQL,(Supports for Data Warehouse,Datalake,data Eng,Streaming,Data App,Data Science,Data Exchange)
#Evolution of Cloud Data Platform:-   on-premises Evolution Data Warehouse ---> 1st Gen Cloud EDW ----> Data lake Hadoop ----> Cloud data Platform(snowflake came). 
#Modern Data Architecture with Snowflake:-     Data Source(oltp,iot,3rdparty) --->ETL Streaming --->Snowflake(on top of cloud) --->Data consumer
#The value of cloud Data platform:-1)One platform one copy of data many workloads(DW,DE,DL,DAPPS,DEC,DS),2)Unlimited performance & scale,3)secure governed access to all data,4)near-zero Maintence as a srvc. 
#
#2)Self-Registration:-with snowflake free trial edition(worth $400 & 30days)   vps edition(virtual private snowflake)
#Goto Snowflake edition help page,pricing page. select platform    here we have 4types of pricings 1)Standard,2)Enterprise,3)Buiness critical,4)Virtual private snowflake(vps)
#Hands on:-Select Cloud & Region, Start for free.give Details,continue.As or Enterprise or business critical. aws,region,get started. goto email & activate.now give user & password. by defaultly we get admin(SYSADMIN) but we have total 5Roles.Help here we can download connectors done,DBS,shares,Data marketplace,warehouse,worksheets,history. all the regions are grouped as 3 global geographic segments(North america,Europe,ASia Pacific). 
#Snowflake comes with a 30days free trial edition & allow you to choose a cloud provider(AWS/Azure/Gcp). this Free trial is loadded with 400$ credit & if this credit is exhausted,& we you want to you further credit card detail is required. 
#Snowflake credit cost depends on the snowflake edition & it does not depend on cloud provider & region. Snowflake standard edition does not get 24hr early access to new weekly releases.Each Snowflake acc is hosted in a single region(MFA is enabled even for free tial edition users & it has to be activated by individual user by going to prefrences).Extended time travel works for enterpride & above.  
#
#3)Snowflak Architecture:-
#Snowflake has 3unique layers:-1)Storage layer,2)Compute layer,3)Cloud srvc layer-brain of the snowflake,(Virtually infinite scalability & Decoupling of srvc)(storage vs compute vs metadata) 
#Shared disk Architecture(Compute=processing=SQL statements or ETL Jobs)1)multiple nodes we can access the single storage system(disk),single point of failure,as it scales up(vertical scaling it becomes more expensive).                  
#Shared nothing Architecture:1)each node in the cluster has a portion of the data along with computing power,no single point failure,add more nodes scales horizontal.  
#Apache Hadoop:-(Distributed computing (storage +compute tightly coupled)),HDFS is distributed storage & map reduce is distributed compute engine. 
#Apache Spark:-(Distributed computing-resilient Distributed Data),it is pure memory computation engine that runs on top of Hadoop ecosystem. 
#Cloudera Impala(MPP = Massive parallel processing)(~shared Nothing Architecture),this is also in the memory query excution engine & runs on the top of cloudera Hadoop distribution. 
#Cassandra(shared Nothing Architecture),
#Traditional/Enterprise data warehouse sloution. they are also MPP engines but they are very expensive.  
#*Snowflake unique architecture:-Hybrid Approach(Decouple Compute & storage=scale them independently.multi cluster shared data Architecture.full Advantage of cloud native features(Elasticity).sf has 3layered unique architecture:1)Data Storage layer(s3,blob,GCP bucket)pay only for stored data,2)Compute & processing layer(EC2,Azure vm,GCP VM),3)cloud srvc layer(brain of sf):-used for Authentication & Authorisation(Each layer can scale independently) 
#1)Snowflake storage layer:-Snowflake stores all data into DBS & the DB is logical grouping of objs with Snowflake ins.objs = tables ,stores any structured data or semi-structured,non-relational data. Snowflake convert then into optimised columnar format. Encrypt it AES 256 strong encryption. The data only accessed by SQL & there are no others means that it is accessible.If the time travel feature is enabled,it is also part of the storage cost.   
#2)Snowflake computer layer:-is where queries executed.Before any query is excuted,comute m/cs need to be create & in snowflake, it is called virtual warehouse(VWH).  
#3)Cloud srvc layer:-brain of the snowflake. this layer also coordinates & manages the entire system.(authentication & authorisation,session management,virtual warehouse management,manage & maintain the life cycle of a query)
#Snowflake=redshift(aws),BigQuery(google),Synapse(Azure),Databricks(AWS/Azure)
#only build for cloud & supported in 3 major cloud platforms(aws,azure,gcp). no on-premises version is avilable.recommended to use olap not for oltp. no indexing,no performance optimisation,no partition,no physical design required. 
#
#4)Classic/Legacy:-showing web interface:-general usage & obj Navigation.  
#Top menu(right):-user profile menu
#Top menu(left):-Databases
#Navigation Tree:-(search,Databases)
#Query pane:-(worksheet)
#Result pane:-(result,Data preview,History)
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
# 
# 
# 

#print("hello")







