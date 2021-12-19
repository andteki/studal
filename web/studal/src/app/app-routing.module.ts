import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ClassComponent } from './class/class.component';
import { InstituteComponent } from './institute/institute.component';
import { NopageComponent } from './nopage/nopage.component';
import { StudentComponent } from './student/student.component';

const routes: Routes = [
  {path: 'institute', component: InstituteComponent },
  {path: 'students', component: StudentComponent },
  {path: 'classes', component: ClassComponent },
  {path: '', redirectTo: 'institute', pathMatch: 'full' },
  {path: '**', component: NopageComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
