import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  base_url = 'http://localhost:5000/api/';
  token = localStorage.getItem('token');
  httpOptions
  constructor(private http: HttpClient) { 
    let headers_object = new HttpHeaders({
      'Content-Type': 'application/json',
       'Authorization': "Bearer " + this.token
    });

    this.httpOptions = {
      headers: headers_object
    };
  }
  public register(userData){
    return this.http.post(this.base_url + 'users', userData, {observe: 'response'});
  }
  public login(userData) {
    return this.http.post(this.base_url + 'login', userData, {observe: 'response'});
  }
  public getAadhar(userId) {
    return this.http.get(this.base_url + 'aadhar/user/' + userId, this.httpOptions);
  }
  public addNewAadhar(aadharNumber, userId) {
    return this.http.post(this.base_url + 'aadhar/user/' + userId, {aadhar_number: aadharNumber}, this.httpOptions);
  }
  public updateAadher(aadharNumber, userId) {
    return this.http.put(this.base_url + 'aadhar/user/' + userId, {aadhar_number: aadharNumber}, this.httpOptions);
  }
}
