import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'TestProj';
  name: string = "Alexander";
  isVisible: boolean = true;
  color = true;

  Show(){
    this.color = !this.color;
  }
}
