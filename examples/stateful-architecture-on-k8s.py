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
    from diagrams.k8s.compute import Pod, StatefulSet
    from diagrams.k8s.network import Service
    from diagrams.k8s.storage import PV, PVC, StorageClass

    with Diagram("Stateful Architecture", show=False) as diagram:
        with Cluster("Apps"):
            svc = Service("svc")
            sts = StatefulSet("sts")

            apps = []
            for _ in range(3):
                pod = Pod("pod")
                pvc = PVC("pvc")
                pod - sts - pvc
                apps.append(svc >> pod >> pvc)

        apps << PV("pv") << StorageClass("sc")
    return (diagram,)


@app.cell
def _(diagram):
    diagram
    return


if __name__ == "__main__":
    app.run()
