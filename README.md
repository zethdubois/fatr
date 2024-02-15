# FATR

# PVTTL Notes

Given the instruction that a filename should be supplied as a `fname` keyword argument, the correct way to call the `write` method with a filename would look like this:

`df.write(fname='test.csv')`

Here, `fname='test.csv'` explicitly names the keyword argument, telling the `write` method what the filename should be. This is a common pattern in Python when a function or method requires specific named arguments rather than positional arguments (which are just passed in order).

Clone the repo `git@github.com:rogerlew/pyvttbl.git` into `venv/lib/sitepackages`
