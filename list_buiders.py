from sphinx.application import Sphinx

def list_builders():
    # Update paths to match your project structure
    srcdir = 'source'  # Directory containing your Sphinx source files including conf.py
    confdir = 'source'  # Directory containing conf.py
    outdir = './_build'  # Output directory for built documents
    doctreedir = './_doctree'  # Directory for doctree files

    # Create a dummy Sphinx application context
    app = Sphinx(
        srcdir=srcdir,
        confdir=confdir,
        outdir=outdir,
        doctreedir=doctreedir,
        buildername='dummy'  # Use a dummy builder to avoid side effects
    )

    # Now app.builder is initialized, you can access the builder registry
    print("Registered builders:")
    for builder_name in sorted(app.registry.builders):
        print(builder_name)

if __name__ == "__main__":
    list_builders()
