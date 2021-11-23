import { Component, OnInit } from '@angular/core';
import { HttpClient } from "@angular/common/http";
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-employee-details',
  templateUrl: './employee-details.component.html',
  styleUrls: ['./employee-details.component.css']
})
export class EmployeeDetailsComponent implements OnInit {
  public employee: any

  constructor(private http: HttpClient, private activeRoute: ActivatedRoute) { }

  ngOnInit(): void {
      let id: string = this.activeRoute.snapshot.params["id"]
      this.http.get(`http://localhost:3201/employee/${id}`)
      .subscribe(
      res => {
        this.employee=res
      },
      err => console.log(err),
      () => console.log("Completed")
    );
  }

}
