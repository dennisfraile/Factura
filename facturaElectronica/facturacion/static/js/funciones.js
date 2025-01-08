let dataTableSujeto;
let dataTableComprobante;
let dataTableApendice;
let dataTableFactura;
let dataTableComprobanteOtroDocAsociado;
let dataTableFacturaDocRel;
let dataTableFacturaOtroDocRel;
let dataTableFacturaTributo;
let dataTableFacturaPago;
let dataTableSujetoMonth;
let dataTableComprobanteMonth;
let dataTableFacturaMonth;
let dataTableSujetoIsInitialized = false;
let dataTableComprobanteIsInitialized = false;
let dataTableFacturaIsInitialized = false;
let dataTableApendiceIsInitialized = false;
let dataTableComprobanteOtroDocAsociadoIsInitialized = false;
let dataTableFacturaDocRelIsInitialized = false;
let dataTableFacturaOtroDocRelIsInitialized = false;
let dataTableFacturaTributoIsInitialized = false;
let dataTableFacturaPagoIsInitialized = false;
let dataTableSujetoMonthIsInitialized = false;
let dataTableComprobanteMonthIsInitialized = false;
let dataTableFacturaMonthIsInitialized = false;

const dataTableSujetoOptions = {
    column: [
        { className: "centered", targets: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] },
        { orderable: false, targets: [9, 10] },
        { searchable: false, targets: [9, 10] }
    ],
    pageLength: 4,
    destroy: true
};

const dataTableApendiceOptions = {
    column: [
        { className: "centered", targets: [0, 1, 2, 3] },
        { orderable: false, targets: [3] },
        { searchable: false, targets: [3] }
    ],
    pageLength: 4,
    destroy: true
};

const dataTableComprobanteOptions = {
    column: [
        { className: "centered", targets: [0, 1, 2, 3, 4, 5, 6,7,8,9] },
        { orderable: false, targets: [8,9] },
        { searchable: false, targets: [8,9] }
    ],
    pageLength: 4,
    destroy: true
};

const dataTableComprobanteOtroDocAsociadoOptions = {
    column: [
        { className: "centered", targets: [0, 1, 2, 3] },
        { orderable: false, targets: [2,3] },
        { searchable: false, targets: [2,3] }
    ],
    pageLength: 4,
    destroy: true
};

const dataTableFacturaOptions = {
    column: [
        { className: "centered", targets: [0, 1, 2, 3, 4, 5 , 6, 7, 8, 9, 
            10, 11, 12, 13, 14, 15, 16, 17] 
        },
        { orderable: false, targets: [16, 17] },
        { searchable: false, targets: [16, 17] }
    ],
    pageLength: 4,
    destroy: true
};

const dataTableFacturaDocRelacionadoOptions = {
    column: [
        { className: "centered", targets: [0, 1, 2, 3] },
        { orderable: false, targets: [3] },
        { searchable: false, targets: [3] }
    ],
    pageLength: 4,
    destroy: true
};

const dataTableFacturaOtroDocRelOptions = {
    column: [
        { className: "centered", targets: [0, 1, 2, 3, 4, 5, 6, 7] },
        { orderable: false, targets: [1,2] },
        { searchable: false, targets: [1,2] }
    ],
    pageLength: 4,
    destroy: true
};

const dataTableFacturaTributoOptions = {
    column: [
        { className: "centered", targets: [0, 1, 2] },
        { orderable: false, targets: [2] },
        { searchable: false, targets: [2] }
    ],
    pageLength: 4,
    destroy: true
};

const dataTableFacturaPagoOptions = {
    column: [
        { className: "centered", targets: [0, 1, 2, 3, 4] },
        { orderable: false, targets: [2] },
        { searchable: false, targets: [2] }
    ],
    pageLength: 4,
    destroy: true
};

const dataTableFacturaSCMonthOptions = {
    column: [
        { className: "centered", targets: [0, 1, 2, 3, 4, 5, 6, 7]},
        { orderable: true, targets: [0, 1, 6]},
        { searchable: false, targets: [6, 7]},
        
    ]
};

const dataTableFacturaMonthOptions = {
    column: [
        { className: "centered", targets: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]},
        { orderable: true, targets: [0, 1, 7, 8]},
        { searchable: false, targets: [8, 9]},
        
    ]
};


