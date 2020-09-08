Feature: Filter products functionality
  As a user I would like to use filters to see the products as per the filters selected

  Scenario Outline: Apply filters on mens footwear section
    Given user is on mens footwear section
    When  user selects filters category <category>
    And   size of the footwear <size>
    And   clicks on the apply filter button
    Then  filter should be applied with correct count <count>
    And   validate the filter within product selected <category> <size>
    Examples:
      | category    | size | count |
      | Boots       |  9   |  2    |
      | Sandals     |  7.5 |  2    |
      | Casual Shoes|   8  |  2    |
      | Dress Shoes | 10.5 |  2    |
      | Sneakers    | 14   |  2    |
      | Sneakers    | 13   |  3    |
