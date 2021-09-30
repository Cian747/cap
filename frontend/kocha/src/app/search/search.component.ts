import { Component, OnInit } from '@angular/core';
import { KochaService } from '../coach-service/kocha.service';
import { Sport } from '../class/sport';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent implements OnInit {

  sports!: Sport[];
  constructor(private kochaService:KochaService) { }

  
  searchSports(input:string){
    if(input){
      console.log(input)
      this.kochaService.searchSport(input).toPromise().then((response:any)=>{
        if(response){
          console.log(response)
          this.sports = response;  
        }
        else{
          alert('Nothing found on ' + input)
        }
      });
    }
  }

  ngOnInit(): void {
    
  }

}
