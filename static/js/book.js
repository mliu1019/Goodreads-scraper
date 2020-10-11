/**
 * Realizes endpoints for the author API. Includes CRUD functions.
 */

var book_list = [];

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
                update_book(id, key, td.innerHTML);
            } else {
                book_list[book_list.length-1][key] = td.innerHTML;
            }
        });
    }
      
    return td;
}

function update_book(id, key, val) {
    http_req('PUT', `/books?_id=${id}`, {[key]: val})
    .then(r => {
        setup_table();
    })
}

function setup_table() {
    /* Sets up the table elements. */
    const table = document.getElementById("book_table");
    table.innerHTML = '';
    http_req('GET', '/books')
    .then(resp => {
        book_list = resp;
        console.log(resp);

        for (var i=0; i<resp.length; ++i) {
            const element = resp[i];
            var tr = document.createElement('tr');
            var td_book = create_td(element._id, 'title'), 
                td_isbn = create_td(element._id, 'isbn'), 
                td_author = create_td(element._id, 'author'), 
                td_rating = create_td(element._id, 'rating'), 
                td_del = create_td(element._id, '', editable = false);
            
            td_book.innerHTML = element.title || ''; 
            td_isbn.innerHTML = element.isbn || '';
            td_author.innerHTML = element.author || '';
            td_rating.innerHTML = element.rating || '';
            td_del.innerHTML = `
            <span class="table-remove">
                <button onclick="ondelete(` + i + `)" type="button" class="btn btn-danger btn-rounded btn-sm my-0">
                    Remove
                </button>
            </span>
            `;

            tr.appendChild(td_book);
            tr.appendChild(td_isbn);
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
    http_req('DELETE', '/book?_id=' + book_list[i]._id)
    .then( r => {
        setup_table();
    })
}

function create_book() {
    http_req('POST', '/book', book_list[book_list.length - 1])
    .then(r => {
        document.getElementById('create-btn').disabled = false;
        setup_table();
    })
}

function oncreate() {
    /* Creates a new table row entry. */
    document.getElementById('create-btn').disabled = true;
    const table = document.getElementById("book_table");
    var tr = document.createElement('tr');
    var td_book = create_td('', 'title', true, false), 
        td_isbn = create_td('', 'isbn', true, false), 
        td_author = create_td('', 'author', true, false), 
        td_rating = create_td('', 'rating', true, false), 
        td_del = create_td('', '', editable = false);
    
    td_book.innerHTML = ''; 
    td_isbn.innerHTML = '';
    td_author.innerHTML = '';
    td_rating.innerHTML = '';
    td_del.innerHTML = `
    <span class="table-remove">
        <button onclick="create_book()" type="button" class="btn btn-danger btn-rounded btn-sm my-0">
            Confirm
        </button>
    </span>
    `;

    book_list.push({});

    tr.appendChild(td_book);
    tr.appendChild(td_isbn);
    tr.appendChild(td_author);
    tr.appendChild(td_rating);
    tr.appendChild(td_del);

    table.appendChild(tr);
}
