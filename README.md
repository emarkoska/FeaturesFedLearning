A basic object-oriented framework for computing transformations on a dataset.
Elena Markoska

# Introduction
The framework uses a domain specific language (DSL) which has been implemented as a subset of Python.
A user-developer creates a config file using this DSL which uses pre-made functionality for modifying dataset columns and preprocessing.
The user-developer is able to specify preprocessing methods, input and output files, supported changes on columns
using lambda expressions.

Refer to the Running section for a quick demo

# Exlanation of modules
The framework consists of four key modules, developed for with flexibility, modularity, and maintainability in mind.
Docstrings have been added where appropriate, not excessively so, with intention to not add more noise than necessary.

InputAdapter.py implements several static methods for opening csv, json, excel files, and illustrates how additional
functions could be implemented too, which would convert sources such as sql query reults etc.

The inner operations of the framework are done using pandas. All internal representations of the dataset
are done with a dataframe and series where applicable.

Transformer.py implements several static methods for data manipulation. The class is divided into transformation functions
and preprocessing functions. The transformation functions create new columns. The preprocessing functions make changes on the
dataframe as a whole. Currently, the Transformer class is rather bare with only 4 methods, however it could be extended to
increase the flexibility of the functionality it offers

OutputAdapter.py, similarly to InputAdapter.py, offers several methods that convert the internal pandas dataframe to csv or json.
This module can also be extended with more methods that are appropriate to the specific problem.

Finally, Parser.py ties everything together.
Parser.py uses eval() to parse the specified config file.
After this parsing, it opens the input file, runs the pre-processing and transformation functions, and makes an output file.

# Running
Unpack the tar.gz file.
Open cmd. Navigate to the project directory
Run 'Parser.py Configuration/test01.config'

An output file should be generated titled out.csv - Check it out. Enjoy!

# Tinkering and testing
Open the Parser.py module.
Scroll down to __main__():
Uncomment the block that's indicated for uncommenting. Comment the following block.

# Known present difficulties
Loading very large files in a pandas object requires a lot of RAM.
A better approach would be to parse the input files row by row. A beginning for this kind of an approach is in the notes folder, named csvmap.
The notes are incomplete and it's not a working program, but it illustrates how we'd use row-parsing instead of file loading and subsequent parsing.

# Advantages
1. The user-developer of this framework doesn't need to have any pandas knowledge.
2. In a very large team, we don't need to pass the complexity of the framework or its inner-design/framework onto the developer. Instead s/he can simply write config files.

