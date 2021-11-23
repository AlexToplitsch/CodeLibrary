import { Component, OnInit } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: 'app-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.css']
})
export class UserComponent implements OnInit {
  public users: any;

  constructor(private http: HttpClient,
              private router: Router) { }
  
  ngOnInit(): 
  
  void {
    this.router.routeReuseStrategy.shouldReuseRoute = () => false; 
    this.http.get("http://localhost:3201/user")
    .subscribe(
      res => {
      this.users=res},
      err => console.log(err),
      () => console.log("Completed")
      );
  }

  public openDetail = (id:string) =>{
    console.log(id);
    this.router.navigate([`/detail/${id}`]);
  }

}
