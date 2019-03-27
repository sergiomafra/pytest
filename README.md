# pytest
PyTest study

### Useful Stuff
#### Installing
    pip install pytest

#### Creating pytest configuration
    touch pytest.ini
    vim pytest.ini

    ## Inside the file
    [pytest]
    python_files = test_* ## Define how a test file looks like
    python_classes = *Tests ## Define how test classes looks like
    python_functions = test* ## Define how python functions looks like

#### Creating a test file

    touch test_something.py
    vim test_something.py

Now, type and save it

    ## Inside the file
    def test_something():
        assert <something>

#### Marking Tests
Marking tests inside a test file:

    from pytest import mark
    
    
    @mark.<mark1>
    def test_one():
        assert ...
    
    @mark.<mark2>
    def test_two():
        assert ...

Then, from the command line, run:

    python -m <markX> ## Run only the specified test with that mark
    python -m "<mark1> and <mark2>" ## Run tests that are marked both mark1 and mark2
    python -m "<mark1> or <mark2>" ## Run tests that has either mark1 or mark2 marks

#### Show markers on command line
First, append to pytest.ini the variable markers

    markers = 
        body: "All body tests"
        engine: "All engine tests"
        entertainment: "All entertainment tests"
        tires: "All tires tests"

Then, from the command line:

    python --markers

#### Creating test classes
Create a test file and put this inside:

    from pytest import mark


    @mark.engine
    class EngineTests:

        def test_accelaration(self):
            assert True

        def test_ pistons(self):
            assert True

        def test_fuel(self):
            assert True

If you mark a class with a marker, all methods of it will be tested
