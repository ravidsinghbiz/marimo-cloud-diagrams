import marimo

__generated_with = "0.14.13"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return


app._unparsable_cell(
    r"""
    from urllib.request import urlretrieve

    from diagrams import Cluster, Diagram
    from diagrams.aws.database import Aurora
    from diagrams.custom import Custom
    from diagrams.k8s.compute import Pod

    # Download an image to be used into a Custom Node class
    rabbitmq_url = \"https://jpadilla.github.io/rabbitmqapp/assets/img/icon.png\"
    rabbitmq_icon = \"rabbitmq.png\"
    urlretrieve(rabbitmq_url, rabbitmq_icon)

    with Diagram(\"Broker Consumers\", show=False) as diagram
        with Cluster(\"Consumers\"):
            consumers = [
                Pod(\"worker\"),
                Pod(\"worker\"),
                Pod(\"worker\")]

        queue = Custom(\"Message queue\", rabbitmq_icon)

        queue >> consumers >> Aurora(\"Database\")
    """,
    name="_"
)


@app.cell
def _(diagram):
    diagram
    return


if __name__ == "__main__":
    app.run()
