import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';


@Component({
  selector: 'app-employee',
  templateUrl: './employee.component.html',
  styleUrls: ['./employee.component.css']
})
export class EmployeeComponent implements OnInit {

  public employees: any;
  public page: number = 1;
  constructor(private http: HttpClient, private router: Router) {  }

  ngOnInit(): void {
    this.getData()
  }

  public getData(){
    this.router.routeReuseStrategy.shouldReuseRoute = () => false; 
    this.http.get(`http://localhost:3201/employee?_page=${this.page}&_limit=10`)
    .subscribe(
      res => {
      this.employees=res},
      err => console.log(err),
      () => console.log("Completed")
      );
  }

  public openDetail(id:string):void{
    this.router.navigate([`/employee_details/${id}`])
  }

  public forward(){
    if(this.page >= 100){
      this.page = 1;
    }
    else{
      this.page = this.page + 1;
    }
    console.log(this.page)
    this.getData()
  }

  public backward(){
    if(this.page <= 1){
      this.page = 100;
    }
    else{
      this.page = this.page - 1;
    }
    console.log(this.page)
    this.getData()
  }

}
