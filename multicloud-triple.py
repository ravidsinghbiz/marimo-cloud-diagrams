import marimo

__generated_with = "0.14.13"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return


@app.cell
def _():
    from diagrams import Diagram, Cluster, Edge
    from diagrams.aws.compute import EC2
    from diagrams.aws.database import RDS
    from diagrams.aws.network import ELB, CloudFront
    from diagrams.aws.storage import S3
    from diagrams.azure.compute import VM
    from diagrams.azure.database import CosmosDb
    from diagrams.azure.network import LoadBalancers, ApplicationGateway
    from diagrams.azure.storage import BlobStorage
    from diagrams.gcp.compute import ComputeEngine
    from diagrams.gcp.database import Firestore
    from diagrams.gcp.network import LoadBalancing
    from diagrams.gcp.storage import GCS
    from diagrams.onprem.client import Users
    from diagrams.onprem.network import Internet

    # Create the multicloud architecture diagram
    with Diagram("Multicloud Architecture", show=False, direction="TB") as cloudiagram:
        # Users and Internet
        users = Users("Users")
        internet = Internet("Internet")
    
        # AWS Cloud
        with Cluster("AWS Cloud"):
            aws_cdn = CloudFront("CloudFront CDN")
            aws_lb = ELB("Application Load Balancer")
        
            with Cluster("AWS Compute"):
                aws_web = [EC2("Web Server 1"), EC2("Web Server 2")]
        
            with Cluster("AWS Data"):
                aws_db = RDS("PostgreSQL")
                aws_storage = S3("S3 Storage")
    
        # Azure Cloud
        with Cluster("Azure Cloud"):
            azure_gateway = ApplicationGateway("App Gateway")
            azure_lb = LoadBalancers("Load Balancer")
        
            with Cluster("Azure Compute"):
                azure_vm = [VM("VM 1"), VM("VM 2")]
        
            with Cluster("Azure Data"):
                azure_db = CosmosDb("Cosmos DB")
                azure_storage = BlobStorage("Blob Storage")
    
        # GCP Cloud
        with Cluster("Google Cloud"):
            gcp_lb = LoadBalancing("Cloud Load Balancer")
        
            with Cluster("GCP Compute"):
                gcp_vm = [ComputeEngine("Instance 1"), ComputeEngine("Instance 2")]
        
            with Cluster("GCP Data"):
                gcp_db = Firestore("Firestore")
                gcp_storage = GCS("Cloud Storage")
    
        # Define connections
        users >> internet
    
        # AWS connections
        internet >> aws_cdn >> aws_lb >> aws_web
        aws_web >> aws_db
        aws_web >> aws_storage
    
        # Azure connections
        internet >> azure_gateway >> azure_lb >> azure_vm
        azure_vm >> azure_db
        azure_vm >> azure_storage
    
        # GCP connections
        internet >> gcp_lb >> gcp_vm
        gcp_vm >> gcp_db
        gcp_vm >> gcp_storage
    
        # Cross-cloud connections (data replication/backup)
        aws_db >> Edge(label="backup", style="dashed") >> azure_db
        azure_storage >> Edge(label="sync", style="dashed") >> gcp_storage
        gcp_db >> Edge(label="replicate", style="dashed") >> aws_db
    return (cloudiagram,)


@app.cell
def _(cloudiagram):
    cloudiagram
    return


if __name__ == "__main__":
    app.run()
