import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map } from 'rxjs/operators';
import { HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  host = 'http://localhost:8000/api/';

  constructor(private http: HttpClient) { }

  addStudent(data: any) {
    let dataStore:any = localStorage.getItem('currentUser');
    let currentUser = JSON.parse(dataStore);
    let token = currentUser.token;     

    let headerObj = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + token
    });
    const httpOption = {
      headers: headerObj
    };

    let endpoint = 'students';
    return this.http.post<any>(this.host + endpoint, data, httpOption)
    .pipe(map(  (res:any) => {
      return res;
    }))
  }

  getStudents() {
    let endpoint = 'students';
    return this.http.get<any>(this.host + endpoint)
    .pipe(map((res:any) => {
      return res;
    }))
  }
  deleteStudent(id: number) {
    let data:any = localStorage.getItem('currentUser');
    let currentUser = JSON.parse(data);
    let token = currentUser.token;    
    let headerObj = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + token
    });
    const httpOption = {
      headers: headerObj
    };

    let endpoint = 'students/';
    return this.http.delete<any>(this.host + endpoint + id, httpOption)
    .pipe(map( res => {
      return res;
    }))
  }
  updateStudent(student: any, id: number) {
    let data:any = localStorage.getItem('currentUser');
    let currentUser = JSON.parse(data);
    let token = currentUser.token;    

    let headerObj = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + token
    });
    const httpOption = {
      headers: headerObj
    };

    let endpoint = 'students/';
    return this.http.put<any>(this.host + endpoint + id, student, httpOption)
    .pipe(map( res => {
      return res;
    }))
    
  }
}
