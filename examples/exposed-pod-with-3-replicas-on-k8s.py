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
    from diagrams.k8s.clusterconfig import HPA
    from diagrams.k8s.compute import Deployment, Pod, ReplicaSet
    from diagrams.k8s.network import Ingress, Service

    with Diagram("Exposed Pod with 3 Replicas", show=False) as diagram:
        net = Ingress("domain.com") >> Service("svc")
        net >> [Pod("pod1"),
                Pod("pod2"),
                Pod("pod3")] << ReplicaSet("rs") << Deployment("dp") << HPA("hpa")

    return (diagram,)


@app.cell
def _(diagram):
    diagram
    return


if __name__ == "__main__":
    app.run()
