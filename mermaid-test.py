import marimo

__generated_with = "0.14.13"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.mermaid

    requirementdiagram = '''
        requirementDiagram

        requirement test_req {
        id: 1
        text: the test text.
        risk: high
        verifymethod: test
        }

        element test_entity {
        type: simulation
        }

        test_entity - satisfies -> test_req

    '''

    mo.mermaid(requirementdiagram)
    return


@app.cell
def _(mo):
    mo.mermaid

    largeflowdiagram = '''
    graph TB
        sq[Square shape] --> ci((Circle shape))

        subgraph A
            od>Odd shape]-- Two line<br/>edge comment --> ro
            di{Diamond with <br/> line break} -.-> ro(Rounded<br>square<br>shape)
            di==>ro2(Rounded square shape)
        end

        %% Notice that no text in shape are added here instead that is appended further down
        e --> od3>Really long text with linebreak<br>in an Odd shape]

        %% Comments after double percent signs
        e((Inner / circle<br>and some odd <br>special characters)) --> f(,.?!+-*ز)

        cyr[Cyrillic]-->cyr2((Circle shape Начало));

         classDef green fill:#9f6,stroke:#333,stroke-width:2px;
         classDef orange fill:#f96,stroke:#333,stroke-width:4px;
         class sq,e green
         class di orange
    '''

    mo.mermaid(largeflowdiagram)
    return


@app.cell
def _(mo):
    mo.mermaid

    mindmapdiagram1 = '''
        mindmap
            id1["`**Root** with a second line
                Unicode works too: 🤓`"]
            id2["`The dog in **the** hog... a *very long text* that wraps to a new line`"]
            id3[Regular labels still works]
    '''

    mo.mermaid(mindmapdiagram1)
    return


@app.cell
def _(mo):
    mo.mermaid

    mindmapdiagram2 = '''
        mindmap
          root((mindmap))
            Origins
              Long history
              ::icon(fa fa-book)
              Popularisation
                British popular psychology author Tony Buzan
            Research
              On effectiveness<br/>and features
              On Automatic creation
                Uses
                    Creative techniques
                    Strategic planning
                    Argument mapping
            Tools
              Pen and paper
              Mermaid
    '''

    mo.mermaid(mindmapdiagram2)
    return


if __name__ == "__main__":
    app.run()
