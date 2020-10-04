import typer
from ssg.site import Site

def main(source="content", dest="dist"):
    config = {"source": source, "dest": dest}

    s = Site(**config).build()

typer.run(main)