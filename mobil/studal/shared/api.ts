
var host = 'http://localhost:8000/api/';

export function getStudents(id: number) {
    let endpoint = 'students/groups/' + id;
    let url = host + endpoint;
    
    return fetch(url)
    .then(res => res.json())
    .catch(err => {
        console.log(err);
    });
}

export function getClassgroups() {
    let endpoint = 'groups';
    let url = host + endpoint;
    
    return fetch(url)
    .then(res => res.json())
    .catch(err => {
        console.log(err);
    });
}
