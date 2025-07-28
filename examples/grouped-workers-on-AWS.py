import marimo

__generated_with = "0.14.13"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return


@app.cell
def _():
    from diagrams import Diagram
    from diagrams.aws.compute import EC2
    from diagrams.aws.database import RDS
    from diagrams.aws.network import ELB

    with Diagram("Grouped Workers", show=False, direction="TB") as diagram:
        ELB("lb") >> [EC2("worker1"),
                      EC2("worker2"),
                      EC2("worker3"),
                      EC2("worker4"),
                      EC2("worker5")] >> RDS("events")

    return (diagram,)


@app.cell
def _(diagram):
    diagram
    return


if __name__ == "__main__":
    app.run()
