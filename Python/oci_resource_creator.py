import oci

# Load OCI config
config = oci.config.from_file()

def create_bucket():
    object_storage = oci.object_storage.ObjectStorageClient(config)
    namespace = object_storage.get_namespace().data

    bucket_name = input("Enter the name of the bucket to create: ")
    compartment_id = config["compartment_id"]

    create_bucket_details = oci.object_storage.models.CreateBucketDetails(
        name=bucket_name,
        compartment_id=compartment_id,
        public_access_type="NoPublicAccess",
        storage_tier="Standard"
    )

    response = object_storage.create_bucket(namespace, create_bucket_details)
    print(f"Bucket '{bucket_name}' created successfully.")
    print(response.data)

def create_instance():
    compute_client = oci.core.ComputeClient(config)
    network_client = oci.core.VirtualNetworkClient(config)

    compartment_id = config["compartment_id"]
    availability_domain = input("Enter availability domain (e.g., 'Uocm:IN-HYD-1-AD-1'): ")
    subnet_id = input("Enter subnet OCID: ")
    image_id = input("Enter image OCID: ")
    shape = "VM.Standard.E2.1.Micro"

    metadata = {
        "ssh_authorized_keys": input("Enter your public SSH key: ")
    }

    launch_instance_details = oci.core.models.LaunchInstanceDetails(
        availability_domain=availability_domain,
        compartment_id=compartment_id,
        shape=shape,
        display_name="DemoInstance",
        image_id=image_id,
        subnet_id=subnet_id,
        metadata=metadata
    )

    response = compute_client.launch_instance(launch_instance_details)
    print("Instance launched. Details:")
    print(response.data)

def main():
    print("What do you want to create?")
    print("1. OCI Bucket")
    print("2. OCI Instance")

    choice = input("Enter 1 or 2: ")

    if choice == "1":
        create_bucket()
    elif choice == "2":
        create_instance()
    else:
        print("Invalid choice. Exiting...")

if __name__ == "__main__":
    main()
