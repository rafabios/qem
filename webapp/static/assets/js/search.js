$("#e7").select2({
    placeholder: "Search for a repository",
    minimumInputLength: 3,
    ajax: {
        url: "https://api.github.com/search/repositories",
        dataType: 'json',
        quietMillis: 250,
        data: function (term, page) { // page is the one-based page number tracked by Select2
            return {
                q: term, //search term
                page: page // page number
            };
        },
        results: function (data, page) {
            var more = (page * 30) < data.total_count; // whether or not there are more results available
 
            // notice we return the value of more so Select2 knows if more results can be loaded
            return { results: data.items, more: more };
        }
    },
    formatResult: repoFormatResult, // omitted for brevity, see the source of this page
    formatSelection: repoFormatSelection, // omitted for brevity, see the source of this page
    dropdownCssClass: "bigdrop", // apply css that makes the dropdown taller
    escapeMarkup: function (m) { return m; } // we do not want to escape markup since we are displaying html in results
});