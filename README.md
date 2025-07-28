
# Marimo Multi-Cloud Diagrams

The purpose of this project to create any cloud diagrams (or really any diagrams) supported by the [diagrams Python package](https://diagrams.mingrammer.com/) in [Marimo](https://marimo.io/) reactive notebooks. The idea here is that as diagrams python code is written and correct, the diagram is rendered immediately in the marimo "reactive" notebook cell without creating any other files. Since the marimo notebook is still a python file, a png (or similar graphics format) file can be created for documentation or whatever from running the command python diagrams-file.py

The main python file multicloud-dual-datancenter.py was generated in Claude Sonnet 4 from the png file internet-multicloud-image/5-dual-DC-cloud-only-MCR.png. This was a rough test for this commit.

The /examples folder recreates diagrams from the [diagrams examples](https://diagrams.mingrammer.com/docs/getting-started/examples) and for custom remote icons from [here](https://diagrams.mingrammer.com/docs/nodes/custom) and [here](https://diagrams.mingrammer.com/docs/getting-started/examples#rabbitmq-consumers-with-custom-nodes)

The python virtual environment is included. That and the project dependencies are managed by [uv](https://docs.astral.sh/uv/). The other requirement for the diagrams module to render the diagram is that [graphviz](https://www.graphviz.org/) needs to be installed as well.

To edit and run the marimo notebook, just run the command: marimo edit file.py



