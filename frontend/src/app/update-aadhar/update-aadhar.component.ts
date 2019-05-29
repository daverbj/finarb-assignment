import { ApiService } from './../services/api.service';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-update-aadhar',
  templateUrl: './update-aadhar.component.html',
  styleUrls: ['./update-aadhar.component.scss']
})
export class UpdateAadharComponent implements OnInit {
  id
  isAadharAvailable = false
  aadharNumber = ''
  constructor(private api:ApiService, private route: ActivatedRoute ) { }

  ngOnInit() {
    this.id = this.route.snapshot.paramMap.get("id")
    this.api.getAadhar(this.id)
      .subscribe(
        (response) => {
          console.log('get aadhar response', response)
          this.isAadharAvailable = true;
          this.aadharNumber = response.data.aadharNumber
        },
        (error) => {
          console.log('get aadhar error', error)
          if (error.status == 401 || error.status == 403){
            alert("Unauthorized access")
          }
          if (error.status == 404) {
            this.isAadharAvailable = false;
          }
        },
        () => {

        }
      )
  }
  onSubmit(){
    if(!this.isAadharAvailable){
      this.api.addNewAadhar(this.aadharNumber, this.id).subscribe(
        (response) => {
          console.log('add aadhar response', response)
        },
        (error) => {
          console.log('add aadhar error', error)
        },
        () => {

        }
      )
    } else {
      this.api.updateAadher(this.aadharNumber, this.id).subscribe(
        (response) => {
          console.log('add aadhar response', response)
        },
        (error) => {
          console.log('add aadhar error', error)
        },
        () => {

        }
      )
    }

  }

}
