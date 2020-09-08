# Automation Test

## Project dependencies
- pytest, pytest-bdd, gherkin, python, pytest-html and selenium

## Project setup
- Clone the git repo
- Solve the dependencies
- `config.cfg` has all the env variables
- Run `pytest --html=Reports/report.html`

## Project Structure
- `base`: Initiate the driver
- `features`: Gherkin feature files
- `lib`: middleware for reading selectors and config elements
- `pages`: All the actions for different page functionalities
- `selectors`: All the selectors are under this directory
- `tests`: All the test cases written

## Solution
Test case is `data parametrized` through `gherkin file` which consists of `6 different filter combinations`. Tests are
compatible with both the websites. `Last filter combination` is an intentional failed test where we are using 2 filters
but assert them to count 3. `Second last filter combination` is also an intentional failed test but only for `callitspring`
because `callitspring` doesn't have size 14 in sneakers but `aldos` has, so, this test case would fail for callitspring but
will pass for aldos. Validation for filter count has also been achieved. You can add additional filter combinations if
you like to under examples section in feature file.


