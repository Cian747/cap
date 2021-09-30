import { Component, OnInit } from '@angular/core';
import { KochaService } from '../coach-service/kocha.service';


@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {

  constructor(private kochaService:KochaService) { }
  register:any;


  ngOnInit(): void {
    this.register = {
      username: '',
      password: '',
      email: '',

    };
  }

  registerUser(){
    this.kochaService.registerUser(this.register).subscribe( response => {
      console.log(response)
      alert('User ' + this.register.username + ' has been created')
    },
    error => {
      console.log('error',error)
    } 
    );
  }

  LoginUser(){
    this.kochaService.loginUser(this.register).subscribe( response => {
      console.log(response)
      alert('User ' + this.register.username + ' has logged in')
    },
    error => {
      console.log('error',error)
    } 
    );
  }



}
