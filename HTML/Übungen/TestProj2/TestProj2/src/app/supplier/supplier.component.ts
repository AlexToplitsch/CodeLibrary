import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Component({
  selector: 'app-supplier',
  templateUrl: './supplier.component.html',
  styleUrls: ['./supplier.component.css']
})
export class SupplierComponent implements OnInit {

  public suppliers: any;
  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    this.http.get("http://localhost:3201/supplier")
    .subscribe(
      res => {
        this.suppliers=res
      },
      err => console.log(err),
      () => console.log("Completed")
    );
  }

}
