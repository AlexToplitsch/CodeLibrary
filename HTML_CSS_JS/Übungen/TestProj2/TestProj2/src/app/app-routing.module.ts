import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, Routes } from '@angular/router';

import { IndexComponent } from './index/index.component';
import { AboutComponent } from './about/about.component';
import { SaxComponent } from './sax/sax.component';
import { FunComponent } from './fun/fun.component';
import { NotfoundComponent } from './notfound/notfound.component';
import { DemoComponent } from './demo/demo.component';
import { UserComponent } from './user/user.component';
import { SupplierComponent } from './supplier/supplier.component';
import { CostumerComponent } from './costumer/costumer.component';
import { DetailComponent } from './detail/detail.component';
import { EmployeeComponent } from './employee/employee.component';
import { EmployeeDetailsComponent } from './employee-details/employee-details.component';


const routes: Routes = [
  {path: 'index', component: IndexComponent},
  {path: '', redirectTo: '/index', pathMatch: 'full'},
  {path: 'about', component: AboutComponent},
  {path: 'sax', component: SaxComponent},
  {path: 'fun', component: FunComponent},
  {path: 'demo', component: DemoComponent},
  {path: 'user', component: UserComponent},
  {path: 'supplier', component: SupplierComponent},
  {path: 'costumer', component: CostumerComponent},
  {path: 'detail/:id', component: DetailComponent},
  {path: 'employee', component: EmployeeComponent},
  {path: 'employee_details/:id', component: EmployeeDetailsComponent},
  {path: '404', component: NotfoundComponent},
  {path: '**', redirectTo: '/404', pathMatch: 'full'}
]

@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    RouterModule.forRoot(routes)
  ],

  exports: [ RouterModule ]
})


export class AppRoutingModule { }
