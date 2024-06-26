$(document).ready(function() {
    // Initialize Select2 on the select element
    $('#Select2').select2();
    $('#waste_type_select2').select2();
   
  });

  
var counter = 2;
function addProductField() {
  var waste_obj = $('#waste_obj').val()
  var waste_list = JSON.parse(waste_obj);
  var container = document.getElementById("dynamicFieldsContainer");
  var newRow = document.createElement("div");
  newRow.className = "row mt-3";
  newRow.id = "row_" + counter;
  var materialId = "wast_id_" + counter;
  var materialPrice = "price_" + counter;
  var materialPercentage = "quantity_" + counter;

  newRow.innerHTML = `
    <div class="col-sm-12 col-md-6 col-lg-3">
      <label for="${materialId}" class="form-label">Waste Type</label>
      <select class="form-select" id="${materialId}" name="${materialId}" aria-label="Waste type select">
        <option selected>Open this select menu</option>
    
      </select>
    </div>
    <div class="col-sm-12 col-md-3 col-lg-3">
        <label for="${materialPrice}" class="form-label">Price</label>
      <input type="text" class="form-control" id="${materialPrice}" name="${materialPrice}" placeholder="Please enter price" aria-label="price">
    </div>
    <div class="col-sm-12 col-md-6 col-lg-3">
      <label for="${materialPercentage}" class="form-label">Quantity</label>
      <input type="text" class="form-control" id="${materialPercentage}" name="${materialPercentage}" placeholder="Please enter quantity" aria-label="Quantity">
    </div>
    <div class="col-sm-12 col-md-6 col-lg-3 my-auto">
      <button type="button" class="btn btn-primary mt-4 add-row-btn" onclick="addProductField()">+ADD</button>
      <button type="button" class="btn btn-danger mt-4" onclick="removeProductField('row_${counter}')">-REMOVE</button>
      </div>
  `;

  container.appendChild(newRow);
  var selectElement = document.getElementById(materialId);
  waste_list.forEach(function(material) {
      var option = document.createElement("option");
      option.text = material.fields.wastename;
      option.value = material.pk;
      selectElement.appendChild(option);
  });


  $(document).ready(function() {
    $('#materialId').select2({
        placeholder: "Select Material",
        theme: "bootstrap5",
        width: "100%" 
    });
});

 
  counter++;
}


function removeProductField(rowId) {
  var row = document.getElementById(rowId);
  row.parentNode.removeChild(row);
}


function save_trnscation(){
    const owner = $("#Select2 :selected").val();
    const given_bags = $('input[name="gridRadios"]:checked').val();
    const lifted_status = $('input[name="gridRadios1"]:checked').val();
    const waste_type = $("#waste_type_select2 :selected").val();
    const startprice = $("#price_1").val();
    const startquantity = $("#quantity_1").val();
  
  
    var wasteData = [];
    wasteData.push({
        wasteType: waste_type,
        price: startprice,
        quantity: startquantity
    })
    for (var i = 1; i < counter; i++) {
        if (document.getElementById(`wast_id_${i}`)) {
            var wasteType = $(`#wast_id_${i} :selected`).val();
            var price = $(`#price_${i}`).val();
            var quantity = $(`#quantity_${i}`).val();
            
            if (wasteType && price && quantity) {
                wasteData.push({
                    wasteType: wasteType,
                    price: price,
                    quantity: quantity
                });
            }
        }
    }
 
    $.ajax({
      url: '/save_transaction_data/',
      method: 'POST',
      data: {
        'owner':owner,
        'given_bags':given_bags,
        'lifted_status':lifted_status,
        'wasteData':wasteData
    
        
      },
      success: function(response){
        show_success(response['message'])
        window.location = response['path']
      },
      error: function(response){
        show_error(response.responseJSON['error'])
      }
    })
  
  }