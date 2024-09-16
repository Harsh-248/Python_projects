import pywhatkit as pw
#input text
txt = """The Python Package Index (PyPI) is a repository of software for the Python programming language.
        f the package is not on PyPI, it might be hosted on GitHub or another repository. For instance, you might find it on GitHub and can install it using pip directly from the repository."""

pw.text_to_handwriting(txt,"demo.py",[0,0,138]) #text,file where to save the ouput file, text color

print(" END ")