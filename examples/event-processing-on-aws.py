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
    from diagrams.aws.compute import ECS, EKS, Lambda
    from diagrams.aws.database import Redshift
    from diagrams.aws.integration import SQS
    from diagrams.aws.storage import S3

    with Diagram("Event Processing", show=False) as diagram:
        source = EKS("k8s source")

        with Cluster("Event Flows"):
            with Cluster("Event Workers"):
                workers = [ECS("worker1"),
                           ECS("worker2"),
                           ECS("worker3")]

            queue = SQS("event queue")

            with Cluster("Processing"):
                handlers = [Lambda("proc1"),
                            Lambda("proc2"),
                            Lambda("proc3")]

        store = S3("events store")
        dw = Redshift("analytics")

        source >> workers >> queue >> handlers
        handlers >> store
        handlers >> dw

    return (diagram,)


@app.cell
def _(diagram):
    diagram
    return


if __name__ == "__main__":
    app.run()
