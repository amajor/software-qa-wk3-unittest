# Python Unit Tests

Use [PyCharm Community](https://www.jetbrains.com/pycharm/download) as a simple IDE.

Unit tests use [unittest](https://docs.python.org/3/library/unittest.html).

Install [coverage](http://www.blog.pythonlibrary.org/2016/07/20/an-intro-to-coverage-py/) using `pip install coverage` 
in your terminal.

## Run Tests

```sh
python -m unittest
```

## Test Coverage

We can test the files found in the `app` directory using:

```sh
coverage run --source=app  -m unittest
```

To see report:

```sh
coverage report
```

Run it all together:

```shell
coverage run --source=app  -m unittest && coverage report
```