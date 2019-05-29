import { ApiService } from './../services/api.service';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})

export class RegisterComponent implements OnInit {
  userData = {
    username: '',
    password: ''
  }
  
  constructor(private api: ApiService, public router:Router) { }

  ngOnInit() {
  }
  onSubmit(){
    console.log('user data', this.userData);
    this.api.register(this.userData)
      .subscribe(
        (response)=>{
          console.log('register reponse', response)
          if (response.status == 200){
            alert("Registration Success");
            this.router.navigate(['/login'])
          }
          
        },
        (error) => {
          alert("Registration fail");
          console.log('register error', error)
        },
        () => {

        }
      )
  }

}
