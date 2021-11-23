import { Component, OnInit } from '@angular/core';
import { HttpClient } from "@angular/common/http";
import { ActivatedRoute } from '@angular/router';


@Component({
  selector: 'app-detail',
  templateUrl: './detail.component.html',
  styleUrls: ['./detail.component.css']
})
export class DetailComponent implements OnInit {
  public user: any;
  constructor(private http: HttpClient,
              private activeRoute: ActivatedRoute) { }

  ngOnInit(): void {
      let id: string = this.activeRoute.snapshot.params["id"]
      this.http.get(`http://localhost:3201/user/${id}`)
      .subscribe(
       res => {
         this.user=res
       },
       err => console.log(err),
       () => console.log("Completed")
     );
  }
}
