import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  base_url = 'http://localhost:5000/api/';
  
  constructor(private http: HttpClient) { 
    
  }
  public register(userData){
    
    return this.http.post(this.base_url + 'users', userData, {observe: 'response'});
  }
  public login(userData) {
    return this.http.post(this.base_url + 'login', userData, {observe: 'response'});
  }
  public getAadhar(userId) {
    let headers_object = new HttpHeaders({
      'Content-Type': 'application/json',
       'Authorization': "Bearer " + localStorage.getItem('token')
    });
  
    let httpOptions = {
      headers: headers_object
    };
    return this.http.get(this.base_url + 'aadhar/user/' + userId, httpOptions);
  }
  public addNewAadhar(aadharNumber, userId) {
    let headers_object = new HttpHeaders({
      'Content-Type': 'application/json',
       'Authorization': "Bearer " + localStorage.getItem('token')
    });
  
    let httpOptions = {
      headers: headers_object
    };
    return this.http.post(this.base_url + 'aadhar/user/' + userId, {aadhar_number: aadharNumber}, httpOptions);
  }
  public updateAadher(aadharNumber, userId) {

    let headers_object = new HttpHeaders({
      'Content-Type': 'application/json',
       'Authorization': "Bearer " + localStorage.getItem('token')
    });
  
    let httpOptions = {
      headers: headers_object
    };
    return this.http.put(this.base_url + 'aadhar/user/' + userId, {aadhar_number: aadharNumber}, httpOptions);
  }
}
