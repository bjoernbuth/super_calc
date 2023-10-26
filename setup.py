from setuptools import setup, find_packages

setup(
    name="supercalc",
    version="1.0.0",
    author="Bjoern",
    packages=find_packages(),
    install_requires=[
        "click",
    ],
    entry_points={
        "console_scripts": [
            "suca = supercalc.simple.simple_calc:cli",
            "sucas = supercalc.scientific.scientific_calc:cli",
            # "ncs = supercalc.scientific.scientific_calc:cli",
            # "supercalc_financial = supercalc.financial.financial_calc:financial_func",
            # "supercalc_graphing = supercalc.graphing.graphing_calc:graph_func",
        ],
    },
)