function addOperacionSujetoExcluidoSelect(){
    var table = document.getElementById("operacionesSujetoExcluido");
    var rowCount = table.rows.length;
    var cellCount = table.rows[0].cells.length; 
    var row = table.insertRow(rowCount);
    for(var i = 0; i <cellCount; i++) {
        var cell = 'cell ' + i;
        if(i==0){
            cell = row.insertRow(i);
            cell =`<tr><td id="col`+ `${i}"><select name="operaciones" id="operaciones" class="form-select">`+ 
                `{% for registro in operaciones %}`+
                `{% if registro.operaciones.id == 0 %}`+
                `<option name="operaciones" selected value="{{registro.id}}">{{registro.tipoItem}}</option>`+
                `{% endif %}`+
                `<option name="operaciones"  value="{{registro.id}}">{{registro.tipoItem}}</option>`+
                `{% endfor %}`+
                `</select></td>`;
            cell.innerHTML=cell;

        }else{
            if(i==1){
               cell = row.insertRow(i);
               cell = `<td id="col`+ `${i}">`+
                        `<a id="operacionver" href="#" class="btn btn-success float-end"`+
                        ` data-bs-toggle="tooltip" data-bs-placement="bottom" title="Ver Operacion"> `+
                        `<span class="material-symbols-outlined">visibility</span>`+
                        `</a></td>` 
            }
        }    
    }
};

function deleteRowsOperacionSujetoExcluido(num){
    var table = document.getElementById('operacionesSujetoExcluido');
    var rowCount = table.rows.length;
    console.log(rowCount);
    console.log(num);
    if(rowCount-1 > num){
      var row = table.deleteRow(rowCount-1);
      rowCount--;
    }
    else{
      alert('Debe haber al menos una operacion sobre el sujeto excluido');
    }
  };

function addApendiceSelect(){
    var table = document.getElementById("tableApendice");
    var rowCount = table.rows.length;
    var cellCount = table.rows[0].cells.length; 
    var row = table.insertRow(rowCount);
    while(rowCount < 11){
        for(var i = 0; i <cellCount; i++) {
            var cell = 'cell ' + i;
            if(i==0){
                cell = row.insertRow(i);
                cell =`<tr><td id="col`+ `${i}"><select name="apendice" id="apendice" class="form-select">`+ 
                    `{% for apendice in apendices %}`+
                    `<option name="apendice"  value="{{apendice.id}}">{{apendice.campo}}</option>`+
                    `{% endfor %}`+
                    `</select></td>`;
                cell.innerHTML=cell;

            }else{
                if(i==1){
                cell = row.insertRow(i);
                cell = `<td id="col`+ `${i}">`+
                        `<a id="apendicever" href="#" class="btn btn-success float-end"`+
                        ` data-bs-toggle="tooltip" data-bs-placement="bottom" title="Ver Apendice"> `+
                        `<span class="material-symbols-outlined">visibility</span>`+
                        `</a></td>` 
                }
            }    
        }
    }
};

function deleteRowsApendice(num){
    var table = document.getElementById('tableApendice');
    var rowCount = table.rows.length;
    console.log(rowCount);
    console.log(num);
    if(rowCount-1 > num){
      var row = table.deleteRow(rowCount-1);
      rowCount--;
    }
    else{
      alert('Debe haber al menos un apendice sobre el sujeto excluido');
    }
  };

document.getElementById('apendice').addEventListener('change', function() {
    var idSeleccionado = this.options[this.selectedIndex].id;
    var enlace = document.getElementById('apendicever');
    enlace.href = '{% url "apendiceVer" %}?id=' + idSeleccionado;
});
document.getElementById('operaciones').addEventListener('change', function() {
    var idSeleccionado = this.options[this.selectedIndex].id;
    var enlace = document.getElementById('operacionver');
    enlace.href = '{% url "operacionVer" %}?id=' + idSeleccionado;
});
document.getElementById('receptor').addEventListener('change', function() {
    var idSeleccionado = this.options[this.selectedIndex].id;
    var enlace = document.getElementById('receptorver');
    enlace.href = '{% url "recpetorVer" %}?id=' + idSeleccionado;
});
document.getElementById('emisor').addEventListener('change', function() {
    var idSeleccionado = this.options[this.selectedIndex].id;
    var enlace = document.getElementById('emisorver');
    enlace.href = '{% url "emisorVer" %}?id=' + idSeleccionado;
});
document.getElementById('identificador').addEventListener('change', function() {
    var idSeleccionado = this.options[this.selectedIndex].id;
    var enlace = document.getElementById('identificadorver');
    enlace.href = '{% url "identificadorVer" %}?id=' + idSeleccionado;
});

