/**
 * Realizes endpoints for the author API. Includes CRUD functions.
 */

var author_list = [];

function http_req(method, url, data=null) {
    /* Makes a new Promise for requests. */
    return new Promise((resolve, reject) => {
        const xhr = new XMLHttpRequest();
        xhr.open(method, '/api' + url);
        if (method === 'POST' || method === 'PUT') {
            xhr.setRequestHeader("Content-Type", "application/json");
            xhr.setRequestHeader("Access-Cdontrol-Allow-Origin", "*");
        }
        xhr.onload = () => resolve(JSON.parse(xhr.responseText));
        xhr.onerror = () => reject(xhr.statusText);
        xhr.send(JSON.stringify(data));
    });
}

function create_td(id, key, editable=true, indb=true) {
    /* Creates the format of table row entries. */
    var td = document.createElement('td');
    td.className = 'pt-3-half';
    td.contentEditable = editable;

    if (editable) {
        td.addEventListener('blur', () => { 
            if (indb) {
                update_author(id, key, td.innerHTML);
            } else {
                author_list[author_list.length-1][key] = td.innerHTML;
            }
        });
    }
      
    return td;
}

function update_author(id, key, val) {
    http_req('PUT', `/authors?_id=${id}`, {[key]: val})
    .then(r => {
        setup_table();
    })
}

function setup_table() {
    /* Sets up the table elements. */
    const table = document.getElementById("author_table");
    table.innerHTML = '';
    http_req('GET', '/authors')
    .then(resp => {
        author_list = resp;
        console.log(resp);

        for (var i=0; i<resp.length; ++i) {
            const element = resp[i];
            var tr = document.createElement('tr');
            var td_author = create_td(element._id, 'name'),  
                td_rating = create_td(element._id, 'rating'), 
                td_del = create_td(element._id, '', editable = false);
            
            td_author.innerHTML = element.name || ''; 
            td_rating.innerHTML = element.rating || '';
            td_del.innerHTML = `
            <span class="table-remove">
                <button onclick="ondelete(` + i + `)" type="button" class="btn btn-danger btn-rounded btn-sm my-0">
                    Remove
                </button>
            </span>
            `;

            tr.appendChild(td_author);
            tr.appendChild(td_rating);
            tr.appendChild(td_del);

            table.appendChild(tr);
        }
    })
    .catch(err => {
        console.log(err);
    })

}

function ondelete(i) {
    http_req('DELETE', '/author?_id=' + author_list[i]._id)
    .then( r => {
        setup_table();
    })
}

function create_author() {
    http_req('POST', '/author', author_list[author_list.length - 1])
    .then(r => {
        document.getElementById('create-btn').disabled = false;
        setup_table();
    })
}

function oncreate() {
    /* Creates a new table row entry. */
    document.getElementById('create-btn').disabled = true;
    const table = document.getElementById("author_table");
    var tr = document.createElement('tr');
    var td_author = create_td('', 'name', true, false), 
        td_rating = create_td('', 'rating', true, false), 
        td_del = create_td('', '', editable = false);
    
    td_author.innerHTML = '';
    td_rating.innerHTML = '';
    td_del.innerHTML = `
    <span class="table-remove">
        <button onclick="create_author()" type="button" class="btn btn-danger btn-rounded btn-sm my-0">
            Confirm
        </button>
    </span>
    `;

    author_list.push({});

    tr.appendChild(td_author);
    tr.appendChild(td_rating);
    tr.appendChild(td_del);

    table.appendChild(tr);
}
