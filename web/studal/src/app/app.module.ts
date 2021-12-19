import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { StudentComponent } from './student/student.component';
import { ClassComponent } from './class/class.component';
import { NopageComponent } from './nopage/nopage.component';
import { InstituteComponent } from './institute/institute.component';

@NgModule({
  declarations: [
    AppComponent,
    StudentComponent,
    ClassComponent,
    NopageComponent,
    InstituteComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
