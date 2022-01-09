
var host = 'http://192.168.5.5:8000/api/';

export function getStudents() {
    let endpoint = 'students';
    let url = host + endpoint;
    
    return fetch(url)
    .then(res => res.json())
    .catch(err => {
        console.log(err);
    });
}

export function getClassgroup() {
    let endpoint = 'classgroup';
    let url = host + endpoint;
    
    return fetch(url)
    .then(res => res.json())
    .catch(err => {
        console.log(err);
    });
}
