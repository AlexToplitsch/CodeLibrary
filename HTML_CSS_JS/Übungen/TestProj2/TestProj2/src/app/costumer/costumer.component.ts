import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-costumer',
  templateUrl: './costumer.component.html',
  styleUrls: ['./costumer.component.css']
})
export class CostumerComponent implements OnInit {
  public costumers: any;
  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    this.http.get("http://localhost:3201/costumer")
    .subscribe(
      res => {
        this.costumers=res
      },
      err => console.log(err),
      () => console.log("Completed")
    );
  }

}
