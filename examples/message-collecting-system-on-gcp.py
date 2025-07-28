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
    from diagrams.gcp.analytics import BigQuery, Dataflow, PubSub
    from diagrams.gcp.compute import AppEngine, Functions
    from diagrams.gcp.database import BigTable
    from diagrams.gcp.iot import IotCore
    from diagrams.gcp.storage import GCS

    with Diagram("Message Collecting", show=False) as diagram:
        pubsub = PubSub("pubsub")

        with Cluster("Source of Data"):
            [IotCore("core1"),
             IotCore("core2"),
             IotCore("core3")] >> pubsub

        with Cluster("Targets"):
            with Cluster("Data Flow"):
                flow = Dataflow("data flow")

            with Cluster("Data Lake"):
                flow >> [BigQuery("bq"),
                         GCS("storage")]

            with Cluster("Event Driven"):
                with Cluster("Processing"):
                    flow >> AppEngine("engine") >> BigTable("bigtable")

                with Cluster("Serverless"):
                    flow >> Functions("func") >> AppEngine("appengine")

        pubsub >> flow

    return (diagram,)


@app.cell
def _(diagram):
    diagram
    return


if __name__ == "__main__":
    app.run()
