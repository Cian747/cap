import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class KochaService {

  KochaUrl = "http://127.0.0.1:8000/api/";

  constructor(private http:HttpClient) { 
  }

  registerUser(userData:any):Observable<any[]>{
    return this.http.post<any[]>('http://127.0.0.1:8000/api/users/', userData)
  }

  loginUser(userData:any):Observable<any[]>{
    return this.http.post<any[]>('http://127.0.0.1:8000/api/auth/', userData)
  }

  getSports():Observable<any[]>{
    return this.http.get<any[]>(this.KochaUrl + 'kocha/sports/')

  }

  getCategories():Observable<any[]>{
    return this.http.get<any[]>(this.KochaUrl + 'kocha/category/')
  }

  searchSport(input:string):Observable<any[]>{
    return this.http.get<any[]>('http://127.0.0.1:8000/api/kocha/sport/name/?search=' + input)
  }
  
}
