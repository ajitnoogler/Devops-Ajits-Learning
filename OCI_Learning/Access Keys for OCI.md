# Access Keys for OCI
Api-key - For accessing resource using Api
Auth-Tokens - For authenticating 3rd party Api
customer secret key - For object storage Api to enable interopearbility with Amazon S3.
oAuth 2.0 - A secure token to access those RestApi endpoints. i.e OCI Cloud Analytics. valid for 1hr.
SMTP Creds - Its used for Sending Email using email delevery service.


# 3 Option to download API_Key:
Identity Domain -> User -> Click test_user -> Resources -> API Keys.
- Generate API Key Pair.
- Choose Public key file
- Paste Public Key

# Connecting to OCI 
- OCID is like Amazon ARN Amazon resource numbering,a unique id for each resources.
- OCID of the user can be found when you click on user under -> User Information.
- OCID of Tenancy can be found when you click on Profile Icon (User Symbol) and click on tenancy.

From Linux CLI: via ssh
$ oci iam region list 
$ oci setup config
    - Location of config
    - paste oci id of user
    - paste oci id of tenancy
    - Choose region by passing Region ID no
    - Enter directory of your keys created [/home/user_test/.oci]:
    - Enter name for yur keys [oci_api_key]
    - Passphares - highly recommended
This will create key pair pri/pub key "cd /home/opc/.oci"
Copy content of Public key

Go to - Identity Domain -> User -> Click test_user -> Resources -> API Keys.
select Paste Public key. and copy paste the public key -> close

Now Lets run oci cli commands
$ oci iam region list // Now you should above to view region list for that tenency.
$ oci os bucket list -- compartment-id <OC-ID> // to list object storage. You get Json Response key value format.