const initDataTableSujetoMonth = async () => {
    if (dataTableSujetoMonthIsInitialized) {
        dataTableSujetoMonth.destroy();
    }
    dataTableSujetoMonth = $("#table-sujetoMonth").DataTable(dataTableFacturaSCMonthOptions);
    dataTableSujetoMonthIsInitialized = true;
};

const initDataTableComprobanteMonth = async () => {
    if (dataTableComprobanteMonthIsInitialized) {
        dataTableComprobanteMonth.destroy();
    }
    dataTableComprobanteMonth = $("#table-comprobanteMonth").DataTable(dataTableFacturaSCMonthOptions);
    dataTableComprobanteMonthIsInitialized = true;
};

const initDataTableFacturaMonth = async () => {
    if (dataTableFacturaMonthIsInitialized) {
        dataTableFacturaMonth.destroy();
    }
    dataTableFacturaMonth = $("#table-facturaMonth").DataTable(dataTableFacturaMonthOptions);
    dataTableFacturaMonthIsInitialized = true;
};
const initDataTableSujeto = async () => {
    if (dataTableSujetoIsInitialized) {
        dataTableSujeto.destroy();
    }
    dataTableSujeto = $("#table-sujeto").DataTable(dataTableSujetoOptions);
    dataTableSujetoIsInitialized = true;
    if(dataTableApendiceIsInitialized){
        dataTableApendice.destroy();
        dataTableApendice = $("#table-Sapendice").DataTable(dataTableApendiceOptions);
    }
    dataTableApendiceIsInitialized = true;
};

const initDataTableComprobante = async () => {
    if (dataTableComprobanteIsInitialized) {
        dataTable.destroy();
    }
    dataTable = $("#table-comprobante").DataTable(dataTableComprobanteOptions);
    dataTableComprobanteIsInitialized = true;
    if(dataTableComprobanteOtroDocAsociadoIsInitialized){
        dataTableComprobanteOtroDocAsociado.destroy();
        dataTableComprobanteOtroDocAsociado = $("#table-comprobanteDocAsociado").DataTable(dataTableComprobanteOtroDocAsociadoOptions);
    }
    dataTableComprobanteOtroDocAsociadoIsInitialized = true;
    if(dataTableApendiceIsInitialized){
        dataTableApendice.destroy();
        dataTableApendice = $("#table-Capendice").DataTable(dataTableApendiceOptions);
    }
    dataTableApendiceIsInitialized = true;
};

const initDataTableFactura = async () => {
    if (dataTableFacturaIsInitialized) {
        dataTable.destroy();
    }
    dataTable = $("#table-factura").DataTable(dataTableFacturaOptions);
    dataTableFacturaIsInitialized = true;
    if(dataTableFacturaDocRelIsInitialized){
        dataTableFacturaDocRel.destroy();
    }
    dataTableFacturaDocRel = $("#table-facturaDocRel").DataTable(dataTableFacturaDocRelacionadoOptions);
    dataTableFacturaDocRelIsInitialized = true;
    if(dataTableFacturaOtroDocRelIsInitialized){
        dataTableFacturaOtroDocRel.destroy();
    }
    dataTableFacturaOtroDocRel = $("#table-facturaOtroDocRel").DataTable(dataTableFacturaOtroDocRelOptions);
    dataTableFacturaOtroDocRelIsInitialized = true;
    if(dataTableFacturaTributoIsInitialized){
        dataTableFacturaTributo.destroy();
    }
    dataTableFacturaTributo = $("#table-facturaTributo").DataTable(dataTableFacturaTributoOptions);
    dataTableFacturaTributoIsInitialized = true;
    if(dataTableFacturaPagoIsInitialized){
        dataTableFacturaPago.destroy();
    }
    dataTableFacturaPago = $("#table-facturaPago").DataTable(dataTableFacturaPagoOptions);
    dataTableFacturaPagoIsInitialized = true;
    if(dataTableApendiceIsInitialized){
        dataTableApendice.destroy();
    }
    dataTableApendice = $("#table-Fapendice").DataTable(dataTableApendiceOptions);
    dataTableApendiceIsInitialized = true;
};

window.addEventListener('load', async () => {
    await initDataTableSujetoMonth();
    await initDataTableComprobanteMonth();
    await initDataTableFacturaMonth();
    await initDataTableSujeto();
    await initDataTableComprobante();
    await initDataTableFactura();

});