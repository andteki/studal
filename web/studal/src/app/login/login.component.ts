import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder } from '@angular/forms';
import { AuthService } from '../shared/auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  loginForm !: FormGroup;
  

  constructor(
    private formBuilder: FormBuilder,
    private auth: AuthService,
    private router: Router
    ) { }

  ngOnInit(): void {
    this.loginForm = this.formBuilder.group({
      name: [''],
      password: ['']
    })
        
  }

  login() { 
    let user = this.loginForm.value.name;
    let pass = this.loginForm.value.password;
    
    this.auth.login(user, pass)
    .subscribe(res => {
      console.log(res.data.token);
      console.log(res.success);

      if (res.success) {
        localStorage.setItem('currentUser', JSON.stringify({ token: res.data.token, name: res.data.name }));
        this.router.navigate(['students'])
      }else {
        alert('A belépés sikertelen!')
      }
    })
    
  }
}
