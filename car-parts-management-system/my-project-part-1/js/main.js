// Base API URL for car parts
var rootURL = "http://localhost/my-project-part-1/api/carparts";

// Holds the currently selected car part
var currentPart;

// DataTable reference (used to destroy/reload table)
var table = null;




// GET ALL PARTS (CRUD + DATATABLE)

// Retrieves all car parts from the API
var findAll = function () {
    console.log('findAll');

    $.ajax({
        type: 'GET',                 // HTTP GET request
        url: rootURL,                // API endpoint
        dataType: "json",            // Expect JSON response
        success: function(data){
            renderList(data);        // Update left CRUD list
            refreshDataTable(data);  // Update DataTable
        }
    });
};




// LEFT CRUD LIST RENDER

// Displays car parts in the left-side list
var renderList = function (data) {

    var list = data.car_part;        // Extract car part array
    $('#carPartList li').remove();   // Clear old list items

    // Loop through all parts and add them to the list
    $.each(list, function(index, part) {
        $('#carPartList').append(
            '<li class="list-group-item">' +
            '<a href="#" id="' + part.id + '">' +
            part.name + '</a></li>'
        );
    });
};




// GET ONE PART → LOAD FORM

// Retrieves a single car part by ID
var findById = function(id){

    $.ajax({
        type: 'GET',
        url: rootURL + '/' + id,     // API endpoint with ID
        dataType:"json",
        success: function(data){
            $('#btnDelete').show();  // Show delete button
            currentPart = data.car_part;
            renderDetails(currentPart); // Load data into form
        }
    });
};




// RENDER FORM FIELDS

// Fills form inputs with selected car part data
var renderDetails = function(part){

    $('#partId').val(part.id);
    $('#name').val(part.name);
    $('#manufacturer').val(part.manufacturer);
    $('#model').val(part.model);
    $('#supplier').val(part.supplier);
    $('#category').val(part.category);
    $('#compatible_with').val(part.compatible_with);
    $('#age_in_years').val(part.age_in_years);
    $('#price').val(part.price);

    // Display image or placeholder
    $('#pic').attr(
        'src',
        part.image ? 'images/' + part.image : 'images/placeholder.png'
    );
};




// NEW PART

// Clears form to add a new car part
function newPart() {

    $('#partId').val('');
    $('#name').val('');
    $('#manufacturer').val('');
    $('#model').val('');
    $('#supplier').val('');
    $('#category').val('');
    $('#compatible_with').val('');
    $('#age_in_years').val('');
    $('#price').val('');

    $('#pic').attr('src', 'images/placeholder.png');
    $('#btnDelete').hide();   // Hide delete button for new entry

    currentPart = null;
}




// JSON BUILDER

// Converts form fields into JSON for API requests
var formToJSON = function () {

  var partId = $('#partId').val();

  return JSON.stringify({
    "id": partId === "" ? null : partId,
    "name": $('#name').val(),
    "manufacturer": $('#manufacturer').val(),
    "model": $('#model').val(),
    "supplier": $('#supplier').val(),
    "category": $('#category').val(),
    "compatible_with": $('#compatible_with').val(),
    "age_in_years": $('#age_in_years').val(),
    "price": $('#price').val(),
    "image": currentPart ? currentPart.image : "placeholder.png"
  });
};




// CREATE PART

// Sends new car part data to the API
var addPart = function () {

    $.ajax({
        type: 'POST',                         // Create request
        contentType: 'application/json',
        url: rootURL,
        dataType: 'json',
        data: formToJSON(),
        success: function () {
            alert('Car part created');
            newPart();                        // Reset form
            findAll();                        // Reload data
        }
    });
};



// UPDATE PART

// Updates an existing car part
var updatePart = function () {

    var id = $('#partId').val();

    $.ajax({
        type: 'PUT',                          // Update request
        contentType: 'application/json',
        url: rootURL + '/' + id,
        dataType: 'json',
        data: formToJSON(),
        success: function () {
            alert('Car part updated');
            findAll();                        // Refresh data
        }
    });
};




// DELETE PART

// Deletes a car part by ID
var deletePart = function(){

    var id = $('#partId').val();

    $.ajax({
        type: 'DELETE',
        url: rootURL + '/' + id,
        success: function(){
            alert('Car part deleted');
            newPart();                        // Clear form
            findAll();                        // Refresh data
        }
    });
};




// DATATABLE SECTION 


// Refreshes the DataTable with new data
function refreshDataTable(data) {

    var list = data.car_part;

    // Destroy existing DataTable if it exists
    if (table !== null) {
        table.destroy();
    }

    // Clear table body
    $('#table_body').html("");

    // Build table rows
    $.each(list, function(index, part) {
        $('#table_body').append(
            '<tr>' +
            '<td>' + part.name + '</td>' +
            '<td>' + part.manufacturer + '</td>' +
            '<td>' + part.model + '</td>' +
            '<td>' + part.price + '</td>' +
            '<td id="' + part.id + '"><a href="#">More Info</a></td>' +
            '</tr>'
        );
    });

    // Reinitialize DataTable
    table = $('#table_id').DataTable();
}




// DATATABLE MODAL DETAILS

// Shows detailed info in a modal popup
var findByIdModal = function(id){

    $.ajax({
        type: "GET",
        url: rootURL + "/" + id,
        dataType: "json",
        success: function(data){

            var p = data.car_part;

            // Build modal HTML content
            var html =
                "<h3>" + p.name + "</h3>" +
                "<p><b>Manufacturer:</b> " + p.manufacturer + "</p>" +
                "<p><b>Model:</b> " + p.model + "</p>" +
                "<p><b>Supplier:</b> " + p.supplier + "</p>" +
                "<p><b>Category:</b> " + p.category + "</p>" +
                "<p><b>Compatible With:</b> " + p.compatible_with + "</p>" +
                "<p><b>Age:</b> " + p.age_in_years + "</p>" +
                "<p><b>Price:</b> " + p.price + "</p>" +
                "<br><img width='200' src='images/" + p.image + "'>";

            $('#dtModalBody').html(html);
            $('#dtModal').modal('show');
        }
    });
};




// DOCUMENT READY

$(document).ready(function(){

    // Load all car parts when page loads
	findAll();

	// Click on CRUD list item
	$(document).on("click",'#carPartList a', function(){
		findById(this.id);
	});

	// Add new part button
	$(document).on("click",'#btnAdd', function(){
        newPart();
    });

	// Save button (add or update)
	$(document).on("click",'#btnSave', function(){
		var id = $('#partId').val();
		if(id === "" || id === null) addPart();
		else updatePart();
	});

	// Delete button
	$(document).on("click",'#btnDelete', function(){
        deletePart();
    });

    // DataTable "More Info" click
    $(document).on("click", '#table_body td', function () {
        findByIdModal(this.id);
    });

});
