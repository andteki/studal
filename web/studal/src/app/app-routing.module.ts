import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ClassComponent } from './class/class.component';
import { InstituteComponent } from './institute/institute.component';
import { LoginComponent } from './login/login.component';
import { NopageComponent } from './nopage/nopage.component';
import { AuthGuard } from './shared/auth.guard';
import { StudentComponent } from './student/student.component';

const routes: Routes = [
  {path: 'institute', component: InstituteComponent },
  {
    path: 'students', 
    component: StudentComponent,
    canActivate: [AuthGuard]
  },
  {path: 'classes', component: ClassComponent },
  {path: 'login', component: LoginComponent },
  {path: '', redirectTo: 'institute', pathMatch: 'full' },
  {path: '**', component: NopageComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
