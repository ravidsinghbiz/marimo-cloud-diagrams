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
    from diagrams.aws.network import VPC
    from diagrams.aws.security import IAM
    from diagrams.azure.compute import VM
    from diagrams.azure.network import VirtualNetworks
    from diagrams.azure.integration import ServiceBus
    from diagrams.gcp.compute import ComputeEngine
    from diagrams.gcp.network import VPC as GCP_VPC
    from diagrams.gcp.devtools import ContainerRegistry
    from diagrams.oci.compute import VM
    from diagrams.oci.network import Vcn
    from diagrams.oci.security import CloudGuard
    from diagrams.generic.network import Router
    from diagrams.generic.compute import Rack

    # Custom styling for different connection types
    private_edge = Edge(color="purple", style="solid", label="Private VIF")
    msft_edge = Edge(color="green", style="dashed", label="MSFT")
    private_connection = Edge(color="blue", style="solid", label="Private")
    dro_connection = Edge(color="red", style="solid", label="DRO")

    with Diagram("Multi-Cloud Network Architecture", show=False, direction="TB") as cloudiagram:
    
        # MCR nodes at the bottom
        with Cluster("MCR01"):
            mcr01 = Router("MCR01")
            rack01 = Rack("DC01")
    
        with Cluster("MCR02"):
            mcr02 = Router("MCR02")
            rack02 = Rack("DC02")
    
        # AWS Cloud
        with Cluster("AWS"):
            with Cluster("VXC01"):
                aws_iam = IAM("Security")
                aws_ec2 = EC2("Compute")
                aws_vpc = VPC("VPC")
        
            with Cluster("VXC05"):
                aws_iam2 = IAM("Security")
                aws_ec2_2 = EC2("Compute")
    
        # Azure Cloud
        with Cluster("Azure"):
            with Cluster("VXC02 (Q-in-Q)"):
                azure_servicebus = ServiceBus("Integration")
                azure_vm = VM("VM")
                azure_network = VirtualNetworks("Network")
        
            with Cluster("VXC06 (Q-in-Q)"):
                azure_servicebus2 = ServiceBus("Integration")
                azure_vm2 = VM("VM")
    
        # Google Cloud
        with Cluster("Google Cloud"):
            with Cluster("VXC03"):
                gcp_registry = ContainerRegistry("Registry")
                gcp_compute = ComputeEngine("Compute")
        
            with Cluster("VXC07"):
                gcp_registry2 = ContainerRegistry("Registry")
                gcp_compute2 = ComputeEngine("Compute")
    
        # Oracle Cloud
        with Cluster("Oracle Cloud"):
            with Cluster("VXC04"):
                oci_guard = CloudGuard("Security")
                oci_vm = VM("VM")
                oci_vcn = Vcn("VCN")
        
            with Cluster("VXC09"):
                oci_guard2 = CloudGuard("Security")
                oci_vm2 = VM("VM")
    
        # Connections from MCR01
        mcr01 >> private_edge >> aws_vpc
        mcr01 >> private_edge >> aws_iam2
        mcr01 >> msft_edge >> azure_network
        mcr01 >> private_connection >> gcp_compute
        mcr01 >> dro_connection >> oci_vcn
    
        # Connections from MCR02
        mcr02 >> private_edge >> aws_vpc
        mcr02 >> private_edge >> aws_iam2
        mcr02 >> msft_edge >> azure_servicebus2
        mcr02 >> private_connection >> gcp_compute2
        mcr02 >> dro_connection >> oci_vm2
    
        # Inter-MCR connection
        mcr01 >> Edge(color="gray", style="solid") >> mcr02
    
        # Cross-connections between clouds (simplified)
        aws_vpc >> Edge(color="purple", style="dotted") >> gcp_compute
        azure_network >> Edge(color="blue", style="dotted") >> oci_vcn
        gcp_compute >> Edge(color="red", style="dotted") >> oci_vcn
    return (cloudiagram,)


@app.cell
def _(cloudiagram):
    cloudiagram
    return


if __name__ == "__main__":
    app.run()
