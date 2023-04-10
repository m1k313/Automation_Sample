Feature: Speedbird Cafe Product List
	As a user, I want to sort my product list so that it's easier for me to find the product I want. When clicking on the dropdown list I should see 4 options

	Scenario: Verify the number of sorting options in the "Sort by" dropdown
		Given the Speedbird Cafe product list page is open
		When I decline cookies
		When the user clicks on the "Sort by" dropdown
		Then there are 4 sorting options available