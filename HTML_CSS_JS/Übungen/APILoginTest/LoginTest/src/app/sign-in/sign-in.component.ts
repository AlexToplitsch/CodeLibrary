import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';


@Component({
  selector: 'app-sign-in',
  templateUrl: './sign-in.component.html',
  styleUrls: ['./sign-in.component.css']
})
export class SignInComponent implements OnInit {

  public error: boolean;
  public registerModel: any;

  constructor(private router: Router, private http: HttpClient) { }

  ngOnInit(): void {
    this.registerModel = {};
  }

  signIn(){
    console.log(this.registerModel);
    this.http.post('http://localhost:5000/api/account/signin', this.registerModel)
    .subscribe(
      res => {
        this.router.navigate([`/login`]);
        console.log(res);
      },
      err => {
        this.error = true;
        console.log(err)
      }
    );
  }
}
