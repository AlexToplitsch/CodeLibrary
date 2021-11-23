import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavComponent } from './nav/nav.component';
import { IndexComponent } from './index/index.component';
import { FunComponent } from './fun/fun.component';
import { FormsModule } from '@angular/forms';
import { DemoComponent } from './demo/demo.component';
import { UserComponent } from './user/user.component';
import { SupplierComponent } from './supplier/supplier.component';
import { CostumerComponent } from './costumer/costumer.component';
import { DetailComponent } from './detail/detail.component';
import { EmployeeComponent } from './employee/employee.component';
import { EmployeeDetailsComponent } from './employee-details/employee-details.component';


@NgModule({
  declarations: [				
    AppComponent,
      NavComponent,
      IndexComponent,
      FunComponent,
      DemoComponent,
      UserComponent,
      SupplierComponent,
      CostumerComponent,
      DetailComponent,
      EmployeeComponent,
      EmployeeDetailsComponent,
   ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
