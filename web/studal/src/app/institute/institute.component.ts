import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-institute',
  templateUrl: './institute.component.html',
  styleUrls: ['./institute.component.css']
})
export class InstituteComponent implements OnInit {

  instituteName = 'Minta Intézmény'
  courses : any;

  constructor() { }

  ngOnInit(): void {
    this.courses = [
      {
        name: 'Angular keretrendszer használata',
        hours: 108
      },
      {
        name: 'Larave keretrendszer használata',
        hours: 108
      },
      {
        name: 'JavaScript használata',
        hours: 108
      },

    ]

    
  }

}
