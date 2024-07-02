function removeCategory(categoryId) {
    // Remove the category box
    var categoryBox = document.getElementById(categoryId);
    categoryBox.parentNode.removeChild(categoryBox);

    // Remove the corresponding search results
    var searchResults = document.getElementById('search-results');
    // Assuming the results are dynamically loaded with IDs that match the category box ID pattern
    var resultsToRemove = searchResults.querySelectorAll(`.result[data-category='${categoryId}']`);
    resultsToRemove.forEach(function(result) {
        result.parentNode.removeChild(result);
    })
}

function openFilterOptions() {
    var filterOptions = document.getElementById("filterOptions");
    filterOptions.style.display = filterOptions.style.display === "block" ? "none" : "block";
}

function closeFilterOptions() {
    var filterOptions = document.getElementById("filterOptions");
    filterOptions.style.display = "none";
}

function applySettings() {
    // Retrieve the selected settings
    var sortByPrice = document.querySelector('input[name="sortByPriceAsc"]').checked;
    var sortByPriceDesc = document.querySelector('input[name="sortByPriceDesc"]').checked;
    var sortByRating = document.querySelector('input[name="sortByRatingAsc"]').checked;
    var sortByRatingDesc = document.querySelector('input[name="sortByRatingDesc"]').checked;

    // Add further logic to save the settings (e.g., send to server, store in localStorage, etc.)
    
    // Close the filter options after saving (optional)
    closeFilterOptions();
}