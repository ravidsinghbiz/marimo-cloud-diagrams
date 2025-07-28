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
    from diagrams.c4 import Person, Container, Database, System, SystemBoundary, Relationship

    graph_attr = {
        "splines": "spline",
    }

    with Diagram("Container diagram for Internet Banking System", direction="TB", graph_attr=graph_attr) as diagram:
        customer = Person(
            name="Personal Banking Customer", description="A customer of the bank, with personal bank accounts."
        )

        with SystemBoundary("Internet Banking System"):
            webapp = Container(
                name="Web Application",
                technology="Java and Spring MVC",
                description="Delivers the static content and the Internet banking single page application.",
            )

            spa = Container(
                name="Single-Page Application",
                technology="Javascript and Angular",
                description="Provides all of the Internet banking functionality to customers via their web browser.",
            )

            mobileapp = Container(
                name="Mobile App",
                technology="Xamarin",
                description="Provides a limited subset of the Internet banking functionality to customers via their mobile device.",
            )

            api = Container(
                name="API Application",
                technology="Java and Spring MVC",
                description="Provides Internet banking functionality via a JSON/HTTPS API.",
            )

            database = Database(
                name="Database",
                technology="Oracle Database Schema",
                description="Stores user registration information, hashed authentication credentials, access logs, etc.",
            )

        email = System(name="E-mail System", description="The internal Microsoft Exchange e-mail system.", external=True)

        mainframe = System(
            name="Mainframe Banking System",
            description="Stores all of the core banking information about customers, accounts, transactions, etc.",
            external=True,
        )

        customer >> Relationship("Visits bigbank.com/ib using [HTTPS]") >> webapp
        customer >> Relationship("Views account balances, and makes payments using") >> [spa, mobileapp]
        webapp >> Relationship("Delivers to the customer's web browser") >> spa
        spa >> Relationship("Make API calls to [JSON/HTTPS]") >> api
        mobileapp >> Relationship("Make API calls to [JSON/HTTPS]") >> api

        api >> Relationship("reads from and writes to") >> database
        api >> Relationship("Sends email using [SMTP]") >> email
        api >> Relationship("Makes API calls to [XML/HTTPS]") >> mainframe
        customer << Relationship("Sends e-mails to") << email

    return (diagram,)


@app.cell
def _(diagram):
    diagram
    return


if __name__ == "__main__":
    app.run()
