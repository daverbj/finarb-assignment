import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { UpdateAadharComponent } from './update-aadhar.component';

describe('UpdateAadharComponent', () => {
  let component: UpdateAadharComponent;
  let fixture: ComponentFixture<UpdateAadharComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ UpdateAadharComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(UpdateAadharComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
