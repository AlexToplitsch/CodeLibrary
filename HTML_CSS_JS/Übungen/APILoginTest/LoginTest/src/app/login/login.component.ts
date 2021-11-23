import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  public loggedIn: boolean;
  public error: boolean;
  public usermodel: any;

  constructor(private router: Router, private http: HttpClient) { }

  ngOnInit(): void {
    this.loggedIn = false;
    this.error = false;
    this.usermodel = {};
  }

  logIn(){
    this.http.post('http://localhost:5000/api/account/login', this.usermodel)
    .subscribe(
      res => {
        this.loggedIn = true;
        this.error = false;
        this.router.navigate([`/home`]);
        console.log("res");
      },
      err => {
        this.error = true;
        console.log("err");
      }
    );
  }

  register(){
    this.router.navigate(['/signin']);
  }

}
