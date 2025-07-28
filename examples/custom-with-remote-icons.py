import marimo

__generated_with = "0.14.13"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return


@app.cell
def _():
    from diagrams import Diagram, Cluster
    from diagrams.custom import Custom
    from urllib.request import urlretrieve

    with Diagram("Custom with remote icons", show=False, filename="custom_remote", direction="LR") as diagram:

      # download the icon image file
      diagrams_url = "https://github.com/mingrammer/diagrams/raw/master/assets/img/diagrams.png"
      diagrams_icon = "diagrams.png"
      urlretrieve(diagrams_url, diagrams_icon)

      diagrams = Custom("Diagrams", diagrams_icon)

      with Cluster("Some Providers"):

        openstack_url = "https://github.com/mingrammer/diagrams/raw/master/resources/openstack/openstack.png"
        openstack_icon = "openstack.png"
        urlretrieve(openstack_url, openstack_icon)

        openstack = Custom("OpenStack", openstack_icon)

        elastic_url = "https://github.com/mingrammer/diagrams/raw/master/resources/elastic/saas/elastic.png"
        elastic_icon = "elastic.png"
        urlretrieve(elastic_url, elastic_icon)

        elastic = Custom("Elastic", elastic_icon)

      diagrams >> openstack
      diagrams >> elastic

    return (diagram,)


@app.cell
def _(diagram):
    diagram
    return


if __name__ == "__main__":
    app.run()
