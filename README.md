# python-git-test

Sandbox for learning the [GitPython](https://gitpython.readthedocs.io/en/stable/) API. Uses [this](https://github.com/aidandj/python-git-test-repo) test repo

## Limitations

From [documentation](https://gitpython.readthedocs.io/en/stable/intro.html#limitations)

> ### Leakage of System Resources
> GitPython is not suited for long-running processes (like daemons) as it tends to leak system resources. It was written in a time where destructors (as implemented in the `__del__` method) > still ran deterministically.
> 
> In case you still want to use it in such a context, you will want to search the codebase for `__del__` implementations and call these yourself when you see fit.
> 
> Another way assure proper cleanup of resources is to factor out GitPython into a separate process which can be dropped periodically.

## Goals

* Clone, commit, push a repo
* Watch a file, commit and push on change
* Handle merge conflicts