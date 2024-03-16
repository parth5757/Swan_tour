document.addEventListener('DOMContentLoaded', function() {
    // Set initial search input by destination city
    var searchDestinationInput = document.getElementById('search-destination');

    // set initial search input by start date
    var searchStartDateInput = document.getElementById('search-start-date');
    
    // search by tour name
    var searchInput = document.getElementById('search-name');
    if (searchInput.value === 'None') {
        searchInput.value = '';
    }

    // search by destination(city) name
    if (searchDestinationInput.value === 'None') {
        searchDestinationInput.value = '';
    }

    // seatch by start date of tour
    if (searchStartDateInput.value === 'None') {
        searchStartDateInput.value = '';
    }

    // apply Destination & start date filter
    document.getElementById('apply-filters').addEventListener('click', function() {
        applyFilters();
    });

    // Apply rating filter
    document.querySelector('.apply-review').addEventListener('click', function () {
        applyFilters();
    });

    // Apply search by name filter
    document.querySelector('.apply-search').addEventListener('click', function () {
        applyFilters();
    });

    // Apply tour type filter
    document.querySelector('.apply-tour-type').addEventListener('click', function () {
        applyFilters();
    });

    // Update pagination links with filters
    document.querySelectorAll('.page-link').forEach(function(link) {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            applyFilters();
        });
    });

    function applyFilters() {
        var selectedRatings = [];
        var reviewCheckboxes = document.querySelectorAll('.review-checkbox:checked');
        reviewCheckboxes.forEach(function (checkbox) {
            selectedRatings.push(checkbox.value);
        });
        
        var selectedTourTypes = [];
        var tourTypeCheckboxes = document.querySelectorAll('.tour-type-checkbox:checked');
        tourTypeCheckboxes.forEach(function (checkbox) {
            selectedTourTypes.push(checkbox.value);
        });

        var searchInput = document.getElementById('search-name');
        var searchName = searchInput.value.trim();

        if (searchName === 'None') {
            searchName = '';
        }

        var searchDestination = searchDestinationInput.value.trim();
        var searchStartDate = searchStartDateInput.value;

        var url = window.location.href.split('?')[0]; // Remove existing query parameters
        var queryParams = [];

        if (selectedRatings.length > 0) {
            queryParams.push('ratings=' + selectedRatings.join(","));
        }
        if (selectedTourTypes.length > 0) {
            queryParams.push('tour_types=' + selectedTourTypes.join(","));
        }
        if (searchName) {
            queryParams.push('search=' + encodeURIComponent(searchName));
        }

        if(searchDestination){
            queryParams.push('destination=' + encodeURIComponent(searchDestination));
        }

        if (searchStartDate) {
            queryParams.push('start_date=' + encodeURIComponent(searchStartDate));
        }

        if (queryParams.length > 0) {
            url += '?' + queryParams.join("&");
        }
        window.location.href = url;
    }
});