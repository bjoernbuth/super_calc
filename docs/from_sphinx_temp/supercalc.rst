
supercalc
*********


scientific
==========

This module contains the code for the scientific calculator: - sin -
cos - tan - log - sqrt

**supercalc.scientific.scientific_calc.tan(x)**

   Calculate tangent of x


simple
======

Example Google style docstrings.

This module demonstrates documentation as specified by the `Google
Python Style Guide
<https://google.github.io/styleguide/pyguide.html>`_. Docstrings may
extend over multiple lines. Sections are created with a section header
and a colon followed by a block of indented text.

-[ Example ]-

Examples can be given using either the ``Example`` or ``Examples``
sections. Sections support any reStructuredText formatting, including
literal blocks:

::

   $ python example_google.py

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

``- module_level_variable1``

   Module level variables may be documented in either the
   ``Attributes`` section of the module docstring, or in an inline
   docstring immediately following the variable.

   Either form is acceptable, but the two should not be mixed. Choose
   one convention to document module level variables and be consistent
   with it.

   :Type:
      int

``- another var``

   laber bla bla

   :Type:
      custom type

**class supercalc.simple.simple_calc.CustomGroup(name: str | None =
None, commands: MutableMapping[str, Command] | Sequence[Command] |
None = None, **attrs: Any)**

   **get_help(ctx)**

      Formats the help into a string and returns it.

      Calls ``format_help()`` internally.

**supercalc.simple.simple_calc.add_orig(numbers)**

   Add numbers together
