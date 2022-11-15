#This will provide the FRAMEWORK to allow the directory structure for most Terraform projects to be created. The directory structure are inline with 
#with terraform best-practices
#
# Fare use, this software is intended for learning purposes, feel free to modify as you see fit. Please branch your work from the main repository. Contact 
# repository owner for main brach merge peer review


#Import os module
import os

#Define path of VPC directory & standard Terraform files
vpc_path = os.path.join("vpc","variables.tf","outputs.tf","main.tf")

#Create VPC directory & standard Terraform files
os.makedirs(vpc_path)

#Define path for vpc backend services directory & standard Terraform files
vpc_services_backend_path = os.path.join("services","back-end","variables.tf","outputs.tf","main.tf")

#Create directory & standard Terraform files for vpc back-end services
os.makedirs(vpc_services_backend_path)

#Define path for vpc front-end services directory & standard Terraform files
vpc_services_frontend_path =  os.path.join("services","front-end","variables.tf","outputs.tf","main.tf")

#Create directory & standard files for vpc front-end services
os.makedirs(vpc_services_frontend_path)

#Define path for webserver-cluster service directory & standard Terraform files
webserver_cluster = os.path.join("services","webserver_cluster","variables.tf","outputs.tf","main.tf")

#Create path for webserver-cluster directory & Terraform standard files
os.makedirs(webserver_cluster)

#Define path for data-storage directory & standard Terraform files for mysql
data_storage_mysql = os.path.join("data-storage","mysql","variables.tf","outputs.tf","main.tf")

#Create path for data-storage directory & stanard Terraform files for mysql
os.makedirs(data_storage_mysql)

#Define path for data-storage directory for standard Terraform files for redis
data_storage_redis = os.path.join("data-storage","redis","variables.tf","outputs.tf","main.tf")

#Create path for data-storage directory & standard Terraform files for redis
os.makedirs(data_storage_redis)

#Define path for s3 directory & Terraform standard files
s3 = os.path.join("global","s3","variables.tf","outputs.tf","main.tf")

#Create path for s3 diretory & Terraform standard files
os.makedirs(s3)

#Define path for jenkins directory & Terraform standard files
jenkins = os.path.join("mgmt","services","jenkins","variables.tf","output.tf","main.tf")

#Create path for jenkins directory & Terraform standard files
os.makedirs(jenkins)

#Define path for bastion_host Terraform standard files
bastion_host = os.path.jon("mgmt","services","bastion_host","main.tf","output.tf","variables.tf")

#Create path for bastion_host directory & Terraform standard files
os.makedirs(bastion_host)

#Define mgmt vpc directory & Terraform standard files 
mgmt_vpc = os.path.join("mgmt","vpc","main.tf","output.tf","variables.tf")

#Create mgmt vpc directory & Terraform standard files
os.makedirs(mgmt_vpc)

#Define 























