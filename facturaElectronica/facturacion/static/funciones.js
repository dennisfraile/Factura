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
            }else{
                if(i==2){
                    cell = row.insertRow(i);
                    cell = `<td id="col`+ `${i}">`+
                             `<a id="operacioncreate" href="{% url 'operacionCreate' %} class="btn btn-success float-end"`+
                             ` data-bs-toggle="tooltip" data-bs-placement="bottom" title="Ingresar Neva Operacion"> `+
                             `<span class="material-symbols-outlined">add</span>`+
                             `</a></td>`+
                             `</tr>` 
                }
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
      alert('Debe haber al menos una nueva fila presupuestaria');
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
                }else{
                    if(i==2){
                        cell = row.insertRow(i);
                        cell = `<td id="col`+ `${i}">`+
                                `<a id="apendicecreate" href="{% url 'apendiceCreate' %} class="btn btn-success float-end"`+
                                ` data-bs-toggle="tooltip" data-bs-placement="bottom" title="Ingresar Nuevo Apendice"> `+
                                `<span class="material-symbols-outlined">add</span>`+
                                `</a></td>`+
                                `</tr>` 
                    }
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
      alert('Debe haber al menos una nueva fila presupuestaria');
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