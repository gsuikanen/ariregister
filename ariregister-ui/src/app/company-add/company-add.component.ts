import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, FormArray, Validators } from '@angular/forms';
import { AriregisterApiService } from '../services/ariregister-api.service';
import { faWarning, faCheckCircle } from '@fortawesome/free-solid-svg-icons';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-company-add',
  templateUrl: './company-add.component.html',
  styleUrls: ['./company-add.component.css']
})
export class CompanyAddComponent implements OnInit {
  title = 'AddCompanyForm';
  AddCompanyForm: FormGroup;
  apiResponse: any;
  warningIcon = faWarning;
  successIcon = faCheckCircle;
  totalCapital = 0;
  subscription: Subscription;

  constructor(private fb: FormBuilder,
    private Api: AriregisterApiService) {
    
  }

  ngOnInit(): void {
    this.AddCompanyForm = this.fb.group({
      companyName: ['', Validators.required],
      companyCode: ['', [Validators.required, Validators.pattern('^.{7}$')]],
      companyRegdt: new Date().toISOString().split('T')[0],
      companyCapital: this.totalCapital,
      owners: this.fb.array([])
    });

    this.subscription = this.owners.valueChanges.subscribe(data => {
      this.totalCapital = data.reduce((a,b) => a + +b.ownerCapital, 0)
    })
   }

  get owners(): FormArray {
    return this.AddCompanyForm.get('owners') as FormArray;
  }

  get companyName() {
    return this.AddCompanyForm.get('companyName');
  }

  get companyCode() {
    return this.AddCompanyForm.get('companyCode');
  }

  newOwner(): FormGroup {
    return this.fb.group({
      ownerName: ['', Validators.required],
      ownerSurname: '',
      ownerType: 'priv',
      ownerCode: ['', Validators.required],
      ownerCapital: [0, [Validators.required, Validators.min(1)]],
    })
  }

  addOwner() {
    this.owners.push(this.newOwner());
  }

  deleteOwner(i: number) {
    this.owners.removeAt(i);
  }

  getOwnerType(i: number): string {
    return this.owners.value.at(i).ownerType
  }

  getTotalCapital(): number {
    let cap = 0;
    //let len = this.owners.value.len();
    // for (let i = 0; i <= len; i++) {
    //   cap += this.owners.value.at(i).ownerCapital;
    // }
    return cap;
  }

  onSubmit() {
    console.log(this.AddCompanyForm.value);
    this.Api.postCompanyData(this.AddCompanyForm.value).subscribe((res: any) => {
      console.log(res);
      this.apiResponse = res;
    })
  }

}