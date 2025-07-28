import marimo

__generated_with = "0.14.13"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return


@app.cell
def _():
    from diagrams import Cluster, Diagram
    from diagrams.aws.compute import ECS
    from diagrams.aws.database import ElastiCache, RDS
    from diagrams.aws.network import ELB
    from diagrams.aws.network import Route53

    with Diagram("Clustered Web Services", show=False) as diagram:
        dns = Route53("dns")
        lb = ELB("lb")

        with Cluster("Services"):
            svc_group = [ECS("web1"),
                         ECS("web2"),
                         ECS("web3")]

        with Cluster("DB Cluster"):
            db_primary = RDS("userdb")
            db_primary - [RDS("userdb ro")]

        memcached = ElastiCache("memcached")

        dns >> lb >> svc_group
        svc_group >> db_primary
        svc_group >> memcached

    return (diagram,)


@app.cell
def _(diagram):
    diagram
    return


if __name__ == "__main__":
    app.run()
