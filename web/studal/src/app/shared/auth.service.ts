import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map } from 'rxjs/operators';
import { HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  host = 'http://localhost:8000/api/';
  constructor(private http: HttpClient) { }

  login(user: string, pass: string) {
    
    let authData = {
      name: user,
      password: pass
    }
    let data = JSON.stringify(authData);
    let headerObj = new HttpHeaders({
      'Content-Type': 'application/json',
    });
    const httpOption = {
      headers: headerObj
    };    
    let endpoint = 'login';
    let url = this.host + endpoint;
    
    return this.http.post<any>(url, data, httpOption)
    .pipe(map( (res:any) => {
      return res;
    }))
  }
}
