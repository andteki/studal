import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { ApiclassService } from '../shared/apiclass.service';
import { ClassgroupModel } from './class.model';

@Component({
  selector: 'app-class',
  templateUrl: './class.component.html',
  styleUrls: ['./class.component.css']
})
export class ClassComponent implements OnInit {


  classgroupForm !: FormGroup;
  classgroupModelObj: ClassgroupModel = new ClassgroupModel();
  classgroupsData !: any;

  showAdd !: boolean;
  showUpdate !: boolean;  


  constructor(
    private formBuilder: FormBuilder,
    private apiclass: ApiclassService
  ) { }

  ngOnInit(): void {
    this.classgroupForm = this.formBuilder.group({
      name: ['']
    });
    this.getAllClassgroup();    
  }

  addClassgroup() {
    this.classgroupModelObj.classgroup = this.classgroupForm.value.name;

    this.apiclass.addClassgroup(this.classgroupModelObj)
    .subscribe( res => {
      console.log(res);
      alert('Osztály hozzáadva');        
      this.classgroupForm.reset();
      this.getAllClassgroup();
    },
      err => {
        alert('Hiba! Az osztály hozzáadása sikertelen!');
      }
    )
    
  }

  getAllClassgroup() {
    this.apiclass.getClassgroups()
    .subscribe( res => {
      this.classgroupsData = res;
    })
  }
  
  deleteClassgroup(id: number) {
    this.apiclass.deleteClassgroup(id)
    .subscribe(res => {
      alert('A tanuló törölve');
      this.getAllClassgroup();
    });
  }
  
  onEdit(classgroup: any) {
    this.showAdd = false;
    this.showUpdate = true;

    this.classgroupModelObj.id = classgroup.id;    
    this.classgroupForm.controls['name'].setValue(classgroup.classgroup);

  }
  updateClassgroup() {
    this.classgroupModelObj.classgroup = this.classgroupForm.value.name;
    
    this.apiclass.updateClassgroup(this.classgroupModelObj, this.classgroupModelObj.id)
    .subscribe( res => {
      console.log(res);
      alert('Módosítás megtörtént');
      this.classgroupForm.reset();
      this.getAllClassgroup();

    })
  }

  clickAddClassgroup() {
    this.classgroupForm.reset();
    this.showAdd = true;
    this.showUpdate = false;
  }

}
