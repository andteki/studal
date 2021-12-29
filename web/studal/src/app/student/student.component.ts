import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { ApiService } from '../shared/api.service';

import { StudentModel } from './student.model';

@Component({
  selector: 'app-student',
  templateUrl: './student.component.html',
  styleUrls: ['./student.component.css']
})
export class StudentComponent implements OnInit {
  
  studentForm !: FormGroup;
  studentModelObj: StudentModel = new StudentModel();
  studentsData !: any;

  showAdd !: boolean;
  showUpdate !: boolean;

  constructor(
    private formBuilder: FormBuilder,
    private api: ApiService
    ) { }

  ngOnInit(): void {
    this.studentForm = this.formBuilder.group({
      name: [''],
      email: [''],
      phone: [''],
      borndate: ['']
    });
    this.getAllStudent();
  }

  addStudent() {
    this.studentModelObj.name = this.studentForm.value.name;
    this.studentModelObj.email = this.studentForm.value.email;
    this.studentModelObj.phone = this.studentForm.value.phone;
    this.studentModelObj.borndate = this.studentForm.value.borndate;
    this.api.addStudent(this.studentModelObj)
    .subscribe( res => {
      console.log(res);
      alert('Tanuló hozzáadva');        
      this.studentForm.reset();
      this.getAllStudent();
    },
      err => {
        alert('Hiba! A tanuló hozzáadása sikertelen!');
      }
    )
    
  }
  getAllStudent() {
    this.api.getStudents()
    .subscribe( res => {
      this.studentsData = res;
    })
  }
  deleteStudent(id: number) {
    this.api.deleteStudent(id)
    .subscribe(res => {
      alert('A tanuló törölve');
      this.getAllStudent();
    });
  }
  onEdit(student: any) {
    this.showAdd = false;
    this.showUpdate = true;

    this.studentModelObj.id = student.id;
    
    this.studentForm.controls['name'].setValue(student.name);
    this.studentForm.controls['email'].setValue(student.email);
    this.studentForm.controls['phone'].setValue(student.phone);
    this.studentForm.controls['borndate'].setValue(student.borndate);

  }
  updateStudent() {
    this.studentModelObj.name = this.studentForm.value.name;
    this.studentModelObj.email = this.studentForm.value.email;
    this.studentModelObj.phone = this.studentForm.value.phone;
    this.studentModelObj.borndate = this.studentForm.value.borndate;
    
    this.api.updateStudent(this.studentModelObj, this.studentModelObj.id)
    .subscribe( res => {
      console.log(res);
      alert('Módosítás megtörtént');
      this.studentForm.reset();
      this.getAllStudent();

    })
  }

  clickAddStudent() {
    this.studentForm.reset();
    this.showAdd = true;
    this.showUpdate = false;
  }
}
