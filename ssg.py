import typer
import Site from ssg.site

def main(source="content", dest="dist"):
    config={}
    config["source"] = source
    config["dest"] = dest
    site = Site(config["source"], config["dest"])
    site.build()

typer.run(main)
