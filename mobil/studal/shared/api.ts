
var host = 'http://localhost:8000/api/';

export function getStudents() {
    let endpoint = 'students';
    let url = host + endpoint;
    
    return fetch(url)
    .then(res => res.json())
    .catch(err => {
        console.log(err);
    });
}