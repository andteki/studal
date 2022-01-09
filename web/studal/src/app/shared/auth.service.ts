import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map } from 'rxjs/operators';
import { HttpHeaders } from '@angular/common/http';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  host = 'http://localhost:8000/api/';
  constructor(
    private http: HttpClient,
    private router: Router
    ) { }

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
  logout() {
    if (localStorage.getItem('currentUser') === null) {
      return;
    }
    let data:any = localStorage.getItem('currentUser');
    localStorage.removeItem('currentUser');
    localStorage.removeItem('selectedClassgroup');
    let currentUser = JSON.parse(data);
    let token = currentUser.token;    
    let headerObj = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + token
    });
    const httpOption = {
      headers: headerObj
    };    
    let endpoint = 'logout';
    let url = this.host + endpoint;
    return this.http.post<any>(url, '', httpOption)
    .subscribe(res => {
      console.log(res);
      this.router.navigate(['login']);
    })
  }

  isLoggedIn() {
    if (localStorage.getItem('currentUser') === null) {
      return false;
    }    
    let data:any = localStorage.getItem('currentUser');
    let currentUser = JSON.parse(data);
    let token = currentUser.token;
    return token;
  }
}
