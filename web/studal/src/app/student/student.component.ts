import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup } from '@angular/forms';
import { ApiService } from '../shared/api.service';
import { ApiclassService } from '../shared/apiclass.service';

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
  classgroups !: any;
  selectedClassgroup = new FormControl('');

  showAdd !: boolean;
  showUpdate !: boolean;

  constructor(
    private formBuilder: FormBuilder,
    private api: ApiService,
    private apiclass: ApiclassService
    ) { }

  ngOnInit(): void {
    this.studentForm = this.formBuilder.group({
      name: [''],
      email: [''],
      phone: [''],
      borndate: [''],
      classgroup_id: ['']
    });

    this.getClassgroups();
    let selected = localStorage.getItem('selectedClassgroup')

    if (selected != null) {
      this.selectedClassgroup.setValue(Number(selected));
      this.getGroupStudent(this.selectedClassgroup.value);      
      this.selectedClassgroup.setValue(selected)
    }
  }

  onChangeGroupSelect(selected : any) {
    let id = selected.target.value;    
    this.getGroupStudent(id);
    this.selectedClassgroup.setValue(id);
    localStorage.setItem('selectedClassgroup', id)
  }

  getClassgroups() {
    this.apiclass.getClassgroups()
    .subscribe(res => {
      console.log(res)
      this.classgroups = res;
    })
  }

  addStudent() {
    this.studentModelObj.name = this.studentForm.value.name;
    this.studentModelObj.email = this.studentForm.value.email;
    this.studentModelObj.phone = this.studentForm.value.phone;
    this.studentModelObj.borndate = this.studentForm.value.borndate;
    this.studentModelObj.classgroup_id = this.selectedClassgroup.value;

    this.api.addStudent(this.studentModelObj)
    .subscribe( res => {
      this.studentForm.reset();
      this.getGroupStudent(this.selectedClassgroup.value);
      alert('Tanuló hozzáadva');
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

  getGroupStudent(id: number) {
    this.api.getGroupStuents(id)
    .subscribe( res => {
      this.studentsData = res;
    })
    
  }

  deleteStudent(id: number) {
    this.api.deleteStudent(id)
    .subscribe(res => {
      this.getGroupStudent(this.selectedClassgroup.value);
      alert('A tanuló törölve');      
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
    this.studentForm.controls['classgroup_id'].setValue(student.classgroup_id);

  }

  updateStudent() {
    this.studentModelObj.name = this.studentForm.value.name;
    this.studentModelObj.email = this.studentForm.value.email;
    this.studentModelObj.phone = this.studentForm.value.phone;
    this.studentModelObj.borndate = this.studentForm.value.borndate;
    this.studentModelObj.classgroup_id = this.studentForm.value.classgroup_id;
    
    this.api.updateStudent(this.studentModelObj, this.studentModelObj.id)
    .subscribe( res => {
      this.studentForm.reset();
      this.getGroupStudent(this.selectedClassgroup.value);
      alert('Módosítás megtörtént');
    })
  }

  clickAddStudent() {
    this.studentForm.reset();
    this.showAdd = true;
    this.showUpdate = false;
  }
}
