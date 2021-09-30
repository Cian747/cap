import { Component, OnInit } from '@angular/core';
import { KochaService } from '../coach-service/kocha.service';
import { Sport } from '../class/sport';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  sports!:Sport[];
  constructor(private kochaService:KochaService) {

   }

  ngOnInit(): void {
    let promise = new Promise<void>((resolve, reject)=>{
      this.kochaService.getSports().toPromise().then((response: any)=>{
        this.sports = response;
        console.log(response)
        resolve();
        
      });
    });
    // return promise;


  

  }

}
