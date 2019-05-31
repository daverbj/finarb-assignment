import { Router } from '@angular/router';
import { ApiService } from './../services/api.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  userData = {
    username: '',
    password: ''
  }
  constructor(private api: ApiService, private router: Router) { }

  ngOnInit() {
    localStorage.removeItem('token');
    localStorage.removeItem('user_id');
  }

  onSubmit(){
    this.api.login(this.userData)
      .subscribe(
        (response)=>{
          console.log('login response', response);
          if(response.status == 200) {
            localStorage.setItem('token', response.body['access_token'])
            localStorage.setItem('user_id', response.body['user_id'])
            //navgate to user page
            this.router.navigate([`/update/${response.body['user_id']}`]);
          }
        },
        (error)=>{
          console.log('login error', error);
          alert("Login failed")
        },
        () => {

        }
      )
  }
}
