# FATR

# setup

## pyvttbl
Clone the repo `git@github.com:rogerlew/pyvttbl.git` into `venv/lib/sitepackages`

requires: scipy

## jupyter-lab

consider setting up Jupyter Lab in user site-packages to avoid redundant installs across projects.

To install Jupyter globally for your user (and not system-wide), ensuring it's available across all your projects, you can use the --user option with pip. Here’s how:

```shell
pip install --user jupyterlab
```

This command installs JupyterLab in your USER_SITE directory, which is typically something like ~/.local/lib/pythonX.Y/site-packages (where X.Y corresponds to your Python version).
Pros of Installing in USER_SITE:

    Space Efficiency: Saves disk space by avoiding redundant installations of the same package in multiple virtual environments.
    Simplified Management: Updates to the package only need to be done once, globally, rather than in each project's virtual environment.

Cons and Considerations:

    Version Conflicts: If a project requires a specific version of a package that's incompatible with the version installed in USER_SITE, you may run into conflicts. This is less of an issue for tools like Jupyter but can be problematic for libraries closely tied to project functionality.
    Isolation: One of the virtual environments' key benefits is complete isolation from global and user installations. Installing packages in USER_SITE breaks this isolation, which can lead to "It works on my machine" issues when your environment differs from others (e.g., in a team or production environment).

Configuring Jupyter to Work with Virtual Environments

While installing Jupyter globally makes it accessible across environments, you'll often want to use it with packages installed within a specific virtual environment. To do this, you can create a kernel for your virtual environment:

    Activate your virtual environment and install ipykernel:

```sh
source /path/to/venv/bin/activate  # Unix-like
.\path\to\venv\Scripts\activate    # Windows

pip install ipykernel
```
Create a new kernel with a name for your project:

```sh
python -m ipykernel install --user --name=myprojectenv
```
Launch JupyterLab (from anywhere, using the global installation):

```sh
jupyter lab
```

    In JupyterLab, you can now select the kernel corresponding to your virtual environment (myprojectenv in this example) when opening a notebook. This setup allows you to access the virtual environment's specific packages and Python version directly from a globally installed JupyterLab.

This approach combines the efficiency of a single Jupyter installation with the isolation benefits of virtual environments for project-specific dependencies.

## use

Given the instruction that a filename should be supplied as a `fname` keyword argument, the correct way to call the `write` method with a filename would look like this:

`df.write(fname='test.csv')`

Here, `fname='test.csv'` explicitly names the keyword argument, telling the `write` method what the filename should be. This is a common pattern in Python when a function or method requires specific named arguments rather than positional arguments (which are just passed in order).

# Conference

![alt text](image.png)

