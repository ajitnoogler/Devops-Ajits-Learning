# Creating User and Identity domain
Create Identity domain.
Create User - IAM user or Identity Center user. and cabalilities Local_pass API Keys Auth Token

Identity & Security -> User -> test_user -> Assign user to group.
Identity & Security -> User -> Click test_user -> Resources -> API Keys.
Identity & Security -> User -> Click test_user -> Resources -> API_Token

# IAM Policies: Part of Identity Service
- Go to Identity & Security. Click default Domain.
- Select Iam_user here you will user part of which group.
- Got to o to Identity & Security, click on "Policies"
- Create Policy -> Name: Policy_for_IAM_User -> select Compartment,
    Policy Builder - Policy-usecase and common policy template.

- Basic Syntax:
    Allow <subject> <verb> <Resource> in <location>
    Subject - user or group or principle
    verb - inspect (3rd Party Auditor) |
           read Internal (auditor )| 
           use (Day to Day end user resources) | 
           manage (Adminstrator)
    Condition i.e Bucket Name etc.

    Allow <subject> <verb> <Resource> in <location> where <condition>

Sample Syntax: "Allow group iamgroup to inspect buckets in tenancy" -> Click Create. Its read-only
               "Allow group iamgroup to manage buckets in tenancy" Click Create. Its has admin rights.

# How to restrict user to parent compartment and out of two child compartment he should only authorised
# to access to only child-3 compartment.
i.e Comapartment ==> OCI_Dev_parent/Child-1/Child-2/Child-3/

"Allow group iamgroup to inspect buckets in compartment Child-1:Child-2:Child-3" -> Create.



# Summary:
Authentication - Who can access cloud resources. OCI IAM Service (Identity Domain).
Authorization  -  What level of access is provided to user to access which Cloud resources.
Policies       - It is used to provide authorization via users and group using policy builder.
Compartments   - Its a logical group of oci resources. like folder and subfolder and files/oci resource under it.








