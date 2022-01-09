import { Component } from '@angular/core';
import { AuthService } from './shared/auth.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  title = 'studal';
  
  constructor(private auth: AuthService) {}

  logout() {
    this.auth.logout();
    console.log('Kilépés itt...')
  }
  
  showLogout() {
    console.log('valami')
  }
}
