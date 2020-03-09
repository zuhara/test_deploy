var create_invoice_table = function (invoices) {
  table = "<table><tr><th>Date</th><th>Particulars</th><th>Amount</th></tr>";

  for (i=0; i<invoices.length; i++) {
    invoice = invoices[i];
    table += "<tr><td>"+invoice.date+"</td><td>"+invoice.particulars+"</td><td>"+invoice.amount+"</td></tr>";
    }
  table += "</table>";
  return table;
};

var handler = function() {
  $.ajax(
    {
      headers:{'Accept':'application/json'}, 
      url:'/invoices?cid='+cid,
      success: function(data, textStatus, jqXHR) {
        table = create_invoice_table(data.invoices);
        $("#invoices").html(table);
        }
    });
  };

var main = function() {
  handler(); // Load the invoice table for the first time.
  $("#createinvoice").click(function(e) {
    e.preventDefault(); 
    $.post({
      url: '/invoices',
      data: $("input").serializeArray(),
      success: function(data, status, xhr) {
        $("#invoices").html("Loading...");
        handler();
      }
    });
    
  });
  };

$(main);
