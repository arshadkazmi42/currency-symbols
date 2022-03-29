## Release

- Build the project using below command

```
python3 setup.py sdist bdist_wheel 
```

- Publish to test pypi repository to test all the changes

```
python3 -m twine upload --repository testpypi dist/*
```

- Publish to pypi repository

```
python3 -m twine upload dist/*
```

**--skip-existing**: Use this flag to override an existing version
